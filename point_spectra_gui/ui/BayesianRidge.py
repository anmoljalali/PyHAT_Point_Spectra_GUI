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
        Form.setWindowTitle(("Form"))
        self.numOfIterationsLabel.setText(("num of iterations"))
        self.numOfIterationsSpinBox.setToolTip(("Maximum number of iterations. Default is 300."))
        self.numOfIterationsSpinBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.toleranceLabel.setText(("Tolerance"))
        self.toleranceDoubleSpinBox.setToolTip(("Stop the algorithm if w has converged. Default is 1.e-3."))
        self.toleranceDoubleSpinBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.alpha1Label.setText(("Alpha 1"))
        self.alpha1DoubleSpinBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.alpha2Label.setText(("Alpha 2"))
        self.alpha2DoubleSpinBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.lambdaLabel.setText(("Lambda"))
        self.lambdaDoubleSpinBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.computerScoreLabel.setText(("Computer Score"))
        self.computerScoreCheckBox.setToolTip(
            _translate("Form", "If True, compute the objective function at each step of the model.\n"
                               "Default is False"))
        self.computerScoreCheckBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.computerScoreCheckBox.setText(("compute the objective function at each step of the model"))
        self.fitInterceptLabel.setText(("Fit Intercept"))
        self.fitInterceptCheckBox.setToolTip(
            _translate("Form", "whether to calculate the intercept for this model. If set to false,\n"
                               "no intercept will be used in calculations (e.g. data is expected to\n"
                               "be already centered). Default is True."))
        self.fitInterceptCheckBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.fitInterceptCheckBox.setText(("calculate the intercept for this model"))
        self.normalizeLabel.setText(("Normalize"))
        self.normalizeCheckBox.setToolTip(
            _translate("Form", "This parameter is ignored when fit_intercept is set to False. If True,\n"
                               "the regressors X will be normalized before regression by subtracting\n"
                               "the mean and dividing by the l2-norm. If you wish to standardize,\n"
                               "please use sklearn.preprocessing.StandardScaler before calling fit on\n"
                               "an estimator with normalize=False."))
        self.normalizeCheckBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.normalizeCheckBox.setText(("regressors X will be normlized before regression"))
        self.copyXLabel.setText(("Copy X"))
        self.copyXCheckBox.setToolTip(("If True, X will be copied; else, it may be overwritten."))
        self.copyXCheckBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.copyXCheckBox.setText(("X will be copied; else, it may be overwritten"))
        self.verboseLabel.setText(("Verbose"))
        self.verboseCheckBox.setToolTip(("Verbose mode when fitting the model."))
        self.verboseCheckBox.setWhatsThis(
            ("http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html"))
        self.verboseCheckBox.setText(("Verbose mode when fitting the model"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
