from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class Photo:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Imagenes', 'english': 'Photo'}
		self.__text = 'Imagenes'
		self.__json_content_by_propierty['Path'] = {'text': {'spanish': 'Ruta imagenes', 'english': 'Images path'}, 'definition': {'spanish': 'Ruta del directorio donde se localizan las imagenes', 'english': 'Path of the directory where the images are located'}, 'type': 'folder', 'default': ''}
		self.__text_by_propierty['Path'] = 'Ruta imagenes'
		self.__widget_by_propierty['Path'] = None
		self.__Path = ""
		self.__Path_value = ""
		self.__json_content_by_propierty['LocationAccuracy2D'] = {'text': {'spanish': 'Precision 2D de OE', 'english': '2D accuracy of EO'}, 'definition': {'spanish': 'Precision horizontal de la orientacion externa de las imagenes en metros', 'english': 'Horizontal accuracy of external orientation of images in meters'}, 'type': 'real', 'decimals': 3, 'minimum': 0.0, 'maximum': 5.0, 'singleStep': 0.01, 'default': 0.08}
		self.__text_by_propierty['LocationAccuracy2D'] = 'Precision 2D de OE'
		self.__widget_by_propierty['LocationAccuracy2D'] = None
		self.__LocationAccuracy2D = 0.08
		self.__LocationAccuracy2D_value = 0.08
		self.__json_content_by_propierty['LocationAccuracyHeight'] = {'text': {'spanish': 'Precision Z de OE', 'english': 'Z accuracy of EO'}, 'definition': {'spanish': 'Precision vertical de la orientacion externa de las imagenes en metros', 'english': 'Vertical accuracy of the external orientation of images in meters'}, 'type': 'real', 'decimals': 3, 'minimum': 0.0, 'maximum': 5.0, 'singleStep': 0.01, 'default': 0.12}
		self.__text_by_propierty['LocationAccuracyHeight'] = 'Precision Z de OE'
		self.__widget_by_propierty['LocationAccuracyHeight'] = None
		self.__LocationAccuracyHeight = 0.12
		self.__LocationAccuracyHeight_value = 0.12
		self.__json_content_by_propierty['Method'] = {'text': {'spanish': 'Fuente OE', 'english': 'Source EO'}, 'definition': {'spanish': 'Fuente de la que se importaran las orientaciones externas de las imagenes', 'english': 'Source from which the external orientations of the images will be imported'}, 'type': 'values', 'values': {'CSV': {'spanish': 'Fichero CSV', 'english': 'CSV file'}, 'EXIF': {'spanish': 'Metadatos de las imagenes', 'english': 'EXIF'}}, 'default': 'EXIF'}
		self.__text_by_propierty['Method'] = 'Fuente OE'
		self.__widget_by_propierty['Method'] = None
		self.__Method = ['Metadatos de las imagenes' ,'Fichero CSV']
		self.__Method_value = 'Metadatos de las imagenes'
		self.__json_content_by_propierty['EPSG'] = {'text': {'spanish': 'Codigo EPSG', 'english': 'EPSG code'}, 'definition': {'spanish': 'Codigo EPSG con el que se importaran las orientaciones externas de las imagenes', 'english': 'EPSG code with which external orientation of the images will be imported'}, 'type': 'string', 'len': 11, 'default': '4326'}
		self.__text_by_propierty['EPSG'] = 'Codigo EPSG'
		self.__widget_by_propierty['EPSG'] = None
		self.__EPSG = "4326"
		self.__EPSG_value = "4326"
		self.__json_content_by_propierty['EoPath'] = {'text': {'spanish': 'Ruta OE', 'english': 'OE path'}, 'definition': {'spanish': 'Ruta del archivo CSV con las orientaciones externas', 'english': 'CSV file path with external orientations'}, 'type': 'file open', 'default': ''}
		self.__text_by_propierty['EoPath'] = 'Ruta OE'
		self.__widget_by_propierty['EoPath'] = None
		self.__EoPath = ""
		self.__EoPath_value = ""
		self.__widget = None

	def get_propierty_json_content(self, value):
		json_content = None
		if value in self.__json_content_by_propierty:
			json_content = self.__json_content_by_propierty[value]
		return json_content

	def get_values_as_dictionary(self):
		values = {}
		values['Path'] = self.__Path_value
		values['LocationAccuracy2D'] = self.__LocationAccuracy2D_value
		values['LocationAccuracyHeight'] = self.__LocationAccuracyHeight_value
		values['Method'] = self.__Method_value
		values['EPSG'] = self.__EPSG_value
		values['EoPath'] = self.__EoPath_value
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
	def Path(self, value: 'widget:file, type:folder, toolTip:Ruta del directorio donde se localizan las imagenes'):
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
	def LocationAccuracy2D(self):
		return self.__LocationAccuracy2D

	@LocationAccuracy2D.setter
	def LocationAccuracy2D(self, value: 'widget:QDoubleSpinBox, decimals:3, minimum:0.0, maximum:5.0, singleStep:0.01, toolTip:Precision horizontal de la orientacion externa de las imagenes en metros'):
		self.__LocationAccuracy2D = value

	def set_LocationAccuracy2D_value(self):
		propierty_LocationAccuracy2D_widget = self.__widget_by_propierty['LocationAccuracy2D'] 
		if isinstance(propierty_LocationAccuracy2D_widget, QSpinBox):
			self.__LocationAccuracy2D_value = propierty_LocationAccuracy2D_widget.value()
		elif isinstance(propierty_LocationAccuracy2D_widget, QDoubleSpinBox):
			self.__LocationAccuracy2D_value = propierty_LocationAccuracy2D_widget.value()
		elif isinstance(propierty_LocationAccuracy2D_widget, QComboBox):
			self.__LocationAccuracy2D_value = propierty_LocationAccuracy2D_widget.currentText()
		elif isinstance(propierty_LocationAccuracy2D_widget, QLineEdit):
			self.__LocationAccuracy2D_value = propierty_LocationAccuracy2D_widget.text()
		elif isinstance(propierty_LocationAccuracy2D_widget, QCheckBox):
			self.__LocationAccuracy2D_value = propierty_LocationAccuracy2D_widget.isChecked()

	@property
	def LocationAccuracyHeight(self):
		return self.__LocationAccuracyHeight

	@LocationAccuracyHeight.setter
	def LocationAccuracyHeight(self, value: 'widget:QDoubleSpinBox, decimals:3, minimum:0.0, maximum:5.0, singleStep:0.01, toolTip:Precision vertical de la orientacion externa de las imagenes en metros'):
		self.__LocationAccuracyHeight = value

	def set_LocationAccuracyHeight_value(self):
		propierty_LocationAccuracyHeight_widget = self.__widget_by_propierty['LocationAccuracyHeight'] 
		if isinstance(propierty_LocationAccuracyHeight_widget, QSpinBox):
			self.__LocationAccuracyHeight_value = propierty_LocationAccuracyHeight_widget.value()
		elif isinstance(propierty_LocationAccuracyHeight_widget, QDoubleSpinBox):
			self.__LocationAccuracyHeight_value = propierty_LocationAccuracyHeight_widget.value()
		elif isinstance(propierty_LocationAccuracyHeight_widget, QComboBox):
			self.__LocationAccuracyHeight_value = propierty_LocationAccuracyHeight_widget.currentText()
		elif isinstance(propierty_LocationAccuracyHeight_widget, QLineEdit):
			self.__LocationAccuracyHeight_value = propierty_LocationAccuracyHeight_widget.text()
		elif isinstance(propierty_LocationAccuracyHeight_widget, QCheckBox):
			self.__LocationAccuracyHeight_value = propierty_LocationAccuracyHeight_widget.isChecked()

	@property
	def Method(self):
		return self.__Method

	@Method.setter
	def Method(self, value: 'widget:QComboBox, toolTip:Fuente de la que se importaran las orientaciones externas de las imagenes'):
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

	@property
	def EPSG(self):
		return self.__EPSG

	@EPSG.setter
	def EPSG(self, value: 'widget:QLineEdit, toolTip:Codigo EPSG con el que se importaran las orientaciones externas de las imagenes'):
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
	def EoPath(self):
		return self.__EoPath

	@EoPath.setter
	def EoPath(self, value: 'widget:file, toolTip:Ruta del archivo CSV con las orientaciones externas'):
		self.__EoPath = value

	def set_EoPath_value(self):
		propierty_EoPath_widget = self.__widget_by_propierty['EoPath'] 
		if isinstance(propierty_EoPath_widget, QSpinBox):
			self.__EoPath_value = propierty_EoPath_widget.value()
		elif isinstance(propierty_EoPath_widget, QDoubleSpinBox):
			self.__EoPath_value = propierty_EoPath_widget.value()
		elif isinstance(propierty_EoPath_widget, QComboBox):
			self.__EoPath_value = propierty_EoPath_widget.currentText()
		elif isinstance(propierty_EoPath_widget, QLineEdit):
			self.__EoPath_value = propierty_EoPath_widget.text()
		elif isinstance(propierty_EoPath_widget, QCheckBox):
			self.__EoPath_value = propierty_EoPath_widget.isChecked()

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
		propierty_LocationAccuracy2D_widget = self.__widget.get_widget('LocationAccuracy2D')
		if isinstance(propierty_LocationAccuracy2D_widget, QSpinBox):
			propierty_LocationAccuracy2D_widget.valueChanged.connect(self.set_LocationAccuracy2D_value)
		elif isinstance(propierty_LocationAccuracy2D_widget, QDoubleSpinBox):
			propierty_LocationAccuracy2D_widget.valueChanged.connect(self.set_LocationAccuracy2D_value)
		elif isinstance(propierty_LocationAccuracy2D_widget, QComboBox):
			propierty_LocationAccuracy2D_widget.currentIndexChanged.connect(self.set_LocationAccuracy2D_value)
		elif isinstance(propierty_LocationAccuracy2D_widget, QLineEdit):
			propierty_LocationAccuracy2D_widget.editingFinished.connect(self.set_LocationAccuracy2D_value)
			propierty_LocationAccuracy2D_widget.textChanged.connect(self.set_LocationAccuracy2D_value)
		elif isinstance(propierty_LocationAccuracy2D_widget, QCheckBox):
			propierty_LocationAccuracy2D_widget.stateChanged.connect(self.set_LocationAccuracy2D_value)
		self.__widget_by_propierty['LocationAccuracy2D'] = propierty_LocationAccuracy2D_widget
		propierty_LocationAccuracyHeight_widget = self.__widget.get_widget('LocationAccuracyHeight')
		if isinstance(propierty_LocationAccuracyHeight_widget, QSpinBox):
			propierty_LocationAccuracyHeight_widget.valueChanged.connect(self.set_LocationAccuracyHeight_value)
		elif isinstance(propierty_LocationAccuracyHeight_widget, QDoubleSpinBox):
			propierty_LocationAccuracyHeight_widget.valueChanged.connect(self.set_LocationAccuracyHeight_value)
		elif isinstance(propierty_LocationAccuracyHeight_widget, QComboBox):
			propierty_LocationAccuracyHeight_widget.currentIndexChanged.connect(self.set_LocationAccuracyHeight_value)
		elif isinstance(propierty_LocationAccuracyHeight_widget, QLineEdit):
			propierty_LocationAccuracyHeight_widget.editingFinished.connect(self.set_LocationAccuracyHeight_value)
			propierty_LocationAccuracyHeight_widget.textChanged.connect(self.set_LocationAccuracyHeight_value)
		elif isinstance(propierty_LocationAccuracyHeight_widget, QCheckBox):
			propierty_LocationAccuracyHeight_widget.stateChanged.connect(self.set_LocationAccuracyHeight_value)
		self.__widget_by_propierty['LocationAccuracyHeight'] = propierty_LocationAccuracyHeight_widget
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
		propierty_EoPath_widget = self.__widget.get_widget('EoPath')
		if isinstance(propierty_EoPath_widget, QSpinBox):
			propierty_EoPath_widget.valueChanged.connect(self.set_EoPath_value)
		elif isinstance(propierty_EoPath_widget, QDoubleSpinBox):
			propierty_EoPath_widget.valueChanged.connect(self.set_EoPath_value)
		elif isinstance(propierty_EoPath_widget, QComboBox):
			propierty_EoPath_widget.currentIndexChanged.connect(self.set_EoPath_value)
		elif isinstance(propierty_EoPath_widget, QLineEdit):
			propierty_EoPath_widget.editingFinished.connect(self.set_EoPath_value)
			propierty_EoPath_widget.textChanged.connect(self.set_EoPath_value)
		elif isinstance(propierty_EoPath_widget, QCheckBox):
			propierty_EoPath_widget.stateChanged.connect(self.set_EoPath_value)
		self.__widget_by_propierty['EoPath'] = propierty_EoPath_widget
