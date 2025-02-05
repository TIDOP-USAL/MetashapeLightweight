from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class SplitTile:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Division en celdas', 'english': 'Split tiles'}
		self.__text = 'Division en celdas'
		self.__json_content_by_propierty['TileSize'] = {'text': {'spanish': 'Tamanio de la celda', 'english': 'Tile Size'}, 'definition': {'spanish': 'Tamanio de las celdas en metros (ej. 50)', 'english': 'Tile size in meters (i.e. 50)'}, 'type': 'integer', 'minimum': 10, 'maximum': 1000, 'singleStep': 10, 'default': 50}
		self.__text_by_propierty['TileSize'] = 'Tamanio de la celda'
		self.__widget_by_propierty['TileSize'] = None
		self.__TileSize = 50
		self.__TileSize_value = 50
		self.__json_content_by_propierty['TileSizeBuffer'] = {'text': {'spanish': 'Ampliacion de las celdas', 'english': 'Buffer tiles'}, 'definition': {'spanish': 'Porcentaje de solape entre celdas (ej. 5)', 'english': 'Tiles percentage overlaps (ex. 5)'}, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'singleStep': 1, 'default': 5}
		self.__text_by_propierty['TileSizeBuffer'] = 'Ampliacion de las celdas'
		self.__widget_by_propierty['TileSizeBuffer'] = None
		self.__TileSizeBuffer = 5
		self.__TileSizeBuffer_value = 5
		self.__json_content_by_propierty['Method'] = {'text': {'spanish': 'Definicion de la malla de celdas a procesar', 'english': 'Grid tiles to process definition'}, 'definition': {'spanish': 'Definicion de la malla de celdas a procesar', 'english': 'Grid tiles to process definition'}, 'type': 'values', 'values': {'AUTO': {'spanish': 'Automatico para toda la ROI o zona estereoscopica', 'english': 'Automatic to ROI or stereoscopi area'}, 'MANUAL': {'spanish': 'Malla editada por el usuario', 'english': 'User edited Grid'}}, 'default': 'Malla editada por el usuario'}
		self.__text_by_propierty['Method'] = 'Definicion de la malla de celdas a procesar'
		self.__widget_by_propierty['Method'] = None
		self.__Method = ['Malla editada por el usuario' ,'Automatico para toda la ROI o zona estereoscopica']
		self.__Method_value = 'Malla editada por el usuario'
		self.__json_content_by_propierty['Path'] = {'text': {'spanish': 'Fichero de la malla', 'english': 'Grid file'}, 'definition': {'spanish': 'Fichero de la malla editado por el usario', 'english': 'Grid file edited by user'}, 'type': 'file save', 'formats': '*.gpkg', 'default': ''}
		self.__text_by_propierty['Path'] = 'Fichero de la malla'
		self.__widget_by_propierty['Path'] = None
		self.__Path = ""
		self.__Path_value = ""
		self.__json_content_by_propierty['MergeMethod'] = {'text': {'spanish': 'Metodo de union', 'english': 'Merge method'}, 'definition': {'spanish': 'Estrategia de union de los productos resultantes', 'english': 'Merged method'}, 'type': 'values', 'values': {'Metashape': {'spanish': 'Metashape', 'english': 'Metashape'}, 'OsgeoLaspy': {'spanish': 'OSGeo (raster) y laspy (nubes de puntos)', 'english': 'OSGeo (raster) and laspy (points clouds)'}}, 'default': 'OSGeo (raster) y laspy (nubes de puntos)'}
		self.__text_by_propierty['MergeMethod'] = 'Metodo de union'
		self.__widget_by_propierty['MergeMethod'] = None
		self.__MergeMethod = ['OSGeo (raster) y laspy (nubes de puntos)' ,'Metashape']
		self.__MergeMethod_value = 'OSGeo (raster) y laspy (nubes de puntos)'
		self.__json_content_by_propierty['MergePointClouds'] = {'text': {'spanish': 'Unir nubes de puntos', 'english': 'Merge points clouds'}, 'definition': {'spanish': 'Unir nubes de puntos', 'english': 'Merge points clouds'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['MergePointClouds'] = 'Unir nubes de puntos'
		self.__widget_by_propierty['MergePointClouds'] = None
		self.__MergePointClouds = True
		self.__MergePointClouds_value = True
		self.__json_content_by_propierty['MergeElevations'] = {'text': {'spanish': 'Unir MDEs', 'english': 'Merge DEMs'}, 'definition': {'spanish': 'Unir MDEs', 'english': 'Merge DEMs'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['MergeElevations'] = 'Unir MDEs'
		self.__widget_by_propierty['MergeElevations'] = None
		self.__MergeElevations = True
		self.__MergeElevations_value = True
		self.__json_content_by_propierty['MergeOrthomosaics'] = {'text': {'spanish': 'Unir ortomosaicos', 'english': 'Merge orthomosaics'}, 'definition': {'spanish': 'Unir ortomosaicos', 'english': 'Merge orthomosaics'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['MergeOrthomosaics'] = 'Unir ortomosaicos'
		self.__widget_by_propierty['MergeOrthomosaics'] = None
		self.__MergeOrthomosaics = True
		self.__MergeOrthomosaics_value = True
		self.__json_content_by_propierty['MergedDEM'] = {'text': {'spanish': 'Tipo de MDE a unir', 'english': 'Type of DEM to merge'}, 'definition': {'spanish': 'Tipo de MDE a unir', 'english': 'Type of DEM to merge'}, 'type': 'values', 'values': {'DSM': {'spanish': 'Modelo Digital de Superficies (MDS)', 'english': 'Digital Surface Model (DSM)'}, 'DTM': {'spanish': 'Modelo Digital del Terreno (MDT)', 'english': 'Digital Terrain Model (DTM)'}}, 'default': 'Modelo Digital de Superficies (MDS)'}
		self.__text_by_propierty['MergedDEM'] = 'Tipo de MDE a unir'
		self.__widget_by_propierty['MergedDEM'] = None
		self.__MergedDEM = ['Modelo Digital de Superficies (MDS)' ,'Modelo Digital del Terreno (MDT)']
		self.__MergedDEM_value = 'Modelo Digital de Superficies (MDS)'
		self.__widget = None

	def get_propierty_json_content(self, value):
		json_content = None
		if value in self.__json_content_by_propierty:
			json_content = self.__json_content_by_propierty[value]
		return json_content

	def get_values_as_dictionary(self):
		values = {}
		values['TileSize'] = self.__TileSize_value
		values['TileSizeBuffer'] = self.__TileSizeBuffer_value
		values['Method'] = self.__Method_value
		values['Path'] = self.__Path_value
		values['MergeMethod'] = self.__MergeMethod_value
		values['MergePointClouds'] = self.__MergePointClouds_value
		values['MergeElevations'] = self.__MergeElevations_value
		values['MergeOrthomosaics'] = self.__MergeOrthomosaics_value
		values['MergedDEM'] = self.__MergedDEM_value
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
	def TileSize(self):
		return self.__TileSize

	@TileSize.setter
	def TileSize(self, value: 'widget:QSpinBox, minimum:10, maximum:1000, singleStep:10, toolTip:Tamanio de las celdas en metros (ej. 50)'):
		self.__TileSize = value

	def set_TileSize_value(self):
		propierty_TileSize_widget = self.__widget_by_propierty['TileSize'] 
		if isinstance(propierty_TileSize_widget, QSpinBox):
			self.__TileSize_value = propierty_TileSize_widget.value()
		elif isinstance(propierty_TileSize_widget, QDoubleSpinBox):
			self.__TileSize_value = propierty_TileSize_widget.value()
		elif isinstance(propierty_TileSize_widget, QComboBox):
			self.__TileSize_value = propierty_TileSize_widget.currentText()
		elif isinstance(propierty_TileSize_widget, QLineEdit):
			self.__TileSize_value = propierty_TileSize_widget.text()
		elif isinstance(propierty_TileSize_widget, QCheckBox):
			self.__TileSize_value = propierty_TileSize_widget.isChecked()

	@property
	def TileSizeBuffer(self):
		return self.__TileSizeBuffer

	@TileSizeBuffer.setter
	def TileSizeBuffer(self, value: 'widget:QSpinBox, minimum:1, maximum:100, singleStep:1, toolTip:Porcentaje de solape entre celdas (ej. 5)'):
		self.__TileSizeBuffer = value

	def set_TileSizeBuffer_value(self):
		propierty_TileSizeBuffer_widget = self.__widget_by_propierty['TileSizeBuffer'] 
		if isinstance(propierty_TileSizeBuffer_widget, QSpinBox):
			self.__TileSizeBuffer_value = propierty_TileSizeBuffer_widget.value()
		elif isinstance(propierty_TileSizeBuffer_widget, QDoubleSpinBox):
			self.__TileSizeBuffer_value = propierty_TileSizeBuffer_widget.value()
		elif isinstance(propierty_TileSizeBuffer_widget, QComboBox):
			self.__TileSizeBuffer_value = propierty_TileSizeBuffer_widget.currentText()
		elif isinstance(propierty_TileSizeBuffer_widget, QLineEdit):
			self.__TileSizeBuffer_value = propierty_TileSizeBuffer_widget.text()
		elif isinstance(propierty_TileSizeBuffer_widget, QCheckBox):
			self.__TileSizeBuffer_value = propierty_TileSizeBuffer_widget.isChecked()

	@property
	def Method(self):
		return self.__Method

	@Method.setter
	def Method(self, value: 'widget:QComboBox, toolTip:Definicion de la malla de celdas a procesar'):
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
	def Path(self):
		return self.__Path

	@Path.setter
	def Path(self, value: 'widget:file, type:save, toolTip:Fichero de la malla editado por el usario, filters: *.gpkg'):
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
	def MergeMethod(self):
		return self.__MergeMethod

	@MergeMethod.setter
	def MergeMethod(self, value: 'widget:QComboBox, toolTip:Estrategia de union de los productos resultantes'):
		self.__MergeMethod = value

	def set_MergeMethod_value(self):
		propierty_MergeMethod_widget = self.__widget_by_propierty['MergeMethod'] 
		if isinstance(propierty_MergeMethod_widget, QSpinBox):
			self.__MergeMethod_value = propierty_MergeMethod_widget.value()
		elif isinstance(propierty_MergeMethod_widget, QDoubleSpinBox):
			self.__MergeMethod_value = propierty_MergeMethod_widget.value()
		elif isinstance(propierty_MergeMethod_widget, QComboBox):
			self.__MergeMethod_value = propierty_MergeMethod_widget.currentText()
		elif isinstance(propierty_MergeMethod_widget, QLineEdit):
			self.__MergeMethod_value = propierty_MergeMethod_widget.text()
		elif isinstance(propierty_MergeMethod_widget, QCheckBox):
			self.__MergeMethod_value = propierty_MergeMethod_widget.isChecked()

	@property
	def MergePointClouds(self):
		return self.__MergePointClouds

	@MergePointClouds.setter
	def MergePointClouds(self, value: 'widget:QCheckBox, toolTip:Unir nubes de puntos'):
		self.__MergePointClouds = value

	def set_MergePointClouds_value(self):
		propierty_MergePointClouds_widget = self.__widget_by_propierty['MergePointClouds'] 
		if isinstance(propierty_MergePointClouds_widget, QSpinBox):
			self.__MergePointClouds_value = propierty_MergePointClouds_widget.value()
		elif isinstance(propierty_MergePointClouds_widget, QDoubleSpinBox):
			self.__MergePointClouds_value = propierty_MergePointClouds_widget.value()
		elif isinstance(propierty_MergePointClouds_widget, QComboBox):
			self.__MergePointClouds_value = propierty_MergePointClouds_widget.currentText()
		elif isinstance(propierty_MergePointClouds_widget, QLineEdit):
			self.__MergePointClouds_value = propierty_MergePointClouds_widget.text()
		elif isinstance(propierty_MergePointClouds_widget, QCheckBox):
			self.__MergePointClouds_value = propierty_MergePointClouds_widget.isChecked()

	@property
	def MergeElevations(self):
		return self.__MergeElevations

	@MergeElevations.setter
	def MergeElevations(self, value: 'widget:QCheckBox, toolTip:Unir MDEs'):
		self.__MergeElevations = value

	def set_MergeElevations_value(self):
		propierty_MergeElevations_widget = self.__widget_by_propierty['MergeElevations'] 
		if isinstance(propierty_MergeElevations_widget, QSpinBox):
			self.__MergeElevations_value = propierty_MergeElevations_widget.value()
		elif isinstance(propierty_MergeElevations_widget, QDoubleSpinBox):
			self.__MergeElevations_value = propierty_MergeElevations_widget.value()
		elif isinstance(propierty_MergeElevations_widget, QComboBox):
			self.__MergeElevations_value = propierty_MergeElevations_widget.currentText()
		elif isinstance(propierty_MergeElevations_widget, QLineEdit):
			self.__MergeElevations_value = propierty_MergeElevations_widget.text()
		elif isinstance(propierty_MergeElevations_widget, QCheckBox):
			self.__MergeElevations_value = propierty_MergeElevations_widget.isChecked()

	@property
	def MergeOrthomosaics(self):
		return self.__MergeOrthomosaics

	@MergeOrthomosaics.setter
	def MergeOrthomosaics(self, value: 'widget:QCheckBox, toolTip:Unir ortomosaicos'):
		self.__MergeOrthomosaics = value

	def set_MergeOrthomosaics_value(self):
		propierty_MergeOrthomosaics_widget = self.__widget_by_propierty['MergeOrthomosaics'] 
		if isinstance(propierty_MergeOrthomosaics_widget, QSpinBox):
			self.__MergeOrthomosaics_value = propierty_MergeOrthomosaics_widget.value()
		elif isinstance(propierty_MergeOrthomosaics_widget, QDoubleSpinBox):
			self.__MergeOrthomosaics_value = propierty_MergeOrthomosaics_widget.value()
		elif isinstance(propierty_MergeOrthomosaics_widget, QComboBox):
			self.__MergeOrthomosaics_value = propierty_MergeOrthomosaics_widget.currentText()
		elif isinstance(propierty_MergeOrthomosaics_widget, QLineEdit):
			self.__MergeOrthomosaics_value = propierty_MergeOrthomosaics_widget.text()
		elif isinstance(propierty_MergeOrthomosaics_widget, QCheckBox):
			self.__MergeOrthomosaics_value = propierty_MergeOrthomosaics_widget.isChecked()

	@property
	def MergedDEM(self):
		return self.__MergedDEM

	@MergedDEM.setter
	def MergedDEM(self, value: 'widget:QComboBox, toolTip:Tipo de MDE a unir'):
		self.__MergedDEM = value

	def set_MergedDEM_value(self):
		propierty_MergedDEM_widget = self.__widget_by_propierty['MergedDEM'] 
		if isinstance(propierty_MergedDEM_widget, QSpinBox):
			self.__MergedDEM_value = propierty_MergedDEM_widget.value()
		elif isinstance(propierty_MergedDEM_widget, QDoubleSpinBox):
			self.__MergedDEM_value = propierty_MergedDEM_widget.value()
		elif isinstance(propierty_MergedDEM_widget, QComboBox):
			self.__MergedDEM_value = propierty_MergedDEM_widget.currentText()
		elif isinstance(propierty_MergedDEM_widget, QLineEdit):
			self.__MergedDEM_value = propierty_MergedDEM_widget.text()
		elif isinstance(propierty_MergedDEM_widget, QCheckBox):
			self.__MergedDEM_value = propierty_MergedDEM_widget.isChecked()

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
		propierty_TileSize_widget = self.__widget.get_widget('TileSize')
		if isinstance(propierty_TileSize_widget, QSpinBox):
			propierty_TileSize_widget.valueChanged.connect(self.set_TileSize_value)
		elif isinstance(propierty_TileSize_widget, QDoubleSpinBox):
			propierty_TileSize_widget.valueChanged.connect(self.set_TileSize_value)
		elif isinstance(propierty_TileSize_widget, QComboBox):
			propierty_TileSize_widget.currentIndexChanged.connect(self.set_TileSize_value)
		elif isinstance(propierty_TileSize_widget, QLineEdit):
			propierty_TileSize_widget.editingFinished.connect(self.set_TileSize_value)
			propierty_TileSize_widget.textChanged.connect(self.set_TileSize_value)
		elif isinstance(propierty_TileSize_widget, QCheckBox):
			propierty_TileSize_widget.stateChanged.connect(self.set_TileSize_value)
		self.__widget_by_propierty['TileSize'] = propierty_TileSize_widget
		propierty_TileSizeBuffer_widget = self.__widget.get_widget('TileSizeBuffer')
		if isinstance(propierty_TileSizeBuffer_widget, QSpinBox):
			propierty_TileSizeBuffer_widget.valueChanged.connect(self.set_TileSizeBuffer_value)
		elif isinstance(propierty_TileSizeBuffer_widget, QDoubleSpinBox):
			propierty_TileSizeBuffer_widget.valueChanged.connect(self.set_TileSizeBuffer_value)
		elif isinstance(propierty_TileSizeBuffer_widget, QComboBox):
			propierty_TileSizeBuffer_widget.currentIndexChanged.connect(self.set_TileSizeBuffer_value)
		elif isinstance(propierty_TileSizeBuffer_widget, QLineEdit):
			propierty_TileSizeBuffer_widget.editingFinished.connect(self.set_TileSizeBuffer_value)
			propierty_TileSizeBuffer_widget.textChanged.connect(self.set_TileSizeBuffer_value)
		elif isinstance(propierty_TileSizeBuffer_widget, QCheckBox):
			propierty_TileSizeBuffer_widget.stateChanged.connect(self.set_TileSizeBuffer_value)
		self.__widget_by_propierty['TileSizeBuffer'] = propierty_TileSizeBuffer_widget
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
		propierty_MergeMethod_widget = self.__widget.get_widget('MergeMethod')
		if isinstance(propierty_MergeMethod_widget, QSpinBox):
			propierty_MergeMethod_widget.valueChanged.connect(self.set_MergeMethod_value)
		elif isinstance(propierty_MergeMethod_widget, QDoubleSpinBox):
			propierty_MergeMethod_widget.valueChanged.connect(self.set_MergeMethod_value)
		elif isinstance(propierty_MergeMethod_widget, QComboBox):
			propierty_MergeMethod_widget.currentIndexChanged.connect(self.set_MergeMethod_value)
		elif isinstance(propierty_MergeMethod_widget, QLineEdit):
			propierty_MergeMethod_widget.editingFinished.connect(self.set_MergeMethod_value)
			propierty_MergeMethod_widget.textChanged.connect(self.set_MergeMethod_value)
		elif isinstance(propierty_MergeMethod_widget, QCheckBox):
			propierty_MergeMethod_widget.stateChanged.connect(self.set_MergeMethod_value)
		self.__widget_by_propierty['MergeMethod'] = propierty_MergeMethod_widget
		propierty_MergePointClouds_widget = self.__widget.get_widget('MergePointClouds')
		if isinstance(propierty_MergePointClouds_widget, QSpinBox):
			propierty_MergePointClouds_widget.valueChanged.connect(self.set_MergePointClouds_value)
		elif isinstance(propierty_MergePointClouds_widget, QDoubleSpinBox):
			propierty_MergePointClouds_widget.valueChanged.connect(self.set_MergePointClouds_value)
		elif isinstance(propierty_MergePointClouds_widget, QComboBox):
			propierty_MergePointClouds_widget.currentIndexChanged.connect(self.set_MergePointClouds_value)
		elif isinstance(propierty_MergePointClouds_widget, QLineEdit):
			propierty_MergePointClouds_widget.editingFinished.connect(self.set_MergePointClouds_value)
			propierty_MergePointClouds_widget.textChanged.connect(self.set_MergePointClouds_value)
		elif isinstance(propierty_MergePointClouds_widget, QCheckBox):
			propierty_MergePointClouds_widget.stateChanged.connect(self.set_MergePointClouds_value)
		self.__widget_by_propierty['MergePointClouds'] = propierty_MergePointClouds_widget
		propierty_MergeElevations_widget = self.__widget.get_widget('MergeElevations')
		if isinstance(propierty_MergeElevations_widget, QSpinBox):
			propierty_MergeElevations_widget.valueChanged.connect(self.set_MergeElevations_value)
		elif isinstance(propierty_MergeElevations_widget, QDoubleSpinBox):
			propierty_MergeElevations_widget.valueChanged.connect(self.set_MergeElevations_value)
		elif isinstance(propierty_MergeElevations_widget, QComboBox):
			propierty_MergeElevations_widget.currentIndexChanged.connect(self.set_MergeElevations_value)
		elif isinstance(propierty_MergeElevations_widget, QLineEdit):
			propierty_MergeElevations_widget.editingFinished.connect(self.set_MergeElevations_value)
			propierty_MergeElevations_widget.textChanged.connect(self.set_MergeElevations_value)
		elif isinstance(propierty_MergeElevations_widget, QCheckBox):
			propierty_MergeElevations_widget.stateChanged.connect(self.set_MergeElevations_value)
		self.__widget_by_propierty['MergeElevations'] = propierty_MergeElevations_widget
		propierty_MergeOrthomosaics_widget = self.__widget.get_widget('MergeOrthomosaics')
		if isinstance(propierty_MergeOrthomosaics_widget, QSpinBox):
			propierty_MergeOrthomosaics_widget.valueChanged.connect(self.set_MergeOrthomosaics_value)
		elif isinstance(propierty_MergeOrthomosaics_widget, QDoubleSpinBox):
			propierty_MergeOrthomosaics_widget.valueChanged.connect(self.set_MergeOrthomosaics_value)
		elif isinstance(propierty_MergeOrthomosaics_widget, QComboBox):
			propierty_MergeOrthomosaics_widget.currentIndexChanged.connect(self.set_MergeOrthomosaics_value)
		elif isinstance(propierty_MergeOrthomosaics_widget, QLineEdit):
			propierty_MergeOrthomosaics_widget.editingFinished.connect(self.set_MergeOrthomosaics_value)
			propierty_MergeOrthomosaics_widget.textChanged.connect(self.set_MergeOrthomosaics_value)
		elif isinstance(propierty_MergeOrthomosaics_widget, QCheckBox):
			propierty_MergeOrthomosaics_widget.stateChanged.connect(self.set_MergeOrthomosaics_value)
		self.__widget_by_propierty['MergeOrthomosaics'] = propierty_MergeOrthomosaics_widget
		propierty_MergedDEM_widget = self.__widget.get_widget('MergedDEM')
		if isinstance(propierty_MergedDEM_widget, QSpinBox):
			propierty_MergedDEM_widget.valueChanged.connect(self.set_MergedDEM_value)
		elif isinstance(propierty_MergedDEM_widget, QDoubleSpinBox):
			propierty_MergedDEM_widget.valueChanged.connect(self.set_MergedDEM_value)
		elif isinstance(propierty_MergedDEM_widget, QComboBox):
			propierty_MergedDEM_widget.currentIndexChanged.connect(self.set_MergedDEM_value)
		elif isinstance(propierty_MergedDEM_widget, QLineEdit):
			propierty_MergedDEM_widget.editingFinished.connect(self.set_MergedDEM_value)
			propierty_MergedDEM_widget.textChanged.connect(self.set_MergedDEM_value)
		elif isinstance(propierty_MergedDEM_widget, QCheckBox):
			propierty_MergedDEM_widget.stateChanged.connect(self.set_MergedDEM_value)
		self.__widget_by_propierty['MergedDEM'] = propierty_MergedDEM_widget
