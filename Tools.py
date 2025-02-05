from PyQt5.QtWidgets import QMessageBox


def error_msg(str_error):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setWindowTitle('Error:')
    msgBox.setText(str_error)
    # msgBox.setInformativeText("Do you want to save your changes?")
    # msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
    # msgBox.setDefaultButton(QMessageBox.Save)
    ret = msgBox.exec()