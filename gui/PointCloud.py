from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class PointCloud:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Nube de puntos', 'english': 'Point cloud'}
		self.__text = 'Nube de puntos'
		self.__json_content_by_propierty['Quality'] = {'text': {'spanish': 'Densidad', 'english': 'Density'}, 'definition': {'spanish': 'Calidad final de la nube de puntos densa', 'english': 'Dense point cloud quality'}, 'type': 'values', 'values': {'Highest': {'spanish': 'Mayor posible', 'english': 'Ultrahigh'}, 'High': {'spanish': 'Alto', 'english': 'High'}, 'Medium': {'spanish': 'Medio', 'english': 'Medium'}, 'Low': {'spanish': 'Bajo', 'english': 'Low'}, 'Lowest': {'spanish': 'Menor posible', 'english': 'Lowest'}}, 'default': 'Mayor posible'}
		self.__text_by_propierty['Quality'] = 'Densidad'
		self.__widget_by_propierty['Quality'] = None
		self.__Quality = ['Mayor posible' ,'Alto' ,'Medio' ,'Bajo' ,'Menor posible']
		self.__Quality_value = 'Mayor posible'
		self.__json_content_by_propierty['FilterMode'] = {'text': {'spanish': 'Tipo de filtrado', 'english': 'Filter type'}, 'definition': {'spanish': 'Tipo de filtrado', 'english': 'Filter type'}, 'type': 'values', 'values': {'False': {'spanish': 'Falso', 'english': 'False'}, 'Mild': {'spanish': 'Suave', 'english': 'Mild'}, 'Moderate': {'spanish': 'Moderado', 'english': 'Moderate'}, 'Aggressive': {'spanish': 'Agresivo', 'english': 'Aggressive'}}, 'default': 'Agresivo'}
		self.__text_by_propierty['FilterMode'] = 'Tipo de filtrado'
		self.__widget_by_propierty['FilterMode'] = None
		self.__FilterMode = ['Agresivo' ,'Falso' ,'Suave' ,'Moderado']
		self.__FilterMode_value = 'Agresivo'
		self.__widget = None

	def get_propierty_json_content(self, value):
		json_content = None
		if value in self.__json_content_by_propierty:
			json_content = self.__json_content_by_propierty[value]
		return json_content

	def get_values_as_dictionary(self):
		values = {}
		values['Quality'] = self.__Quality_value
		values['FilterMode'] = self.__FilterMode_value
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
	def Quality(self):
		return self.__Quality

	@Quality.setter
	def Quality(self, value: 'widget:QComboBox, toolTip:Calidad final de la nube de puntos densa'):
		self.__Quality = value

	def set_Quality_value(self):
		propierty_Quality_widget = self.__widget_by_propierty['Quality'] 
		if isinstance(propierty_Quality_widget, QSpinBox):
			self.__Quality_value = propierty_Quality_widget.value()
		elif isinstance(propierty_Quality_widget, QDoubleSpinBox):
			self.__Quality_value = propierty_Quality_widget.value()
		elif isinstance(propierty_Quality_widget, QComboBox):
			self.__Quality_value = propierty_Quality_widget.currentText()
		elif isinstance(propierty_Quality_widget, QLineEdit):
			self.__Quality_value = propierty_Quality_widget.text()
		elif isinstance(propierty_Quality_widget, QCheckBox):
			self.__Quality_value = propierty_Quality_widget.isChecked()

	@property
	def FilterMode(self):
		return self.__FilterMode

	@FilterMode.setter
	def FilterMode(self, value: 'widget:QComboBox, toolTip:Tipo de filtrado'):
		self.__FilterMode = value

	def set_FilterMode_value(self):
		propierty_FilterMode_widget = self.__widget_by_propierty['FilterMode'] 
		if isinstance(propierty_FilterMode_widget, QSpinBox):
			self.__FilterMode_value = propierty_FilterMode_widget.value()
		elif isinstance(propierty_FilterMode_widget, QDoubleSpinBox):
			self.__FilterMode_value = propierty_FilterMode_widget.value()
		elif isinstance(propierty_FilterMode_widget, QComboBox):
			self.__FilterMode_value = propierty_FilterMode_widget.currentText()
		elif isinstance(propierty_FilterMode_widget, QLineEdit):
			self.__FilterMode_value = propierty_FilterMode_widget.text()
		elif isinstance(propierty_FilterMode_widget, QCheckBox):
			self.__FilterMode_value = propierty_FilterMode_widget.isChecked()

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
		propierty_Quality_widget = self.__widget.get_widget('Quality')
		if isinstance(propierty_Quality_widget, QSpinBox):
			propierty_Quality_widget.valueChanged.connect(self.set_Quality_value)
		elif isinstance(propierty_Quality_widget, QDoubleSpinBox):
			propierty_Quality_widget.valueChanged.connect(self.set_Quality_value)
		elif isinstance(propierty_Quality_widget, QComboBox):
			propierty_Quality_widget.currentIndexChanged.connect(self.set_Quality_value)
		elif isinstance(propierty_Quality_widget, QLineEdit):
			propierty_Quality_widget.editingFinished.connect(self.set_Quality_value)
			propierty_Quality_widget.textChanged.connect(self.set_Quality_value)
		elif isinstance(propierty_Quality_widget, QCheckBox):
			propierty_Quality_widget.stateChanged.connect(self.set_Quality_value)
		self.__widget_by_propierty['Quality'] = propierty_Quality_widget
		propierty_FilterMode_widget = self.__widget.get_widget('FilterMode')
		if isinstance(propierty_FilterMode_widget, QSpinBox):
			propierty_FilterMode_widget.valueChanged.connect(self.set_FilterMode_value)
		elif isinstance(propierty_FilterMode_widget, QDoubleSpinBox):
			propierty_FilterMode_widget.valueChanged.connect(self.set_FilterMode_value)
		elif isinstance(propierty_FilterMode_widget, QComboBox):
			propierty_FilterMode_widget.currentIndexChanged.connect(self.set_FilterMode_value)
		elif isinstance(propierty_FilterMode_widget, QLineEdit):
			propierty_FilterMode_widget.editingFinished.connect(self.set_FilterMode_value)
			propierty_FilterMode_widget.textChanged.connect(self.set_FilterMode_value)
		elif isinstance(propierty_FilterMode_widget, QCheckBox):
			propierty_FilterMode_widget.stateChanged.connect(self.set_FilterMode_value)
		self.__widget_by_propierty['FilterMode'] = propierty_FilterMode_widget
