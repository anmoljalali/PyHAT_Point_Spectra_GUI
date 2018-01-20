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
        self.numOfIterationsLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.numOfIterationsLineEdit.setProperty("maximum", 999999999)
        self.numOfIterationsLineEdit.setProperty("value", 300)
        self.numOfIterationsLineEdit.setObjectName("numOfIterationsLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numOfIterationsLineEdit)
        self.toleranceLabel = QtWidgets.QLabel(self.formGroupBox)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.toleranceLabel)
        self.toleranceLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.toleranceLineEdit.setProperty("decimals", 8)
        self.toleranceLineEdit.setProperty("singleStep", 0.001)
        self.toleranceLineEdit.setProperty("value", 0.001)
        self.toleranceLineEdit.setObjectName("toleranceLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.toleranceLineEdit)
        self.alpha1Label = QtWidgets.QLabel(self.formGroupBox)
        self.alpha1Label.setObjectName("alpha1Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.alpha1Label)
        self.alpha1LineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.alpha1LineEdit.setProperty("decimals", 5)
        self.alpha1LineEdit.setProperty("singleStep", 0.001)
        self.alpha1LineEdit.setProperty("value", 0.001)
        self.alpha1LineEdit.setObjectName("alpha1LineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.alpha1LineEdit)
        self.alpha2Label = QtWidgets.QLabel(self.formGroupBox)
        self.alpha2Label.setObjectName("alpha2Label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alpha2Label)
        self.alpha2LineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.alpha2LineEdit.setProperty("decimals", 8)
        self.alpha2LineEdit.setProperty("singleStep", 1e-06)
        self.alpha2LineEdit.setProperty("value", 1e-06)
        self.alpha2LineEdit.setObjectName("alpha2LineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.alpha2LineEdit)
        self.lambdaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.lambdaLabel.setObjectName("lambdaLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lambdaLabel)
        self.lambdaLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.lambdaLineEdit.setProperty("decimals", 8)
        self.lambdaLineEdit.setProperty("singleStep", 1e-06)
        self.lambdaLineEdit.setProperty("value", 1e-06)
        self.lambdaLineEdit.setObjectName("lambdaLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lambdaLineEdit)
        self.lambdaLabel_2 = QtWidgets.QLabel(self.formGroupBox)
        self.lambdaLabel_2.setObjectName("lambdaLabel_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lambdaLabel_2)
        self.lambdaLineEdit_2 = QtWidgets.QLineEdit(self.formGroupBox)
        self.lambdaLineEdit_2.setProperty("decimals", 8)
        self.lambdaLineEdit_2.setProperty("singleStep", 1e-06)
        self.lambdaLineEdit_2.setProperty("value", 1e-06)
        self.lambdaLineEdit_2.setObjectName("lambdaLineEdit_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lambdaLineEdit_2)
        self.thresholdLambdaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.thresholdLambdaLabel.setObjectName("thresholdLambdaLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.thresholdLambdaLabel)
        self.thresholdLambdaLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.thresholdLambdaLineEdit.setProperty("maximum", 999999999)
        self.thresholdLambdaLineEdit.setProperty("value", 100000)
        self.thresholdLambdaLineEdit.setObjectName("thresholdLambdaLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.thresholdLambdaLineEdit)
        self.fitInterceptLabel = QtWidgets.QLabel(self.formGroupBox)
        self.fitInterceptLabel.setObjectName("fitInterceptLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.fitInterceptLabel)
        self.fitIntercept_list = QtWidgets.QListWidget(self.formGroupBox)
        self.fitIntercept_list.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fitIntercept_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.fitIntercept_list.setObjectName("fitIntercept_list")
        item = QtWidgets.QListWidgetItem()
        self.fitIntercept_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.fitIntercept_list.addItem(item)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.fitIntercept_list)
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalize_list = QtWidgets.QListWidget(self.formGroupBox)
        self.normalize_list.setMaximumSize(QtCore.QSize(16777215, 50))
        self.normalize_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.normalize_list.setObjectName("normalize_list")
        item = QtWidgets.QListWidgetItem()
        self.normalize_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.normalize_list.addItem(item)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.normalize_list)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.numOfIterationsLineEdit, self.toleranceLineEdit)
        Form.setTabOrder(self.toleranceLineEdit, self.alpha1LineEdit)
        Form.setTabOrder(self.alpha1LineEdit, self.alpha2LineEdit)
        Form.setTabOrder(self.alpha2LineEdit, self.lambdaLineEdit)
        Form.setTabOrder(self.lambdaLineEdit, self.lambdaLineEdit_2)
        Form.setTabOrder(self.lambdaLineEdit_2, self.thresholdLambdaLineEdit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setToolTip((
                                     "<html><head/><body><p>Fit regression model with Bayesian Ridge Regression.</p><p>See Bayesian Ridge Regression for more information on the regressor.</p><p>Compared to the OLS (ordinary least squares) estimator, the coefficient weights are slightly shifted toward zeros, which stabilises them.</p><p>The histogram of the estimated weights is very peaked, as a sparsity-inducing prior is implied on the weights.</p><p>The estimation of the model is done by iteratively maximizing the marginal log-likelihood of the observations.</p></body></html>"))
        self.formGroupBox.setTitle(("ARD"))
        self.numOfIterationsLabel.setText(("num of iterations"))
        self.numOfIterationsLineEdit.setText(("300"))
        self.toleranceLabel.setText(("Tolerance"))
        self.toleranceLineEdit.setText(("0.001"))
        self.alpha1Label.setText(("Alpha 1"))
        self.alpha1LineEdit.setText(("0.000001"))
        self.alpha2Label.setText(("Alpha 2"))
        self.alpha2LineEdit.setText(("0.000001"))
        self.lambdaLabel.setText(("Lambda 1"))
        self.lambdaLineEdit.setText(("0.000001"))
        self.lambdaLabel_2.setText(("Lambda 2"))
        self.lambdaLineEdit_2.setText(("0.000001"))
        self.thresholdLambdaLabel.setText(("Threshold Lambda"))
        self.thresholdLambdaLineEdit.setText(("10000"))
        self.fitInterceptLabel.setText(("Fit Intercept"))
        __sortingEnabled = self.fitIntercept_list.isSortingEnabled()
        self.fitIntercept_list.setSortingEnabled(False)
        item = self.fitIntercept_list.item(0)
        item.setText(("True"))
        item = self.fitIntercept_list.item(1)
        item.setText(("False"))
        self.fitIntercept_list.setSortingEnabled(__sortingEnabled)
        self.normalizeLabel.setText(("Normalize"))
        __sortingEnabled = self.normalize_list.isSortingEnabled()
        self.normalize_list.setSortingEnabled(False)
        item = self.normalize_list.item(0)
        item.setText(("True"))
        item = self.normalize_list.item(1)
        item.setText(("False"))
        self.normalize_list.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
