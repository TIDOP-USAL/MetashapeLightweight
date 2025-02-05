# authors:
# David Hernandez Lopez, david.hernandez@uclm.es
# Ana del Campo Sanchez, ana.delcampo@usal.es

import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QFileDialog, QPushButton, QComboBox
from PyQt5.QtCore import QDir, QFileInfo, QFile
from gui.VPyFormGenerator.VPyGUIGenerator import VPyGUIGenerator
from gui.CameraCalibration import CameraCalibration
from gui.InstallRequirement import InstallRequirement
from gui.Photo import Photo
from gui.PointCloud import PointCloud
from gui.Project import Project
from gui.Roi import ROI
from gui.Workflow import Workflow
from gui.OptimizeAlignment import OptimizeAlignment
from gui.SplitTile import SplitTile
from gui import gui_defines
import json
import Tools


class MshBigPsxDialog(QDialog):
    """Employee dialog."""

    def __init__(self,
                 settings,
                 parametersManager,
                 parent=None):
        super().__init__(parent)
        loadUi("MshBigPsxDialog.ui", self)
        self.settings = settings
        self.parametersManager = parametersManager
        self.initialize()

    def addProject(self):
        title = "Select Project File"
        fileName, aux = QFileDialog.getOpenFileName(self, title, self.path, "Project File (*.json)")
        if fileName:
            if not fileName in self.projects:
                self.projects.append(fileName)
                self.projectsComboBox.addItem(fileName)
                strProjects = ""
                cont = 0
                for project in self.projects:
                    if cont > 0:
                        strProjects = strProjects + gui_defines.CONST_PROJECTS_STRING_SEPARATOR
                    strProjects += project
                    cont = cont + 1
                self.settings.setValue("projects", strProjects)
                self.settings.sync()
            pos = self.projectsComboBox.findText(fileName)
            if pos >= 0:
                self.projectsComboBox.setCurrentIndex(pos)
            self.path = QFileInfo(fileName).absolutePath()
            self.settings.setValue("last_path", self.path)
            self.settings.sync()
        return

    def initialize(self):
        self.path = self.settings.value("last_path")
        current_dir = QDir.current()
        if not self.path:
            self.path = QDir.currentPath()
            self.settings.setValue("last_path", self.path)
            self.settings.sync()
        self.geoids_path = self.settings.value("geoids_path")
        if self.geoids_path:
            self.geoids_path = os.path.normpath(self.geoids_path)
            if not current_dir.exists(self.geoids_path):
                self.geoids_path = ''
        else:
            self.geoids_path = ''
        if self.geoids_path:
            if not current_dir.exists(self.geoids_path):
                program_files_path = os.environ["ProgramFiles"]
                geoids_path = program_files_path + "/" + gui_defines.DEFAULT_GEOIDS_PATH
                geoids_path = os.path.normpath(geoids_path)
                if current_dir.exists(geoids_path):
                    self.geoids_path = geoids_path
                else:
                    self.geoids_path = ''
        self.settings.setValue("geoids_path", self.geoids_path)
        self.settings.sync()
        self.conda_env_path = self.settings.value("conda_env_path")
        if self.conda_env_path:
            self.conda_env_path = os.path.normpath(self.conda_env_path)
            if not current_dir.exists(self.conda_env_path):
                self.conda_env_path = None
        else:
            self.conda_env_path = ''
        self.settings.setValue("conda_env_path", self.conda_env_path)
        self.settings.sync()
        self.openProjectPushButton.setEnabled(False)
        self.closeProjectPushButton.setEnabled(False)
        self.removeProjectPushButton.setEnabled(False)
        self.projectFileEditionGroupBox.setEnabled(False)
        self.selectProjectFilePushButton.setEnabled(False)
        self.saveProjectPushButton.setEnabled(False)
        self.projectLineEdit.clear()
        self.processPushButton.setEnabled(False)
        self.projectsComboBox.currentIndexChanged.connect(self.selectProject)
        self.projectFile = None
        self.class_path = os.path.dirname(os.path.realpath(__file__))
        self.template_path = self.class_path + gui_defines.TEMPLATE_PATH
        self.path = self.settings.value("last_path")
        current_dir = QDir.current()
        if not self.path:
            self.path = QDir.currentPath()
            self.settings.setValue("last_path", self.path)
            self.settings.sync()
        self.geoids_path = self.settings.value("geoids_path")
        if self.geoids_path:
            if not current_dir.exists(self.geoids_path):
                self.geoids_path = None
        if not current_dir.exists(self.geoids_path):
            program_files_path = os.environ["ProgramFiles"]
            geoids_path = program_files_path + "/" + gui_defines.DEFAULT_GEOIDS_PATH
            geoids_path = os.path.normpath(geoids_path)
            if current_dir.exists(geoids_path):
                self.geoids_path = geoids_path
        self.settings.setValue("geoids_path", self.geoids_path)
        self.settings.sync()
        self.conda_env_path = self.settings.value("conda_env_path")
        if self.conda_env_path:
            if not current_dir.exists(self.conda_env_path):
                self.conda_env_path = None
        self.settings.setValue("conda_env_path", self.conda_env_path)
        self.settings.sync()
        self.projects = []
        strProjects = self.settings.value("projects")
        if strProjects:
            self.projects = strProjects.split(gui_defines.CONST_PROJECTS_STRING_SEPARATOR)
        self.projectsComboBox.clear()
        self.projectsComboBox.addItem(gui_defines.CONST_NO_COMBO_SELECT)
        for project in self.projects:
            self.projectsComboBox.addItem(project)
        self.addProjectPushButton.clicked.connect(self.addProject)
        self.projectsComboBox.currentIndexChanged.connect(self.selectProject)
        self.openProjectPushButton.clicked.connect(self.openProject)
        self.closeProjectPushButton.clicked.connect(self.closeProject)
        self.removeProjectPushButton.clicked.connect(self.removeProject)
        self.selectProjectFilePushButton.clicked.connect(self.selectOutputProjectFile)
        self.saveProjectPushButton.clicked.connect(self.saveProject)
        self.processPushButton.clicked.connect(self.process)
        self.openProjectPushButton.setEnabled(False)
        self.closeProjectPushButton.setEnabled(False)
        self.removeProjectPushButton.setEnabled(False)
        self.projectFileEditionGroupBox.setEnabled(False)
        self.selectProjectFilePushButton.setEnabled(False)
        self.saveProjectPushButton.setEnabled(False)
        self.addCheckBox.setEnabled(False)
        self.projectLineEdit.clear()
        self.processPushButton.setEnabled(False)
        self.object_by_name = {}
        self.object_dlg_by_name = {}

    def closeProject(self):
        if not self.selectProjectFile:
            return
        self.addProjectPushButton.setEnabled(True)
        self.openProjectPushButton.setEnabled(False)
        self.closeProjectPushButton.setEnabled(False)
        self.removeProjectPushButton.setEnabled(False)
        self.selectProjectFile = None
        self.projectsComboBox.setEnabled(True)
        self.projectsComboBox.setCurrentIndex(0)
        self.selectProjectFilePushButton.setEnabled(False)
        self.saveProjectPushButton.setEnabled(False)
        self.addCheckBox.setEnabled(False)
        for class_name in gui_defines.GUI_CLASSES:
            self.object_by_name[class_name] = None
            self.object_dlg_by_name[class_name] = None
        for i in range(self.objectsGridLayout.count()):
            self.objectsGridLayout.itemAt(i).widget().close()
        return

    def loadProjectFromJSonFile(self,
                                project_file):
        str_error = ""
        current_dir = QDir.current()
        if not os.path.isfile(project_file):
            str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
            str_error += ("\nNot exists file: {}".format(project_file))
            return str_error
        f = open(project_file)
        try:
            json_content = json.load(f)
        except:
            str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
            str_error += ("\nInvalid JSON file: {}".format(project_file))
            f.close()
            return str_error
        f.close()
        gui_classes = gui_defines.GUI_CLASSES
        class_in_json_file_by_gui_class = {}
        for class_name in gui_classes:
            if class_name in json_content:
                class_in_json_file_by_gui_class[class_name] = class_name
            else:
                for class_in_json in json_content:
                    if class_name.lower() == class_in_json.lower():
                        class_in_json_file_by_gui_class[class_name] = class_in_json
        for class_name in gui_classes:
            if not class_name in class_in_json_file_by_gui_class:
                str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
                str_error += ("\nClass: {} not in JSON file: {}".format(class_name, project_file))
                return str_error
            class_name_json = class_in_json_file_by_gui_class[class_name]
            json_class_content = json_content[class_name_json]
            attributes_tag = None
            attributes_tag = self.object_by_name[class_name].get_values_as_dictionary()
            values = {}
            for attributes_in_definitions in attributes_tag:
                if not attributes_in_definitions in json_class_content:
                    str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
                    str_error += ("\nAttribute: {} not in class: {} not in JSON file: {}"
                                  .format(attributes_in_definitions, class_name, project_file))
                    return str_error
                value = json_class_content[attributes_in_definitions]
                if type(attributes_tag[attributes_in_definitions]) == bool:
                    if type(value) == str:
                        if value.lower() == 'true':
                            value = True
                        elif value.lower() == 'false':
                            value = False
                        else:
                            str_error = MshBigPsxDialog.__name__ + "." + self.loadProjectFromJSonFile.__name__
                            str_error += ("\nAttribute: {} in class: {} in JSON file: {} invalid boolean: {}"
                                          .format(attributes_in_definitions, class_name, project_file, value))
                            return str_error
                values[attributes_in_definitions] = value
            if class_name == gui_defines.OBJECT_CLASS_INSTALL_REQUIREMENT:
                conda_env_path = values[gui_defines.REQUIREMENTS_CONDA_ENVIRONMENT_TAG]
                if conda_env_path:
                    conda_env_path = os.path.normpath(conda_env_path)
                    if current_dir.exists(conda_env_path):
                        if self.conda_env_path != conda_env_path:
                            self.conda_env_path = conda_env_path
                            self.settings.setValue("conda_env_path", self.conda_env_path)
                            self.settings.sync()
                    else:
                        if self.conda_env_path:
                            values[gui_defines.REQUIREMENTS_CONDA_ENVIRONMENT_TAG] = self.conda_env_path
                else:
                    if self.conda_env_path:
                        values[gui_defines.REQUIREMENTS_CONDA_ENVIRONMENT_TAG] = self.conda_env_path
                geoids_path = values[gui_defines.REQUIREMENTS_GEOIDS_PATH_TAG]
                if geoids_path:
                    geoids_path = os.path.normpath(geoids_path)
                    if current_dir.exists(geoids_path):
                        if self.geoids_path != geoids_path:
                            self.geoids_path = geoids_path
                            self.settings.setValue("geoids_path", self.geoids_path)
                            self.settings.sync()
                else:
                    if self.geoids_path:
                        values[gui_defines.REQUIREMENTS_GEOIDS_PATH_TAG] = self.geoids_path
            self.object_by_name[class_name].set_values_from_dictionary(values)
        return str_error

    def openProject(self):
        self.addProjectPushButton.setEnabled(False)
        self.closeProjectPushButton.setEnabled(False)
        self.removeProjectPushButton.setEnabled(False)
        self.projectFileEditionGroupBox.setEnabled(False)
        self.selectProjectFilePushButton.setEnabled(False)
        self.saveProjectPushButton.setEnabled(False)
        self.processPushButton.setEnabled(False)
        self.selectProjectFile = None
        projectFile = self.projectsComboBox.currentText()
        if projectFile == gui_defines.CONST_NO_COMBO_SELECT:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle(self.windowTitle)
            msgBox.setText("Select project before")
            msgBox.exec_()
            return
        for class_name in gui_defines.GUI_CLASSES:
            self.object_by_name[class_name] = None
            self.object_dlg_by_name[class_name] = None
            if class_name == gui_defines.OBJECT_CLASS_CAMERA_CALIBRATION:
                self.object_by_name[class_name] = CameraCalibration()
            elif class_name == gui_defines.OBJECT_CLASS_INSTALL_REQUIREMENT:
                self.object_by_name[class_name] = InstallRequirement()
            elif class_name == gui_defines.OBJECT_CLASS_PHOTO:
                self.object_by_name[class_name] = Photo()
            elif class_name == gui_defines.OBJECT_CLASS_POINT_CLOUD:
                self.object_by_name[class_name] = PointCloud()
            elif class_name == gui_defines.OBJECT_CLASS_PROJECT:
                self.object_by_name[class_name] = Project()
            elif class_name == gui_defines.OBJECT_CLASS_WORKFLOW:
                self.object_by_name[class_name] = Workflow()
            elif class_name == gui_defines.OBJECT_CLASS_ROI:
                self.object_by_name[class_name] = ROI()
            elif class_name == gui_defines.OBJECT_CLASS_OPTIMIZE_ALIGNMENT:
                self.object_by_name[class_name] = OptimizeAlignment()
            elif class_name == gui_defines.OBJECT_CLASS_SPLIT_TILE:
                self.object_by_name[class_name] = SplitTile()
            row_in_grid_layout = gui_defines.GRID_LAYOUT_POSITION_BY_CLASS[class_name][0]
            column_in_grid_layout = gui_defines.GRID_LAYOUT_POSITION_BY_CLASS[class_name][1]
            object_title = self.object_by_name[class_name].get_text()
            self.objectsGridLayout.addWidget(QPushButton(object_title), row_in_grid_layout, column_in_grid_layout)
        for class_name in gui_defines.GUI_CLASSES:
            row_in_grid_layout = gui_defines.GRID_LAYOUT_POSITION_BY_CLASS[class_name][0]
            column_in_grid_layout = gui_defines.GRID_LAYOUT_POSITION_BY_CLASS[class_name][1]
            object_title = self.object_by_name[class_name].get_text()
            obj_push_button = QPushButton(object_title)
            self.objectsGridLayout.addWidget(obj_push_button, row_in_grid_layout, column_in_grid_layout)
            obj_dlg = VPyGUIGenerator.create_gui(self.object_by_name[class_name])
            obj_dlg.setWindowTitle(object_title)
            text_by_propierty = self.object_by_name[class_name].get_text_by_propierty()
            for propierty in text_by_propierty:
                label_propierty = 'label_' + propierty
                obj_dlg.get_widget(label_propierty).setText(text_by_propierty[propierty])
            self.object_dlg_by_name[class_name] = obj_dlg
            self.object_by_name[class_name].set_widget(self.object_dlg_by_name[class_name])
            obj_push_button.clicked.connect(obj_dlg.exec)
        str_error = self.loadProjectFromJSonFile(projectFile)
        if str_error:
            Tools.error_msg(str_error)
            return
        self.selectProjectFile = projectFile
        self.closeProjectPushButton.setEnabled(True)
        self.openProjectPushButton.setEnabled(False)
        self.projectsComboBox.setEnabled(False)
        self.projectFileEditionGroupBox.setEnabled(True)
        self.saveProjectPushButton.setEnabled(False)
        self.addCheckBox.setEnabled(False)
        self.selectProjectFilePushButton.setEnabled(True)

    def process(self):
        output_file = self.projectLineEdit.text()
        if not output_file:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle(self.windowTitle())
            msgBox.setText("Select output JSON project file before")
            msgBox.exec_()
            return
        output_file = os.path.normpath(output_file)
        if not QFile.exists(output_file):
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle(self.windowTitle())
            msgBox.setText("Save output JSON file project before")
            msgBox.exec_()
            return

        return

    def removeProject(self):
        projectPath = self.projectsComboBox.currentText()
        if projectPath == gui_defines.CONST_NO_COMBO_SELECT:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle(self.windowTitle)
            msgBox.setText("Select project to remove from list")
            msgBox.exec_()
            return
        self.projects.remove(projectPath)
        strProjects = ""
        cont = 0
        for project in self.projects:
            if cont > 0:
                strProjects = strProjects + gui_defines.CONST_PROJECTS_STRING_SEPARATOR
            strProjects += project
            cont = cont + 1
        self.settings.setValue("projects", strProjects)
        self.settings.sync()
        self.projectsComboBox.currentIndexChanged.disconnect(self.selectProject)
        self.projectsComboBox.clear()
        self.projectsComboBox.addItem(gui_defines.CONST_NO_COMBO_SELECT)
        for project in self.projects:
            self.projectsComboBox.addItem(project)
        self.projectsComboBox.currentIndexChanged.connect(self.selectProject)
        self.projectsComboBox.setCurrentIndex(0)

    def selectOutputProjectFile(self):
        title = "Select Project File"
        previous_file = self.projectLineEdit.text()
        fileName, aux = QFileDialog.getSaveFileName(self, title, self.path, "Project File (*.json)")
        if fileName:
            self.projectLineEdit.setText(fileName)
            self.saveProjectPushButton.setEnabled(True)
            self.addCheckBox.setEnabled(True)
        else:
            if not previous_file:
                self.saveProjectPushButton.setEnabled(False)
                self.addCheckBox.setEnabled(False)
        return

    def saveProject(self):
        self.processPushButton.setEnabled(False)
        output_file = self.projectLineEdit.text()
        if not output_file:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle(self.windowTitle())
            msgBox.setText("Select output JSON project file before")
            msgBox.exec_()
            return
        output_file = os.path.normpath(output_file)
        json_content = {}
        values = {}
        for class_name in self.object_by_name:
            object_values = self.object_by_name[class_name].get_values_as_dictionary()
            for object_value in object_values:
                if type(object_values[object_value]) == bool:
                    if object_values[object_value]:
                        object_values[object_value] = "True"
                    else:
                        object_values[object_value] = "False"
                propierty_widget = self.object_by_name[class_name].get_widget_propierty(object_value)
                if not propierty_widget:
                    msgBox = QMessageBox(self)
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setWindowTitle(self.windowTitle())
                    msgBox.setText("Not exists widget for propierty: {} in class: {}".
                                   format(object_value, class_name))
                    msgBox.exec_()
                    return
                if isinstance(propierty_widget, QComboBox):
                    json_content = self.object_by_name[class_name].get_propierty_json_content(object_value)
                    if not json_content:
                        msgBox = QMessageBox(self)
                        msgBox.setIcon(QMessageBox.Information)
                        msgBox.setWindowTitle(self.windowTitle())
                        msgBox.setText("Not exists json content for propierty: {} in class: {}".
                                       format(object_value, class_name))
                        msgBox.exec_()
                        return
                    json_values = json_content[gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG]
                    new_value = None
                    for json_value in json_values:
                        values_language = json_values[json_value]
                        for value_language in values_language:
                            if values_language[value_language] == object_values[object_value]:
                                new_value = json_value
                                break
                    if not new_value:
                        msgBox = QMessageBox(self)
                        msgBox.setIcon(QMessageBox.Information)
                        msgBox.setWindowTitle(self.windowTitle())
                        msgBox.setText("Not exists valid coincidence value for propierty: {} in class: {}".
                                       format(object_value, class_name))
                        msgBox.exec_()
                        return
                    object_values[object_value] = new_value
            values[class_name] = object_values
        json_content = values
        json_object = json.dumps(json_content, indent=4)
        with open(output_file, "w") as outfile:
            outfile.write(json_object)
        self.processPushButton.setEnabled(True)
        if self.addCheckBox.isChecked():
            if not output_file in self.projects:
                self.projects.append(output_file)
                self.projectsComboBox.addItem(output_file)
                strProjects = ""
                cont = 0
                for project in self.projects:
                    if cont > 0:
                        strProjects = strProjects + gui_defines.CONST_PROJECTS_STRING_SEPARATOR
                    strProjects += project
                    cont = cont + 1
                self.settings.setValue("projects", strProjects)
                self.settings.sync()
        return

    def selectProject(self):
        self.addProjectPushButton.setEnabled(False)
        self.openProjectPushButton.setEnabled(False)
        self.closeProjectPushButton.setEnabled(False)
        self.removeProjectPushButton.setEnabled(False)
        projectFilePath = self.projectsComboBox.currentText()
        self.selectProjectFilePushButton.setEnabled(False)
        self.saveProjectPushButton.setEnabled(False)
        self.addCheckBox.setEnabled(False)
        if projectFilePath == gui_defines.CONST_NO_COMBO_SELECT:
            self.addProjectPushButton.setEnabled(True)
            self.projectFileEditionGroupBox.setEnabled(False)
            self.projectLineEdit.clear()
            self.processPushButton.setEnabled(False)
            if self.projectFile:
                self.closeProject()
        else:
            self.addProjectPushButton.setEnabled(False)
            self.projectFileEditionGroupBox.setEnabled(False)
            self.openProjectPushButton.setEnabled(True)
            self.closeProjectPushButton.setEnabled(False)
            self.removeProjectPushButton.setEnabled(True)
        return
