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
        self.alphaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.alphaLabel)
        self.alphaLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.alphaLineEdit.setObjectName("alphaLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.alphaLineEdit)
        self.kernelLabel = QtWidgets.QLabel(self.formGroupBox)
        self.kernelLabel.setObjectName("kernelLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.kernelLabel)
        self.gammaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.gammaLabel.setObjectName("gammaLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.gammaLabel)
        self.gammaLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.gammaLineEdit.setObjectName("gammaLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gammaLineEdit)
        self.degreeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.degreeLabel.setObjectName("degreeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.degreeLabel)
        self.degreeLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.degreeLineEdit.setProperty("maximum", 9999999.0)
        self.degreeLineEdit.setProperty("value", 3.0)
        self.degreeLineEdit.setObjectName("degreeLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.degreeLineEdit)
        self.coeff0Label = QtWidgets.QLabel(self.formGroupBox)
        self.coeff0Label.setObjectName("coeff0Label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.coeff0Label)
        self.coeff0LineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.coeff0LineEdit.setProperty("maximum", 9999999.0)
        self.coeff0LineEdit.setProperty("value", 1.0)
        self.coeff0LineEdit.setObjectName("coeff0LineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.coeff0LineEdit)
        self.kernelParametersLabel = QtWidgets.QLabel(self.formGroupBox)
        self.kernelParametersLabel.setObjectName("kernelParametersLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.kernelParametersLabel)
        self.kernelParametersLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.kernelParametersLineEdit.setObjectName("kernelParametersLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.kernelParametersLineEdit)
        self.kernel_list = QtWidgets.QListWidget(self.formGroupBox)
        self.kernel_list.setMaximumSize(QtCore.QSize(16777215, 100))
        self.kernel_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.kernel_list.setObjectName("kernel_list")
        item = QtWidgets.QListWidgetItem()
        self.kernel_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.kernel_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.kernel_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.kernel_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.kernel_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.kernel_list.addItem(item)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kernel_list)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.alphaLabel.setText(("Alpha"))
        self.kernelLabel.setText(("Kernel"))
        self.gammaLabel.setText(("Gamma"))
        self.gammaLineEdit.setText(("None"))
        self.degreeLabel.setText(("Degree"))
        self.coeff0Label.setText(("Coeff 0"))
        self.kernelParametersLabel.setText(("Kernel Parameters"))
        self.kernelParametersLineEdit.setText(("None"))
        __sortingEnabled = self.kernel_list.isSortingEnabled()
        self.kernel_list.setSortingEnabled(False)
        item = self.kernel_list.item(0)
        item.setText(("Linear"))
        item = self.kernel_list.item(1)
        item.setText(("Radial Basis Function"))
        item = self.kernel_list.item(2)
        item.setText(("Polynomial"))
        item = self.kernel_list.item(3)
        item.setText(("Sigmoid"))
        item = self.kernel_list.item(4)
        item.setText(("Laplacian"))
        item = self.kernel_list.item(5)
        item.setText(("Chi-Squared"))
        self.kernel_list.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
