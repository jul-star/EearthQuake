from PySide2.QtCore import SIGNAL
from PySide2.QtCore import (QPointF)
from PySide2.QtWidgets import (QMainWindow, QAction, QApplication, QFileDialog)
from PySide2.QtCharts import (QtCharts)
import logging

from FileParser import FileParser


class MainView(QMainWindow):
    def __init__(self, _app: QApplication):
        QMainWindow.__init__(self)

        self.app = _app
        self.status = self.statusBar()
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        self.chartView = QtCharts.QChartView()

        self.SetViewGeometry()
        self.setWindowTitle('EearthQuake: my first App with PySide2')
        self.InitWidgets()

    def InitCentralWidget(self):
        self.setCentralWidget(self.chartView)

    def InitWidgets(self):
        self.InitMenuBar()
        self.InitStatusBar()
        self.InitCentralWidget()

    def InitStatusBar(self):
        self.status.showMessage('Data loaded and plotted')

    def InitMenuBar(self):
        file_read = QAction("Load data", self)
        file_read.triggered.connect(lambda: self.ShowFileContent())
        self.file_menu.addAction(file_read)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(lambda: self.close())
        self.file_menu.addAction(exit_action)

    def SetViewGeometry(self):
        geometry = self.app.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)

    def OpenFileDialog(self) -> tuple:
        file_name: tuple = QFileDialog.getOpenFileName(self,
                                                       self.app.tr('Open Data Files'),
                                                       "../data",
                                                       self.app.tr('CSV Files (*.csv )'));
        return file_name

    def ShowFileContent(self):
        file_name = self.OpenFileDialog()
        logging.warning('FileName:{}'.format(file_name))
        date, magnitude = FileParser.GetMagnitudeTime(FileParser.Read4File(file_name[0]))
        qListP = []
        for i in range(len(date)):
            qListP.append(QPointF(i, magnitude[i]))
        series = QtCharts.QLineSeries()
        series.append(qListP)
        self.chartView.chart().removeAllSeries()
        self.chartView.chart().addSeries(series)
        self.chartView.chart().createDefaultAxes()
        self.chartView.show()
