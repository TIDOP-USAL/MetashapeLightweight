from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class Workflow:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Flujo de trabajo', 'english': 'Workflow'}
		self.__text = 'Flujo de trabajo'
		self.__json_content_by_propierty['CleanPrevious'] = {'text': {'spanish': 'Reseteo directorio previo', 'english': 'Reset previous directory'}, 'definition': {'spanish': 'Proceso que ejecuta la limpieza del trabajo anterior', 'english': 'Process that executes the cleanup of the previous job'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['CleanPrevious'] = 'Reseteo directorio previo'
		self.__widget_by_propierty['CleanPrevious'] = None
		self.__CleanPrevious = True
		self.__CleanPrevious_value = True
		self.__json_content_by_propierty['Initialize'] = {'text': {'spanish': 'Inicializacion del proyecto', 'english': 'Project initialization'}, 'definition': {'spanish': 'Proceso que ejecuta la creacion del proyecto e importacion de los datos de entrada', 'english': 'Process that executes project creation and import of input data'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['Initialize'] = 'Inicializacion del proyecto'
		self.__widget_by_propierty['Initialize'] = None
		self.__Initialize = True
		self.__Initialize_value = True
		self.__json_content_by_propierty['Preprocess'] = {'text': {'spanish': 'Preproceso del proyecto', 'english': 'Project preprocess'}, 'definition': {'spanish': 'Proceso que ejecuta el cosido y alineamiento inicial', 'english': 'Process performing initial matching and alignment'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['Preprocess'] = 'Preproceso del proyecto'
		self.__widget_by_propierty['Preprocess'] = None
		self.__Preprocess = True
		self.__Preprocess_value = True
		self.__json_content_by_propierty['Optimize'] = {'text': {'spanish': 'Optimizacion de OI', 'english': 'Optimization of IO'}, 'definition': {'spanish': 'Proceso que ejecuta la optimizacion del alineamiento inicial con puntos de apoyo', 'english': 'Process that performs the optimization of the initial alignment with reference points.'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['Optimize'] = 'Optimizacion de OI'
		self.__widget_by_propierty['Optimize'] = None
		self.__Optimize = True
		self.__Optimize_value = True
		self.__json_content_by_propierty['Split'] = {'text': {'spanish': 'Particion del proyecto', 'english': 'Project splitting'}, 'definition': {'spanish': 'Proceso que ejecuta la particion del trabajo en tiles', 'english': 'Process that executes the splitting of the job into tiles.'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['Split'] = 'Particion del proyecto'
		self.__widget_by_propierty['Split'] = None
		self.__Split = True
		self.__Split_value = True
		self.__json_content_by_propierty['PointCloud'] = {'text': {'spanish': 'Construccion de nube de puntos', 'english': 'Point cloud creation'}, 'definition': {'spanish': 'Proceso que ejecuta la creacion y exportacion de la nube de puntos densa', 'english': 'Process that executes the creation and export of the dense point cloud'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['PointCloud'] = 'Construccion de nube de puntos'
		self.__widget_by_propierty['PointCloud'] = None
		self.__PointCloud = True
		self.__PointCloud_value = True
		self.__json_content_by_propierty['DEMs'] = {'text': {'spanish': 'Construccion de los modelos digitales de elevaciones', 'english': 'Digital elevation models creation'}, 'definition': {'spanish': 'Proceso que ejecuta la creacion y exportacion de los modelos digitales de elevaciones', 'english': 'Process that executes the creation and export of digital elevation models'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['DEMs'] = 'Construccion de los modelos digitales de elevaciones'
		self.__widget_by_propierty['DEMs'] = None
		self.__DEMs = True
		self.__DEMs_value = True
		self.__json_content_by_propierty['Orthomosaic'] = {'text': {'spanish': 'Construccion del ortomosaico', 'english': 'Orthomosaic creation'}, 'definition': {'spanish': 'Proceso que ejecuta la creacion y exportacion del ortomosaico', 'english': 'Process that executes the creation and export of the orthomosaic'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['Orthomosaic'] = 'Construccion del ortomosaico'
		self.__widget_by_propierty['Orthomosaic'] = None
		self.__Orthomosaic = True
		self.__Orthomosaic_value = True
		self.__json_content_by_propierty['Report'] = {'text': {'spanish': 'Construccion del informe', 'english': 'Report creation'}, 'definition': {'spanish': 'Proceso que ejecuta la exportacion del informe de resultados', 'english': 'Process that executes the export of the results report'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['Report'] = 'Construccion del informe'
		self.__widget_by_propierty['Report'] = None
		self.__Report = True
		self.__Report_value = True
		self.__widget = None

	def get_propierty_json_content(self, value):
		json_content = None
		if value in self.__json_content_by_propierty:
			json_content = self.__json_content_by_propierty[value]
		return json_content

	def get_values_as_dictionary(self):
		values = {}
		values['CleanPrevious'] = self.__CleanPrevious_value
		values['Initialize'] = self.__Initialize_value
		values['Preprocess'] = self.__Preprocess_value
		values['Optimize'] = self.__Optimize_value
		values['Split'] = self.__Split_value
		values['PointCloud'] = self.__PointCloud_value
		values['DEMs'] = self.__DEMs_value
		values['Orthomosaic'] = self.__Orthomosaic_value
		values['Report'] = self.__Report_value
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
	def CleanPrevious(self):
		return self.__CleanPrevious

	@CleanPrevious.setter
	def CleanPrevious(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la limpieza del trabajo anterior'):
		self.__CleanPrevious = value

	def set_CleanPrevious_value(self):
		propierty_CleanPrevious_widget = self.__widget_by_propierty['CleanPrevious'] 
		if isinstance(propierty_CleanPrevious_widget, QSpinBox):
			self.__CleanPrevious_value = propierty_CleanPrevious_widget.value()
		elif isinstance(propierty_CleanPrevious_widget, QDoubleSpinBox):
			self.__CleanPrevious_value = propierty_CleanPrevious_widget.value()
		elif isinstance(propierty_CleanPrevious_widget, QComboBox):
			self.__CleanPrevious_value = propierty_CleanPrevious_widget.currentText()
		elif isinstance(propierty_CleanPrevious_widget, QLineEdit):
			self.__CleanPrevious_value = propierty_CleanPrevious_widget.text()
		elif isinstance(propierty_CleanPrevious_widget, QCheckBox):
			self.__CleanPrevious_value = propierty_CleanPrevious_widget.isChecked()

	@property
	def Initialize(self):
		return self.__Initialize

	@Initialize.setter
	def Initialize(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creacion del proyecto e importacion de los datos de entrada'):
		self.__Initialize = value

	def set_Initialize_value(self):
		propierty_Initialize_widget = self.__widget_by_propierty['Initialize'] 
		if isinstance(propierty_Initialize_widget, QSpinBox):
			self.__Initialize_value = propierty_Initialize_widget.value()
		elif isinstance(propierty_Initialize_widget, QDoubleSpinBox):
			self.__Initialize_value = propierty_Initialize_widget.value()
		elif isinstance(propierty_Initialize_widget, QComboBox):
			self.__Initialize_value = propierty_Initialize_widget.currentText()
		elif isinstance(propierty_Initialize_widget, QLineEdit):
			self.__Initialize_value = propierty_Initialize_widget.text()
		elif isinstance(propierty_Initialize_widget, QCheckBox):
			self.__Initialize_value = propierty_Initialize_widget.isChecked()

	@property
	def Preprocess(self):
		return self.__Preprocess

	@Preprocess.setter
	def Preprocess(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta el cosido y alineamiento inicial'):
		self.__Preprocess = value

	def set_Preprocess_value(self):
		propierty_Preprocess_widget = self.__widget_by_propierty['Preprocess'] 
		if isinstance(propierty_Preprocess_widget, QSpinBox):
			self.__Preprocess_value = propierty_Preprocess_widget.value()
		elif isinstance(propierty_Preprocess_widget, QDoubleSpinBox):
			self.__Preprocess_value = propierty_Preprocess_widget.value()
		elif isinstance(propierty_Preprocess_widget, QComboBox):
			self.__Preprocess_value = propierty_Preprocess_widget.currentText()
		elif isinstance(propierty_Preprocess_widget, QLineEdit):
			self.__Preprocess_value = propierty_Preprocess_widget.text()
		elif isinstance(propierty_Preprocess_widget, QCheckBox):
			self.__Preprocess_value = propierty_Preprocess_widget.isChecked()

	@property
	def Optimize(self):
		return self.__Optimize

	@Optimize.setter
	def Optimize(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la optimizacion del alineamiento inicial con puntos de apoyo'):
		self.__Optimize = value

	def set_Optimize_value(self):
		propierty_Optimize_widget = self.__widget_by_propierty['Optimize'] 
		if isinstance(propierty_Optimize_widget, QSpinBox):
			self.__Optimize_value = propierty_Optimize_widget.value()
		elif isinstance(propierty_Optimize_widget, QDoubleSpinBox):
			self.__Optimize_value = propierty_Optimize_widget.value()
		elif isinstance(propierty_Optimize_widget, QComboBox):
			self.__Optimize_value = propierty_Optimize_widget.currentText()
		elif isinstance(propierty_Optimize_widget, QLineEdit):
			self.__Optimize_value = propierty_Optimize_widget.text()
		elif isinstance(propierty_Optimize_widget, QCheckBox):
			self.__Optimize_value = propierty_Optimize_widget.isChecked()

	@property
	def Split(self):
		return self.__Split

	@Split.setter
	def Split(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la particion del trabajo en tiles'):
		self.__Split = value

	def set_Split_value(self):
		propierty_Split_widget = self.__widget_by_propierty['Split'] 
		if isinstance(propierty_Split_widget, QSpinBox):
			self.__Split_value = propierty_Split_widget.value()
		elif isinstance(propierty_Split_widget, QDoubleSpinBox):
			self.__Split_value = propierty_Split_widget.value()
		elif isinstance(propierty_Split_widget, QComboBox):
			self.__Split_value = propierty_Split_widget.currentText()
		elif isinstance(propierty_Split_widget, QLineEdit):
			self.__Split_value = propierty_Split_widget.text()
		elif isinstance(propierty_Split_widget, QCheckBox):
			self.__Split_value = propierty_Split_widget.isChecked()

	@property
	def PointCloud(self):
		return self.__PointCloud

	@PointCloud.setter
	def PointCloud(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creacion y exportacion de la nube de puntos densa'):
		self.__PointCloud = value

	def set_PointCloud_value(self):
		propierty_PointCloud_widget = self.__widget_by_propierty['PointCloud'] 
		if isinstance(propierty_PointCloud_widget, QSpinBox):
			self.__PointCloud_value = propierty_PointCloud_widget.value()
		elif isinstance(propierty_PointCloud_widget, QDoubleSpinBox):
			self.__PointCloud_value = propierty_PointCloud_widget.value()
		elif isinstance(propierty_PointCloud_widget, QComboBox):
			self.__PointCloud_value = propierty_PointCloud_widget.currentText()
		elif isinstance(propierty_PointCloud_widget, QLineEdit):
			self.__PointCloud_value = propierty_PointCloud_widget.text()
		elif isinstance(propierty_PointCloud_widget, QCheckBox):
			self.__PointCloud_value = propierty_PointCloud_widget.isChecked()

	@property
	def DEMs(self):
		return self.__DEMs

	@DEMs.setter
	def DEMs(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creacion y exportacion de los modelos digitales de elevaciones'):
		self.__DEMs = value

	def set_DEMs_value(self):
		propierty_DEMs_widget = self.__widget_by_propierty['DEMs'] 
		if isinstance(propierty_DEMs_widget, QSpinBox):
			self.__DEMs_value = propierty_DEMs_widget.value()
		elif isinstance(propierty_DEMs_widget, QDoubleSpinBox):
			self.__DEMs_value = propierty_DEMs_widget.value()
		elif isinstance(propierty_DEMs_widget, QComboBox):
			self.__DEMs_value = propierty_DEMs_widget.currentText()
		elif isinstance(propierty_DEMs_widget, QLineEdit):
			self.__DEMs_value = propierty_DEMs_widget.text()
		elif isinstance(propierty_DEMs_widget, QCheckBox):
			self.__DEMs_value = propierty_DEMs_widget.isChecked()

	@property
	def Orthomosaic(self):
		return self.__Orthomosaic

	@Orthomosaic.setter
	def Orthomosaic(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la creacion y exportacion del ortomosaico'):
		self.__Orthomosaic = value

	def set_Orthomosaic_value(self):
		propierty_Orthomosaic_widget = self.__widget_by_propierty['Orthomosaic'] 
		if isinstance(propierty_Orthomosaic_widget, QSpinBox):
			self.__Orthomosaic_value = propierty_Orthomosaic_widget.value()
		elif isinstance(propierty_Orthomosaic_widget, QDoubleSpinBox):
			self.__Orthomosaic_value = propierty_Orthomosaic_widget.value()
		elif isinstance(propierty_Orthomosaic_widget, QComboBox):
			self.__Orthomosaic_value = propierty_Orthomosaic_widget.currentText()
		elif isinstance(propierty_Orthomosaic_widget, QLineEdit):
			self.__Orthomosaic_value = propierty_Orthomosaic_widget.text()
		elif isinstance(propierty_Orthomosaic_widget, QCheckBox):
			self.__Orthomosaic_value = propierty_Orthomosaic_widget.isChecked()

	@property
	def Report(self):
		return self.__Report

	@Report.setter
	def Report(self, value: 'widget:QCheckBox, toolTip:Proceso que ejecuta la exportacion del informe de resultados'):
		self.__Report = value

	def set_Report_value(self):
		propierty_Report_widget = self.__widget_by_propierty['Report'] 
		if isinstance(propierty_Report_widget, QSpinBox):
			self.__Report_value = propierty_Report_widget.value()
		elif isinstance(propierty_Report_widget, QDoubleSpinBox):
			self.__Report_value = propierty_Report_widget.value()
		elif isinstance(propierty_Report_widget, QComboBox):
			self.__Report_value = propierty_Report_widget.currentText()
		elif isinstance(propierty_Report_widget, QLineEdit):
			self.__Report_value = propierty_Report_widget.text()
		elif isinstance(propierty_Report_widget, QCheckBox):
			self.__Report_value = propierty_Report_widget.isChecked()

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
		propierty_CleanPrevious_widget = self.__widget.get_widget('CleanPrevious')
		if isinstance(propierty_CleanPrevious_widget, QSpinBox):
			propierty_CleanPrevious_widget.valueChanged.connect(self.set_CleanPrevious_value)
		elif isinstance(propierty_CleanPrevious_widget, QDoubleSpinBox):
			propierty_CleanPrevious_widget.valueChanged.connect(self.set_CleanPrevious_value)
		elif isinstance(propierty_CleanPrevious_widget, QComboBox):
			propierty_CleanPrevious_widget.currentIndexChanged.connect(self.set_CleanPrevious_value)
		elif isinstance(propierty_CleanPrevious_widget, QLineEdit):
			propierty_CleanPrevious_widget.editingFinished.connect(self.set_CleanPrevious_value)
			propierty_CleanPrevious_widget.textChanged.connect(self.set_CleanPrevious_value)
		elif isinstance(propierty_CleanPrevious_widget, QCheckBox):
			propierty_CleanPrevious_widget.stateChanged.connect(self.set_CleanPrevious_value)
		self.__widget_by_propierty['CleanPrevious'] = propierty_CleanPrevious_widget
		propierty_Initialize_widget = self.__widget.get_widget('Initialize')
		if isinstance(propierty_Initialize_widget, QSpinBox):
			propierty_Initialize_widget.valueChanged.connect(self.set_Initialize_value)
		elif isinstance(propierty_Initialize_widget, QDoubleSpinBox):
			propierty_Initialize_widget.valueChanged.connect(self.set_Initialize_value)
		elif isinstance(propierty_Initialize_widget, QComboBox):
			propierty_Initialize_widget.currentIndexChanged.connect(self.set_Initialize_value)
		elif isinstance(propierty_Initialize_widget, QLineEdit):
			propierty_Initialize_widget.editingFinished.connect(self.set_Initialize_value)
			propierty_Initialize_widget.textChanged.connect(self.set_Initialize_value)
		elif isinstance(propierty_Initialize_widget, QCheckBox):
			propierty_Initialize_widget.stateChanged.connect(self.set_Initialize_value)
		self.__widget_by_propierty['Initialize'] = propierty_Initialize_widget
		propierty_Preprocess_widget = self.__widget.get_widget('Preprocess')
		if isinstance(propierty_Preprocess_widget, QSpinBox):
			propierty_Preprocess_widget.valueChanged.connect(self.set_Preprocess_value)
		elif isinstance(propierty_Preprocess_widget, QDoubleSpinBox):
			propierty_Preprocess_widget.valueChanged.connect(self.set_Preprocess_value)
		elif isinstance(propierty_Preprocess_widget, QComboBox):
			propierty_Preprocess_widget.currentIndexChanged.connect(self.set_Preprocess_value)
		elif isinstance(propierty_Preprocess_widget, QLineEdit):
			propierty_Preprocess_widget.editingFinished.connect(self.set_Preprocess_value)
			propierty_Preprocess_widget.textChanged.connect(self.set_Preprocess_value)
		elif isinstance(propierty_Preprocess_widget, QCheckBox):
			propierty_Preprocess_widget.stateChanged.connect(self.set_Preprocess_value)
		self.__widget_by_propierty['Preprocess'] = propierty_Preprocess_widget
		propierty_Optimize_widget = self.__widget.get_widget('Optimize')
		if isinstance(propierty_Optimize_widget, QSpinBox):
			propierty_Optimize_widget.valueChanged.connect(self.set_Optimize_value)
		elif isinstance(propierty_Optimize_widget, QDoubleSpinBox):
			propierty_Optimize_widget.valueChanged.connect(self.set_Optimize_value)
		elif isinstance(propierty_Optimize_widget, QComboBox):
			propierty_Optimize_widget.currentIndexChanged.connect(self.set_Optimize_value)
		elif isinstance(propierty_Optimize_widget, QLineEdit):
			propierty_Optimize_widget.editingFinished.connect(self.set_Optimize_value)
			propierty_Optimize_widget.textChanged.connect(self.set_Optimize_value)
		elif isinstance(propierty_Optimize_widget, QCheckBox):
			propierty_Optimize_widget.stateChanged.connect(self.set_Optimize_value)
		self.__widget_by_propierty['Optimize'] = propierty_Optimize_widget
		propierty_Split_widget = self.__widget.get_widget('Split')
		if isinstance(propierty_Split_widget, QSpinBox):
			propierty_Split_widget.valueChanged.connect(self.set_Split_value)
		elif isinstance(propierty_Split_widget, QDoubleSpinBox):
			propierty_Split_widget.valueChanged.connect(self.set_Split_value)
		elif isinstance(propierty_Split_widget, QComboBox):
			propierty_Split_widget.currentIndexChanged.connect(self.set_Split_value)
		elif isinstance(propierty_Split_widget, QLineEdit):
			propierty_Split_widget.editingFinished.connect(self.set_Split_value)
			propierty_Split_widget.textChanged.connect(self.set_Split_value)
		elif isinstance(propierty_Split_widget, QCheckBox):
			propierty_Split_widget.stateChanged.connect(self.set_Split_value)
		self.__widget_by_propierty['Split'] = propierty_Split_widget
		propierty_PointCloud_widget = self.__widget.get_widget('PointCloud')
		if isinstance(propierty_PointCloud_widget, QSpinBox):
			propierty_PointCloud_widget.valueChanged.connect(self.set_PointCloud_value)
		elif isinstance(propierty_PointCloud_widget, QDoubleSpinBox):
			propierty_PointCloud_widget.valueChanged.connect(self.set_PointCloud_value)
		elif isinstance(propierty_PointCloud_widget, QComboBox):
			propierty_PointCloud_widget.currentIndexChanged.connect(self.set_PointCloud_value)
		elif isinstance(propierty_PointCloud_widget, QLineEdit):
			propierty_PointCloud_widget.editingFinished.connect(self.set_PointCloud_value)
			propierty_PointCloud_widget.textChanged.connect(self.set_PointCloud_value)
		elif isinstance(propierty_PointCloud_widget, QCheckBox):
			propierty_PointCloud_widget.stateChanged.connect(self.set_PointCloud_value)
		self.__widget_by_propierty['PointCloud'] = propierty_PointCloud_widget
		propierty_DEMs_widget = self.__widget.get_widget('DEMs')
		if isinstance(propierty_DEMs_widget, QSpinBox):
			propierty_DEMs_widget.valueChanged.connect(self.set_DEMs_value)
		elif isinstance(propierty_DEMs_widget, QDoubleSpinBox):
			propierty_DEMs_widget.valueChanged.connect(self.set_DEMs_value)
		elif isinstance(propierty_DEMs_widget, QComboBox):
			propierty_DEMs_widget.currentIndexChanged.connect(self.set_DEMs_value)
		elif isinstance(propierty_DEMs_widget, QLineEdit):
			propierty_DEMs_widget.editingFinished.connect(self.set_DEMs_value)
			propierty_DEMs_widget.textChanged.connect(self.set_DEMs_value)
		elif isinstance(propierty_DEMs_widget, QCheckBox):
			propierty_DEMs_widget.stateChanged.connect(self.set_DEMs_value)
		self.__widget_by_propierty['DEMs'] = propierty_DEMs_widget
		propierty_Orthomosaic_widget = self.__widget.get_widget('Orthomosaic')
		if isinstance(propierty_Orthomosaic_widget, QSpinBox):
			propierty_Orthomosaic_widget.valueChanged.connect(self.set_Orthomosaic_value)
		elif isinstance(propierty_Orthomosaic_widget, QDoubleSpinBox):
			propierty_Orthomosaic_widget.valueChanged.connect(self.set_Orthomosaic_value)
		elif isinstance(propierty_Orthomosaic_widget, QComboBox):
			propierty_Orthomosaic_widget.currentIndexChanged.connect(self.set_Orthomosaic_value)
		elif isinstance(propierty_Orthomosaic_widget, QLineEdit):
			propierty_Orthomosaic_widget.editingFinished.connect(self.set_Orthomosaic_value)
			propierty_Orthomosaic_widget.textChanged.connect(self.set_Orthomosaic_value)
		elif isinstance(propierty_Orthomosaic_widget, QCheckBox):
			propierty_Orthomosaic_widget.stateChanged.connect(self.set_Orthomosaic_value)
		self.__widget_by_propierty['Orthomosaic'] = propierty_Orthomosaic_widget
		propierty_Report_widget = self.__widget.get_widget('Report')
		if isinstance(propierty_Report_widget, QSpinBox):
			propierty_Report_widget.valueChanged.connect(self.set_Report_value)
		elif isinstance(propierty_Report_widget, QDoubleSpinBox):
			propierty_Report_widget.valueChanged.connect(self.set_Report_value)
		elif isinstance(propierty_Report_widget, QComboBox):
			propierty_Report_widget.currentIndexChanged.connect(self.set_Report_value)
		elif isinstance(propierty_Report_widget, QLineEdit):
			propierty_Report_widget.editingFinished.connect(self.set_Report_value)
			propierty_Report_widget.textChanged.connect(self.set_Report_value)
		elif isinstance(propierty_Report_widget, QCheckBox):
			propierty_Report_widget.stateChanged.connect(self.set_Report_value)
		self.__widget_by_propierty['Report'] = propierty_Report_widget
