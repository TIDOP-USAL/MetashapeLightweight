# authors:
# David Hernandez Lopez, david.hernandez@uclm.es
# Ana del Campo Sanchez, ana.delcampo@usal.es

import sys, os
from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication
from gui import gui_defines
from ParameterManager import ParametersManager
import Tools


def main():
    app = QApplication(sys.argv)
    current_path = os.path.dirname(os.path.realpath(__file__))
    path_file_qsettings = current_path + "/" + gui_defines.SETTINGS_FILE
    settings = QSettings(path_file_qsettings, QSettings.IniFormat)
    parametersManager = ParametersManager()
    params_definitions_file = current_path + "/" + gui_defines.PARAMS_DEFINITION_FILE
    params_definitions_file = os.path.normpath(params_definitions_file)
    str_error = parametersManager.from_json_file(params_definitions_file)
    if str_error:
        Tools.error_msg(str_error)
        return

    from MshBigPsxDialog import MshBigPsxDialog
    dialog = MshBigPsxDialog(settings,
                             parametersManager)
    if not dialog.initialize():
        exit()
    dialog.show()
    app.exec()


if __name__ == '__main__':
    main()
