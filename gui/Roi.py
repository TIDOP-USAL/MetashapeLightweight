from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class ROI:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Region de interes', 'english': 'Region of interest'}
		self.__text = 'Region de interes'
		self.__json_content_by_propierty['Path'] = {'text': {'spanish': 'Ruta ROI', 'english': 'ROI path'}, 'definition': {'spanish': 'Ruta del archivo de la ROI', 'english': 'ROI path file'}, 'type': 'file open', 'default': ''}
		self.__text_by_propierty['Path'] = 'Ruta ROI'
		self.__widget_by_propierty['Path'] = None
		self.__Path = ""
		self.__Path_value = ""
		self.__json_content_by_propierty['Method'] = {'text': {'spanish': 'Fuente ROI', 'english': 'ROI source'}, 'definition': {'spanish': 'Metodo de definicion de la ROI', 'english': 'Method for ROI definition'}, 'type': 'values', 'values': {'0': {'spanish': 'Region total con recubrimiento', 'english': 'Full stereoscopic region'}, 'SHP': {'spanish': 'Importada de shapefile', 'english': 'From shapefile'}}, 'default': 'Region total con recubrimiento'}
		self.__text_by_propierty['Method'] = 'Fuente ROI'
		self.__widget_by_propierty['Method'] = None
		self.__Method = ['Region total con recubrimiento' ,'Importada de shapefile']
		self.__Method_value = 'Region total con recubrimiento'
		self.__widget = None

	def get_propierty_json_content(self, value):
		json_content = None
		if value in self.__json_content_by_propierty:
			json_content = self.__json_content_by_propierty[value]
		return json_content

	def get_values_as_dictionary(self):
		values = {}
		values['Path'] = self.__Path_value
		values['Method'] = self.__Method_value
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
	def Path(self):
		return self.__Path

	@Path.setter
	def Path(self, value: 'widget:file, toolTip:Ruta del archivo de la ROI'):
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
	def Method(self):
		return self.__Method

	@Method.setter
	def Method(self, value: 'widget:QComboBox, toolTip:Metodo de definicion de la ROI'):
		self.__Method = value

	def set_Method_value(self):
		propierty_Method_widget = self.__widget_by_propierty['Method'] 
		if isinstance(propierty_Method_widget, QSpinBox):
			self.__Method_value = propierty_Method_widget.value()
		elif isinstance(propierty_Method_widget, QDoubleSpinBox):
			self.__Method_value = propierty_Method_widget.value()
		elif isinstance(propierty_Method_widget, QComboBox):
			self.__Method_value = propierty_Method_widget.currentText()
		elif isinstance(propierty_Method_widget, QLineEdit):
			self.__Method_value = propierty_Method_widget.text()
		elif isinstance(propierty_Method_widget, QCheckBox):
			self.__Method_value = propierty_Method_widget.isChecked()

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
		propierty_Method_widget = self.__widget.get_widget('Method')
		if isinstance(propierty_Method_widget, QSpinBox):
			propierty_Method_widget.valueChanged.connect(self.set_Method_value)
		elif isinstance(propierty_Method_widget, QDoubleSpinBox):
			propierty_Method_widget.valueChanged.connect(self.set_Method_value)
		elif isinstance(propierty_Method_widget, QComboBox):
			propierty_Method_widget.currentIndexChanged.connect(self.set_Method_value)
		elif isinstance(propierty_Method_widget, QLineEdit):
			propierty_Method_widget.editingFinished.connect(self.set_Method_value)
			propierty_Method_widget.textChanged.connect(self.set_Method_value)
		elif isinstance(propierty_Method_widget, QCheckBox):
			propierty_Method_widget.stateChanged.connect(self.set_Method_value)
		self.__widget_by_propierty['Method'] = propierty_Method_widget
