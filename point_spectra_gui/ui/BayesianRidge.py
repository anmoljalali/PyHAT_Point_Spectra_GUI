# -*- coding: utf-8 -*-

# Form implementation generated from reading util file 'C:\Users\nfinch\Desktop\GitHub\PySAT_Point_Spectra_GUI\util\BayesianRidge.util'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(405, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.numOfIterationsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.numOfIterationsLabel.setObjectName("numOfIterationsLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.numOfIterationsLabel)
        self.numOfIterationsSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.numOfIterationsSpinBox.setMaximum(999999999)
        self.numOfIterationsSpinBox.setProperty("value", 300)
        self.numOfIterationsSpinBox.setObjectName("numOfIterationsSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numOfIterationsSpinBox)
        self.toleranceLabel = QtWidgets.QLabel(self.formGroupBox)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.toleranceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.toleranceDoubleSpinBox.setDecimals(5)
        self.toleranceDoubleSpinBox.setSingleStep(0.001)
        self.toleranceDoubleSpinBox.setProperty("value", 0.001)
        self.toleranceDoubleSpinBox.setObjectName("toleranceDoubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.toleranceDoubleSpinBox)
        self.alpha1Label = QtWidgets.QLabel(self.formGroupBox)
        self.alpha1Label.setObjectName("alpha1Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.alpha1Label)
        self.alpha1DoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.alpha1DoubleSpinBox.setDecimals(5)
        self.alpha1DoubleSpinBox.setSingleStep(0.001)
        self.alpha1DoubleSpinBox.setProperty("value", 0.001)
        self.alpha1DoubleSpinBox.setObjectName("alpha1DoubleSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.alpha1DoubleSpinBox)
        self.alpha2Label = QtWidgets.QLabel(self.formGroupBox)
        self.alpha2Label.setObjectName("alpha2Label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alpha2Label)
        self.alpha2DoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.alpha2DoubleSpinBox.setDecimals(8)
        self.alpha2DoubleSpinBox.setSingleStep(1e-06)
        self.alpha2DoubleSpinBox.setProperty("value", 1e-06)
        self.alpha2DoubleSpinBox.setObjectName("alpha2DoubleSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.alpha2DoubleSpinBox)
        self.lambdaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.lambdaLabel.setObjectName("lambdaLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lambdaLabel)
        self.lambdaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.lambdaDoubleSpinBox.setDecimals(8)
        self.lambdaDoubleSpinBox.setSingleStep(1e-06)
        self.lambdaDoubleSpinBox.setProperty("value", 1e-06)
        self.lambdaDoubleSpinBox.setObjectName("lambdaDoubleSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lambdaDoubleSpinBox)
        self.computerScoreLabel = QtWidgets.QLabel(self.formGroupBox)
        self.computerScoreLabel.setObjectName("computerScoreLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.computerScoreLabel)
        self.computerScoreCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.computerScoreCheckBox.setObjectName("computerScoreCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.computerScoreCheckBox)
        self.fitInterceptLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitInterceptCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.fitInterceptCheckBox.setChecked(True)
        self.fitInterceptCheckBox.setObjectName("fitInterceptCheckBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.fitInterceptCheckBox)
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)
        self.copyXLabel = QtWidgets.QLabel(self.formGroupBox)
        self.copyXLabel.setObjectName("copyXLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.copyXLabel)
        self.copyXCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.copyXCheckBox.setChecked(True)
        self.copyXCheckBox.setObjectName("copyXCheckBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.copyXCheckBox)
        self.verboseLabel = QtWidgets.QLabel(self.formGroupBox)
        self.verboseLabel.setObjectName("verboseLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.verboseLabel)
        self.verboseCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.verboseCheckBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.numOfIterationsLabel.setText(_translate("Form", "num of iterations"))
        self.toleranceLabel.setText(_translate("Form", "Tolerance"))
        self.alpha1Label.setText(_translate("Form", "Alpha 1"))
        self.alpha2Label.setText(_translate("Form", "Alpha 2"))
        self.lambdaLabel.setText(_translate("Form", "Lambda"))
        self.computerScoreLabel.setText(_translate("Form", "Computer Score"))
        self.computerScoreCheckBox.setText(_translate("Form", "compute the objective function at each step of the model"))
        self.fitInterceptLabel.setText(_translate("Form", "Fit Intercept"))
        self.fitInterceptCheckBox.setText(_translate("Form", "calculate the intercept for this model"))
        self.normalizeLabel.setText(_translate("Form", "Normalize"))
        self.normalizeCheckBox.setText(_translate("Form", "regressors X will be normlized before regression"))
        self.copyXLabel.setText(_translate("Form", "Copy X"))
        self.copyXCheckBox.setText(_translate("Form", "X will be copied; else, it may be overwritten"))
        self.verboseLabel.setText(_translate("Form", "Verbose"))
        self.verboseCheckBox.setText(_translate("Form", "Verbose mode when fitting the model"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

