# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *  # PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from get_mouse.get_mouse_pos_ui import *  # 导入designer工具生成的login模块
from PyQt5.QtCore import *
import pyautogui


class BackendThread(QThread):
    update_date = pyqtSignal(str)  # 通过类成员对象定义信号

    # 处理业务逻辑
    def run(self):
        while True:
            x, y = pyautogui.position()
            res = "X: " + str(x) + ", Y: " + str(y)
            self.update_date.emit(str(res))


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setWindowTitle("MainWindow")
        self.setupUi(self)

    def initUI(self):
        self.backend = BackendThread()  # 创建线程
        self.backend.update_date.connect(self.handleDisplay)  # 连接信号
        self.backend.start()  # 开始线程

    def handleDisplay(self, data):
        cursor = self.QTextEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        self.QTextEdit.setText(data)
        # cursor.insertText(data + '\n')
        # self.QTextEdit.setTextCursor(cursor)
        # self.QTextEdit.ensureCursorVisible()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    myWin = MyMainForm()
    myWin.initUI()
    myWin.show()
    sys.exit(app.exec())
