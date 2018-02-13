import pandas as pd
from PyQt5 import QtWidgets
from libpysat.spectral.spectral_data import spectral_data

from point_spectra_gui.ui.LoadData import Ui_loadData
from point_spectra_gui.util.Modules import Modules


class LoadData(Ui_loadData, Modules):
    count = -1

    def __init__(self):
        LoadData.count += 1
        self.curr_count = LoadData.count
        print('Added LoadData with ID {}'.format(self.curr_count))

    def __del__(self):
        LoadData.count -= 1
        del self.datakeys[-1] # delete last item on the list
        pass

    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.newFilePushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.fileNameLineEdit))

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Data File", self.outpath, "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def setup(self):
        try:
            filename = self.fileNameLineEdit.text()
            keyname = self.dataSetNameLineEdit.text()
            print('Loading data file: ' + str(filename))
            self.data[keyname] = spectral_data(pd.read_csv(filename, header=[0, 1], verbose=True, nrows=2))
            self.list_amend(self.datakeys, self.curr_count, keyname)
        except:
            pass

    def run(self):
        filename = self.fileNameLineEdit.text()
        keyname = self.dataSetNameLineEdit.text()
        print('Loading data file: ' + str(filename))
        # if keyname in self.datakeys:
        #     raise Exception("That data set name is already in use. Try something else.")
        # else:
        self.data[keyname] = spectral_data(pd.read_csv(filename, header=[0, 1], verbose=True))
        self.list_amend(self.datakeys, self.curr_count, keyname)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = LoadData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
