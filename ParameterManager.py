import json
import os
from gui import gui_defines


class ParametersManager:
    def __init__(self):
        self.json_file = None
        self.json_content = None
        self.parameters = gui_defines.parameters

    def build_parameter_file(self,
                             class_name,
                             language,
                             json_class_content):
        str_error = ""
        current_path = os.path.dirname(os.path.realpath(__file__))
        class_file_path = current_path + gui_defines.GUI_CLASSES_PATH
        class_file_path = os.path.normpath(class_file_path)
        if not os.path.exists(class_file_path):
            os.makedirs(class_file_path)
            if not os.path.exists(class_file_path):
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nError making Classes path: {}".format(class_file_path))
                return str_error
        class_file = class_file_path + "/" + class_name + ".py"
        class_file = os.path.normpath(class_file)
        f = open(class_file, "w")
        f.write('from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox\n')
        f.write('from . import gui_defines\n')
        f.write('\nclass {}:\n'.format(class_name))
        f.write('\tdef __init__(self):\n')
        f.write('\t\tself.__text_by_propierty = {}\n')
        f.write('\t\tself.__widget_by_propierty = {}\n')
        f.write('\t\tself.__json_content_by_propierty = {}\n')
        propierty_field_definition = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_DEFINITION_TAG
        propierty_field_type = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_TYPE_TAG
        propierty_field_default = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_DEFAULT_TAG
        propierty_field_decimals = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_DECIMALS_TAG
        propierty_field_maximum = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_MAXIMUM_TAG
        propierty_field_minimum = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_MINIMUM_TAG
        propierty_field_single_step = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_SINGLE_STEP_TAG
        propierty_field_formats = gui_defines.GUI_CLASSES_PROPIERTY_FIELD_FORMATS_TAG
        for propierty_name in json_class_content:
            json_propierty_content = json_class_content[propierty_name]
            f.write('\t\tself.__json_content_by_propierty[\'{}\'] = {}\n'
                    .format(propierty_name, json_propierty_content))
            if propierty_name == gui_defines.GUI_CLASSES_TEXT_TAG:
                if not language in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists language: {}"
                                  .format(class_name, gui_defines.GUI_CLASSES_TEXT_TAG, language))
                    return str_error
                text = '\t\tself.__' + propierty_name + " = \'" + json_propierty_content[language] + "\'"
                text += "\n"
                f.write(text)
                continue
            if not gui_defines.GUI_CLASSES_TEXT_TAG in json_propierty_content:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, gui_defines.GUI_CLASSES_TEXT_TAG))
                return str_error
            if not language in json_propierty_content[gui_defines.GUI_CLASSES_TEXT_TAG]:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, in field: {}, not exists language: {}"
                              .format(class_name, propierty_name, gui_defines.GUI_CLASSES_TEXT_TAG, language))
                return str_error
            f.write('\t\tself.__text_by_propierty[\'{}\'] = \'{}\'\n'.
                    format(propierty_name, json_propierty_content[gui_defines.GUI_CLASSES_TEXT_TAG][language]))
            f.write('\t\tself.__widget_by_propierty[\'{}\'] = None\n'.format(propierty_name))
            if not propierty_field_type in json_propierty_content:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_type))
                return str_error
            propierty_type = json_propierty_content[propierty_field_type]
            if not propierty_field_default in json_propierty_content:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_default))
                return str_error
            propierty_default_value = str(json_propierty_content[propierty_field_default])
            if propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                if propierty_default_value != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TRUE \
                        and propierty_default_value != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_FALSE:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, field: {} must be {} or {}"
                                  .format(class_name, propierty_name, propierty_field_default,
                                          gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TRUE,
                                          gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_FALSE))
                    return str_error
            text = '\t\tself.__' + propierty_name + " = "
            text_value = '\t\tself.__' + propierty_name + gui_defines.GUI_CLASSES_PROPIERTY_VALUE_SUFFIX + " = "
            if propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG:
                values_content = json_propierty_content[propierty_type]
                text += "["
                pos_default_in_values_content = -1
                cont = 0
                for value_tag in values_content:
                    value_content = values_content[value_tag]
                    if not language in value_content:
                        str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                        str_error += ("\nFor class: {}, in attribute: {}, in field: {}, "
                                      "in value: {}, not exists language: {}"
                                      .format(class_name, propierty_name,
                                              propierty_field_definition, value_tag, language))
                        return str_error
                    for value_language in value_content:
                        value = value_content[value_language]
                        if value == propierty_default_value:
                            value = value_content[language]
                            text += ('\'{}\''.format(value))
                            text_value += ('\'{}\''.format(value))
                            pos_default_in_values_content = cont
                            if value_language != language:
                                propierty_default_value = value_content[language]
                            break
                    cont = cont + 1
                if pos_default_in_values_content == -1:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, field: {}, "
                                  "default value: {} is not in valid values"
                                  .format(class_name, propierty_name, propierty_field_type,
                                          propierty_default_value))
                cont = 0
                for value_tag in values_content:
                    if cont == pos_default_in_values_content:
                        cont = cont + 1
                        continue
                    value_content = values_content[value_tag]
                    if not language in value_content:
                        str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                        str_error += ("\nFor class: {}, in attribute: {}, in field: {}, "
                                      "in value: {}, not exists language: {}"
                                      .format(class_name, propierty_name,
                                              propierty_field_definition, value_tag, language))
                        return str_error
                    value = value_content[language]
                    text += (' ,\'{}\''.format(value))
                    cont = cont + 1
                text += "]"
                text += "\n"
                f.write(text)
                text_value += "\n"
                f.write(text_value)
                continue
            if propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_REAL_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_INTEGER_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                text += '\"'
                text_value += '\"'
            text += propierty_default_value
            text_value += propierty_default_value
            if propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_REAL_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_INTEGER_TAG \
                    and propierty_type != gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                text += '\"'
                text_value += '\"'
            text += "\n"
            text_value += "\n"
            f.write(text)
            f.write(text_value)
        f.write('\t\tself.__widget = None\n')
        f.write('\n\tdef get_propierty_json_content(self, value):\n')
        f.write('\t\tjson_content = None\n')
        f.write('\t\tif value in self.__json_content_by_propierty:\n')
        f.write('\t\t\tjson_content = self.__json_content_by_propierty[value]\n')
        f.write('\t\treturn json_content\n')
        f.write('\n\tdef get_values_as_dictionary(self):\n')
        f.write('\t\tvalues = {}\n')
        for propierty_name in json_class_content:
            json_propierty_content = json_class_content[propierty_name]
            if propierty_name == gui_defines.GUI_CLASSES_TEXT_TAG:
                continue
            f.write('\t\tvalues[\'{}\'] = self.__{}{}\n'
                    .format(propierty_name, propierty_name,
                            gui_defines.GUI_CLASSES_PROPIERTY_VALUE_SUFFIX))
        f.write('\t\treturn values\n')
        f.write('\n\tdef get_text(self):\n')
        f.write('\t\treturn self.__text\n')
        f.write('\n\tdef get_text_by_propierty(self):\n')
        f.write('\t\treturn self.__text_by_propierty\n')
        f.write('\n\tdef get_widget_propierty(self, value):\n')
        f.write('\t\twidget_propierty = None\n')
        f.write('\t\tif value in self.__widget_by_propierty:\n')
        f.write('\t\t\twidget_propierty = self.__widget_by_propierty[value]\n')
        f.write('\t\treturn widget_propierty\n')
        for propierty_name in json_class_content:
            json_propierty_content = json_class_content[propierty_name]
            if propierty_name == gui_defines.GUI_CLASSES_TEXT_TAG:
                continue
            propierty_name = propierty_name
            propiertyIsString = False
            propiertyIsReal = False
            propiertyIsFolder = False
            propiertyIsFileOpen = False
            propiertyIsFileSave = False
            propiertyIsFileAny = False
            propiertyIsInteger = False
            propiertyIsValuesList = False
            propiertyIsBoolean = False
            if not propierty_field_definition in json_propierty_content:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_definition))
                return str_error
            if not language in json_propierty_content[propierty_field_definition]:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, in field: {}, not exists language: {}"
                              .format(class_name, propierty_name,
                                      propierty_field_definition, language))
                return str_error
            propierty_definition = json_propierty_content[propierty_field_definition][language]
            if not propierty_field_type in json_propierty_content:
                str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                              .format(class_name, propierty_name, propierty_field_type))
                return str_error
            propierty_type = json_propierty_content[propierty_field_type]
            propierty_text = ('widget:QLineEdit, toolTip:{}'.format(propierty_definition))
            if propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_BOOLEAN_TAG:
                propiertyIsBoolean = True
                propierty_text = ('widget:QCheckBox, toolTip:{}'
                                  .format(propierty_definition))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_STRING_TAG:
                propiertyIsString = True
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_REAL_TAG:
                propiertyIsReal = True
                if not propierty_field_decimals in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_decimals))
                    return str_error
                propierty_decimals = json_propierty_content[propierty_field_decimals]
                if not propierty_field_minimum in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_minimum))
                    return str_error
                propierty_minimum = json_propierty_content[propierty_field_minimum]
                if not propierty_field_maximum in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_maximum))
                    return str_error
                propierty_maximum = json_propierty_content[propierty_field_maximum]
                if not propierty_field_single_step in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_single_step))
                    return str_error
                propierty_single_step = json_propierty_content[propierty_field_single_step]
                propierty_text = (
                    'widget:QDoubleSpinBox, decimals:{}, minimum:{}, maximum:{}, singleStep:{}, toolTip:{}'
                    .format(propierty_decimals, propierty_minimum,
                            propierty_maximum, propierty_single_step, propierty_definition))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_INTEGER_TAG:
                propiertyIsInteger = True
                if not propierty_field_minimum in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_minimum))
                    return str_error
                propierty_minimum = json_propierty_content[propierty_field_minimum]
                if not propierty_field_maximum in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_maximum))
                    return str_error
                propierty_maximum = json_propierty_content[propierty_field_maximum]
                if not propierty_field_single_step in json_propierty_content:
                    str_error = ParametersManager.__name__ + "." + self.build_parameter_file.__name__
                    str_error += ("\nFor class: {}, in attribute: {}, not exists field: {}"
                                  .format(class_name, propierty_name, propierty_field_single_step))
                    return str_error
                propierty_single_step = json_propierty_content[propierty_field_single_step]
                propierty_text = (
                    'widget:QSpinBox, minimum:{}, maximum:{}, singleStep:{}, toolTip:{}'
                    .format(propierty_minimum,
                            propierty_maximum, propierty_single_step, propierty_definition))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG:
                propiertyIsValuesList = True
                propierty_text = (
                    'widget:QComboBox, toolTip:{}'.format(propierty_definition))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_FOLDER_TAG:
                propiertyIsFolder = True
                propierty_text = ('widget:file, type:folder, toolTip:{}'.format(propierty_definition))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_FILE_OPEN_TAG:
                propiertyIsFileOpen = True
                str_propierty_formats = None
                if propierty_field_formats in json_propierty_content:
                    str_propierty_formats = json_propierty_content[propierty_field_formats]
                if not str_propierty_formats:
                    propierty_text = ('widget:file, toolTip:{}'.format(propierty_definition))
                else:
                    propierty_text = ('widget:file, toolTip:{}, filters: {}'.
                                      format(propierty_definition, str_propierty_formats))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_FILE_SAVE_TAG:
                propiertyIsFileSave = True
                str_propierty_formats = None
                if propierty_field_formats in json_propierty_content:
                    str_propierty_formats = json_propierty_content[propierty_field_formats]
                if not str_propierty_formats:
                    propierty_text = ('widget:file, type:save, toolTip:{}'.format(propierty_definition))
                else:
                    propierty_text = ('widget:file, type:save, toolTip:{}, filters: {}'.
                                      format(propierty_definition, str_propierty_formats))
            elif propierty_type == gui_defines.GUI_CLASSES_PROPIERTY_TYPE_FILE_ANY_TAG:
                propiertyIsFileAny = True
                str_propierty_formats = None
                if propierty_field_formats in json_propierty_content:
                    str_propierty_formats = json_propierty_content[propierty_field_formats]
                if not str_propierty_formats:
                    propierty_text = ('widget:file, type:any, toolTip:{}'.format(propierty_definition))
                else:
                    propierty_text = ('widget:file, type:any, toolTip:{}, filters: {}'.
                                      format(propierty_definition, str_propierty_formats))
            f.write('\n\t@property\n')
            f.write('\tdef {}(self):\n'.format(propierty_name))
            f.write('\t\treturn self.__{}\n'.format(propierty_name))
            f.write('\n\t@{}.setter\n'.format(propierty_name))
            f.write('\tdef {}(self, value: \'{}\'):\n'.format(propierty_name, propierty_text))
            f.write('\t\tself.__{} = value\n'.format(propierty_name))
            f.write('\n\tdef set_{}_value(self):\n'.format(propierty_name))
            f.write('\t\tpropierty_{}_widget = self.__widget_by_propierty[\'{}\'] \n'
                    .format(propierty_name, propierty_name))
            f.write('\t\tif isinstance(propierty_{}_widget, QSpinBox):\n'.format(propierty_name))
            f.write('\t\t\tself.__{}_value = propierty_{}_widget.value()\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QDoubleSpinBox):\n'.format(propierty_name))
            f.write('\t\t\tself.__{}_value = propierty_{}_widget.value()\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QComboBox):\n'.format(propierty_name))
            f.write('\t\t\tself.__{}_value = propierty_{}_widget.currentText()\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QLineEdit):\n'.format(propierty_name))
            f.write('\t\t\tself.__{}_value = propierty_{}_widget.text()\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QCheckBox):\n'.format(propierty_name))
            f.write('\t\t\tself.__{}_value = propierty_{}_widget.isChecked()\n'
                    .format(propierty_name, propierty_name))
        f.write('\n\tdef set_values_from_dictionary(self, values):\n')
        f.write('\t\tfor value in values:\n')
        f.write('\t\t\tpropierty_widget = self.__widget_by_propierty[value]\n')
        f.write('\t\t\tif isinstance(propierty_widget, QComboBox):\n')
        f.write('\t\t\t\tjson_values = self.__json_content_by_propierty[value][gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG]\n')
        f.write('\t\t\t\tif values[value] in json_values:\n')
        f.write('\t\t\t\t\tfor language in json_values[values[value]]:\n')
        f.write('\t\t\t\t\t\tvalue_language = json_values[values[value]][language]\n')
        f.write('\t\t\t\t\t\tpos = propierty_widget.findText(value_language)\n')
        f.write('\t\t\t\t\t\tif pos != -1:\n')
        f.write('\t\t\t\t\t\t\tpropierty_widget.setCurrentIndex(pos)\n')
        f.write('\t\t\t\t\t\t\tbreak\n')
        f.write('\t\t\telif isinstance(propierty_widget, QSpinBox):\n')
        f.write('\t\t\t\tint_value = int(values[value])\n')
        f.write('\t\t\t\tpropierty_widget.setValue(int_value)\n')
        f.write('\t\t\telif isinstance(propierty_widget, QDoubleSpinBox):\n')
        f.write('\t\t\t\tfloat_value = float(values[value])\n')
        f.write('\t\t\t\tpropierty_widget.setValue(float_value)\n')
        f.write('\t\t\telif isinstance(propierty_widget, QLineEdit):\n')
        f.write('\t\t\t\tpropierty_widget.setText(values[value])\n')
        f.write('\t\t\telif isinstance(propierty_widget, QCheckBox):\n')
        f.write('\t\t\t\tpropierty_widget.setChecked(values[value])\n')
        f.write('\t\treturn\n')
        f.write('\n\tdef set_widget(self, widget):\n')
        f.write('\t\tself.__widget = widget\n')
        for propierty_name in json_class_content:
            if propierty_name == gui_defines.GUI_CLASSES_TEXT_TAG:
                continue
            f.write('\t\tpropierty_{}_widget = self.__widget.get_widget(\'{}\')\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\tif isinstance(propierty_{}_widget, QSpinBox):\n'.format(propierty_name))
            f.write('\t\t\tpropierty_{}_widget.valueChanged.connect(self.set_{}_value)\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QDoubleSpinBox):\n'.format(propierty_name))
            f.write('\t\t\tpropierty_{}_widget.valueChanged.connect(self.set_{}_value)\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QComboBox):\n'.format(propierty_name))
            f.write('\t\t\tpropierty_{}_widget.currentIndexChanged.connect(self.set_{}_value)\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QLineEdit):\n'.format(propierty_name))
            f.write('\t\t\tpropierty_{}_widget.editingFinished.connect(self.set_{}_value)\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\t\tpropierty_{}_widget.textChanged.connect(self.set_{}_value)\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\telif isinstance(propierty_{}_widget, QCheckBox):\n'.format(propierty_name))
            f.write('\t\t\tpropierty_{}_widget.stateChanged.connect(self.set_{}_value)\n'
                    .format(propierty_name, propierty_name))
            f.write('\t\tself.__widget_by_propierty[\'{}\'] = propierty_{}_widget\n'
                    .format(propierty_name, propierty_name))
        f.close()
        return str_error

    def from_json_file(self,
                       definitions_file):
        str_error = ""
        if not os.path.isfile(definitions_file):
            str_error = ParametersManager.__name__ + "." + self.from_json_file.__name__
            str_error += ("\nNot exists file: {}".format(definitions_file))
            return str_error
        f = open(definitions_file)
        try:
            json_content = json.load(f)
        except:
            str_error = ParametersManager.__name__ + "." + self.from_json_file.__name__
            str_error += ("\nInvalid JSON file: {}".format(definitions_file))
            f.close()
            return str_error
        f.close()
        if not gui_defines.GUI_LANGUAGE_TAG in json_content:
            str_error = ParametersManager.__name__ + "." + self.from_json_file.__name__
            str_error += ("\n{} not in JSON file: {}".format(gui_defines.GUI_LANGUAGE_TAG, definitions_file))
            return str_error
        language = json_content[gui_defines.GUI_LANGUAGE_TAG]
        for class_name in self.parameters:
            if not class_name in json_content:
                str_error = ParametersManager.__name__ + "." + self.from_json_file.__name__
                str_error += ("\nClass: {} not in JSON file: {}".format(class_name, definitions_file))
                return str_error
            if (class_name != 'Project'
                    and class_name != 'Workflow'
                    and class_name != 'Photo'
                    and class_name != "OptimizeAlignment"
                    and class_name != "SplitTile"
                    and class_name != "PointCloud"
                    and class_name != "Raster"
                    and class_name != "Installation"):
                continue
            # class_is_valid = False
            # for gui_class in gui_defines.GUI_CLASSES:
            #     if class_name == gui_class:
            #         class_is_valid = True
            #         break
            # if not class_is_valid:
            #     continue
            # debug
            if class_name == "Photo":
                yo = 1
            elif class_name == "Raster":
                yo = 1
            # debug
            json_class_content = json_content[class_name]
            str_error = self.build_parameter_file(class_name,
                                                  language,
                                                  json_class_content)
            if str_error:
                return str_error
            self.parameters[class_name][gui_defines.PARAMETER_JSON_CONTENT] = json_class_content
        self.json_file = definitions_file
        self.json_content = json_content
        return str_error
