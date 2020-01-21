# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topLayout = QtWidgets.QGridLayout()
        self.topLayout.setObjectName("topLayout")
        self.chooseDataLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseDataLabel.setObjectName("chooseDataLabel")
        self.topLayout.addWidget(self.chooseDataLabel, 0, 0, 1, 1)
        self.chooseDataComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseDataComboBox.setToolTip("")
        self.chooseDataComboBox.setObjectName("chooseDataComboBox")
        self.topLayout.addWidget(self.chooseDataComboBox, 0, 1, 1, 1)
        self.figureNameLabel = QtWidgets.QLabel(self.groupBox)
        self.figureNameLabel.setObjectName("figureNameLabel")
        self.topLayout.addWidget(self.figureNameLabel, 1, 0, 1, 1)
        self.figureNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.figureNameLineEdit.setObjectName("figureNameLineEdit")
        self.topLayout.addWidget(self.figureNameLineEdit, 1, 1, 1, 1)
        self.plotTitleLabel = QtWidgets.QLabel(self.groupBox)
        self.plotTitleLabel.setObjectName("plotTitleLabel")
        self.topLayout.addWidget(self.plotTitleLabel, 2, 0, 1, 1)
        self.plotTitleLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.plotTitleLineEdit.setObjectName("plotTitleLineEdit")
        self.topLayout.addWidget(self.plotTitleLineEdit, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.topLayout)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.XYLayout = QtWidgets.QHBoxLayout()
        self.XYLayout.setObjectName("XYLayout")
        self.xLayout = QtWidgets.QFormLayout()
        self.xLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.xLayout.setObjectName("xLayout")
        self.chooseXVariableLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseXVariableLabel.setObjectName("chooseXVariableLabel")
        self.xLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chooseXVariableLabel)
        self.chooseXVariableComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseXVariableComboBox.setObjectName("chooseXVariableComboBox")
        self.xLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chooseXVariableComboBox)
        self.xTitleLabel = QtWidgets.QLabel(self.groupBox)
        self.xTitleLabel.setObjectName("xTitleLabel")
        self.xLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.xTitleLabel)
        self.xTitleLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.xTitleLineEdit.setObjectName("xTitleLineEdit")
        self.xLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.xTitleLineEdit)
        self.xMinLabel = QtWidgets.QLabel(self.groupBox)
        self.xMinLabel.setObjectName("xMinLabel")
        self.xLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.xMinLabel)
        self.xMaxLabel = QtWidgets.QLabel(self.groupBox)
        self.xMaxLabel.setObjectName("xMaxLabel")
        self.xLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.xMaxLabel)
        self.xMinDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.xMinDoubleSpinBox.setMinimum(-999999999.0)
        self.xMinDoubleSpinBox.setMaximum(999999999.0)
        self.xMinDoubleSpinBox.setObjectName("xMinDoubleSpinBox")
        self.xLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.xMinDoubleSpinBox)
        self.xMaxDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.xMaxDoubleSpinBox.setMinimum(-999999999.0)
        self.xMaxDoubleSpinBox.setMaximum(999999999.0)
        self.xMaxDoubleSpinBox.setObjectName("xMaxDoubleSpinBox")
        self.xLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.xMaxDoubleSpinBox)
        self.XYLayout.addLayout(self.xLayout)
        self.yLayout = QtWidgets.QFormLayout()
        self.yLayout.setObjectName("yLayout")
        self.chooseYVariableLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseYVariableLabel.setObjectName("chooseYVariableLabel")
        self.yLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.chooseYVariableLabel)
        self.chooseYVariableComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseYVariableComboBox.setObjectName("chooseYVariableComboBox")
        self.yLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.chooseYVariableComboBox)
        self.yTitleLabel = QtWidgets.QLabel(self.groupBox)
        self.yTitleLabel.setObjectName("yTitleLabel")
        self.yLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.yTitleLabel)
        self.yTitleLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.yTitleLineEdit.setObjectName("yTitleLineEdit")
        self.yLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.yTitleLineEdit)
        self.yMinLabel = QtWidgets.QLabel(self.groupBox)
        self.yMinLabel.setObjectName("yMinLabel")
        self.yLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.yMinLabel)
        self.yMaxLabel = QtWidgets.QLabel(self.groupBox)
        self.yMaxLabel.setObjectName("yMaxLabel")
        self.yLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.yMaxLabel)
        self.yMinDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.yMinDoubleSpinBox.setMinimum(-999999999.0)
        self.yMinDoubleSpinBox.setMaximum(999999999.0)
        self.yMinDoubleSpinBox.setObjectName("yMinDoubleSpinBox")
        self.yLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yMinDoubleSpinBox)
        self.yMaxDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.yMaxDoubleSpinBox.setObjectName("yMaxDoubleSpinBox")
        self.yLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.yMaxDoubleSpinBox)
        self.XYLayout.addLayout(self.yLayout)
        self.verticalLayout.addLayout(self.XYLayout)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.comboBoxcolorvar = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxcolorvar.setObjectName("comboBoxcolorvar")
        self.gridLayout.addWidget(self.comboBoxcolorvar, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.botLayout = QtWidgets.QGridLayout()
        self.botLayout.setObjectName("botLayout")
        self.oneToOneLabel = QtWidgets.QLabel(self.groupBox)
        self.oneToOneLabel.setObjectName("oneToOneLabel")
        self.botLayout.addWidget(self.oneToOneLabel, 1, 0, 1, 1)
        self.legendLabel = QtWidgets.QLabel(self.groupBox)
        self.legendLabel.setObjectName("legendLabel")
        self.botLayout.addWidget(self.legendLabel, 0, 0, 1, 1)
        self.alphaLabel = QtWidgets.QLabel(self.groupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.botLayout.addWidget(self.alphaLabel, 5, 0, 1, 1)
        self.markerLabel = QtWidgets.QLabel(self.groupBox)
        self.markerLabel.setObjectName("markerLabel")
        self.botLayout.addWidget(self.markerLabel, 4, 0, 1, 1)
        self.alphaDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.alphaDoubleSpinBox.setObjectName("alphaDoubleSpinBox")
        self.botLayout.addWidget(self.alphaDoubleSpinBox, 5, 1, 1, 1)
        self.plotFilenameLabel = QtWidgets.QLabel(self.groupBox)
        self.plotFilenameLabel.setObjectName("plotFilenameLabel")
        self.botLayout.addWidget(self.plotFilenameLabel, 6, 0, 1, 1)
        self.lineComboBox = QtWidgets.QComboBox(self.groupBox)
        self.lineComboBox.setObjectName("lineComboBox")
        self.botLayout.addWidget(self.lineComboBox, 3, 1, 1, 1)
        self.lineLabel = QtWidgets.QLabel(self.groupBox)
        self.lineLabel.setObjectName("lineLabel")
        self.botLayout.addWidget(self.lineLabel, 3, 0, 1, 1)
        self.plotFilenameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.plotFilenameLineEdit.setReadOnly(True)
        self.plotFilenameLineEdit.setObjectName("plotFilenameLineEdit")
        self.botLayout.addWidget(self.plotFilenameLineEdit, 6, 1, 1, 1)
        self.colorComboBox = QtWidgets.QComboBox(self.groupBox)
        self.colorComboBox.setObjectName("colorComboBox")
        self.botLayout.addWidget(self.colorComboBox, 2, 1, 1, 1)
        self.colorLabel = QtWidgets.QLabel(self.groupBox)
        self.colorLabel.setObjectName("colorLabel")
        self.botLayout.addWidget(self.colorLabel, 2, 0, 1, 1)
        self.markerComboBox = QtWidgets.QComboBox(self.groupBox)
        self.markerComboBox.setObjectName("markerComboBox")
        self.botLayout.addWidget(self.markerComboBox, 4, 1, 1, 1)
        self.plotFilenamePushButton = QtWidgets.QPushButton(self.groupBox)
        self.plotFilenamePushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.plotFilenamePushButton.setObjectName("plotFilenamePushButton")
        self.botLayout.addWidget(self.plotFilenamePushButton, 6, 2, 1, 1)
        self.legendLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.legendLineEdit.setObjectName("legendLineEdit")
        self.botLayout.addWidget(self.legendLineEdit, 0, 1, 1, 1)
        self.oneToOneCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.oneToOneCheckBox.setText("")
        self.oneToOneCheckBox.setObjectName("oneToOneCheckBox")
        self.botLayout.addWidget(self.oneToOneCheckBox, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.botLayout)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.chooseDataComboBox, self.figureNameLineEdit)
        Form.setTabOrder(self.figureNameLineEdit, self.plotTitleLineEdit)
        Form.setTabOrder(self.plotTitleLineEdit, self.chooseXVariableComboBox)
        Form.setTabOrder(self.chooseXVariableComboBox, self.xTitleLineEdit)
        Form.setTabOrder(self.xTitleLineEdit, self.xMinDoubleSpinBox)
        Form.setTabOrder(self.xMinDoubleSpinBox, self.xMaxDoubleSpinBox)
        Form.setTabOrder(self.xMaxDoubleSpinBox, self.chooseYVariableComboBox)
        Form.setTabOrder(self.chooseYVariableComboBox, self.yTitleLineEdit)
        Form.setTabOrder(self.yTitleLineEdit, self.yMinDoubleSpinBox)
        Form.setTabOrder(self.yMinDoubleSpinBox, self.yMaxDoubleSpinBox)
        Form.setTabOrder(self.yMaxDoubleSpinBox, self.legendLineEdit)
        Form.setTabOrder(self.legendLineEdit, self.oneToOneCheckBox)
        Form.setTabOrder(self.oneToOneCheckBox, self.colorComboBox)
        Form.setTabOrder(self.colorComboBox, self.lineComboBox)
        Form.setTabOrder(self.lineComboBox, self.markerComboBox)
        Form.setTabOrder(self.markerComboBox, self.alphaDoubleSpinBox)
        Form.setTabOrder(self.alphaDoubleSpinBox, self.plotFilenameLineEdit)
        Form.setTabOrder(self.plotFilenameLineEdit, self.plotFilenamePushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Plot"))
        self.chooseDataLabel.setText(("Choose data"))
        self.figureNameLabel.setText(("Figure name"))
        self.plotTitleLabel.setText(("Plot Title"))
        self.chooseXVariableLabel.setText(("Choose X Variable"))
        self.xTitleLabel.setText(("X title"))
        self.xMinLabel.setText(("X min"))
        self.xMaxLabel.setText(("X max"))
        self.chooseYVariableLabel.setText(("Choose Y Variable"))
        self.yTitleLabel.setText(("Y title"))
        self.yMinLabel.setText(("Y min"))
        self.yMaxLabel.setText(("Y max"))
        self.label.setText(("Choose variable to color code points (optional)"))
        self.oneToOneLabel.setText(("One to One"))
        self.legendLabel.setText(("Legend"))
        self.alphaLabel.setText(("Opacity"))
        self.markerLabel.setText(("Marker"))
        self.plotFilenameLabel.setText(("Plot Filename"))
        self.lineLabel.setText(("Line"))
        self.colorLabel.setText(("Color"))
        self.plotFilenamePushButton.setText(("..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

