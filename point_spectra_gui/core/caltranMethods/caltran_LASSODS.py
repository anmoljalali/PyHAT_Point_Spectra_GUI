import numpy as np
from PyQt5 import QtWidgets, QtCore

from point_spectra_gui.ui.caltran_LASSODS import Ui_Form
from point_spectra_gui.util.Modules import Modules

class Ui_Form(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        pass

    def run(self):

        params = {
                  'reg':['lasso'],
                  'rho': self.rho_spin.value(),
                  'beta': self.beta_spin.value(),
                  'max_iter': self.niter_spinBox.value(),
                  'epsilon': self.epsilon_doubleSpinBox.value()}

        return params


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
