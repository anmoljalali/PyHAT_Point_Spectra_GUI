# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.cLabel = QtWidgets.QLabel(self.formGroupBox)
        self.cLabel.setObjectName("cLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cLabel)
        self.cDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.cDoubleSpinBox.setProperty("value", 1.0)
        self.cDoubleSpinBox.setObjectName("cDoubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cDoubleSpinBox)
        self.epsilonLabel = QtWidgets.QLabel(self.formGroupBox)
        self.epsilonLabel.setObjectName("epsilonLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.epsilonLabel)
        self.epsilonDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.epsilonDoubleSpinBox.setProperty("value", 0.1)
        self.epsilonDoubleSpinBox.setObjectName("epsilonDoubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.epsilonDoubleSpinBox)
        self.kernelLabel = QtWidgets.QLabel(self.formGroupBox)
        self.kernelLabel.setObjectName("kernelLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.kernelLabel)
        self.kernelComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.kernelComboBox.setObjectName("kernelComboBox")
        self.kernelComboBox.addItem("")
        self.kernelComboBox.addItem("")
        self.kernelComboBox.addItem("")
        self.kernelComboBox.addItem("")
        self.kernelComboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.kernelComboBox)
        self.degreeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.degreeLabel.setObjectName("degreeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.degreeLabel)
        self.gammaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.gammaLabel.setObjectName("gammaLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.gammaLabel)
        self.gammaComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.gammaComboBox.setObjectName("gammaComboBox")
        self.gammaComboBox.addItem("")
        self.gammaComboBox.addItem("")
        self.gammaComboBox.addItem("")
        self.gammaComboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gammaComboBox)
        self.coeff0Label = QtWidgets.QLabel(self.formGroupBox)
        self.coeff0Label.setObjectName("coeff0Label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.coeff0Label)
        self.coeff0DoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.coeff0DoubleSpinBox.setObjectName("coeff0DoubleSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.coeff0DoubleSpinBox)
        self.shrinkingLabel = QtWidgets.QLabel(self.formGroupBox)
        self.shrinkingLabel.setObjectName("shrinkingLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.shrinkingLabel)
        self.shrinkingCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.shrinkingCheckBox.setObjectName("shrinkingCheckBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.shrinkingCheckBox)
        self.toleranceLabel = QtWidgets.QLabel(self.formGroupBox)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.toleranceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.toleranceDoubleSpinBox.setDecimals(3)
        self.toleranceDoubleSpinBox.setProperty("value", 0.001)
        self.toleranceDoubleSpinBox.setObjectName("toleranceDoubleSpinBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.toleranceDoubleSpinBox)
        self.cacheSizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.cacheSizeLabel.setObjectName("cacheSizeLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.cacheSizeLabel)
        self.cacheSizeSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.cacheSizeSpinBox.setMaximum(999)
        self.cacheSizeSpinBox.setProperty("value", 200)
        self.cacheSizeSpinBox.setObjectName("cacheSizeSpinBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.cacheSizeSpinBox)
        self.verboseLabel = QtWidgets.QLabel(self.formGroupBox)
        self.verboseLabel.setObjectName("verboseLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.verboseLabel)
        self.verboseCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.verboseCheckBox)
        self.maxIterationsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.maxIterationsLabel.setObjectName("maxIterationsLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.maxIterationsLabel)
        self.maxIterationsSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.maxIterationsSpinBox.setMinimum(-1)
        self.maxIterationsSpinBox.setMaximum(9999999)
        self.maxIterationsSpinBox.setProperty("value", -1)
        self.maxIterationsSpinBox.setObjectName("maxIterationsSpinBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.maxIterationsSpinBox)
        self.degreeSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.degreeSpinBox.setObjectName("degreeSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.degreeSpinBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.cLabel.setText(("C"))
        self.cDoubleSpinBox.setToolTip(("Penalty parameter C of the error term."))
        self.cDoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))
        self.epsilonLabel.setText(("Epsilon"))
        self.epsilonDoubleSpinBox.setToolTip(
            _translate("Form", "Epsilon in the epsilon-SVR model. It specifies the epsilon-tube\n"
                               "within which no penalty is associated in the training loss function\n"
                               "with points predicted within a distance epsilon from the actual\n"
                               "value."))
        self.epsilonDoubleSpinBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))
        self.kernelLabel.setText(("Kernel"))
        self.kernelComboBox.setToolTip(
            _translate("Form", "Specifies the kernel type to be used in the algorithm. It must be one\n"
                               "of \'linear\', \'poly\', \'rbf\', \'sigmoid\', \'precomputed\' or a callable.\n"
                               "If none is given, \'rbf\' will be used. If a callable is given it is\n"
                               "used to precompute the kernel matrix."))
        self.kernelComboBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))
        self.kernelComboBox.setItemText(0, ("rbf"))
        self.kernelComboBox.setItemText(1, ("poly"))
        self.kernelComboBox.setItemText(2, ("sigmoid"))
        self.kernelComboBox.setItemText(3, ("linear"))
        self.kernelComboBox.setItemText(4, ("precomputed"))
        self.degreeLabel.setText(("Degree"))
        self.gammaLabel.setText(("Gamma"))
        self.gammaComboBox.setToolTip(
            _translate("Form", "Kernel coefficient for \'rbf\', \'poly\' and \'sigmoid\'. If gamma is \'auto\'\n"
                               "then 1/n_features will be used instead."))
        self.gammaComboBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))
        self.gammaComboBox.setItemText(0, ("auto"))
        self.gammaComboBox.setItemText(1, ("rbf"))
        self.gammaComboBox.setItemText(2, ("poly"))
        self.gammaComboBox.setItemText(3, ("sigmoid"))
        self.coeff0Label.setText(("Coeff 0"))
        self.coeff0DoubleSpinBox.setToolTip(
            _translate("Form", "Independent term in kernel function. It is only significant in \'poly\'\n"
                               "and \'sigmoid\'."))
        self.coeff0DoubleSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))
        self.shrinkingLabel.setText(("Shrinking"))
        self.shrinkingCheckBox.setToolTip(("Whether to use the shrinking heuristic."))
        self.shrinkingCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))
        self.toleranceLabel.setText(("Tolerance"))
        self.toleranceDoubleSpinBox.setToolTip(("Tolerance for stopping criterion."))
        self.toleranceDoubleSpinBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))
        self.cacheSizeLabel.setText(("Cache Size"))
        self.cacheSizeSpinBox.setToolTip(("Specify the size of the kernel cache (in MB)."))
        self.cacheSizeSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))
        self.verboseLabel.setText(("Verbose"))
        self.verboseCheckBox.setToolTip(
            _translate("Form", "Enable verbose output. Note that this setting takes advantage of a\n"
                               "per-process runtime setting in libsvm that, if enabled, may not work\n"
                               "properly in a multithreaded context."))
        self.verboseCheckBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))
        self.maxIterationsLabel.setText(("Max Iterations"))
        self.maxIterationsSpinBox.setToolTip(("Hard limit on iterations within solver, or -1 for no limit."))
        self.maxIterationsSpinBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))
        self.degreeSpinBox.setToolTip(("Degree of the polynomial kernel function (\'poly\'). Ignored by all\n"
                                       "other kernels."))
        self.degreeSpinBox.setWhatsThis(("http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
