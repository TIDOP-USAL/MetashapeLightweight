from lib import GeneralTools
from metashape import MetashapeTools

gt = GeneralTools()
mt = MetashapeTools()

if eval(gt.params.get("Workflow")["CleanPrevious"]):
    gt.clear_output_folder()

mt.check_initial()

if eval(gt.params.get("Workflow")["Initialize"]):
    mt.initial_psx()
    mt.import_photos()

if eval(gt.params.get("Workflow")["Preprocess"]):
    mt.preprocess()
    mt.import_roi()
    mt.set_region()
    mt.set_z_shape(label_shape='ROI_layer')
    mt.export_roi_shape()

if eval(gt.params.get("Workflow")["Optimize"]):
    mt.check_optimize_method()
    mt.set_region()
    mt.set_z_shape(label_shape='ROI_layer')

if eval(gt.params.get("Workflow")["Split"]):
    mt.check_split_path()
    mt.split_chunks()

psxs = gt.read_chunks()
if eval(gt.params.get("Workflow")["PointCloud"]):
    if psxs:
        for i in psxs:
            mt.process_point_cloud(label=i)
    else:
        mt.process_point_cloud()

psxs = gt.read_chunks()
if eval(gt.params.get("Workflow")["DEMs"]):
    if psxs:
        for i in psxs:
            mt.process_dems(label=i)
    else:
        mt.process_dems()

if eval(gt.params.get("Workflow")["Orthomosaic"]):
    if psxs:
        for i in psxs:
            mt.process_orthomosaic(label=i)
    else:
        mt.process_orthomosaic()

if eval(gt.params.get("Workflow")["Split"]):
    if gt.params.get("SplitTile")["MergeMethod"] == "Metashape":
        mt.merge_chunks()
        if eval(gt.params.get("SplitTile")["MergePointClouds"]):
            mt.export_pointcloud()
        if eval(gt.params.get("SplitTile")["MergeElevations"]):
            mt.export_dems()
        if eval(gt.params.get("SplitTile")["MergeOrthomosaics"]):
            mt.export_orthomosaic()
    elif gt.params.get("SplitTile")["MergeMethod"] == 'OsgeoLaspy':
        if eval(gt.params.get("Workflow")["PointCloud"]) and eval(gt.params.get("SplitTile")["MergePointClouds"]):
            mt.merge_pointclouds()
        if eval(gt.params.get("Workflow")["DEMs"]) and eval(gt.params.get("SplitTile")["MergeElevations"]):
            mt.merge_dems()
        if eval(gt.params.get("Workflow")["Orthomosaic"]) and eval(gt.params.get("SplitTile")["MergeOrthomosaics"]):
            mt.merge_orthomosaic()

if eval(gt.params.get("Workflow")["Report"]):
    mt.process_report()

mt.destroy_srs()
gt.update_log('Complete process DONE!')
