from PyQt5 import QtCore, QtGui, QtWidgets

from graphic import draw_graphic


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(199, 310)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(199, 310))
        MainWindow.setMaximumSize(QtCore.QSize(199, 310))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 161, 54))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.buttons_area = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.buttons_area.setContentsMargins(0, 0, 0, 0)
        self.buttons_area.setObjectName("buttons_area")
        self.bisectionMethodButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bisectionMethodButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bisectionMethodButton.setCheckable(False)
        self.bisectionMethodButton.setObjectName("bisectionMethodButton")
        self.buttons_area.addWidget(self.bisectionMethodButton)
        self.iterationMethodButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.iterationMethodButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.iterationMethodButton.setMouseTracking(False)
        self.iterationMethodButton.setObjectName("iterationMethodButton")
        self.buttons_area.addWidget(self.iterationMethodButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 160, 86))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.input_area = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.input_area.setContentsMargins(0, 0, 0, 0)
        self.input_area.setObjectName("input_area")
        self.left_border_text = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.left_border_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.left_border_text.setAlignment(QtCore.Qt.AlignCenter)
        self.left_border_text.setObjectName("left_border_text")
        self.input_area.addWidget(self.left_border_text)
        self.left_border = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.left_border.setMinimum(-99)
        self.left_border.setObjectName("left_border")
        self.input_area.addWidget(self.left_border)
        self.right_border_text = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.right_border_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.right_border_text.setAlignment(QtCore.Qt.AlignCenter)
        self.right_border_text.setObjectName("right_border_text")
        self.input_area.addWidget(self.right_border_text)
        self.right_border = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.right_border.setMinimum(-99)
        self.right_border.setObjectName("right_border")
        self.input_area.addWidget(self.right_border)
        self.background = QtWidgets.QWidget(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 199, 310))
        self.background.setMaximumSize(QtCore.QSize(199, 310))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("background-color: rgb(72, 72, 72);")
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.background)
        self.label.setGeometry(QtCore.QRect(20, 210, 161, 81))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.background.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.click_handler()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "root searcher"))
        self.bisectionMethodButton.setText(_translate("MainWindow", "Метод бисекций"))
        self.iterationMethodButton.setText(_translate("MainWindow", "Метод итераций"))
        self.left_border_text.setText(_translate("MainWindow", "Левая граница"))
        self.right_border_text.setText(_translate("MainWindow", "Правая граница"))

    def click_handler(self):
        self.bisectionMethodButton.clicked.connect(lambda ch, method='bisections': self.search_roots(method))
        self.iterationMethodButton.clicked.connect(lambda ch, method='iteratons': self.search_roots(method))

    def search_roots(self, method):
        if method == 'bisections':
            from methods.bisection_method import get_root, function
        elif method == 'iteratons':
            from methods.iteration_method import get_root, function

        a = self.left_border.value()
        b = self.right_border.value()
        left = a
        eps = 1e-6

        roots = []
        iter_counter = 0

        while result := get_root(left, b, eps):
            left = result['root'] + eps
            iter_counter += result['iter_counter']
            flag = False

            for root in roots:
                if round(root, 6) == round(result['root'], 6):
                    flag = True
                    break
            if flag:
                break

            roots.append(result['root'])

        if len(roots) != 0:
            roots_str = ',\n'.join([str(root) for root in roots])
            text = f'Корни:\n {roots_str}, \nКоличество итераций: {iter_counter}'
        else:
            text = 'На заданном промежутке \nкорни отсутсвуют'

        self.label.setText(text)

        draw_graphic(a, b, function)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
