from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class Project:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Proyecto', 'english': 'Project'}
		self.__text = 'Proyecto'
		self.__json_content_by_propierty['Label'] = {'text': {'spanish': 'Etiqueta', 'english': 'Label'}, 'definition': {'spanish': 'Etiqueta con la que se nombraran los productos resultantes', 'english': 'Label to be used to name the resulting products'}, 'type': 'string', 'len': 50, 'default': 'Example project'}
		self.__text_by_propierty['Label'] = 'Etiqueta'
		self.__widget_by_propierty['Label'] = None
		self.__Label = "Example project"
		self.__Label_value = "Example project"
		self.__json_content_by_propierty['EPSG'] = {'text': {'spanish': 'Codigo EPSG', 'english': 'EPSG code'}, 'definition': {'spanish': 'Codigo EPSG con el que se exportaran los productos resultantes', 'english': 'EPSG code under which the resulting products are to be exported'}, 'type': 'string', 'len': 11, 'default': '25830+5782'}
		self.__text_by_propierty['EPSG'] = 'Codigo EPSG'
		self.__widget_by_propierty['EPSG'] = None
		self.__EPSG = "25830+5782"
		self.__EPSG_value = "25830+5782"
		self.__json_content_by_propierty['Path'] = {'text': {'spanish': 'Directorio de resultados', 'english': 'Output path'}, 'definition': {'spanish': 'Ruta del directorio de resultados', 'english': 'Results directory path'}, 'type': 'folder', 'default': ''}
		self.__text_by_propierty['Path'] = 'Directorio de resultados'
		self.__widget_by_propierty['Path'] = None
		self.__Path = ""
		self.__Path_value = ""
		self.__json_content_by_propierty['DemGSD'] = {'text': {'spanish': 'GSD para MDT y MDS en metros', 'english': 'GSD for DTM and DSM in meters'}, 'definition': {'spanish': 'Resolucion en metros con la que se exportaran el modelo digital de superficies y del terreno (0 para maxima posible)', 'english': 'Resolution in metres at which the digital surface and terrain model will be exported (0 for maximum possible).'}, 'type': 'real', 'decimals': 3, 'minimum': 0.0, 'maximum': 2.0, 'singleStep': 0.01, 'default': 0.05}
		self.__text_by_propierty['DemGSD'] = 'GSD para MDT y MDS en metros'
		self.__widget_by_propierty['DemGSD'] = None
		self.__DemGSD = 0.05
		self.__DemGSD_value = 0.05
		self.__json_content_by_propierty['OrthoGSD'] = {'text': {'spanish': 'GSD para ortomosaico en metros', 'english': 'GSD for Orthomosaic in meters'}, 'definition': {'spanish': 'Resolucion en metros con la que se exportara el ortomosaico (0 para maxima posible)', 'english': 'Resolution in metres at which the orthomosaic will be exported (0 for maximum possible)'}, 'type': 'real', 'decimals': 3, 'minimum': 0.0, 'maximum': 2.0, 'singleStep': 0.01, 'default': 0.05}
		self.__text_by_propierty['OrthoGSD'] = 'GSD para ortomosaico en metros'
		self.__widget_by_propierty['OrthoGSD'] = None
		self.__OrthoGSD = 0.05
		self.__OrthoGSD_value = 0.05
		self.__widget = None

	def get_propierty_json_content(self, value):
		json_content = None
		if value in self.__json_content_by_propierty:
			json_content = self.__json_content_by_propierty[value]
		return json_content

	def get_values_as_dictionary(self):
		values = {}
		values['Label'] = self.__Label_value
		values['EPSG'] = self.__EPSG_value
		values['Path'] = self.__Path_value
		values['DemGSD'] = self.__DemGSD_value
		values['OrthoGSD'] = self.__OrthoGSD_value
		return values

	def get_text(self):
		return self.__text

	def get_text_by_propierty(self):
		return self.__text_by_propierty

	def get_widget_propierty(self, value):
		widget_propierty = None
		if value in self.__widget_by_propierty:
			widget_propierty = self.__widget_by_propierty[value]
		return widget_propierty

	@property
	def Label(self):
		return self.__Label

	@Label.setter
	def Label(self, value: 'widget:QLineEdit, toolTip:Etiqueta con la que se nombraran los productos resultantes'):
		self.__Label = value

	def set_Label_value(self):
		propierty_Label_widget = self.__widget_by_propierty['Label'] 
		if isinstance(propierty_Label_widget, QSpinBox):
			self.__Label_value = propierty_Label_widget.value()
		elif isinstance(propierty_Label_widget, QDoubleSpinBox):
			self.__Label_value = propierty_Label_widget.value()
		elif isinstance(propierty_Label_widget, QComboBox):
			self.__Label_value = propierty_Label_widget.currentText()
		elif isinstance(propierty_Label_widget, QLineEdit):
			self.__Label_value = propierty_Label_widget.text()
		elif isinstance(propierty_Label_widget, QCheckBox):
			self.__Label_value = propierty_Label_widget.isChecked()

	@property
	def EPSG(self):
		return self.__EPSG

	@EPSG.setter
	def EPSG(self, value: 'widget:QLineEdit, toolTip:Codigo EPSG con el que se exportaran los productos resultantes'):
		self.__EPSG = value

	def set_EPSG_value(self):
		propierty_EPSG_widget = self.__widget_by_propierty['EPSG'] 
		if isinstance(propierty_EPSG_widget, QSpinBox):
			self.__EPSG_value = propierty_EPSG_widget.value()
		elif isinstance(propierty_EPSG_widget, QDoubleSpinBox):
			self.__EPSG_value = propierty_EPSG_widget.value()
		elif isinstance(propierty_EPSG_widget, QComboBox):
			self.__EPSG_value = propierty_EPSG_widget.currentText()
		elif isinstance(propierty_EPSG_widget, QLineEdit):
			self.__EPSG_value = propierty_EPSG_widget.text()
		elif isinstance(propierty_EPSG_widget, QCheckBox):
			self.__EPSG_value = propierty_EPSG_widget.isChecked()

	@property
	def Path(self):
		return self.__Path

	@Path.setter
	def Path(self, value: 'widget:file, type:folder, toolTip:Ruta del directorio de resultados'):
		self.__Path = value

	def set_Path_value(self):
		propierty_Path_widget = self.__widget_by_propierty['Path'] 
		if isinstance(propierty_Path_widget, QSpinBox):
			self.__Path_value = propierty_Path_widget.value()
		elif isinstance(propierty_Path_widget, QDoubleSpinBox):
			self.__Path_value = propierty_Path_widget.value()
		elif isinstance(propierty_Path_widget, QComboBox):
			self.__Path_value = propierty_Path_widget.currentText()
		elif isinstance(propierty_Path_widget, QLineEdit):
			self.__Path_value = propierty_Path_widget.text()
		elif isinstance(propierty_Path_widget, QCheckBox):
			self.__Path_value = propierty_Path_widget.isChecked()

	@property
	def DemGSD(self):
		return self.__DemGSD

	@DemGSD.setter
	def DemGSD(self, value: 'widget:QDoubleSpinBox, decimals:3, minimum:0.0, maximum:2.0, singleStep:0.01, toolTip:Resolucion en metros con la que se exportaran el modelo digital de superficies y del terreno (0 para maxima posible)'):
		self.__DemGSD = value

	def set_DemGSD_value(self):
		propierty_DemGSD_widget = self.__widget_by_propierty['DemGSD'] 
		if isinstance(propierty_DemGSD_widget, QSpinBox):
			self.__DemGSD_value = propierty_DemGSD_widget.value()
		elif isinstance(propierty_DemGSD_widget, QDoubleSpinBox):
			self.__DemGSD_value = propierty_DemGSD_widget.value()
		elif isinstance(propierty_DemGSD_widget, QComboBox):
			self.__DemGSD_value = propierty_DemGSD_widget.currentText()
		elif isinstance(propierty_DemGSD_widget, QLineEdit):
			self.__DemGSD_value = propierty_DemGSD_widget.text()
		elif isinstance(propierty_DemGSD_widget, QCheckBox):
			self.__DemGSD_value = propierty_DemGSD_widget.isChecked()

	@property
	def OrthoGSD(self):
		return self.__OrthoGSD

	@OrthoGSD.setter
	def OrthoGSD(self, value: 'widget:QDoubleSpinBox, decimals:3, minimum:0.0, maximum:2.0, singleStep:0.01, toolTip:Resolucion en metros con la que se exportara el ortomosaico (0 para maxima posible)'):
		self.__OrthoGSD = value

	def set_OrthoGSD_value(self):
		propierty_OrthoGSD_widget = self.__widget_by_propierty['OrthoGSD'] 
		if isinstance(propierty_OrthoGSD_widget, QSpinBox):
			self.__OrthoGSD_value = propierty_OrthoGSD_widget.value()
		elif isinstance(propierty_OrthoGSD_widget, QDoubleSpinBox):
			self.__OrthoGSD_value = propierty_OrthoGSD_widget.value()
		elif isinstance(propierty_OrthoGSD_widget, QComboBox):
			self.__OrthoGSD_value = propierty_OrthoGSD_widget.currentText()
		elif isinstance(propierty_OrthoGSD_widget, QLineEdit):
			self.__OrthoGSD_value = propierty_OrthoGSD_widget.text()
		elif isinstance(propierty_OrthoGSD_widget, QCheckBox):
			self.__OrthoGSD_value = propierty_OrthoGSD_widget.isChecked()

	def set_values_from_dictionary(self, values):
		for value in values:
			propierty_widget = self.__widget_by_propierty[value]
			if isinstance(propierty_widget, QComboBox):
				json_values = self.__json_content_by_propierty[value][gui_defines.GUI_CLASSES_PROPIERTY_TYPE_VALUES_LIST_TAG]
				if values[value] in json_values:
					for language in json_values[values[value]]:
						value_language = json_values[values[value]][language]
						pos = propierty_widget.findText(value_language)
						if pos != -1:
							propierty_widget.setCurrentIndex(pos)
							break
			elif isinstance(propierty_widget, QSpinBox):
				int_value = int(values[value])
				propierty_widget.setValue(int_value)
			elif isinstance(propierty_widget, QDoubleSpinBox):
				float_value = float(values[value])
				propierty_widget.setValue(float_value)
			elif isinstance(propierty_widget, QLineEdit):
				propierty_widget.setText(values[value])
			elif isinstance(propierty_widget, QCheckBox):
				propierty_widget.setChecked(values[value])
		return

	def set_widget(self, widget):
		self.__widget = widget
		propierty_Label_widget = self.__widget.get_widget('Label')
		if isinstance(propierty_Label_widget, QSpinBox):
			propierty_Label_widget.valueChanged.connect(self.set_Label_value)
		elif isinstance(propierty_Label_widget, QDoubleSpinBox):
			propierty_Label_widget.valueChanged.connect(self.set_Label_value)
		elif isinstance(propierty_Label_widget, QComboBox):
			propierty_Label_widget.currentIndexChanged.connect(self.set_Label_value)
		elif isinstance(propierty_Label_widget, QLineEdit):
			propierty_Label_widget.editingFinished.connect(self.set_Label_value)
			propierty_Label_widget.textChanged.connect(self.set_Label_value)
		elif isinstance(propierty_Label_widget, QCheckBox):
			propierty_Label_widget.stateChanged.connect(self.set_Label_value)
		self.__widget_by_propierty['Label'] = propierty_Label_widget
		propierty_EPSG_widget = self.__widget.get_widget('EPSG')
		if isinstance(propierty_EPSG_widget, QSpinBox):
			propierty_EPSG_widget.valueChanged.connect(self.set_EPSG_value)
		elif isinstance(propierty_EPSG_widget, QDoubleSpinBox):
			propierty_EPSG_widget.valueChanged.connect(self.set_EPSG_value)
		elif isinstance(propierty_EPSG_widget, QComboBox):
			propierty_EPSG_widget.currentIndexChanged.connect(self.set_EPSG_value)
		elif isinstance(propierty_EPSG_widget, QLineEdit):
			propierty_EPSG_widget.editingFinished.connect(self.set_EPSG_value)
			propierty_EPSG_widget.textChanged.connect(self.set_EPSG_value)
		elif isinstance(propierty_EPSG_widget, QCheckBox):
			propierty_EPSG_widget.stateChanged.connect(self.set_EPSG_value)
		self.__widget_by_propierty['EPSG'] = propierty_EPSG_widget
		propierty_Path_widget = self.__widget.get_widget('Path')
		if isinstance(propierty_Path_widget, QSpinBox):
			propierty_Path_widget.valueChanged.connect(self.set_Path_value)
		elif isinstance(propierty_Path_widget, QDoubleSpinBox):
			propierty_Path_widget.valueChanged.connect(self.set_Path_value)
		elif isinstance(propierty_Path_widget, QComboBox):
			propierty_Path_widget.currentIndexChanged.connect(self.set_Path_value)
		elif isinstance(propierty_Path_widget, QLineEdit):
			propierty_Path_widget.editingFinished.connect(self.set_Path_value)
			propierty_Path_widget.textChanged.connect(self.set_Path_value)
		elif isinstance(propierty_Path_widget, QCheckBox):
			propierty_Path_widget.stateChanged.connect(self.set_Path_value)
		self.__widget_by_propierty['Path'] = propierty_Path_widget
		propierty_DemGSD_widget = self.__widget.get_widget('DemGSD')
		if isinstance(propierty_DemGSD_widget, QSpinBox):
			propierty_DemGSD_widget.valueChanged.connect(self.set_DemGSD_value)
		elif isinstance(propierty_DemGSD_widget, QDoubleSpinBox):
			propierty_DemGSD_widget.valueChanged.connect(self.set_DemGSD_value)
		elif isinstance(propierty_DemGSD_widget, QComboBox):
			propierty_DemGSD_widget.currentIndexChanged.connect(self.set_DemGSD_value)
		elif isinstance(propierty_DemGSD_widget, QLineEdit):
			propierty_DemGSD_widget.editingFinished.connect(self.set_DemGSD_value)
			propierty_DemGSD_widget.textChanged.connect(self.set_DemGSD_value)
		elif isinstance(propierty_DemGSD_widget, QCheckBox):
			propierty_DemGSD_widget.stateChanged.connect(self.set_DemGSD_value)
		self.__widget_by_propierty['DemGSD'] = propierty_DemGSD_widget
		propierty_OrthoGSD_widget = self.__widget.get_widget('OrthoGSD')
		if isinstance(propierty_OrthoGSD_widget, QSpinBox):
			propierty_OrthoGSD_widget.valueChanged.connect(self.set_OrthoGSD_value)
		elif isinstance(propierty_OrthoGSD_widget, QDoubleSpinBox):
			propierty_OrthoGSD_widget.valueChanged.connect(self.set_OrthoGSD_value)
		elif isinstance(propierty_OrthoGSD_widget, QComboBox):
			propierty_OrthoGSD_widget.currentIndexChanged.connect(self.set_OrthoGSD_value)
		elif isinstance(propierty_OrthoGSD_widget, QLineEdit):
			propierty_OrthoGSD_widget.editingFinished.connect(self.set_OrthoGSD_value)
			propierty_OrthoGSD_widget.textChanged.connect(self.set_OrthoGSD_value)
		elif isinstance(propierty_OrthoGSD_widget, QCheckBox):
			propierty_OrthoGSD_widget.stateChanged.connect(self.set_OrthoGSD_value)
		self.__widget_by_propierty['OrthoGSD'] = propierty_OrthoGSD_widget
