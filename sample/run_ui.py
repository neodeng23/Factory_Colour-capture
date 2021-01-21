# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *  # PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtCore import *
from get_pos_config import *
from get_color import *
import datetime, time
import os
from main_ui import *


class BackendThread(QThread):
    update_date = pyqtSignal(str)

    # 处理业务逻辑
    def run(self):
        while True:
            pic_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"
            img_path = "/Users/" + current_user + "/Desktop/pic/" + pic_name
            os.system("screencapture -x /Users/" + current_user + "/Desktop/pic/" + pic_name)
            x, y = get_win_pos()
            time.sleep(0.3)
            img = Image.open(img_path)
            if x != 9999 and y != 9999:
                for unit in ["A", "B", "C", "D"]:
                    x1, x2, y1, y2 = get_channel_config(unit, x, y)
                    image = img.crop((x1, y1, x2, y2))  # (left, upper, right, lower)
                    image = image.convert('RGB')
                    text = get_text(image)
                    (r, g, b) = get_dominant_color(image)
                    color = recognize_color(r, g, b)
                    #print(color)
                    if unit == "A":

                        myWin.lineEdit.setText("A : " + text + " " + color)
                        if color == "Red":
                            myWin.label.setStyleSheet(m_red_SheetStyle)
                        elif color == "Green":
                            myWin.label.setStyleSheet(m_green_SheetStyle)
                        else:
                            myWin.label.setStyleSheet(m_grey_SheetStyle)

                    if unit == "B":

                        myWin.lineEdit_2.setText("B : " + text + " " + color)
                        if color == "Red":
                            myWin.label_2.setStyleSheet(m_red_SheetStyle)
                        elif color == "Green":
                            myWin.label_2.setStyleSheet(m_green_SheetStyle)
                        else:
                            myWin.label_2.setStyleSheet(m_grey_SheetStyle)

                    if unit == "C":
                        myWin.lineEdit_3.setText("C : " + text + " " + color)
                        if color == "Red":
                            myWin.label_3.setStyleSheet(m_red_SheetStyle)
                        elif color == "Green":
                            myWin.label_3.setStyleSheet(m_green_SheetStyle)
                        else:
                            myWin.label_3.setStyleSheet(m_grey_SheetStyle)

                    if unit == "D":
                        # image.save("/Users/" + current_user + "/Desktop/pic/" + pic_name + ".png")
                        myWin.lineEdit_4.setText("D : " + text + " " + color)
                        if color == "Red":
                            myWin.label_4.setStyleSheet(m_red_SheetStyle)
                        elif color == "Green":
                            myWin.label_4.setStyleSheet(m_green_SheetStyle)
                        else:
                            myWin.label_4.setStyleSheet(m_grey_SheetStyle)

            else:
                # myWin.label.setStyleSheet(m_grey_SheetStyle)
                # myWin.label_2.setStyleSheet(m_grey_SheetStyle)
                # myWin.label_3.setStyleSheet(m_grey_SheetStyle)
                # myWin.label_4.setStyleSheet(m_grey_SheetStyle)
                myWin.lineEdit.setText("")
                myWin.lineEdit_2.setText("")
                myWin.lineEdit_3.setText("")
                myWin.lineEdit_4.setText("")
            # os.system("rm /Users/" + current_user + "/Desktop/pic/" + pic_name)


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setWindowTitle("MainWindow")
        self.setupUi(self)

    def initUI(self):
        self.backend = BackendThread()  # 创建线程
        #self.backend.update_date.connect(self.handleDisplay)  # 连接信号
        self.backend.start()  # 开始线程


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    myWin = MyMainForm()
    myWin.initUI()
    myWin.show()
    sys.exit(app.exec())
