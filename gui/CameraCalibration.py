from PyQt5.QtWidgets import QDoubleSpinBox, QSpinBox, QComboBox, QLineEdit, QCheckBox
from . import gui_defines

class CameraCalibration:
	def __init__(self):
		self.__text_by_propierty = {}
		self.__widget_by_propierty = {}
		self.__json_content_by_propierty = {}
		self.__json_content_by_propierty['text'] = {'spanish': 'Calibracion de camara', 'english': 'Camera calibration'}
		self.__text = 'Calibracion de camara'
		self.__json_content_by_propierty['f'] = {'text': {'spanish': 'Focal', 'english': 'Focal'}, 'definition': {'spanish': 'Seleccionar si se calibra la focal', 'english': 'Select calibrate focal'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['f'] = 'Focal'
		self.__widget_by_propierty['f'] = None
		self.__f = True
		self.__f_value = True
		self.__json_content_by_propierty['cx'] = {'text': {'spanish': 'X PPA', 'english': 'X PPA'}, 'definition': {'spanish': 'Seleccionar si se calibra la coordenada X del PPA', 'english': 'Select calibrate PPA X coordinate'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['cx'] = 'X PPA'
		self.__widget_by_propierty['cx'] = None
		self.__cx = True
		self.__cx_value = True
		self.__json_content_by_propierty['cy'] = {'text': {'spanish': 'Y PPA', 'english': 'Y PPA'}, 'definition': {'spanish': 'Seleccionar si se calibra la coordenada Y del PPA', 'english': 'Select calibrate PPA Y coordinate'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['cy'] = 'Y PPA'
		self.__widget_by_propierty['cy'] = None
		self.__cy = True
		self.__cy_value = True
		self.__json_content_by_propierty['k1'] = {'text': {'spanish': 'k1', 'english': 'k1'}, 'definition': {'spanish': 'Seleccionar si se calibra k1 de distorsion radial', 'english': 'Select calibrate k1 radial distortion'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['k1'] = 'k1'
		self.__widget_by_propierty['k1'] = None
		self.__k1 = True
		self.__k1_value = True
		self.__json_content_by_propierty['k2'] = {'text': {'spanish': 'k2', 'english': 'k2'}, 'definition': {'spanish': 'Seleccionar si se calibra k2 de distorsion radial', 'english': 'Select calibrate k2 radial distortion'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['k2'] = 'k2'
		self.__widget_by_propierty['k2'] = None
		self.__k2 = True
		self.__k2_value = True
		self.__json_content_by_propierty['k3'] = {'text': {'spanish': 'k3', 'english': 'k3'}, 'definition': {'spanish': 'Seleccionar si se calibra k3 de distorsion radial', 'english': 'Select calibrate k3 radial distortion'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['k3'] = 'k3'
		self.__widget_by_propierty['k3'] = None
		self.__k3 = True
		self.__k3_value = True
		self.__json_content_by_propierty['k4'] = {'text': {'spanish': 'k4', 'english': 'k4'}, 'definition': {'spanish': 'Seleccionar si se calibra k4 de distorsion radial', 'english': 'Select calibrate k4 radial distortion'}, 'type': 'boolean', 'default': 'False'}
		self.__text_by_propierty['k4'] = 'k4'
		self.__widget_by_propierty['k4'] = None
		self.__k4 = False
		self.__k4_value = False
		self.__json_content_by_propierty['b1'] = {'text': {'spanish': 'Afinidad', 'english': 'Affinity'}, 'definition': {'spanish': 'Seleccionar si se calibra la relacion de aspecto', 'english': 'Select calibrate aspect ratio'}, 'type': 'boolean', 'default': 'False'}
		self.__text_by_propierty['b1'] = 'Afinidad'
		self.__widget_by_propierty['b1'] = None
		self.__b1 = False
		self.__b1_value = False
		self.__json_content_by_propierty['b2'] = {'text': {'spanish': 'Asimetria', 'english': 'Skew'}, 'definition': {'spanish': 'Seleccionar si se calibra la asimetria', 'english': 'Select calibrate skew'}, 'type': 'boolean', 'default': 'False'}
		self.__text_by_propierty['b2'] = 'Asimetria'
		self.__widget_by_propierty['b2'] = None
		self.__b2 = False
		self.__b2_value = False
		self.__json_content_by_propierty['p1'] = {'text': {'spanish': 'p1', 'english': 'p1'}, 'definition': {'spanish': 'Seleccionar si se calibra p1 de distorsion tangencial', 'english': 'Select calibrate p1 tangential distortion'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['p1'] = 'p1'
		self.__widget_by_propierty['p1'] = None
		self.__p1 = True
		self.__p1_value = True
		self.__json_content_by_propierty['p2'] = {'text': {'spanish': 'p2', 'english': 'p2'}, 'definition': {'spanish': 'Seleccionar si se calibra p2 de distorsion tangencial', 'english': 'Select calibrate p2 tangential distortion'}, 'type': 'boolean', 'default': 'True'}
		self.__text_by_propierty['p2'] = 'p2'
		self.__widget_by_propierty['p2'] = None
		self.__p2 = True
		self.__p2_value = True
		self.__widget = None

	def get_propierty_json_content(self, value):
		json_content = None
		if value in self.__json_content_by_propierty:
			json_content = self.__json_content_by_propierty[value]
		return json_content

	def get_values_as_dictionary(self):
		values = {}
		values['f'] = self.__f_value
		values['cx'] = self.__cx_value
		values['cy'] = self.__cy_value
		values['k1'] = self.__k1_value
		values['k2'] = self.__k2_value
		values['k3'] = self.__k3_value
		values['k4'] = self.__k4_value
		values['b1'] = self.__b1_value
		values['b2'] = self.__b2_value
		values['p1'] = self.__p1_value
		values['p2'] = self.__p2_value
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
	def f(self):
		return self.__f

	@f.setter
	def f(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra la focal'):
		self.__f = value

	def set_f_value(self):
		propierty_f_widget = self.__widget_by_propierty['f'] 
		if isinstance(propierty_f_widget, QSpinBox):
			self.__f_value = propierty_f_widget.value()
		elif isinstance(propierty_f_widget, QDoubleSpinBox):
			self.__f_value = propierty_f_widget.value()
		elif isinstance(propierty_f_widget, QComboBox):
			self.__f_value = propierty_f_widget.currentText()
		elif isinstance(propierty_f_widget, QLineEdit):
			self.__f_value = propierty_f_widget.text()
		elif isinstance(propierty_f_widget, QCheckBox):
			self.__f_value = propierty_f_widget.isChecked()

	@property
	def cx(self):
		return self.__cx

	@cx.setter
	def cx(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra la coordenada X del PPA'):
		self.__cx = value

	def set_cx_value(self):
		propierty_cx_widget = self.__widget_by_propierty['cx'] 
		if isinstance(propierty_cx_widget, QSpinBox):
			self.__cx_value = propierty_cx_widget.value()
		elif isinstance(propierty_cx_widget, QDoubleSpinBox):
			self.__cx_value = propierty_cx_widget.value()
		elif isinstance(propierty_cx_widget, QComboBox):
			self.__cx_value = propierty_cx_widget.currentText()
		elif isinstance(propierty_cx_widget, QLineEdit):
			self.__cx_value = propierty_cx_widget.text()
		elif isinstance(propierty_cx_widget, QCheckBox):
			self.__cx_value = propierty_cx_widget.isChecked()

	@property
	def cy(self):
		return self.__cy

	@cy.setter
	def cy(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra la coordenada Y del PPA'):
		self.__cy = value

	def set_cy_value(self):
		propierty_cy_widget = self.__widget_by_propierty['cy'] 
		if isinstance(propierty_cy_widget, QSpinBox):
			self.__cy_value = propierty_cy_widget.value()
		elif isinstance(propierty_cy_widget, QDoubleSpinBox):
			self.__cy_value = propierty_cy_widget.value()
		elif isinstance(propierty_cy_widget, QComboBox):
			self.__cy_value = propierty_cy_widget.currentText()
		elif isinstance(propierty_cy_widget, QLineEdit):
			self.__cy_value = propierty_cy_widget.text()
		elif isinstance(propierty_cy_widget, QCheckBox):
			self.__cy_value = propierty_cy_widget.isChecked()

	@property
	def k1(self):
		return self.__k1

	@k1.setter
	def k1(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra k1 de distorsion radial'):
		self.__k1 = value

	def set_k1_value(self):
		propierty_k1_widget = self.__widget_by_propierty['k1'] 
		if isinstance(propierty_k1_widget, QSpinBox):
			self.__k1_value = propierty_k1_widget.value()
		elif isinstance(propierty_k1_widget, QDoubleSpinBox):
			self.__k1_value = propierty_k1_widget.value()
		elif isinstance(propierty_k1_widget, QComboBox):
			self.__k1_value = propierty_k1_widget.currentText()
		elif isinstance(propierty_k1_widget, QLineEdit):
			self.__k1_value = propierty_k1_widget.text()
		elif isinstance(propierty_k1_widget, QCheckBox):
			self.__k1_value = propierty_k1_widget.isChecked()

	@property
	def k2(self):
		return self.__k2

	@k2.setter
	def k2(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra k2 de distorsion radial'):
		self.__k2 = value

	def set_k2_value(self):
		propierty_k2_widget = self.__widget_by_propierty['k2'] 
		if isinstance(propierty_k2_widget, QSpinBox):
			self.__k2_value = propierty_k2_widget.value()
		elif isinstance(propierty_k2_widget, QDoubleSpinBox):
			self.__k2_value = propierty_k2_widget.value()
		elif isinstance(propierty_k2_widget, QComboBox):
			self.__k2_value = propierty_k2_widget.currentText()
		elif isinstance(propierty_k2_widget, QLineEdit):
			self.__k2_value = propierty_k2_widget.text()
		elif isinstance(propierty_k2_widget, QCheckBox):
			self.__k2_value = propierty_k2_widget.isChecked()

	@property
	def k3(self):
		return self.__k3

	@k3.setter
	def k3(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra k3 de distorsion radial'):
		self.__k3 = value

	def set_k3_value(self):
		propierty_k3_widget = self.__widget_by_propierty['k3'] 
		if isinstance(propierty_k3_widget, QSpinBox):
			self.__k3_value = propierty_k3_widget.value()
		elif isinstance(propierty_k3_widget, QDoubleSpinBox):
			self.__k3_value = propierty_k3_widget.value()
		elif isinstance(propierty_k3_widget, QComboBox):
			self.__k3_value = propierty_k3_widget.currentText()
		elif isinstance(propierty_k3_widget, QLineEdit):
			self.__k3_value = propierty_k3_widget.text()
		elif isinstance(propierty_k3_widget, QCheckBox):
			self.__k3_value = propierty_k3_widget.isChecked()

	@property
	def k4(self):
		return self.__k4

	@k4.setter
	def k4(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra k4 de distorsion radial'):
		self.__k4 = value

	def set_k4_value(self):
		propierty_k4_widget = self.__widget_by_propierty['k4'] 
		if isinstance(propierty_k4_widget, QSpinBox):
			self.__k4_value = propierty_k4_widget.value()
		elif isinstance(propierty_k4_widget, QDoubleSpinBox):
			self.__k4_value = propierty_k4_widget.value()
		elif isinstance(propierty_k4_widget, QComboBox):
			self.__k4_value = propierty_k4_widget.currentText()
		elif isinstance(propierty_k4_widget, QLineEdit):
			self.__k4_value = propierty_k4_widget.text()
		elif isinstance(propierty_k4_widget, QCheckBox):
			self.__k4_value = propierty_k4_widget.isChecked()

	@property
	def b1(self):
		return self.__b1

	@b1.setter
	def b1(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra la relacion de aspecto'):
		self.__b1 = value

	def set_b1_value(self):
		propierty_b1_widget = self.__widget_by_propierty['b1'] 
		if isinstance(propierty_b1_widget, QSpinBox):
			self.__b1_value = propierty_b1_widget.value()
		elif isinstance(propierty_b1_widget, QDoubleSpinBox):
			self.__b1_value = propierty_b1_widget.value()
		elif isinstance(propierty_b1_widget, QComboBox):
			self.__b1_value = propierty_b1_widget.currentText()
		elif isinstance(propierty_b1_widget, QLineEdit):
			self.__b1_value = propierty_b1_widget.text()
		elif isinstance(propierty_b1_widget, QCheckBox):
			self.__b1_value = propierty_b1_widget.isChecked()

	@property
	def b2(self):
		return self.__b2

	@b2.setter
	def b2(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra la asimetria'):
		self.__b2 = value

	def set_b2_value(self):
		propierty_b2_widget = self.__widget_by_propierty['b2'] 
		if isinstance(propierty_b2_widget, QSpinBox):
			self.__b2_value = propierty_b2_widget.value()
		elif isinstance(propierty_b2_widget, QDoubleSpinBox):
			self.__b2_value = propierty_b2_widget.value()
		elif isinstance(propierty_b2_widget, QComboBox):
			self.__b2_value = propierty_b2_widget.currentText()
		elif isinstance(propierty_b2_widget, QLineEdit):
			self.__b2_value = propierty_b2_widget.text()
		elif isinstance(propierty_b2_widget, QCheckBox):
			self.__b2_value = propierty_b2_widget.isChecked()

	@property
	def p1(self):
		return self.__p1

	@p1.setter
	def p1(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra p1 de distorsion tangencial'):
		self.__p1 = value

	def set_p1_value(self):
		propierty_p1_widget = self.__widget_by_propierty['p1'] 
		if isinstance(propierty_p1_widget, QSpinBox):
			self.__p1_value = propierty_p1_widget.value()
		elif isinstance(propierty_p1_widget, QDoubleSpinBox):
			self.__p1_value = propierty_p1_widget.value()
		elif isinstance(propierty_p1_widget, QComboBox):
			self.__p1_value = propierty_p1_widget.currentText()
		elif isinstance(propierty_p1_widget, QLineEdit):
			self.__p1_value = propierty_p1_widget.text()
		elif isinstance(propierty_p1_widget, QCheckBox):
			self.__p1_value = propierty_p1_widget.isChecked()

	@property
	def p2(self):
		return self.__p2

	@p2.setter
	def p2(self, value: 'widget:QCheckBox, toolTip:Seleccionar si se calibra p2 de distorsion tangencial'):
		self.__p2 = value

	def set_p2_value(self):
		propierty_p2_widget = self.__widget_by_propierty['p2'] 
		if isinstance(propierty_p2_widget, QSpinBox):
			self.__p2_value = propierty_p2_widget.value()
		elif isinstance(propierty_p2_widget, QDoubleSpinBox):
			self.__p2_value = propierty_p2_widget.value()
		elif isinstance(propierty_p2_widget, QComboBox):
			self.__p2_value = propierty_p2_widget.currentText()
		elif isinstance(propierty_p2_widget, QLineEdit):
			self.__p2_value = propierty_p2_widget.text()
		elif isinstance(propierty_p2_widget, QCheckBox):
			self.__p2_value = propierty_p2_widget.isChecked()

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
		propierty_f_widget = self.__widget.get_widget('f')
		if isinstance(propierty_f_widget, QSpinBox):
			propierty_f_widget.valueChanged.connect(self.set_f_value)
		elif isinstance(propierty_f_widget, QDoubleSpinBox):
			propierty_f_widget.valueChanged.connect(self.set_f_value)
		elif isinstance(propierty_f_widget, QComboBox):
			propierty_f_widget.currentIndexChanged.connect(self.set_f_value)
		elif isinstance(propierty_f_widget, QLineEdit):
			propierty_f_widget.editingFinished.connect(self.set_f_value)
			propierty_f_widget.textChanged.connect(self.set_f_value)
		elif isinstance(propierty_f_widget, QCheckBox):
			propierty_f_widget.stateChanged.connect(self.set_f_value)
		self.__widget_by_propierty['f'] = propierty_f_widget
		propierty_cx_widget = self.__widget.get_widget('cx')
		if isinstance(propierty_cx_widget, QSpinBox):
			propierty_cx_widget.valueChanged.connect(self.set_cx_value)
		elif isinstance(propierty_cx_widget, QDoubleSpinBox):
			propierty_cx_widget.valueChanged.connect(self.set_cx_value)
		elif isinstance(propierty_cx_widget, QComboBox):
			propierty_cx_widget.currentIndexChanged.connect(self.set_cx_value)
		elif isinstance(propierty_cx_widget, QLineEdit):
			propierty_cx_widget.editingFinished.connect(self.set_cx_value)
			propierty_cx_widget.textChanged.connect(self.set_cx_value)
		elif isinstance(propierty_cx_widget, QCheckBox):
			propierty_cx_widget.stateChanged.connect(self.set_cx_value)
		self.__widget_by_propierty['cx'] = propierty_cx_widget
		propierty_cy_widget = self.__widget.get_widget('cy')
		if isinstance(propierty_cy_widget, QSpinBox):
			propierty_cy_widget.valueChanged.connect(self.set_cy_value)
		elif isinstance(propierty_cy_widget, QDoubleSpinBox):
			propierty_cy_widget.valueChanged.connect(self.set_cy_value)
		elif isinstance(propierty_cy_widget, QComboBox):
			propierty_cy_widget.currentIndexChanged.connect(self.set_cy_value)
		elif isinstance(propierty_cy_widget, QLineEdit):
			propierty_cy_widget.editingFinished.connect(self.set_cy_value)
			propierty_cy_widget.textChanged.connect(self.set_cy_value)
		elif isinstance(propierty_cy_widget, QCheckBox):
			propierty_cy_widget.stateChanged.connect(self.set_cy_value)
		self.__widget_by_propierty['cy'] = propierty_cy_widget
		propierty_k1_widget = self.__widget.get_widget('k1')
		if isinstance(propierty_k1_widget, QSpinBox):
			propierty_k1_widget.valueChanged.connect(self.set_k1_value)
		elif isinstance(propierty_k1_widget, QDoubleSpinBox):
			propierty_k1_widget.valueChanged.connect(self.set_k1_value)
		elif isinstance(propierty_k1_widget, QComboBox):
			propierty_k1_widget.currentIndexChanged.connect(self.set_k1_value)
		elif isinstance(propierty_k1_widget, QLineEdit):
			propierty_k1_widget.editingFinished.connect(self.set_k1_value)
			propierty_k1_widget.textChanged.connect(self.set_k1_value)
		elif isinstance(propierty_k1_widget, QCheckBox):
			propierty_k1_widget.stateChanged.connect(self.set_k1_value)
		self.__widget_by_propierty['k1'] = propierty_k1_widget
		propierty_k2_widget = self.__widget.get_widget('k2')
		if isinstance(propierty_k2_widget, QSpinBox):
			propierty_k2_widget.valueChanged.connect(self.set_k2_value)
		elif isinstance(propierty_k2_widget, QDoubleSpinBox):
			propierty_k2_widget.valueChanged.connect(self.set_k2_value)
		elif isinstance(propierty_k2_widget, QComboBox):
			propierty_k2_widget.currentIndexChanged.connect(self.set_k2_value)
		elif isinstance(propierty_k2_widget, QLineEdit):
			propierty_k2_widget.editingFinished.connect(self.set_k2_value)
			propierty_k2_widget.textChanged.connect(self.set_k2_value)
		elif isinstance(propierty_k2_widget, QCheckBox):
			propierty_k2_widget.stateChanged.connect(self.set_k2_value)
		self.__widget_by_propierty['k2'] = propierty_k2_widget
		propierty_k3_widget = self.__widget.get_widget('k3')
		if isinstance(propierty_k3_widget, QSpinBox):
			propierty_k3_widget.valueChanged.connect(self.set_k3_value)
		elif isinstance(propierty_k3_widget, QDoubleSpinBox):
			propierty_k3_widget.valueChanged.connect(self.set_k3_value)
		elif isinstance(propierty_k3_widget, QComboBox):
			propierty_k3_widget.currentIndexChanged.connect(self.set_k3_value)
		elif isinstance(propierty_k3_widget, QLineEdit):
			propierty_k3_widget.editingFinished.connect(self.set_k3_value)
			propierty_k3_widget.textChanged.connect(self.set_k3_value)
		elif isinstance(propierty_k3_widget, QCheckBox):
			propierty_k3_widget.stateChanged.connect(self.set_k3_value)
		self.__widget_by_propierty['k3'] = propierty_k3_widget
		propierty_k4_widget = self.__widget.get_widget('k4')
		if isinstance(propierty_k4_widget, QSpinBox):
			propierty_k4_widget.valueChanged.connect(self.set_k4_value)
		elif isinstance(propierty_k4_widget, QDoubleSpinBox):
			propierty_k4_widget.valueChanged.connect(self.set_k4_value)
		elif isinstance(propierty_k4_widget, QComboBox):
			propierty_k4_widget.currentIndexChanged.connect(self.set_k4_value)
		elif isinstance(propierty_k4_widget, QLineEdit):
			propierty_k4_widget.editingFinished.connect(self.set_k4_value)
			propierty_k4_widget.textChanged.connect(self.set_k4_value)
		elif isinstance(propierty_k4_widget, QCheckBox):
			propierty_k4_widget.stateChanged.connect(self.set_k4_value)
		self.__widget_by_propierty['k4'] = propierty_k4_widget
		propierty_b1_widget = self.__widget.get_widget('b1')
		if isinstance(propierty_b1_widget, QSpinBox):
			propierty_b1_widget.valueChanged.connect(self.set_b1_value)
		elif isinstance(propierty_b1_widget, QDoubleSpinBox):
			propierty_b1_widget.valueChanged.connect(self.set_b1_value)
		elif isinstance(propierty_b1_widget, QComboBox):
			propierty_b1_widget.currentIndexChanged.connect(self.set_b1_value)
		elif isinstance(propierty_b1_widget, QLineEdit):
			propierty_b1_widget.editingFinished.connect(self.set_b1_value)
			propierty_b1_widget.textChanged.connect(self.set_b1_value)
		elif isinstance(propierty_b1_widget, QCheckBox):
			propierty_b1_widget.stateChanged.connect(self.set_b1_value)
		self.__widget_by_propierty['b1'] = propierty_b1_widget
		propierty_b2_widget = self.__widget.get_widget('b2')
		if isinstance(propierty_b2_widget, QSpinBox):
			propierty_b2_widget.valueChanged.connect(self.set_b2_value)
		elif isinstance(propierty_b2_widget, QDoubleSpinBox):
			propierty_b2_widget.valueChanged.connect(self.set_b2_value)
		elif isinstance(propierty_b2_widget, QComboBox):
			propierty_b2_widget.currentIndexChanged.connect(self.set_b2_value)
		elif isinstance(propierty_b2_widget, QLineEdit):
			propierty_b2_widget.editingFinished.connect(self.set_b2_value)
			propierty_b2_widget.textChanged.connect(self.set_b2_value)
		elif isinstance(propierty_b2_widget, QCheckBox):
			propierty_b2_widget.stateChanged.connect(self.set_b2_value)
		self.__widget_by_propierty['b2'] = propierty_b2_widget
		propierty_p1_widget = self.__widget.get_widget('p1')
		if isinstance(propierty_p1_widget, QSpinBox):
			propierty_p1_widget.valueChanged.connect(self.set_p1_value)
		elif isinstance(propierty_p1_widget, QDoubleSpinBox):
			propierty_p1_widget.valueChanged.connect(self.set_p1_value)
		elif isinstance(propierty_p1_widget, QComboBox):
			propierty_p1_widget.currentIndexChanged.connect(self.set_p1_value)
		elif isinstance(propierty_p1_widget, QLineEdit):
			propierty_p1_widget.editingFinished.connect(self.set_p1_value)
			propierty_p1_widget.textChanged.connect(self.set_p1_value)
		elif isinstance(propierty_p1_widget, QCheckBox):
			propierty_p1_widget.stateChanged.connect(self.set_p1_value)
		self.__widget_by_propierty['p1'] = propierty_p1_widget
		propierty_p2_widget = self.__widget.get_widget('p2')
		if isinstance(propierty_p2_widget, QSpinBox):
			propierty_p2_widget.valueChanged.connect(self.set_p2_value)
		elif isinstance(propierty_p2_widget, QDoubleSpinBox):
			propierty_p2_widget.valueChanged.connect(self.set_p2_value)
		elif isinstance(propierty_p2_widget, QComboBox):
			propierty_p2_widget.currentIndexChanged.connect(self.set_p2_value)
		elif isinstance(propierty_p2_widget, QLineEdit):
			propierty_p2_widget.editingFinished.connect(self.set_p2_value)
			propierty_p2_widget.textChanged.connect(self.set_p2_value)
		elif isinstance(propierty_p2_widget, QCheckBox):
			propierty_p2_widget.stateChanged.connect(self.set_p2_value)
		self.__widget_by_propierty['p2'] = propierty_p2_widget
