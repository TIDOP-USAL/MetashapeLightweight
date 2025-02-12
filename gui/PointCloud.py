from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class PointCloud:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Nube de puntos', 'english': 'Point cloud'}
		self.__text = 'Nube de puntos'
		self.__json_content_by_propierty['Quality'] = {'text': {'spanish': 'Densidad', 'english': 'Density'}, 'definition': {'spanish': 'Calidad final de la nube de puntos densa', 'english': 'Dense point cloud quality'}, 'type': 'values', 'values': {'Ultrahigh': {'spanish': 'Mayor posible', 'english': 'Ultrahigh'}, 'High': {'spanish': 'Alto', 'english': 'High'}, 'Medium': {'spanish': 'Medio', 'english': 'Medium'}, 'Low': {'spanish': 'Bajo', 'english': 'Low'}, 'Lowest': {'spanish': 'Menor posible', 'english': 'Lowest'}}, 'default': 'Mayor posible'}
		self.__text_by_propierty['Quality'] = 'Densidad'
		self.__widget_by_propierty['Quality'] = None
		self.__Quality = ['Mayor posible' ,'Alto' ,'Medio' ,'Bajo' ,'Menor posible']
		self.__Quality_value = 'Mayor posible'
		self.__json_content_by_propierty['FilterMode'] = {'text': {'spanish': 'Tipo de filtrado', 'english': 'Filter type'}, 'definition': {'spanish': 'Tipo de filtrado', 'english': 'Filter type'}, 'type': 'values', 'values': {'False': {'spanish': 'Falso', 'english': 'False'}, 'Mild': {'spanish': 'Suave', 'english': 'Mild'}, 'Moderate': {'spanish': 'Moderado', 'english': 'Moderate'}, 'Aggressive': {'spanish': 'Agresivo', 'english': 'Aggressive'}}, 'default': 'Agresivo'}
		self.__text_by_propierty['FilterMode'] = 'Tipo de filtrado'
		self.__widget_by_propierty['FilterMode'] = None
		self.__FilterMode = ['Agresivo' ,'Falso' ,'Suave' ,'Moderado']
		self.__FilterMode_value = 'Agresivo'
		self.__json_content_by_propierty['ConfidenceRangeMin'] = {'text': {'spanish': 'Confianza. Umbral minimo', 'english': 'Confidence. Minimum threshold'}, 'definition': {'spanish': 'Numero minimo de mapas de profundidad implicados en la generacion de puntos', 'english': 'Minimum number of depth maps involved in the point generation'}, 'type': 'integer', 'minimum': 0, 'maximum': 255, 'singleStep': 1, 'default': 0}
		self.__text_by_propierty['ConfidenceRangeMin'] = 'Confianza. Umbral minimo'
		self.__widget_by_propierty['ConfidenceRangeMin'] = None
		self.__ConfidenceRangeMin = 0
		self.__ConfidenceRangeMin_value = 0
		self.__json_content_by_propierty['ConfidenceRangeMax'] = {'text': {'spanish': 'Confianza. Umbral maximo', 'english': 'Confidence. Maximum threshold'}, 'definition': {'spanish': 'Numero maximo de mapas de profundidad implicados en la generacion de puntos', 'english': 'Maximum number of depth maps involved in the point generation'}, 'type': 'integer', 'minimum': 0, 'maximum': 255, 'singleStep': 1, 'default': 255}
		self.__text_by_propierty['ConfidenceRangeMax'] = 'Confianza. Umbral maximo'
		self.__widget_by_propierty['ConfidenceRangeMax'] = None
		self.__ConfidenceRangeMax = 255
		self.__ConfidenceRangeMax_value = 255
		self.__json_content_by_propierty['GroundMaxAngle'] = {'text': {'spanish': 'Terreno. Angulo maximo', 'english': 'Ground. Max angle (deg)'}, 'definition': {'spanish': '', 'english': 'Sets limitation for an angle between terrain model and the line to connect the point in question with a point from a ground class'}, 'type': 'integer', 'minimum': 0, 'maximum': 45, 'singleStep': 1, 'default': 15}
		self.__text_by_propierty['GroundMaxAngle'] = 'Terreno. Angulo maximo'
		self.__widget_by_propierty['GroundMaxAngle'] = None
		self.__GroundMaxAngle = 15
		self.__GroundMaxAngle_value = 15
		self.__json_content_by_propierty['GroundMaxDistance'] = {'text': {'spanish': 'Terreno. Distancia maxima (m)', 'english': 'Ground. Max distance (m)'}, 'definition': {'spanish': '', 'english': 'Maximum distance between the point in question and terrain model'}, 'type': 'integer', 'minimum': 0, 'maximum': 5, 'singleStep': 1, 'default': 1}
		self.__text_by_propierty['GroundMaxDistance'] = 'Terreno. Distancia maxima (m)'
		self.__widget_by_propierty['GroundMaxDistance'] = None
		self.__GroundMaxDistance = 1
		self.__GroundMaxDistance_value = 1
		self.__json_content_by_propierty['GroundMaxSlope'] = {'text': {'spanish': 'Terreno. Pendiente maxima (deg)', 'english': 'Ground. Max terrain slope (deg)'}, 'definition': {'spanish': '', 'english': 'The parameter helps to determine whether classification is used for mountainous terrain or not'}, 'type': 'integer', 'minimum': 0, 'maximum': 90, 'singleStep': 1, 'default': 45}
		self.__text_by_propierty['GroundMaxSlope'] = 'Terreno. Pendiente maxima (deg)'
		self.__widget_by_propierty['GroundMaxSlope'] = None
		self.__GroundMaxSlope = 45
		self.__GroundMaxSlope_value = 45
		self.__json_content_by_propierty['GroundCellSize'] = {'text': {'spanish': 'Terreno. Tamaño malla (m)', 'english': 'Ground. Cell size (m)'}, 'definition': {'spanish': '', 'english': 'Determines the size of the cells for point cloud to be divided into as a preparatory step in ground points classification procedure'}, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'singleStep': 1, 'default': 50}
		self.__text_by_propierty['GroundCellSize'] = 'Terreno. Tamaño malla (m)'
		self.__widget_by_propierty['GroundCellSize'] = None
		self.__GroundCellSize = 50
		self.__GroundCellSize_value = 50
		self.__json_content_by_propierty['GroundErosionRadius'] = {'text': {'spanish': 'Terreno. Radio erosion (m)', 'english': 'Ground. Erosion radius (m)'}, 'definition': {'spanish': '', 'english': 'Determines the indentation (in meters) from unclassified points to create an additional area around the object, it is useful when classifying houses and trees to exclude the remaining "stumps" when building DTM.'}, 'type': 'real', 'decimals': 2, 'minimum': 0, 'maximum': 100, 'singleStep': 1, 'default': 0}
		self.__text_by_propierty['GroundErosionRadius'] = 'Terreno. Radio erosion (m)'
		self.__widget_by_propierty['GroundErosionRadius'] = None
		self.__GroundErosionRadius = 0
		self.__GroundErosionRadius_value = 0
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
		values['ConfidenceRangeMin'] = self.__ConfidenceRangeMin_value
		values['ConfidenceRangeMax'] = self.__ConfidenceRangeMax_value
		values['GroundMaxAngle'] = self.__GroundMaxAngle_value
		values['GroundMaxDistance'] = self.__GroundMaxDistance_value
		values['GroundMaxSlope'] = self.__GroundMaxSlope_value
		values['GroundCellSize'] = self.__GroundCellSize_value
		values['GroundErosionRadius'] = self.__GroundErosionRadius_value
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

	@property
	def ConfidenceRangeMin(self):
		return self.__ConfidenceRangeMin

	@ConfidenceRangeMin.setter
	def ConfidenceRangeMin(self, value: 'widget:QSpinBox, minimum:0, maximum:255, singleStep:1, toolTip:Numero minimo de mapas de profundidad implicados en la generacion de puntos'):
		self.__ConfidenceRangeMin = value

	def set_ConfidenceRangeMin_value(self):
		propierty_ConfidenceRangeMin_widget = self.__widget_by_propierty['ConfidenceRangeMin'] 
		if isinstance(propierty_ConfidenceRangeMin_widget, QSpinBox):
			self.__ConfidenceRangeMin_value = propierty_ConfidenceRangeMin_widget.value()
		elif isinstance(propierty_ConfidenceRangeMin_widget, QDoubleSpinBox):
			self.__ConfidenceRangeMin_value = propierty_ConfidenceRangeMin_widget.value()
		elif isinstance(propierty_ConfidenceRangeMin_widget, QComboBox):
			self.__ConfidenceRangeMin_value = propierty_ConfidenceRangeMin_widget.currentText()
		elif isinstance(propierty_ConfidenceRangeMin_widget, QLineEdit):
			self.__ConfidenceRangeMin_value = propierty_ConfidenceRangeMin_widget.text()
		elif isinstance(propierty_ConfidenceRangeMin_widget, QCheckBox):
			self.__ConfidenceRangeMin_value = propierty_ConfidenceRangeMin_widget.isChecked()

	@property
	def ConfidenceRangeMax(self):
		return self.__ConfidenceRangeMax

	@ConfidenceRangeMax.setter
	def ConfidenceRangeMax(self, value: 'widget:QSpinBox, minimum:0, maximum:255, singleStep:1, toolTip:Numero maximo de mapas de profundidad implicados en la generacion de puntos'):
		self.__ConfidenceRangeMax = value

	def set_ConfidenceRangeMax_value(self):
		propierty_ConfidenceRangeMax_widget = self.__widget_by_propierty['ConfidenceRangeMax'] 
		if isinstance(propierty_ConfidenceRangeMax_widget, QSpinBox):
			self.__ConfidenceRangeMax_value = propierty_ConfidenceRangeMax_widget.value()
		elif isinstance(propierty_ConfidenceRangeMax_widget, QDoubleSpinBox):
			self.__ConfidenceRangeMax_value = propierty_ConfidenceRangeMax_widget.value()
		elif isinstance(propierty_ConfidenceRangeMax_widget, QComboBox):
			self.__ConfidenceRangeMax_value = propierty_ConfidenceRangeMax_widget.currentText()
		elif isinstance(propierty_ConfidenceRangeMax_widget, QLineEdit):
			self.__ConfidenceRangeMax_value = propierty_ConfidenceRangeMax_widget.text()
		elif isinstance(propierty_ConfidenceRangeMax_widget, QCheckBox):
			self.__ConfidenceRangeMax_value = propierty_ConfidenceRangeMax_widget.isChecked()

	@property
	def GroundMaxAngle(self):
		return self.__GroundMaxAngle

	@GroundMaxAngle.setter
	def GroundMaxAngle(self, value: 'widget:QSpinBox, minimum:0, maximum:45, singleStep:1, toolTip:'):
		self.__GroundMaxAngle = value

	def set_GroundMaxAngle_value(self):
		propierty_GroundMaxAngle_widget = self.__widget_by_propierty['GroundMaxAngle'] 
		if isinstance(propierty_GroundMaxAngle_widget, QSpinBox):
			self.__GroundMaxAngle_value = propierty_GroundMaxAngle_widget.value()
		elif isinstance(propierty_GroundMaxAngle_widget, QDoubleSpinBox):
			self.__GroundMaxAngle_value = propierty_GroundMaxAngle_widget.value()
		elif isinstance(propierty_GroundMaxAngle_widget, QComboBox):
			self.__GroundMaxAngle_value = propierty_GroundMaxAngle_widget.currentText()
		elif isinstance(propierty_GroundMaxAngle_widget, QLineEdit):
			self.__GroundMaxAngle_value = propierty_GroundMaxAngle_widget.text()
		elif isinstance(propierty_GroundMaxAngle_widget, QCheckBox):
			self.__GroundMaxAngle_value = propierty_GroundMaxAngle_widget.isChecked()

	@property
	def GroundMaxDistance(self):
		return self.__GroundMaxDistance

	@GroundMaxDistance.setter
	def GroundMaxDistance(self, value: 'widget:QSpinBox, minimum:0, maximum:5, singleStep:1, toolTip:'):
		self.__GroundMaxDistance = value

	def set_GroundMaxDistance_value(self):
		propierty_GroundMaxDistance_widget = self.__widget_by_propierty['GroundMaxDistance'] 
		if isinstance(propierty_GroundMaxDistance_widget, QSpinBox):
			self.__GroundMaxDistance_value = propierty_GroundMaxDistance_widget.value()
		elif isinstance(propierty_GroundMaxDistance_widget, QDoubleSpinBox):
			self.__GroundMaxDistance_value = propierty_GroundMaxDistance_widget.value()
		elif isinstance(propierty_GroundMaxDistance_widget, QComboBox):
			self.__GroundMaxDistance_value = propierty_GroundMaxDistance_widget.currentText()
		elif isinstance(propierty_GroundMaxDistance_widget, QLineEdit):
			self.__GroundMaxDistance_value = propierty_GroundMaxDistance_widget.text()
		elif isinstance(propierty_GroundMaxDistance_widget, QCheckBox):
			self.__GroundMaxDistance_value = propierty_GroundMaxDistance_widget.isChecked()

	@property
	def GroundMaxSlope(self):
		return self.__GroundMaxSlope

	@GroundMaxSlope.setter
	def GroundMaxSlope(self, value: 'widget:QSpinBox, minimum:0, maximum:90, singleStep:1, toolTip:'):
		self.__GroundMaxSlope = value

	def set_GroundMaxSlope_value(self):
		propierty_GroundMaxSlope_widget = self.__widget_by_propierty['GroundMaxSlope'] 
		if isinstance(propierty_GroundMaxSlope_widget, QSpinBox):
			self.__GroundMaxSlope_value = propierty_GroundMaxSlope_widget.value()
		elif isinstance(propierty_GroundMaxSlope_widget, QDoubleSpinBox):
			self.__GroundMaxSlope_value = propierty_GroundMaxSlope_widget.value()
		elif isinstance(propierty_GroundMaxSlope_widget, QComboBox):
			self.__GroundMaxSlope_value = propierty_GroundMaxSlope_widget.currentText()
		elif isinstance(propierty_GroundMaxSlope_widget, QLineEdit):
			self.__GroundMaxSlope_value = propierty_GroundMaxSlope_widget.text()
		elif isinstance(propierty_GroundMaxSlope_widget, QCheckBox):
			self.__GroundMaxSlope_value = propierty_GroundMaxSlope_widget.isChecked()

	@property
	def GroundCellSize(self):
		return self.__GroundCellSize

	@GroundCellSize.setter
	def GroundCellSize(self, value: 'widget:QSpinBox, minimum:1, maximum:100, singleStep:1, toolTip:'):
		self.__GroundCellSize = value

	def set_GroundCellSize_value(self):
		propierty_GroundCellSize_widget = self.__widget_by_propierty['GroundCellSize'] 
		if isinstance(propierty_GroundCellSize_widget, QSpinBox):
			self.__GroundCellSize_value = propierty_GroundCellSize_widget.value()
		elif isinstance(propierty_GroundCellSize_widget, QDoubleSpinBox):
			self.__GroundCellSize_value = propierty_GroundCellSize_widget.value()
		elif isinstance(propierty_GroundCellSize_widget, QComboBox):
			self.__GroundCellSize_value = propierty_GroundCellSize_widget.currentText()
		elif isinstance(propierty_GroundCellSize_widget, QLineEdit):
			self.__GroundCellSize_value = propierty_GroundCellSize_widget.text()
		elif isinstance(propierty_GroundCellSize_widget, QCheckBox):
			self.__GroundCellSize_value = propierty_GroundCellSize_widget.isChecked()

	@property
	def GroundErosionRadius(self):
		return self.__GroundErosionRadius

	@GroundErosionRadius.setter
	def GroundErosionRadius(self, value: 'widget:QDoubleSpinBox, decimals:2, minimum:0, maximum:100, singleStep:1, toolTip:'):
		self.__GroundErosionRadius = value

	def set_GroundErosionRadius_value(self):
		propierty_GroundErosionRadius_widget = self.__widget_by_propierty['GroundErosionRadius'] 
		if isinstance(propierty_GroundErosionRadius_widget, QSpinBox):
			self.__GroundErosionRadius_value = propierty_GroundErosionRadius_widget.value()
		elif isinstance(propierty_GroundErosionRadius_widget, QDoubleSpinBox):
			self.__GroundErosionRadius_value = propierty_GroundErosionRadius_widget.value()
		elif isinstance(propierty_GroundErosionRadius_widget, QComboBox):
			self.__GroundErosionRadius_value = propierty_GroundErosionRadius_widget.currentText()
		elif isinstance(propierty_GroundErosionRadius_widget, QLineEdit):
			self.__GroundErosionRadius_value = propierty_GroundErosionRadius_widget.text()
		elif isinstance(propierty_GroundErosionRadius_widget, QCheckBox):
			self.__GroundErosionRadius_value = propierty_GroundErosionRadius_widget.isChecked()

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
		propierty_ConfidenceRangeMin_widget = self.__widget.get_widget('ConfidenceRangeMin')
		if isinstance(propierty_ConfidenceRangeMin_widget, QSpinBox):
			propierty_ConfidenceRangeMin_widget.valueChanged.connect(self.set_ConfidenceRangeMin_value)
		elif isinstance(propierty_ConfidenceRangeMin_widget, QDoubleSpinBox):
			propierty_ConfidenceRangeMin_widget.valueChanged.connect(self.set_ConfidenceRangeMin_value)
		elif isinstance(propierty_ConfidenceRangeMin_widget, QComboBox):
			propierty_ConfidenceRangeMin_widget.currentIndexChanged.connect(self.set_ConfidenceRangeMin_value)
		elif isinstance(propierty_ConfidenceRangeMin_widget, QLineEdit):
			propierty_ConfidenceRangeMin_widget.editingFinished.connect(self.set_ConfidenceRangeMin_value)
			propierty_ConfidenceRangeMin_widget.textChanged.connect(self.set_ConfidenceRangeMin_value)
		elif isinstance(propierty_ConfidenceRangeMin_widget, QCheckBox):
			propierty_ConfidenceRangeMin_widget.stateChanged.connect(self.set_ConfidenceRangeMin_value)
		self.__widget_by_propierty['ConfidenceRangeMin'] = propierty_ConfidenceRangeMin_widget
		propierty_ConfidenceRangeMax_widget = self.__widget.get_widget('ConfidenceRangeMax')
		if isinstance(propierty_ConfidenceRangeMax_widget, QSpinBox):
			propierty_ConfidenceRangeMax_widget.valueChanged.connect(self.set_ConfidenceRangeMax_value)
		elif isinstance(propierty_ConfidenceRangeMax_widget, QDoubleSpinBox):
			propierty_ConfidenceRangeMax_widget.valueChanged.connect(self.set_ConfidenceRangeMax_value)
		elif isinstance(propierty_ConfidenceRangeMax_widget, QComboBox):
			propierty_ConfidenceRangeMax_widget.currentIndexChanged.connect(self.set_ConfidenceRangeMax_value)
		elif isinstance(propierty_ConfidenceRangeMax_widget, QLineEdit):
			propierty_ConfidenceRangeMax_widget.editingFinished.connect(self.set_ConfidenceRangeMax_value)
			propierty_ConfidenceRangeMax_widget.textChanged.connect(self.set_ConfidenceRangeMax_value)
		elif isinstance(propierty_ConfidenceRangeMax_widget, QCheckBox):
			propierty_ConfidenceRangeMax_widget.stateChanged.connect(self.set_ConfidenceRangeMax_value)
		self.__widget_by_propierty['ConfidenceRangeMax'] = propierty_ConfidenceRangeMax_widget
		propierty_GroundMaxAngle_widget = self.__widget.get_widget('GroundMaxAngle')
		if isinstance(propierty_GroundMaxAngle_widget, QSpinBox):
			propierty_GroundMaxAngle_widget.valueChanged.connect(self.set_GroundMaxAngle_value)
		elif isinstance(propierty_GroundMaxAngle_widget, QDoubleSpinBox):
			propierty_GroundMaxAngle_widget.valueChanged.connect(self.set_GroundMaxAngle_value)
		elif isinstance(propierty_GroundMaxAngle_widget, QComboBox):
			propierty_GroundMaxAngle_widget.currentIndexChanged.connect(self.set_GroundMaxAngle_value)
		elif isinstance(propierty_GroundMaxAngle_widget, QLineEdit):
			propierty_GroundMaxAngle_widget.editingFinished.connect(self.set_GroundMaxAngle_value)
			propierty_GroundMaxAngle_widget.textChanged.connect(self.set_GroundMaxAngle_value)
		elif isinstance(propierty_GroundMaxAngle_widget, QCheckBox):
			propierty_GroundMaxAngle_widget.stateChanged.connect(self.set_GroundMaxAngle_value)
		self.__widget_by_propierty['GroundMaxAngle'] = propierty_GroundMaxAngle_widget
		propierty_GroundMaxDistance_widget = self.__widget.get_widget('GroundMaxDistance')
		if isinstance(propierty_GroundMaxDistance_widget, QSpinBox):
			propierty_GroundMaxDistance_widget.valueChanged.connect(self.set_GroundMaxDistance_value)
		elif isinstance(propierty_GroundMaxDistance_widget, QDoubleSpinBox):
			propierty_GroundMaxDistance_widget.valueChanged.connect(self.set_GroundMaxDistance_value)
		elif isinstance(propierty_GroundMaxDistance_widget, QComboBox):
			propierty_GroundMaxDistance_widget.currentIndexChanged.connect(self.set_GroundMaxDistance_value)
		elif isinstance(propierty_GroundMaxDistance_widget, QLineEdit):
			propierty_GroundMaxDistance_widget.editingFinished.connect(self.set_GroundMaxDistance_value)
			propierty_GroundMaxDistance_widget.textChanged.connect(self.set_GroundMaxDistance_value)
		elif isinstance(propierty_GroundMaxDistance_widget, QCheckBox):
			propierty_GroundMaxDistance_widget.stateChanged.connect(self.set_GroundMaxDistance_value)
		self.__widget_by_propierty['GroundMaxDistance'] = propierty_GroundMaxDistance_widget
		propierty_GroundMaxSlope_widget = self.__widget.get_widget('GroundMaxSlope')
		if isinstance(propierty_GroundMaxSlope_widget, QSpinBox):
			propierty_GroundMaxSlope_widget.valueChanged.connect(self.set_GroundMaxSlope_value)
		elif isinstance(propierty_GroundMaxSlope_widget, QDoubleSpinBox):
			propierty_GroundMaxSlope_widget.valueChanged.connect(self.set_GroundMaxSlope_value)
		elif isinstance(propierty_GroundMaxSlope_widget, QComboBox):
			propierty_GroundMaxSlope_widget.currentIndexChanged.connect(self.set_GroundMaxSlope_value)
		elif isinstance(propierty_GroundMaxSlope_widget, QLineEdit):
			propierty_GroundMaxSlope_widget.editingFinished.connect(self.set_GroundMaxSlope_value)
			propierty_GroundMaxSlope_widget.textChanged.connect(self.set_GroundMaxSlope_value)
		elif isinstance(propierty_GroundMaxSlope_widget, QCheckBox):
			propierty_GroundMaxSlope_widget.stateChanged.connect(self.set_GroundMaxSlope_value)
		self.__widget_by_propierty['GroundMaxSlope'] = propierty_GroundMaxSlope_widget
		propierty_GroundCellSize_widget = self.__widget.get_widget('GroundCellSize')
		if isinstance(propierty_GroundCellSize_widget, QSpinBox):
			propierty_GroundCellSize_widget.valueChanged.connect(self.set_GroundCellSize_value)
		elif isinstance(propierty_GroundCellSize_widget, QDoubleSpinBox):
			propierty_GroundCellSize_widget.valueChanged.connect(self.set_GroundCellSize_value)
		elif isinstance(propierty_GroundCellSize_widget, QComboBox):
			propierty_GroundCellSize_widget.currentIndexChanged.connect(self.set_GroundCellSize_value)
		elif isinstance(propierty_GroundCellSize_widget, QLineEdit):
			propierty_GroundCellSize_widget.editingFinished.connect(self.set_GroundCellSize_value)
			propierty_GroundCellSize_widget.textChanged.connect(self.set_GroundCellSize_value)
		elif isinstance(propierty_GroundCellSize_widget, QCheckBox):
			propierty_GroundCellSize_widget.stateChanged.connect(self.set_GroundCellSize_value)
		self.__widget_by_propierty['GroundCellSize'] = propierty_GroundCellSize_widget
		propierty_GroundErosionRadius_widget = self.__widget.get_widget('GroundErosionRadius')
		if isinstance(propierty_GroundErosionRadius_widget, QSpinBox):
			propierty_GroundErosionRadius_widget.valueChanged.connect(self.set_GroundErosionRadius_value)
		elif isinstance(propierty_GroundErosionRadius_widget, QDoubleSpinBox):
			propierty_GroundErosionRadius_widget.valueChanged.connect(self.set_GroundErosionRadius_value)
		elif isinstance(propierty_GroundErosionRadius_widget, QComboBox):
			propierty_GroundErosionRadius_widget.currentIndexChanged.connect(self.set_GroundErosionRadius_value)
		elif isinstance(propierty_GroundErosionRadius_widget, QLineEdit):
			propierty_GroundErosionRadius_widget.editingFinished.connect(self.set_GroundErosionRadius_value)
			propierty_GroundErosionRadius_widget.textChanged.connect(self.set_GroundErosionRadius_value)
		elif isinstance(propierty_GroundErosionRadius_widget, QCheckBox):
			propierty_GroundErosionRadius_widget.stateChanged.connect(self.set_GroundErosionRadius_value)
		self.__widget_by_propierty['GroundErosionRadius'] = propierty_GroundErosionRadius_widget
