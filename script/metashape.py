import os
import shutil
import json
import Metashape
import numpy
from osgeo import gdal, ogr, osr
import laspy

from lib import GeneralTools

gt = GeneralTools()

class MetashapeTools:

    def __init__(self):
        self.photos_location_accuracy = Metashape.Vector((
            float(gt.params.get("Photo")["LocationAccuracy2D"]),
            float(gt.params.get("Photo")["LocationAccuracy2D"]),
            float(gt.params.get("Photo")["LocationAccuracyHeight"])))
        self.image_compression = Metashape.ImageCompression()
        self.image_compression.tiff_big = True
        self.image_compression.tiff_tiled = False
        self.image_compression.tiff_overviews = True
        self.image_compression.tiff_compression = Metashape.ImageCompression.TiffCompressionLZW

    def check_gcps(self):
        if os.path.isfile(gt.params.get("OptimizeAlignment")["Path"]) \
                and os.path.exists(gt.params.get("OptimizeAlignment")["Path"]):
            return True
        else:
            gt.update_log('No .csv file with GCP found.')
            return False

    def check_geoids(self):
        geoids = ["https://s3-eu-west-1.amazonaws.com/download.agisoft.com/gtg/us_nga_egm2008_1.tif",
                  "https://s3-eu-west-1.amazonaws.com/download.agisoft.com/gtg/es_ign_EGM08_REDNAP.tif",
                  "https://s3-eu-west-1.amazonaws.com/download.agisoft.com/gtg/es_ign_EGM08_REDNAP_Canarias.tif"]
        for url in geoids:
            file = url.split('/')[-1]
            dst = os.path.join(gt.params.get("InstallRequirement")["Geoid"], file)
            if not os.path.exists(dst):
                gt.update_log('NEEDED ' + dst + '\n' +
                              'Download from ' + url + ' before execute.')
                os.startfile(gt.params.get("InstallRequirement")["Geoid"])
                raise SystemExit(0)
            Metashape.CoordinateSystem.addGeoid(dst)

    def check_initial(self):
        gt.update_log('EXECUTION PARAMETERS:')
        # comprueba OS
        gt.is_platform('win32')
        # comprueba geoides
        self.check_geoids()
        # comprueba licencia
        if not Metashape.license.valid:
            gt.update_log(text="License = Not valid")
            raise SystemExit(0)
        if not Metashape.app.activated:
            gt.update_log(text="License = Not activated")
            raise SystemExit(0)
        # comprueba versión
        compatible_major_version = "2.2"
        found_major_version = ".".join(Metashape.app.version.split('.')[:2])
        if found_major_version != compatible_major_version:
            gt.update_log(text="Incompatible Metashape version: {} != {}"
                          .format(found_major_version, compatible_major_version))
            raise SystemExit(0)
        # check metashape parameters
        binary = '0b'
        text_gpus = ''
        selected_gpus = gt.params.get("InstallRequirement")["SelectedGPUs"][0:-1] + ',]'
        selected_gpus = selected_gpus[1:-1].split('},')
        for read_gpu in Metashape.app.enumGPUDevices():
            for i in selected_gpus:
                if not i == '':
                    i = i + '}'
                    dict = i.replace("'", "\"")
                    dict = json.loads(dict)
                    if read_gpu == dict:
                        binary = binary + '1'
                        text_gpus = text_gpus + read_gpu.get('name') + ', '
                    else:
                        binary = binary + '0'
        if binary == '0b':
            Metashape.app.gpu_mask = 0
            Metashape.app.cpu_enable = True
        else:
            Metashape.app.gpu_mask = int(binary, 2)
            Metashape.app.cpu_enable = False
        gt.update_log(text='Metashape checks:\n' +
                           'Valid license = ' + str(Metashape.License.valid) + '\n' +
                           'Activated license = ' + str(Metashape.app.activated) + '\n' +
                           'Version = ' + str(Metashape.app.version) + '\n' +
                           'Selected GPUs = ' + text_gpus)
        file = os.path.normpath(gt.params_file)
        with open(file) as config_file:
            parsed = json.load(config_file)
            parsed_text = json.dumps(parsed, indent=2)
        gt.update_log('INPUT PARAMETERS:\n' + parsed_text)

    def check_markers(self):
        if os.path.isfile(gt.params.get("OptimizeAlignment")["Path"]) \
                and os.path.exists(gt.params.get("OptimizeAlignment")["Path"]):
            return True
        else:
            gt.update_log('No .xml file with Metashape markers found.')
            return False

    def check_marker_photointerpretation(self, label=gt.label):
        self.set_chunk(label)
        projections = sum([len(marker.projections) for marker in self.chunk.markers])
        if projections > 0:
            gt.update_log("Founded manual photo-interpretation of the markers.")
            return True
        else:
            return False

    def check_optimize_method(self):
        if gt.params.get("OptimizeAlignment")["Method"] == 'PSX':
            gt.update_log('Alignment optimization method = METASHAPE PROJECT')
            if self.check_marker_photointerpretation():
                self.optimize_alignment()
            elif self.check_gcps():
                self.import_gcps()
                gt.update_log('AWAITING MANUAL PHOTO-INTERPRETATION OF THE MARKERS UNDER PROJECT =\n' +
                              gt.project_path)
                raise SystemExit(0)
        elif gt.params.get("OptimizeAlignment")["Method"] == 'XML':
            gt.update_log('Alignment optimization method = METASHAPE MARKERS')
            if self.check_markers():
                self.import_markers()
            self.optimize_alignment()
        else:
            gt.update_log('No valid alignment optimization method selected.\n' +
                          'AWAITING THE ALIGNMENT OPTIMIZATION METHOD')
            raise SystemExit(0)

    def check_roi(self):
        if gt.params.get("ROI")["Method"] == "0":
            return False
        elif gt.params.get("ROI")["Method"] == "SHP":
            if os.path.isfile(gt.params.get("ROI")["Path"]) and os.path.exists(gt.params.get("ROI")["Path"]):
                return True
            else:
                gt.update_log('No .shp file with region of interest found.')
                raise SystemExit(0)
        else:
            return False
            gt.update_log('No valid method of application of the region of interest selected.\n' +
                          'AWAITING THE METHOD OF APPLICATION OF THE REGION OF INTEREST AND RESTART')
            raise SystemExit(0)

    def check_split_path(self, label=gt.label):
        self.set_chunk(label)
        path = gt.params.get("SplitTile")["Path"]
        if gt.params.get("SplitTile")["Method"] == "AUTO":
            gt.update_log('Splitting method = automatic for the whole area.')
            self.create_tile_grid(label)
            self.export_tile_grid(label=label)
        elif gt.params.get("SplitTile")["Method"] == "MANUAL":
            gt.update_log('Splitting method = manual selection of tiles from file\n' + path)
            if os.path.exists(path) and os.path.isfile(path):
                self.import_tile_grid(label)
            else:
                self.create_tile_grid(label)
                self.export_tile_grid(label=label)
                self.export_tile_grid(output_path=path, label=label)
                gt.update_log('Splitting method:\nAWAITING FOR THE EDITING OF THE TILING LAYER AND RESTART.')
                raise SystemExit(0)

    def create_tile_grid(self, label=gt.label):
        self.set_chunk(label)
        self.set_crs_definition()
        region = self.chunk.region
        # read corners
        corners = [region.center + region.rot *
                   Metashape.Vector([region.size[0] * ((i & 1) - 0.5),
                                     0.5 * region.size[1] * ((i & 2) - 1),
                                     0.25 * region.size[2] * ((i & 4) - 2)])
                   for i in [0, 1, 2, 3, 4, 5, 6, 7]]
        corner_min = Metashape.Vector([0, 0, 0])
        corner_max = Metashape.Vector([0, 0, 0])
        for corner in corners:
            corner_min[0] = min(corner_min[0], corner.x)
            corner_min[1] = min(corner_min[1], corner.y)
            corner_min[2] = min(corner_min[2], corner.z)
            corner_max[0] = max(corner_max[0], corner.x)
            corner_max[1] = max(corner_max[1], corner.y)
            corner_max[2] = max(corner_max[2], corner.z)
        # place in the middle
        tile_size = gt.tile_size * (1 / self.T.scale())
        buffer = tile_size * gt.params.get("SplitTile")["TileSizeBuffer"] / 100
        range = corner_max - corner_min
        n_tiles_x = round(range[0] / tile_size, ndigits=0) + 1
        dif_x = abs((range[0] - tile_size * n_tiles_x) / 2)
        corner_min[0] = corner_min[0] - dif_x - tile_size
        corner_max[0] = corner_max[0] + dif_x + tile_size
        n_tiles_y = round(range[1] / tile_size, ndigits=0) + 1
        dif_y = abs((range[1] - tile_size * n_tiles_y) / 2)
        corner_min[1] = corner_min[1] - dif_y - tile_size
        corner_max[1] = corner_max[1] + dif_y + tile_size
        corner_min = self.estimate_region_coords(x=corner_min[0], y=corner_min[1], z=corner_min[2], plane='top')
        corner_max = self.estimate_region_coords(x=corner_max[0], y=corner_max[1], z=corner_max[2], plane='top')
        # get roi for intersection
        if self.check_roi():
            driver = ogr.GetDriverByName('GPKG')
            dst_ds = driver.Open(gt.shape_path, 1)
            src_lyr = dst_ds.GetLayerByName('roi')
            for feature in src_lyr:
                roi = feature.GetGeometryRef()
        else:
            corners_shapes_crs = [self.T.mulp(x) for x in corners]
            corners_shapes_crs = [self.chunk.shapes.crs.project(x) for x in corners_shapes_crs]
            roi_geomcol = ogr.Geometry(ogr.wkbGeometryCollection)
            for corner in corners_shapes_crs:
                wkt = "POINT Z (%f %f %f)" % (float(corner[0]), float(corner[1]), float(corner[2]))
                point = ogr.CreateGeometryFromWkt(wkt)
                roi_geomcol.AddGeometry(point)
            roi = roi_geomcol.ConvexHull()
        # create layer
        list = []
        for shape in self.chunk.shapes:
            if shape.group.label == 'TileGrid_layer':
                list.append(shape)
        for i in self.chunk.shapes.groups:
            if i.label == 'TileGrid_layer':
                list.append(i)
        if len(list) > 0:
            self.chunk.shapes.remove(list)
        group = self.chunk.shapes.addGroup()
        group.label = 'TileGrid_layer'
        group.color = (255, 0, 0)
        group.show_labels = True
        self.doc.save()
        # creation tiles
        tile_count = 0
        col = 0
        tile_min = [corner_min[0], corner_min[1], corner_min[2]]
        while tile_min[0] < corner_max[0]:
            row = 0
            tile_min[1] = corner_min[1]
            while tile_min[1] < corner_max[1]:
                tile_max = [tile_min[0] + tile_size, tile_min[1] + tile_size, corner_max[2]]
                ax, ay, az = tile_min[0] - buffer, tile_min[1] - buffer, tile_min[2]
                a = self.estimate_region_coords(x=ax, y=ay, z=az, plane='top').tolist()
                bx, by, bz = tile_min[0] - buffer, tile_max[1] + buffer, tile_min[2]
                b = self.estimate_region_coords(x=bx, y=by, z=bz, plane='top').tolist()
                cx, cy, cz = tile_max[0] + buffer, tile_max[1] + buffer, tile_min[2]
                c = self.estimate_region_coords(x=cx, y=cy, z=cz, plane='top').tolist()
                dx, dy, dz = tile_max[0] + buffer, tile_min[1] - buffer, tile_min[2]
                d = self.estimate_region_coords(x=dx, y=dy, z=dz, plane='top').tolist()
                tile_corners = [a, b, c, d, a]
                # prepare to roi intersection in shapes crs
                ring_ogr = ogr.Geometry(ogr.wkbLinearRing)
                ring = []
                # reproject internal crs to shapes crs
                for point in tile_corners:
                    src_vector = Metashape.Vector(point)
                    dst_vector = self.T.mulp(src_vector)
                    dst_vector = self.chunk.shapes.crs.project(dst_vector)
                    ring.append(dst_vector)
                    ring_ogr.AddPoint(dst_vector.x, dst_vector.y, dst_vector.z)
                polygon = ogr.Geometry(ogr.wkbPolygon)
                polygon.AddGeometry(ring_ogr)
                # intersection + creation
                if polygon.Intersects(roi) or polygon.Contains(roi) or polygon.Within(roi) or polygon.Overlaps(roi):
                    tile_count = tile_count + 1
                    tile_label = "{:02d}".format(row) + '_' + "{:02d}".format(col)
                    shape = self.chunk.shapes.addShape()
                    shape.label = tile_label
                    shape.group = group
                    shape.geometry = Metashape.Geometry.Polygon(ring)
                    shape.boundary_type = Metashape.Shape.BoundaryType.NoBoundary
                    self.doc.save()
                    gt.update_log('Created tile = ' + tile_label)
                row = row + 1
                tile_min[1] = tile_min[1] + tile_size
            col = col + 1
            tile_min[0] = tile_min[0] + tile_size
        dst_ds = None
        gt.update_log('Created tiled grid shapes = ' + str(tile_count) + ' tiles')

    def estimate_distance_line_region(self, point, label=gt.label):
        previous_label = self.chunk.label
        self.set_chunk(label)
        point = numpy.array(point)
        corners = [self.chunk.region.center + self.chunk.region.rot * Metashape.Vector([
            self.chunk.region.size[0] * ((i & 1) - 0.5),
            0.5 * self.chunk.region.size[1] * ((i & 2) - 1),
            0.25 * self.chunk.region.size[2] * ((i & 4) - 2)
        ]) for i in [0, 1, 2, 3, 4, 5, 6, 7]]
        center = numpy.array([self.chunk.region.center.x, self.chunk.region.center.y, self.chunk.region.center.z])
        v01 = corners[1] - corners[0]
        line01 = numpy.copy(center), v01
        plane01 = (line01[1], -numpy.dot(line01[1], point))
        lamb01 = -(numpy.dot(line01[0], plane01[0]) + plane01[1]) / numpy.dot(line01[1], plane01[0])
        point_line01 = line01[0] + lamb01 * line01[1]
        distance01 = numpy.linalg.norm(point - point_line01)
        v02 = corners[2] - corners[0]
        line02 = numpy.copy(center), v02
        plane02 = (line02[1], -numpy.dot(line02[1], point))
        lamb02 = -(numpy.dot(line02[0], plane02[0]) + plane02[1]) / numpy.dot(line02[1], plane02[0])
        point_line02 = line02[0] + lamb02 * line02[1]
        distance02 = numpy.linalg.norm(point - point_line02)
        print(str(center))
        print(str(corners))
        print(str(distance01) + ' ' + str(distance02))
        print(str(point))
        self.set_chunk(previous_label)
        return distance01, distance02

    def estimate_distance_line_tile(self, point, center, label=gt.label):
        previous_label = self.chunk.label
        self.set_chunk(label)
        point = numpy.array(point)
        center = numpy.array(center)
        corners = [self.chunk.region.center + self.chunk.region.rot * Metashape.Vector([
            self.chunk.region.size[0] * ((i & 1) - 0.5),
            0.5 * self.chunk.region.size[1] * ((i & 2) - 1),
            0.25 * self.chunk.region.size[2] * ((i & 4) - 2)
        ]) for i in [0, 1, 2, 3, 4, 5, 6, 7]]
        v01 = corners[1] - corners[0]
        line01 = numpy.copy(center), v01
        plane01 = (line01[1], -numpy.dot(line01[1], point))
        lamb01 = -(numpy.dot(line01[0], plane01[0]) + plane01[1]) / numpy.dot(line01[1], plane01[0])
        point_line01 = line01[0] + lamb01 * line01[1]
        distance01 = numpy.linalg.norm(point - point_line01)
        v02 = corners[2] - corners[0]
        line02 = numpy.copy(center), v02
        plane02 = (line02[1], -numpy.dot(line02[1], point))
        lamb02 = -(numpy.dot(line02[0], plane02[0]) + plane02[1]) / numpy.dot(line02[1], plane02[0])
        point_line02 = line02[0] + lamb02 * line02[1]
        distance02 = numpy.linalg.norm(point - point_line02)
        self.set_chunk(previous_label)
        return distance01, distance02

    def estimate_error_control_points(self):
        self.set_chunk()
        if len(self.chunk.markers) == 0:
            error = 0
            return error
        crs = self.chunk.crs
        if self.chunk.marker_crs:
            transform = Metashape.CoordinateSystem.datumTransform(crs, self.chunk.marker_crs) * self.T
            crs = self.chunk.marker_crs
        ecef_crs = self.chunk.crs.geoccs
        if ecef_crs is None:
            ecef_crs = Metashape.CoordinateSystem('LOCAL')
        sum_sqrt_list = []
        for marker in self.chunk.markers:
            estimated_location = None
            reference_location = None
            error_location = None
            location_ecef = transform.mulp(marker.position)
            estimated_location = Metashape.CoordinateSystem.transform(location_ecef, ecef_crs, crs)
            if marker.reference.location:
                reference_location = marker.reference.location
                error_location = Metashape.CoordinateSystem.transform(estimated_location, crs, ecef_crs) - \
                                 Metashape.CoordinateSystem.transform(reference_location, crs, ecef_crs)
                error_location = crs.localframe(location_ecef).rotation() * error_location
            total = error_location.norm()
            sum_sqrt = total ** 2
            sum_sqrt_list += [sum_sqrt]
        suma = sum(sum_sqrt_list)
        n = len(sum_sqrt_list)
        if not n == 0:
            error = round((suma / n) ** 0.5, 4)
        else:
            error = 'Non value'
        self.set_crs_definition()
        return error

    def estimate_region_coords(self, x, y, z, plane, label=gt.label):
        previous_label = self.chunk.label
        self.set_chunk(label)
        corners = [self.chunk.region.center + self.chunk.region.rot * Metashape.Vector([
            self.chunk.region.size[0] * ((i & 1) - 0.5),
            0.5 * self.chunk.region.size[1] * ((i & 2) - 1),
            0.25 * self.chunk.region.size[2] * ((i & 4) - 2)
        ]) for i in [0, 1, 2, 3, 4, 5, 6, 7]]
        if plane == 'top':
            corner_a = corners[4]
            corner_b = corners[5]
            corner_c = corners[6]
        elif plane == 'center':
            corner_a = (corners[0] + corners[4]) / 2
            corner_b = (corners[1] + corners[5]) / 2
            corner_c = (corners[2] + corners[6]) / 2
        elif plane == 'bottom':
            corner_a = corners[0]
            corner_b = corners[1]
            corner_c = corners[2]
        np_a = numpy.array([corner_a.x, corner_a.y, corner_a.z])
        np_b = numpy.array([corner_b.x, corner_b.y, corner_b.z])
        np_c = numpy.array([corner_c.x, corner_c.y, corner_c.z])
        normal = numpy.cross(np_b - np_a, np_c - np_a)
        # ax + by + cz + d = 0
        # a = normal[0]
        # b = normal[1]
        # c = normal[2]
        d = -numpy.dot(normal, np_a)
        plane_ec = (normal, d)
        normalize = numpy.linalg.norm(normal)
        nomalized_normal = normal / normalize
        point = numpy.array((x, y, z))
        line_ec = numpy.copy(point), nomalized_normal
        lamb = -(numpy.dot(line_ec[0], plane_ec[0]) + plane_ec[1]) / numpy.dot(line_ec[1], plane_ec[0])
        vector = line_ec[0] + lamb * line_ec[1]
        self.set_chunk(previous_label)
        return vector

    def export_roi_shape(self, label=gt.label):
        self.set_chunk(label)
        self.set_crs_definition()
        driver = ogr.GetDriverByName('GPKG')
        dst_ds = driver.CreateDataSource(gt.shape_path)
        dst_lyr = dst_ds.CreateLayer('roi',
                                     geom_type=ogr.wkbPolygon,
                                     srs=self.shapes_crs_osgeo)
        polygon = ogr.Geometry(ogr.wkbPolygon)
        if gt.params.get("ROI")["Method"] == '0':
            geomcol = ogr.Geometry(ogr.wkbGeometryCollection)
            corners = [self.T.mulp(self.chunk.region.center + self.chunk.region.rot * Metashape.Vector([
                self.chunk.region.size[0] * ((i & 1) - 0.5),
                0.5 * self.chunk.region.size[1] * ((i & 2) - 1),
                0.25 * self.chunk.region.size[2] * ((i & 4) - 2)
            ])) for i in [0, 1, 2, 3, 4, 5, 6, 7]]
            corners = [self.chunk.shapes.crs.project(x) for x in corners]
            for corner in corners:
                wkt = "POINT Z (%f %f %f)" % (float(corner.x), float(corner.y), float(corner.z))
                point = ogr.CreateGeometryFromWkt(wkt)
                geomcol.AddGeometry(point)
            polygon = geomcol.ConvexHull()
        elif gt.params.get("ROI")["Method"] == 'SHP':
            ring = ogr.Geometry(ogr.wkbLinearRing)
            for shape in self.chunk.shapes:
                if shape.group.label == 'ROI_layer':
                    for vertice in shape.geometry.coordinates[0]:
                        dst_vector = Metashape.CoordinateSystem.transform(vertice, self.chunk.shapes.crs, self.chunk.shapes.crs)
                        ring.AddPoint(dst_vector.x, dst_vector.y, dst_vector.z)
                    polygon.AddGeometry(ring)
        new_feature = ogr.Feature(dst_lyr.GetLayerDefn())
        new_feature.SetGeometry(polygon)
        dst_lyr.CreateFeature(new_feature)
        dst_ds = None
        gt.update_log('Exported shape of region of interest')

    def export_dems(self, label='Merged Chunk'):
        self.set_chunk(label)
        label_dem = gt.params.get("SplitTile")["MergedDEM"]
        if float(gt.params.get("Project")["DemGSD"]) > 0:
            self.chunk.exportRaster(
                path=os.path.join(gt.output_path,
                                  gt.label + '_' + label_dem.lower() + '_' + str(
                                      int(float(gt.params.get("Project")["DemGSD"]) * 1000)) + 'mm.tif'),
                source_data=Metashape.ElevationData,
                resolution=float(gt.params.get("Project")["DemGSD"]),
                image_compression=self.image_compression,
                clip_to_boundary=True,
                save_alpha=True,
            )
            gt.update_log(
                'Exported full ' + label_dem + ':\nGSD = ' + str(gt.params.get("Project")["DemGSD"]) + ' m')
        else:
            self.chunk.elevation = self.chunk.elevations[0]
            resolution = round(self.chunk.elevation.resolution, ndigits=3)
            self.chunk.exportRaster(
                path=os.path.join(gt.output_path,
                                  gt.label + '_' + label_dem.lower() + '_' + str(
                                      int(float(resolution) * 1000)) + 'mm.tif'),
                source_data=Metashape.ElevationData,
                image_compression=self.image_compression,
                clip_to_boundary=True,
                save_alpha=True,
            )
            gt.update_log('Exported full ' + label_dem + ':\nGSD = ' + str(resolution) + ' m')

    def export_orthomosaic(self, label='Merged Chunk'):
        self.set_chunk(label)
        if float(gt.params.get("Project")["DemGSD"]) > 0:
            self.chunk.exportRaster(
                path=os.path.join(gt.output_path,
                                  gt.label + '_orthomosaic_' + str(
                                      int(float(gt.params.get("Project")["DemGSD"]) * 1000)) + 'mm.tif'),
                source_data=Metashape.OrthomosaicData,
                resolution=float(gt.params.get("Project")["DemGSD"]),
                image_compression=self.image_compression,
                clip_to_boundary=True,
                save_alpha=True,
            )
            gt.update_log(
                'Exported full orthomosaic:\nGSD = ' + str(gt.params.get("Project")["DemGSD"]) + ' m')
        else:
            self.chunk.elevation = self.chunk.elevations[0]
            resolution = round(self.chunk.elevation.resolution, ndigits=3)
            self.chunk.exportRaster(
                path=os.path.join(gt.output_path,
                                  gt.label + '_orthomosaic_' + str(
                                      int(float(resolution) * 1000)) + 'mm.tif'),
                source_data=Metashape.OrthomosaicData,
                image_compression=self.image_compression,
                clip_to_boundary=True,
                save_alpha=True,
            )
            gt.update_log('Exported full orthomosaic:\nGSD = ' + str(resolution) + ' m')

    def export_pointcloud(self, label='Merged Chunk'):
        self.set_chunk(label)
        self.chunk.exportPointCloud(
            path=os.path.join(gt.output_path, gt.label + '_point_cloud.las'),
            source_data=Metashape.PointCloudData,
            crs=self.project_crs,
            clip_to_boundary=True,
            save_point_color=True,
            save_point_normal=False,
            save_point_intensity=True,
            save_point_classification=True,
            save_point_confidence=True,
            save_point_return_number=False,
            save_point_scan_angle=False,
            save_point_source_id=False,
            save_point_timestamp=False,
            save_point_index=False,
        )
        gt.update_log('Exported full dense point cloud')

    def export_tile_grid(self, output_path=gt.shape_path, label=gt.label):
        self.set_chunk(label)
        driver = ogr.GetDriverByName('GPKG')
        if output_path == gt.shape_path:
            dst_ds = driver.Open(output_path, 1)
            for i in range(dst_ds.GetLayerCount()):
                dst_lyr = dst_ds.GetLayerByIndex(i)
                if dst_lyr.GetName() == 'tile':
                    dst_ds.DeleteLayer(i)
                    break
        else:
            dst_ds = driver.CreateDataSource(output_path)
        dst_lyr = dst_ds.CreateLayer('tile',
                                     geom_type=ogr.wkbPolygon,
                                     srs=self.shapes_crs_osgeo)
        dst_lyr.CreateField(ogr.FieldDefn("label", ogr.OFTString))
        dst_lyr.CreateField(ogr.FieldDefn("ignore", ogr.OFTInteger))
        for shape in self.chunk.shapes:
            if shape.group.label == 'TileGrid_layer':
                ring = ogr.Geometry(ogr.wkbLinearRing)
                for vertice in shape.geometry.coordinates[0]:
                    ring.AddPoint(vertice.x, vertice.y, vertice.z)
                polygon = ogr.Geometry(ogr.wkbPolygon)
                polygon.AddGeometry(ring)
                new_feature = ogr.Feature(dst_lyr.GetLayerDefn())
                new_feature.SetGeometry(polygon)
                new_feature.SetField('label', shape.label)
                new_feature.SetField('ignore', 0)
                dst_lyr.CreateFeature(new_feature)
        dst_ds = None

    def import_gcps(self, label=gt.label):
        self.set_chunk(label)
        self.chunk.importReference(
            path=gt.params.get("OptimizeAlignment")["Path"],
            columns='nxyz',
            create_markers=True,
            crs=self.gcp_crs,
            delimiter=";",
            skip_rows=0,
        )
        self.set_crs_definition()
        self.doc.save()
        gt.update_log('Imported GCP file =\n' +
                      gt.params.get("OptimizeAlignment")["Path"])

    def import_markers(self, label=gt.label):
        self.set_chunk(label)
        gt.update_log('Imported markers file =\n' +
                      gt.params.get("OptimizeAlignment")["Path"])
        self.chunk.importMarkers(path=gt.params.get("OptimizeAlignment")["Path"])
        self.set_crs_definition()
        self.doc.save()

    def import_photos(self, label=gt.label):
        self.set_chunk(label)
        photos = gt.find_files(gt.params.get("Photo")["Path"], [".jpg", ".jpeg", ".tif", ".tiff"])
        if gt.params.get("Photo")["Method"] == 'EXIF':
            self.chunk.addPhotos(
                filenames=photos,
                strip_extensions=False,
            )
        elif gt.params.get("Photo")["Method"] == 'CSV':
            if os.path.isfile(gt.params.get("Photo")["EoPath"]) and os.path.exists(gt.params.get("Photo")["EoPath"]):
                self.chunk.addPhotos(
                    filenames=photos,
                    load_reference=False,
                    strip_extensions=False,
                )
                self.chunk.importReference(
                    path=gt.params.get("Photo")["EoPath"],
                    columns='nxyz',
                    create_markers=False,
                    crs=self.photos_crs,
                    delimiter=";",
                    skip_rows=0,
                )
                self.chunk.updateTransform()
            else:
                gt.update_log('ERROR: No csv file with external orientations found.')
                raise SystemExit(0)
        else:
            self.chunk.addPhotos(photos)
        self.chunk.camera_location_accuracy = self.photos_location_accuracy
        self.set_crs_definition()
        self.doc.save()
        params = {
            "f": "F", "cx": "Cx", "cy": "Cy",
            "k1": "K1", "k2": "K2", "k3": "K3", "k4": "K4",
            "p1": "P1", "p2": "P2",
            "b1": "B1", "b2": "B2"
        }
        fixed_params = []
        unfixed_params = []
        for key, value in gt.params.get("CameraCalibration").items():
            if value == "True":
                unfixed_params.append(params[key])
            else:
                fixed_params.append(params[key])
        sensor = self.chunk.sensors[0]
        sensor.fixed = True
        sensor.fixed_params = fixed_params
        self.doc.save()
        gt.update_log('CRS applied on: \n'
                      'EPSG Project = ' + str(gt.params.get("Project")["EPSG"]) + '\n' +
                      'EPSG Photos = ' + str(gt.params.get("Photo")["EPSG"]) + '\n' +
                      'EPSG GCPs = ' + str(gt.params.get("OptimizeAlignment")["EPSG"]) + '\n' +
                      'Fixed internal orientation parameters = ' + str(fixed_params)[1:-1].replace("'", "") + '\n' +
                      'Calibrated internal orientation parameters = ' + str(unfixed_params)[1:-1].replace("'", ""))
        gt.update_log('Loaded photos = ' + str(len(self.chunk.cameras)) + ' photos\n' +
                      'Photos location horizontal accuracy = ' +
                      str(gt.params.get("Photo")["LocationAccuracy2D"]) + ' m\n' +
                      'Photos location vertical accuracy = ' +
                      str(gt.params.get("Photo")["LocationAccuracyHeight"]) + ' m')

    def import_roi(self, label=gt.label):
        self.set_chunk(label)
        if self.check_roi():
            self.set_crs_definition()
            group = self.chunk.shapes.addGroup()
            group.label = 'ROI_layer'
            group.color = (0, 0, 0)
            group.show_labels = True
            self.doc.save()
            driver = ogr.GetDriverByName('ESRI Shapefile')
            src_ds = driver.Open(gt.params.get("ROI")["Path"], 1)
            src_lyr = src_ds.GetLayer()
            for feature in src_lyr:
                roi = feature.GetGeometryRef()
                ring = roi.GetGeometryRef(0)
                points = ring.GetPointCount()
                ring_ecef = []
                for i in range(points):
                    lon, lat, z = ring.GetPoint(i)
                    vector = Metashape.Vector([lon, lat, z])
                    vector_ecef = Metashape.CoordinateSystem.transform(vector, self.chunk.shapes.crs, self.chunk.shapes.crs)
                    ring_ecef.append(vector_ecef)
                shape = self.chunk.shapes.addShape()
                shape.group = group
                shape.geometry = Metashape.Geometry.Polygon(ring_ecef)
                shape.label = 'ROI'
                shape.boundary_type = Metashape.Shape.BoundaryType.OuterBoundary
            self.doc.save()
            gt.update_log('Imported region of interest =\n' + gt.params.get("ROI")["Path"])

    def import_tile_grid(self, label=gt.label):
        self.set_chunk(label)
        path = gt.params.get("SplitTile")["Path"]
        label_shape = "TileGrid_layer"
        list = []
        for shape in self.chunk.shapes:
            if shape.group.label == label_shape:
                list.append(shape)
        self.chunk.shapes.remove(list)
        for group in self.chunk.shapes.groups:
            if group.label == label_shape:
                self.chunk.shapes.remove(group)
        self.doc.save()
        group = self.chunk.shapes.addGroup()
        group.label = label_shape
        group.color = (255, 0, 0)
        group.show_labels = True
        self.doc.save()
        driver = ogr.GetDriverByName('GPKG')
        dst_ds = driver.Open(path, 0)
        dst_lyr = dst_ds.GetLayerByName('tile')
        for feature in dst_lyr:
            ignore = feature.GetField('ignore')
            if ignore == 0:
                polygon = feature.GetGeometryRef()
                ring = polygon.GetGeometryRef(0)
                points = ring.GetPointCount()
                polygon_2import = []
                for p in range(points):
                    lon, lat, z = ring.GetPoint(p)
                    vertice = Metashape.Vector([lon, lat, z])
                    polygon_2import.append(vertice)
                new_shape = self.chunk.shapes.addShape()
                new_shape.group = group
                new_shape.label = feature.GetField('label')
                new_shape.geometry.type = Metashape.Geometry.Type.PolygonType
                new_shape.geometry = Metashape.Geometry.Polygon(polygon_2import)
                new_shape.boundary_type = Metashape.Shape.BoundaryType.NoBoundary
                self.doc.save()
        self.set_z_shape(label_shape=label_shape)
        self.doc.save()
        gt.update_log('Imported tiled grid shapes from file =\n' + path)

    def initial_psx(self, label=gt.label):
        self.doc = Metashape.Document()
        self.doc.save(gt.project_path)
        self.chunk = self.doc.addChunk()
        self.chunk.label = label
        self.set_crs_definition()
        self.doc.save()
        gt.update_log('Created Metashape project')

    def merge_chunks(self, label=gt.label):
        self.set_chunk(label)
        psxs = gt.read_chunks()
        for psx in psxs:
            path = os.path.join(gt.output_path, psx + '_project.psx')
            doc_tile = Metashape.Document()
            doc_tile.open(path)
            self.doc.append(document=doc_tile)
            self.doc.save()
        self.doc.mergeChunks(
            copy_laser_scans=False,
            copy_models=False,
            copy_tiled_models=False,
            merge_markers=False,
            merge_tiepoints=False,
            merge_assets=True,
            copy_depth_maps=True,
            copy_point_clouds=eval(gt.params.get("SplitTile")["MergePointClouds"]),
            copy_elevations=eval(gt.params.get("SplitTile")["MergeElevations"]),
            copy_orthomosaics=eval(gt.params.get("SplitTile")["MergeOrthomosaics"]),
            chunks=[chunk.key for chunk in self.doc.chunks])
        self.doc.remove(self.doc.chunks[1:-1])
        self.doc.save()

    def merge_dems(self):
        psxs = gt.read_chunks()
        for label_dem in ["DSM", "DTM"]:
            gsd = int(float(gt.params.get("Project")["DemGSD"])*1000)
            dst_path = os.path.join(gt.output_path,
                                    gt.label + '_' + label_dem.lower() + '_' + str(gsd) + 'mm.tif')
            files = [os.path.join(gt.output_path,
                                  psx + '_' + label_dem.lower() + '_' + str(gsd) + 'mm.tif')
                     for psx in psxs]
            options = gdal.WarpOptions(
                format="GTiff",
                creationOptions=["COMPRESS=LZW", "TILED=YES", "BIGTIFF=IF_NEEDED"]
            )
            g = gdal.Warp(dst_path, files, options=options)
            g = None
            gt.update_log('Merged full ' + label_dem + ':\nGSD = ' + str(gsd) + ' mm')

    def merge_orthomosaic(self):
        psxs = gt.read_chunks()
        gsd = int(float(gt.params.get("Project")["OrthoGSD"])*1000)
        dst_path = os.path.join(gt.output_path,
                                gt.label + '_orthomosaic_' + str(gsd) + 'mm.tif')
        files = [os.path.join(gt.output_path,
                              psx + '_orthomosaic_' + str(gsd) + 'mm.tif')
                 for psx in psxs]
        options = gdal.WarpOptions(
            format="GTiff",
            creationOptions=["COMPRESS=LZW", "TILED=YES", "BIGTIFF=IF_NEEDED"]
        )
        g = gdal.Warp(dst_path, files, options=options)
        g = None
        gt.update_log('Merged full orthomosaic:\nGSD = ' + str(gsd) + ' mm')

    def merge_pointclouds(self):
        psxs = gt.read_chunks()
        tmp_offset = [1e100, 1e100, 1e100]
        n_max = 2000000000
        dic_rows = {}
        n = 0
        for psx in psxs:
            src_path = os.path.join(gt.output_path, psx + '_point_cloud.las')
            src_las = laspy.read(src_path)
            row = psx.split('_')[0]
            points = len(src_las.points)
            n = n + points
            try:
                previous = dic_rows[row]
                dic_rows[row] = previous + points
            except:
                dic_rows[row] = points
            src_path = os.path.join(gt.output_path, psx + '_point_cloud.las')
            src_las = laspy.read(src_path)
            src_offset = src_las.header.offset
            tmp_offset[0] = min(tmp_offset[0], src_offset[0])
            tmp_offset[1] = min(tmp_offset[1], src_offset[1])
            tmp_offset[2] = min(tmp_offset[2], src_offset[2])
        if n < n_max:
            dst_path = os.path.join(gt.output_path, gt.label + '_point_cloud.laz')
            dst_las = laspy.LasData(src_las.header)
            dst_las.header.offset = tmp_offset
            dst_las.write(dst_path)
            for psx in psxs:
                src_path = os.path.join(gt.output_path, psx + '_point_cloud.las')
                src_las = laspy.read(src_path)
                with laspy.open(dst_path, mode='a') as dst_las:
                    with laspy.open(src_path, mode='r') as src_las:
                        for points in src_las.chunk_iterator(2_000_000):
                            points.change_scaling(offsets=tmp_offset)
                            dst_las.append_points(points)
            gt.update_log('Merged full dense point cloud')
        else:
            dic_files = {}
            n_file = 0
            file_id = 0
            rows_to_append = []
            for row in dic_rows:
                if n_file + dic_rows[row] < n_max:
                    rows_to_append.append(row)
                    n_file = n_file + dic_rows[row]
                else:
                    dic_files[file_id] = rows_to_append
                    rows_to_append = []
                    n_file = 0
                    file_id = file_id + 1
                    rows_to_append.append(row)
                    n_file = n_file + dic_rows[row]
            dic_files[file_id] = rows_to_append
            for file in dic_files:
                dst_path = os.path.join(gt.output_path, gt.label + '_point_cloud' + str(file) + '.laz')
                tmp_offset = [1e100, 1e100, 1e100]
                for psx in psxs:
                    row = psx.split('_')[0]
                    if row in dic_files[file]:
                        src_path = os.path.join(gt.output_path, psx + '_point_cloud.las')
                        src_las = laspy.read(src_path)
                        src_offset = src_las.header.offset
                        tmp_offset[0] = min(tmp_offset[0], src_offset[0])
                        tmp_offset[1] = min(tmp_offset[1], src_offset[1])
                        tmp_offset[2] = min(tmp_offset[2], src_offset[2])
                dst_las = laspy.LasData(src_las.header)
                dst_las.header.offset = tmp_offset
                dst_las.write(dst_path)
                for psx in psxs:
                    row = psx.split('_')[0]
                    if row in dic_files[file]:
                        src_path = os.path.join(gt.output_path, psx + '_point_cloud.las')
                        src_las = laspy.read(src_path)
                        with laspy.open(dst_path, mode='a') as dst_las:
                            with laspy.open(src_path, mode='r') as src_las:
                                for points in src_las.chunk_iterator(2_000_000):
                                    points.change_scaling(offsets=tmp_offset)
                                    dst_las.append_points(points)
                gt.update_log('Merged full dense point cloud (' + str(n_max) + 'points) = ' +
                              str(file + 1) + '/' + str(len(dic_files)) + 'point clouds')

    def optimize_alignment(self, label=gt.label):
        self.set_chunk(label)
        self.chunk.exportMarkers(
            path=os.path.join(gt.output_path, label + '_markers.xml'),
            crs=self.project_crs,
        )
        projections = sum([len(marker.projections) for marker in self.chunk.markers])
        gt.update_log('Founded markers projections = ' + str(projections) + ' projections\n' +
                      'Error control points = ' + str(self.estimate_error_control_points()) + ' m\n' +
                      'Adjusted focal = ' + str(round(self.chunk.sensors[0].calibration.f, 4)) + ' pix')
        self.chunk.updateTransform()
        self.doc.save()
        self.doc.save(gt.project_path.replace(".psx", "_initial.psx"))
        self.set_chunk(label)
        self.chunk.optimizeCameras(
            adaptive_fitting=False,
            fit_b1=eval(gt.params.get("CameraCalibration")["b1"]),
            fit_b2=eval(gt.params.get("CameraCalibration")["b2"]),
            fit_corrections=False,
            fit_cx=eval(gt.params.get("CameraCalibration")["cx"]),
            fit_cy=eval(gt.params.get("CameraCalibration")["cy"]),
            fit_f=eval(gt.params.get("CameraCalibration")["f"]),
            fit_k1=eval(gt.params.get("CameraCalibration")["k1"]),
            fit_k2=eval(gt.params.get("CameraCalibration")["k2"]),
            fit_k3=eval(gt.params.get("CameraCalibration")["k3"]),
            fit_k4=eval(gt.params.get("CameraCalibration")["k4"]),
            fit_p1=eval(gt.params.get("CameraCalibration")["p1"]),
            fit_p2=eval(gt.params.get("CameraCalibration")["p2"]),
            tiepoint_covariance=False,
        )
        self.doc.save()
        self.chunk.updateTransform()
        self.doc.save()
        gt.update_log('Optimized alignment done:\n' +
                      'Error control points = ' + str(self.estimate_error_control_points()) + ' m\n' +
                      'Adjusted focal = ' + str(round(self.chunk.sensors[0].calibration.f, 4)) + ' pix')

    def preprocess(self, label=gt.label):
        self.set_chunk(label)
        params_acc = {
            "Highest": 0,
            "High": 1,
            "Medium": 2,
            "Low": 4,
            "Lowest": 8
        }
        params_ref = {
            "Source": Metashape.ReferencePreselectionSource,
            "Estimated": Metashape.ReferencePreselectionEstimated,
            "Sequential": Metashape.ReferencePreselectionSequential
        }
        if not gt.params.get("OptimizeAlignment")["ReferencePreselection"]:
            preselection = False
            preselection_mode = Metashape.ReferencePreselectionSource
        else:
            preselection = True
            preselection_mode = params_ref[gt.params.get("OptimizeAlignment")["ReferencePreselection"]]
        self.chunk.matchPhotos(
            downscale=params_acc[gt.params.get("OptimizeAlignment")["Accuracy"]],
            generic_preselection=True,
            reference_preselection=preselection,
            reference_preselection_mode=preselection_mode,
            keypoint_limit=40000,
            tiepoint_limit=gt.params.get("OptimizeAlignment")["TiePointLimit"],
            filter_stationary_points=True
        )
        self.doc.save()
        self.chunk.alignCameras(adaptive_fitting=False)
        self.doc.save()
        aligned = [camera for camera in self.chunk.cameras if
                   camera.transform and camera.type == Metashape.Camera.Type.Regular]
        gt.update_log('Matched and aligned photos = ' +
                      str(len(aligned)) + '/' + str(len(self.chunk.cameras)) + ' photos')

    def process_dems(self, label=gt.label):
        self.set_chunk(label)
        if len(self.chunk.elevations) < 2 and not self.chunk.point_cloud is None:
            if len(self.chunk.elevations) == 1:
                self.chunk.remove(self.chunk.elevations[0])
            self.chunk.buildDem(source_data=Metashape.PointCloudData)
            self.chunk.elevation.label = 'DSM'
            self.doc.save()
            if float(gt.params.get("Project")["DemGSD"]) > 0:
                self.chunk.exportRaster(
                    path=os.path.join(gt.output_path,
                                      label + '_dsm_' + str(
                                          int(float(gt.params.get("Project")["DemGSD"]) * 1000)) + 'mm.tif'),
                    source_data=Metashape.ElevationData,
                    resolution=float(gt.params.get("Project")["DemGSD"]),
                    image_compression=self.image_compression,
                    clip_to_boundary=True,
                    save_alpha=True,
                )
                gt.update_log('Completed DSM for chunk ' + label + ':\nGSD = ' + str(gt.params.get("Project")["DemGSD"]) + ' m')
            else:
                self.chunk.elevation = self.chunk.elevations[0]
                resolution = round(self.chunk.elevation.resolution, ndigits=3)
                self.chunk.exportRaster(
                    path=os.path.join(gt.output_path,
                                      label + '_dsm_' + str(
                                          int(float(resolution) * 1000)) + 'mm.tif'),
                    source_data=Metashape.ElevationData,
                    image_compression=self.image_compression,
                    clip_to_boundary=True,
                    save_alpha=True,
                )
                gt.update_log('Completed DSM for chunk ' + label + ':\nGSD = ' + str(resolution) + ' m')
            self.chunk.buildDem(
                source_data=Metashape.PointCloudData,
                interpolation=Metashape.Interpolation.Extrapolated,
                classes=[2],
            )
            self.doc.save()
            self.chunk.elevation = self.chunk.elevations[1]
            self.chunk.elevation.label = 'DTM'
            self.doc.save()
            if float(gt.params.get("Project")["DemGSD"]) > 0:
                self.chunk.exportRaster(
                    path=os.path.join(gt.output_path,
                                      label + '_dtm_' + str(
                                          int(float(gt.params.get("Project")["DemGSD"]) * 1000)) + 'mm.tif'),
                    source_data=Metashape.ElevationData,
                    resolution=float(gt.params.get("Project")["DemGSD"]),
                    image_compression=self.image_compression,
                    clip_to_boundary=True,
                    save_alpha=True,
                )
                gt.update_log('Completed DTM for chunk ' + label + ':\nGSD = ' + str(gt.params.get("Project")["DemGSD"]) + ' m')
            else:
                resolution = round(self.chunk.elevation.resolution, ndigits=3)
                self.chunk.exportRaster(
                    path=os.path.join(gt.output_path,
                                      label + '_dtm_' + str(
                                          int(float(resolution) * 1000)) + 'mm.tif'),
                    source_data=Metashape.ElevationData,
                    image_compression=self.image_compression,
                    clip_to_boundary=True,
                    save_alpha=True,
                )
                gt.update_log('Completed DTM for chunk ' + label + ':\nGSD = ' + str(resolution) + ' m')
        else:
            gt.update_log('Founded DEMs for chunk ' + label)

    def process_orthomosaic(self, label=gt.label):
        self.set_chunk(label)
        if len(self.chunk.elevations) == 0:
            return
        self.chunk.elevation = self.chunk.elevations[0]
        if len(self.chunk.orthomosaics) == 0:
            self.chunk.buildOrthomosaic(
                surface_data=Metashape.ElevationData,
                blending_mode=Metashape.MosaicBlending,
                fill_holes=True,
                refine_seamlines=False,
            )
            self.doc.save()
            if float(gt.params.get("Project")["OrthoGSD"]) > 0:
                self.chunk.exportRaster(
                    path=os.path.join(gt.output_path,
                                      label + '_orthomosaic_' + str(
                                          int(float(gt.params.get("Project")["OrthoGSD"]) * 1000)) + 'mm.tif'),
                    source_data=Metashape.OrthomosaicData,
                    resolution=float(gt.params.get("Project")["OrthoGSD"]),
                    image_compression=self.image_compression,
                    clip_to_boundary=True,
                    save_alpha=True,
                )
                gt.update_log('Completed orthomosaic for chunk ' + label + ':\nGSD = ' + str(gt.params.get("Project")["OrthoGSD"]) + ' m')
            else:
                resolution = round(self.chunk.orthomosaic.resolution, ndigits=3)
                self.chunk.exportRaster(
                    path=os.path.join(gt.output_path,
                                      label + '_orthomosaic_' + str(
                                          int(float(resolution) * 1000)) + 'mm.tif'),
                    source_data=Metashape.OrthomosaicData,
                    image_compression=self.image_compression,
                    clip_to_boundary=True,
                    save_alpha=True,
                )
                gt.update_log('Completed orthomosaic for chunk ' + label + ':\nGSD = ' + str(resolution) + ' m')
        else:
            gt.update_log('Founded orthomosaic for chunk ' + label)

    def process_point_cloud(self, label=gt.label):
        self.set_chunk(label)
        params_quality = {
            "Ultrahigh": 1,
            "High": 2,
            "Medium": 4,
            "Low": 8,
            "Lowest": 16
        }
        params_filter = {
            "False": Metashape.NoFiltering,
            "Mild": Metashape.MildFiltering,
            "Moderate": Metashape.ModerateFiltering,
            "Aggressive": Metashape.AggressiveFiltering
        }
        if self.chunk.depth_maps is None or self.chunk.point_cloud is None:
            self.chunk.buildDepthMaps(
                downscale=params_quality[gt.params.get("PointCloud")["Quality"]],
                filter_mode=params_filter[gt.params.get("PointCloud")["FilterMode"]],
            )
            self.doc.save()
            if self.chunk.depth_maps is None:
                files = gt.find_files(folder=gt.output_path, types=['.psx'])
                for file in files:
                    if label in file:
                        os.remove(file)
                        del self.doc
                        shutil.rmtree(file.replace('.psx', '.files'))
                        gt.update_log('No points and removed chunk ' + label)
                        return
            self.chunk.buildPointCloud(point_confidence=True)
            self.doc.save()
            gt.update_log('Completed dense point cloud for chunk ' +
                          label + ' = ' + str(self.chunk.point_cloud.point_count) + ' points')
            if self.chunk.point_cloud.point_count == 0:
                files = gt.find_files(folder=gt.output_path, types=['.psx'])
                for file in files:
                    if label in file:
                        os.remove(file)
                        del self.doc
                        shutil.rmtree(file.replace('.psx', '.files'))
                        gt.update_log('No points and removed chunk ' + label)
                        return
            else:
                self.chunk.point_cloud.setConfidenceFilter(
                    gt.params.get("PointCloud")["ConfidenceRangeMin"],
                    gt.params.get("PointCloud")["ConfidenceRangeMax"]
                )
                self.chunk.point_cloud.removePoints(list(range(128)))
                self.chunk.point_cloud.resetFilters()
                self.chunk.point_cloud.compactPoints()
                self.doc.save()
                gt.update_log('Filtered dense point cloud for chunk ' +
                              label + ' = ' + str(self.chunk.point_cloud.point_count) + ' points')
            if self.chunk.point_cloud.point_count == 0:
                files = gt.find_files(folder=gt.output_path, types=['.psx'])
                for file in files:
                    if label in file:
                        os.remove(file)
                        del self.doc
                        shutil.rmtree(file.replace('.psx', '.files'))
                        gt.update_log('No points and removed chunk ' + label)
                        break
            else:
                self.chunk.point_cloud.assignClass(0)
                self.doc.save()
                self.chunk.point_cloud.classifyGroundPoints(
                    max_angle=gt.params.get("PointCloud")["GroundMaxAngle"],
                    max_distance=gt.params.get("PointCloud")["GroundMaxDistance"],
                    max_terrain_slope=gt.params.get("PointCloud")["GroundMaxSlope"],
                    cell_size=gt.params.get("PointCloud")["GroundCellSize"],
                    erosion_radius=gt.params.get("PointCloud")["GroundErosionRadius"]
                )
                self.doc.save()
                self.chunk.exportPointCloud(
                    path=os.path.join(gt.output_path, label + '_point_cloud.las'),
                    source_data=Metashape.PointCloudData,
                    crs=self.project_crs,
                    # clip_to_boundary=True,
                    clip_to_boundary=False,
                    save_point_color=True,
                    save_point_normal=False,
                    save_point_intensity=True,
                    save_point_classification=True,
                    save_point_confidence=True,
                    save_point_return_number=False,
                    save_point_scan_angle=False,
                    save_point_source_id=False,
                    save_point_timestamp=False,
                    save_point_index=False,
                )
                # TODO get ground count
                gt.update_log('Classified ground in dense point cloud for chunk ' + label)
        else:
            gt.update_log('Founded dense point cloud for chunk ' + label)

    def process_report(self, label=gt.label):
        self.set_chunk(label)
        self.chunk.exportReport(
            path=os.path.join(gt.output_path, label + '_report.pdf'),
            include_system_info=False,
            title='Automatic process report for ' + label,
        )
        gt.update_log('Completed report')

    def set_chunk(self, label=gt.label):
        if label == gt.label or label == 'Merged Chunk':
            path = gt.project_path
        else:
            path = os.path.join(gt.output_path, label + '_project.psx')
        if os.path.isfile(path) and os.path.exists(path):
            self.doc = Metashape.Document()
            self.doc.open(path)
            for chunk in self.doc.chunks:
                if chunk.label == label:
                    self.chunk = chunk
            self.set_crs_definition()
        else:
            self.initial_psx(label=label)
        self.chunk.updateTransform()
        self.doc.save()
        self.T = self.chunk.transform.matrix

    def set_crs_definition(self):
        self.check_geoids()
        epsg = gt.params.get("Project")["EPSG"]
        self.project_crs_osgeo = ogr.osr.SpatialReference()
        self.project_crs = Metashape.CoordinateSystem('EPSG::' + epsg)
        self.chunk.crs = self.project_crs
        self.chunk.crs.init('EPSG::' + epsg)
        if not gt.params.get("Photo")["EPSG"] == "0":
            self.photos_crs = Metashape.CoordinateSystem('EPSG::' + gt.params.get("Photo")["EPSG"])
            self.chunk.camera_crs = self.photos_crs
            self.chunk.camera_crs.init('EPSG::' + gt.params.get("Photo")["EPSG"])
        if not gt.params.get("OptimizeAlignment")["EPSG"] == "0":
            self.gcp_crs = Metashape.CoordinateSystem('EPSG::' + gt.params.get("OptimizeAlignment")["EPSG"])
            self.chunk.marker_crs = self.gcp_crs
            self.chunk.marker_crs.init('EPSG::' + gt.params.get("OptimizeAlignment")["EPSG"])
        self.chunk.updateTransform()
        if '+' in epsg:
            epsg_horizontal, epsg_vertical = epsg.split('+')
            srs_horizontal = ogr.osr.SpatialReference()
            srs_horizontal.ImportFromEPSG(int(epsg_horizontal))
            srs_vertical = ogr.osr.SpatialReference()
            srs_vertical.ImportFromEPSG(int(epsg_vertical))
            self.project_crs_osgeo.SetCompoundCS('', srs_horizontal, srs_vertical)
        else:
            self.project_crs_osgeo.ImportFromEPSG(int(epsg))
        if self.chunk.shapes is None:
            self.chunk.shapes = Metashape.Shapes()
        epsg = 4326
        self.chunk.shapes.crs = Metashape.CoordinateSystem('EPSG::' + str(epsg))
        self.shapes_crs_osgeo = ogr.osr.SpatialReference()
        self.shapes_crs_osgeo.ImportFromEPSG(epsg)

    def set_region(self, label=gt.label):
        self.set_chunk(label)
        self.chunk.resetRegion()
        original_region = self.chunk.region
        self.chunk.updateTransform()
        self.doc.save()
        shape_2_iterate = False
        if label == gt.label and self.check_roi():
            for shape in self.chunk.shapes:
                if shape.group.label == 'ROI_layer':
                    shape_2_iterate = shape
                else:
                    continue
        else:
            for shape in self.chunk.shapes:
                if shape.group.label == 'TileROI_layer':
                    shape_2_iterate = shape
                else:
                    continue
        # set center
        if shape_2_iterate == False:
            return
        for vertice in shape_2_iterate.geometry.coordinates[0]:
            new_tmp = self.chunk.shapes.crs.unproject(vertice)
            new = self.T.inv().mulp(new_tmp)
            if not 'M' in locals() or not 'm' in locals():
                M = Metashape.Vector([new.x, new.y, new.z])
                m = Metashape.Vector([new.x, new.y, new.z])
            M[0] = max(M[0], new.x)
            M[1] = max(M[1], new.y)
            M[2] = max(M[2], new.z)
            m[0] = min(m[0], new.x)
            m[1] = min(m[1], new.y)
            m[2] = min(m[2], new.z)
        M = Metashape.Vector(self.estimate_region_coords(x=M[0], y=M[1], z=M[2], plane='center').tolist())
        m = Metashape.Vector(self.estimate_region_coords(x=m[0], y=m[1], z=m[2], plane='center').tolist())
        center = (M + m) / 2
        self.chunk.region.center = center
        self.chunk.updateTransform()
        self.doc.save()
        # set size
        size = M - m
        size[2] = original_region.size.z
        self.chunk.region.size = size
        self.chunk.region.rot = Metashape.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.chunk.updateTransform()
        self.doc.save()

    def set_z_shape(self, label_shape, label=gt.label):
        self.set_chunk(label)
        group_tmp = self.chunk.shapes.addGroup()
        group_tmp.label = 'tmp_layer'
        self.doc.save()
        list = []
        for shape in self.chunk.shapes:
            if shape.group.label == label_shape:
                new_polygon = []
                for vertice in shape.geometry.coordinates[0]:
                    vertice = self.chunk.shapes.crs.unproject(vertice)
                    vertice = self.T.inv().mulp(vertice)
                    v = self.estimate_region_coords(x=vertice[0], y=vertice[1], z=vertice[2], plane='top')
                    vertice = Metashape.Vector([v[0], v[1], v[2]])
                    vertice = self.T.mulp(vertice)
                    vertice = self.chunk.shapes.crs.project(vertice)
                    new_polygon.append(vertice)
                new_shape = self.chunk.shapes.addShape()
                new_shape.label = shape.label
                new_shape.group = group_tmp
                new_shape.geometry.type = Metashape.Geometry.Type.PolygonType
                new_shape.geometry = Metashape.Geometry.Polygon(new_polygon)
                new_shape.boundary_type = shape.boundary_type
                list.append(shape)
        list.append(group_tmp)
        self.chunk.shapes.remove(list)
        self.doc.save()
        group = None
        for i in self.chunk.shapes.groups:
            if i.label == label_shape:
                group = i
        list = []
        for shape in self.chunk.shapes:
            if shape.group.label == 'tmp_layer':
                new_shape = self.chunk.shapes.addShape()
                new_shape.label = shape.label
                new_shape.group = group
                new_shape.geometry.type = shape.geometry.type
                new_shape.geometry = shape.geometry
                new_shape.boundary_type = shape.boundary_type
                list.append(shape)
        list.append(group_tmp)
        self.chunk.shapes.remove(list)
        self.doc.save()

    def split_chunks(self):
        self.set_chunk(label=gt.label)
        for shape in self.chunk.shapes:
            label_tile = shape.label
            path = os.path.join(gt.output_path, label_tile + "_project.psx")
            if os.path.isfile(path) and os.path.exists(path):
                gt.update_log('Founded chunk for tile = ' + label_tile)
            else:
                if shape.group.label == 'TileGrid_layer':
                    gt.update_log('Creating chunk for tile = ' + label_tile)
                    self.doc.save(path)
                    doc = Metashape.Document()
                    doc.open(path)
                    chunk = doc.chunk
                    chunk.label = label_tile
                    doc.save()
                    group = chunk.shapes.addGroup()
                    group.label = 'TileROI_layer'
                    group.color = (0, 0, 0)
                    group.show_labels = True
                    doc.save()
                    list = []
                    for shape in chunk.shapes:
                        if shape.label == label_tile:
                            new_shape = chunk.shapes.addShape()
                            new_shape.label = 'TileROI'
                            new_shape.group = group
                            new_shape.geometry = shape.geometry
                            doc.save()
                            list.append(shape)
                    chunk.shapes.remove(list)
                    doc.save()
                    self.set_region(label=label_tile)
                    self.set_chunk(label=gt.label)
        gt.update_log('Completed chunk splitting')
