import os
import shutil
import sys
import time
import json


class GeneralTools:

    def __init__(self):
        self.current_path = os.path.dirname(os.path.realpath(__file__)).replace('"', '')
        self.params_file = os.path.join(self.current_path, 'params.json')
        self.params = self.read_params()
        self.label = self.params.get('Project')["Label"]
        self.output_path = os.path.join(self.params.get('Project')["Path"], self.label)
        self.log_file = os.path.join(self.output_path, self.label + '_log.txt')
        self.project_path = os.path.join(self.output_path, self.label + '_project.psx')
        self.shape_path = os.path.join(self.output_path, self.label + '_shapes.gpkg')
        self.tile_size = self.params.get("SplitTile")["TileSize"]

    def clear_output_folder(self):
        if os.path.exists(self.output_path) and os.path.isdir(self.output_path):
            # TODO advertencia al usuario del borrado
            shutil.rmtree(self.output_path)
        os.mkdir(self.output_path)
        # TODO advertencia al usuario si parámetros de entrada son incorrectos

    def find_files(self, folder, types):
        return [entry.path for entry in os.scandir(folder)
                if (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]

    def is_platform(self, name):
        self.update_log('System platform = ' + sys.platform)
        return sys.platform == name

    def read_chunks(self):
        psxs = []
        files = self.find_files(folder=self.output_path, types=['.psx'])
        if len(files) > 2:
            for psx in files:
                file = os.path.basename(psx)
                if self.label in file:
                    continue
                label_tile = file.split('_project')[0]
                psxs.append(label_tile)
        return psxs

    def read_params(self):
        pathfile = os.path.normpath(self.params_file)
        with open(pathfile) as config_file:
            config_file_contents = config_file.read()
        params = json.loads(config_file_contents)
        return params

    def update_log(self, text=None):
        time.strftime("%Y%m%d %H:%M:%S")
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write(time.strftime("%d/%m/%Y %H:%M:%S") + ' Initialized process\n')
        if text is None:
            text = '...'
        with open(self.log_file, 'a') as f:
            f.write(time.strftime("%d/%m/%Y %H:%M:%S") + ' ' + text)
            f.write('\n')
        print(time.strftime("%d/%m/%Y %H:%M:%S") + ' ' + text)
