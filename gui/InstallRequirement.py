from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class InstallRequirement:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Requisitos de instalacion', 'english': 'Install requirements'}
		self.__text = 'Requisitos de instalacion'
		self.__json_content_by_propierty['Env'] = {'text': {'spanish': 'Carpeta del entorno conda', 'english': 'Conda environment folder'}, 'definition': {'spanish': 'Carpeta del entorno conda', 'english': 'Conda environment folder'}, 'type': 'folder', 'default': ''}
		self.__text_by_propierty['Env'] = 'Carpeta del entorno conda'
		self.__widget_by_propierty['Env'] = None
		self.__Env = ""
		self.__Env_value = ""
		self.__json_content_by_propierty['Geoid'] = {'text': {'spanish': 'Carpeta con los modelos del geoide', 'english': 'Geoids folder'}, 'definition': {'spanish': 'Carpeta con los modelos del geoide', 'english': 'Geoids folder'}, 'type': 'folder', 'default': ''}
		self.__text_by_propierty['Geoid'] = 'Carpeta con los modelos del geoide'
		self.__widget_by_propierty['Geoid'] = None
		self.__Geoid = ""
		self.__Geoid_value = ""
		self.__widget = None

	def get_propierty_json_content(self, value):
		json_content = None
		if value in self.__json_content_by_propierty:
			json_content = self.__json_content_by_propierty[value]
		return json_content

	def get_values_as_dictionary(self):
		values = {}
		values['Env'] = self.__Env_value
		values['Geoid'] = self.__Geoid_value
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
	def Env(self):
		return self.__Env

	@Env.setter
	def Env(self, value: 'widget:file, type:folder, toolTip:Carpeta del entorno conda'):
		self.__Env = value

	def set_Env_value(self):
		propierty_Env_widget = self.__widget_by_propierty['Env'] 
		if isinstance(propierty_Env_widget, QSpinBox):
			self.__Env_value = propierty_Env_widget.value()
		elif isinstance(propierty_Env_widget, QDoubleSpinBox):
			self.__Env_value = propierty_Env_widget.value()
		elif isinstance(propierty_Env_widget, QComboBox):
			self.__Env_value = propierty_Env_widget.currentText()
		elif isinstance(propierty_Env_widget, QLineEdit):
			self.__Env_value = propierty_Env_widget.text()
		elif isinstance(propierty_Env_widget, QCheckBox):
			self.__Env_value = propierty_Env_widget.isChecked()

	@property
	def Geoid(self):
		return self.__Geoid

	@Geoid.setter
	def Geoid(self, value: 'widget:file, type:folder, toolTip:Carpeta con los modelos del geoide'):
		self.__Geoid = value

	def set_Geoid_value(self):
		propierty_Geoid_widget = self.__widget_by_propierty['Geoid'] 
		if isinstance(propierty_Geoid_widget, QSpinBox):
			self.__Geoid_value = propierty_Geoid_widget.value()
		elif isinstance(propierty_Geoid_widget, QDoubleSpinBox):
			self.__Geoid_value = propierty_Geoid_widget.value()
		elif isinstance(propierty_Geoid_widget, QComboBox):
			self.__Geoid_value = propierty_Geoid_widget.currentText()
		elif isinstance(propierty_Geoid_widget, QLineEdit):
			self.__Geoid_value = propierty_Geoid_widget.text()
		elif isinstance(propierty_Geoid_widget, QCheckBox):
			self.__Geoid_value = propierty_Geoid_widget.isChecked()

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
		propierty_Env_widget = self.__widget.get_widget('Env')
		if isinstance(propierty_Env_widget, QSpinBox):
			propierty_Env_widget.valueChanged.connect(self.set_Env_value)
		elif isinstance(propierty_Env_widget, QDoubleSpinBox):
			propierty_Env_widget.valueChanged.connect(self.set_Env_value)
		elif isinstance(propierty_Env_widget, QComboBox):
			propierty_Env_widget.currentIndexChanged.connect(self.set_Env_value)
		elif isinstance(propierty_Env_widget, QLineEdit):
			propierty_Env_widget.editingFinished.connect(self.set_Env_value)
			propierty_Env_widget.textChanged.connect(self.set_Env_value)
		elif isinstance(propierty_Env_widget, QCheckBox):
			propierty_Env_widget.stateChanged.connect(self.set_Env_value)
		self.__widget_by_propierty['Env'] = propierty_Env_widget
		propierty_Geoid_widget = self.__widget.get_widget('Geoid')
		if isinstance(propierty_Geoid_widget, QSpinBox):
			propierty_Geoid_widget.valueChanged.connect(self.set_Geoid_value)
		elif isinstance(propierty_Geoid_widget, QDoubleSpinBox):
			propierty_Geoid_widget.valueChanged.connect(self.set_Geoid_value)
		elif isinstance(propierty_Geoid_widget, QComboBox):
			propierty_Geoid_widget.currentIndexChanged.connect(self.set_Geoid_value)
		elif isinstance(propierty_Geoid_widget, QLineEdit):
			propierty_Geoid_widget.editingFinished.connect(self.set_Geoid_value)
			propierty_Geoid_widget.textChanged.connect(self.set_Geoid_value)
		elif isinstance(propierty_Geoid_widget, QCheckBox):
			propierty_Geoid_widget.stateChanged.connect(self.set_Geoid_value)
		self.__widget_by_propierty['Geoid'] = propierty_Geoid_widget
