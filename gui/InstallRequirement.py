from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class InstallRequirement:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Requisitos de instalacion', 'english': 'Install requirements'}
		self.__text = 'Requisitos de instalacion'
		self.__json_content_by_propierty['Geoid'] = {'text': {'spanish': 'Carpeta con los modelos del geoide', 'english': 'Geoids folder'}, 'definition': {'spanish': 'Carpeta con los modelos del geoide', 'english': 'Geoids folder'}, 'type': 'folder', 'default': ''}
		self.__text_by_propierty['Geoid'] = 'Carpeta con los modelos del geoide'
		self.__widget_by_propierty['Geoid'] = None
		self.__Geoid = ""
		self.__Geoid_value = ""
		self.__json_content_by_propierty['SelectedGPUs'] = {'text': {'spanish': 'GPUs activadas', 'english': 'Activated GPUs'}, 'definition': {'spanish': 'Seleccion de GPUs activadas para el proceso', 'english': 'Selection of activated GPUs for processing'}, 'type': 'string', 'len': 1000, 'default': ''}
		self.__text_by_propierty['SelectedGPUs'] = 'GPUs activadas'
		self.__widget_by_propierty['SelectedGPUs'] = None
		self.__SelectedGPUs = ""
		self.__SelectedGPUs_value = ""
		self.__json_content_by_propierty['UseCPU'] = {'text': {'spanish': 'Utilizar la CPU', 'english': 'Use CPU'}, 'definition': {'spanish': 'Utilizar la CPU al realizar un procesamiento acelerado por GPU', 'english': 'Use CPU when performing GPU accelerated processing'}, 'type': 'boolean', 'default': 'False'}
		self.__text_by_propierty['UseCPU'] = 'Utilizar la CPU'
		self.__widget_by_propierty['UseCPU'] = None
		self.__UseCPU = False
		self.__UseCPU_value = False
		self.__widget = None

	def get_propierty_json_content(self, value):
		json_content = None
		if value in self.__json_content_by_propierty:
			json_content = self.__json_content_by_propierty[value]
		return json_content

	def get_values_as_dictionary(self):
		values = {}
		values['Geoid'] = self.__Geoid_value
		values['SelectedGPUs'] = self.__SelectedGPUs_value
		values['UseCPU'] = self.__UseCPU_value
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

	@property
	def SelectedGPUs(self):
		return self.__SelectedGPUs

	@SelectedGPUs.setter
	def SelectedGPUs(self, value: 'widget:QLineEdit, toolTip:Seleccion de GPUs activadas para el proceso'):
		self.__SelectedGPUs = value

	def set_SelectedGPUs_value(self):
		propierty_SelectedGPUs_widget = self.__widget_by_propierty['SelectedGPUs'] 
		if isinstance(propierty_SelectedGPUs_widget, QSpinBox):
			self.__SelectedGPUs_value = propierty_SelectedGPUs_widget.value()
		elif isinstance(propierty_SelectedGPUs_widget, QDoubleSpinBox):
			self.__SelectedGPUs_value = propierty_SelectedGPUs_widget.value()
		elif isinstance(propierty_SelectedGPUs_widget, QComboBox):
			self.__SelectedGPUs_value = propierty_SelectedGPUs_widget.currentText()
		elif isinstance(propierty_SelectedGPUs_widget, QLineEdit):
			self.__SelectedGPUs_value = propierty_SelectedGPUs_widget.text()
		elif isinstance(propierty_SelectedGPUs_widget, QCheckBox):
			self.__SelectedGPUs_value = propierty_SelectedGPUs_widget.isChecked()

	@property
	def UseCPU(self):
		return self.__UseCPU

	@UseCPU.setter
	def UseCPU(self, value: 'widget:QCheckBox, toolTip:Utilizar la CPU al realizar un procesamiento acelerado por GPU'):
		self.__UseCPU = value

	def set_UseCPU_value(self):
		propierty_UseCPU_widget = self.__widget_by_propierty['UseCPU'] 
		if isinstance(propierty_UseCPU_widget, QSpinBox):
			self.__UseCPU_value = propierty_UseCPU_widget.value()
		elif isinstance(propierty_UseCPU_widget, QDoubleSpinBox):
			self.__UseCPU_value = propierty_UseCPU_widget.value()
		elif isinstance(propierty_UseCPU_widget, QComboBox):
			self.__UseCPU_value = propierty_UseCPU_widget.currentText()
		elif isinstance(propierty_UseCPU_widget, QLineEdit):
			self.__UseCPU_value = propierty_UseCPU_widget.text()
		elif isinstance(propierty_UseCPU_widget, QCheckBox):
			self.__UseCPU_value = propierty_UseCPU_widget.isChecked()

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
		propierty_SelectedGPUs_widget = self.__widget.get_widget('SelectedGPUs')
		if isinstance(propierty_SelectedGPUs_widget, QSpinBox):
			propierty_SelectedGPUs_widget.valueChanged.connect(self.set_SelectedGPUs_value)
		elif isinstance(propierty_SelectedGPUs_widget, QDoubleSpinBox):
			propierty_SelectedGPUs_widget.valueChanged.connect(self.set_SelectedGPUs_value)
		elif isinstance(propierty_SelectedGPUs_widget, QComboBox):
			propierty_SelectedGPUs_widget.currentIndexChanged.connect(self.set_SelectedGPUs_value)
		elif isinstance(propierty_SelectedGPUs_widget, QLineEdit):
			propierty_SelectedGPUs_widget.editingFinished.connect(self.set_SelectedGPUs_value)
			propierty_SelectedGPUs_widget.textChanged.connect(self.set_SelectedGPUs_value)
		elif isinstance(propierty_SelectedGPUs_widget, QCheckBox):
			propierty_SelectedGPUs_widget.stateChanged.connect(self.set_SelectedGPUs_value)
		self.__widget_by_propierty['SelectedGPUs'] = propierty_SelectedGPUs_widget
		propierty_UseCPU_widget = self.__widget.get_widget('UseCPU')
		if isinstance(propierty_UseCPU_widget, QSpinBox):
			propierty_UseCPU_widget.valueChanged.connect(self.set_UseCPU_value)
		elif isinstance(propierty_UseCPU_widget, QDoubleSpinBox):
			propierty_UseCPU_widget.valueChanged.connect(self.set_UseCPU_value)
		elif isinstance(propierty_UseCPU_widget, QComboBox):
			propierty_UseCPU_widget.currentIndexChanged.connect(self.set_UseCPU_value)
		elif isinstance(propierty_UseCPU_widget, QLineEdit):
			propierty_UseCPU_widget.editingFinished.connect(self.set_UseCPU_value)
			propierty_UseCPU_widget.textChanged.connect(self.set_UseCPU_value)
		elif isinstance(propierty_UseCPU_widget, QCheckBox):
			propierty_UseCPU_widget.stateChanged.connect(self.set_UseCPU_value)
		self.__widget_by_propierty['UseCPU'] = propierty_UseCPU_widget
