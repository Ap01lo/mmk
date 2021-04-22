from PyQt5              import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets    import *
import sys
from PyQt5.QtCore       import *
from PyQt5.QtGui        import *
import time
from ClassRoomCopy      import *
from AddClassInfo       import *
from DelClassInfo       import *
from CorClassInfo       import *

QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

class Admin(QWidget):
    def __init__(self,username):
        super(Admin, self).__init__()
        self.username = username
        self.setWindowTitle('教室多媒体钥匙管理系统')
        self.setupUi(self)
        self.retranslateUi(self)
        self.c = ClassRoom().ShowAll()
        self.additem()
        
        # 设置时钟动态显示
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start()


    def setupUi(self, Form):
        Form.setObjectName("教室多媒体钥匙管理系统")
        Form.resize(850, 472)
        Form.setFixedSize(855, 472)


        iconpath = 'image/login.ico'
        Icon = QIcon(iconpath)
        self.setWindowIcon(Icon)
        
        # 显示标签
        self.IdLab = QtWidgets.QLabel(Form)
        self.IdLab.setGeometry(QtCore.QRect(20, 120, 71, 21))
        self.IdLab.setObjectName("IdLab")
        self.StatusLab = QtWidgets.QLabel(Form)
        self.StatusLab.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.StatusLab.setObjectName("StatusLab")
        self.TitleLab = QtWidgets.QLabel(Form)
        self.TitleLab.setGeometry(QtCore.QRect(150, 20, 541, 41))
        self.TitleLab.setObjectName("TitleLab")

        # 添加按钮
        self.Add_btn = QPushButton(Form)
        self.Add_btn.setGeometry(QtCore.QRect(760, 110, 80, 30))
        self.Add_btn.setText('添加')
        self.Add_btn.clicked.connect(self.AddInfo)

        # 删除按钮
        self.Del_btn = QPushButton(Form)        
        self.Del_btn.setGeometry(QtCore.QRect(760, 150, 80, 30))
        self.Del_btn.setText('删除')
        self.Del_btn.clicked.connect(self.DelInfo)

        # 修改按钮
        self.Cor_btn = QPushButton(Form)
        self.Cor_btn.setGeometry(QtCore.QRect(760, 190, 80, 30))
        self.Cor_btn.setText('修改')
        self.Cor_btn.clicked.connect(self.CorInfo)
        
        # 审批按钮
        self.Appr_btn = QPushButton(Form)
        self.Appr_btn.setGeometry(QtCore.QRect(760, 230, 80, 30))
        self.Appr_btn.setText('审批')
        self.Appr_btn.clicked.connect(self.ApprInfo)

        # 定义表控件
        self.InfoTable = QtWidgets.QTableWidget(Form)
        self.InfoTable.setSortingEnabled(True)
        self.InfoTable.setGeometry(QtCore.QRect(210, 110, 548, 351))
        self.InfoTable.setObjectName("InfoTable")
        self.InfoTable.setColumnCount(5)
        self.InfoTable.setRowCount(0)
        self.InfoTable.setShowGrid(False)

        # 添加表格
        item = QtWidgets.QTableWidgetItem()
        self.InfoTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.InfoTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.InfoTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.InfoTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.InfoTable.setHorizontalHeaderItem(4, item)

        # 边框线
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 180, 185, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(195, 110, 20, 351))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(20, 100, 185, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(10, 110, 20, 351))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(20, 450, 185, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        # 时间动态显示
        self.TimeLab = QtWidgets.QLabel(Form)
        self.TimeLab.setGeometry(QtCore.QRect(310, 70, 251, 31))
        self.TimeLab.setObjectName("TimeLab")
        # id 显示
        self.IdEdit = QtWidgets.QLabel(Form)
        self.IdEdit.setGeometry(QtCore.QRect(110, 120, 91, 20))
        self.IdEdit.setObjectName("IdEdit")
        # 状态显示
        self.StatusEdit = QtWidgets.QLabel(Form)
        self.StatusEdit.setGeometry(QtCore.QRect(110, 160, 91, 20))
        self.StatusEdit.setObjectName("StatusEdit")

        DuringList = ['8:00~9:35',
                      '9:50~11:25',
                      '13:45~15:20',
                      '15:35~17:10',
                      '18:30~21:00',
                      '任意']

        # 左侧查找布局
        # 教学楼选择
        self.BuldingCombo = QComboBox(Form)
        self.BuldingCombo.setGeometry(QtCore.QRect(21, 230, 80, 30))
        self.BuldingCombo.addItems(['任意','教2','教3','教4'])
        # 楼层选择
        self.FloorCombo = QComboBox(Form)
        self.FloorCombo.setGeometry(QtCore.QRect(121, 230, 80, 30))
        self.FloorCombo.addItems(['任意','1楼','2楼','3楼','4楼'])
        # 时段选择
        self.TimeCombo = QComboBox(Form)
        self.TimeCombo.setGeometry(QtCore.QRect(21, 280, 180, 30))
        self.TimeCombo.addItems(DuringList)


        # 确认按钮
        self.SearchBtn = QPushButton(Form)
        self.SearchBtn.setText('搜索')
        self.SearchBtn.setGeometry(QtCore.QRect(21, 320, 180, 30))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def show_time(self):
        datatime = QDateTime.currentDateTime()
        localtime = datatime.toString()
        self.TimeLab.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">{localtime}</span></p></body></html>")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.IdLab.setText('ID')
        self.StatusLab.setText('status')
        self.TitleLab.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">教室多媒体钥匙管理系统管理端</span></p></body></html>"))

        # 添加横向表头
        item = self.InfoTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.InfoTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "教室"))
        item = self.InfoTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "时段"))
        item = self.InfoTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "容纳人数"))
        item = self.InfoTable.horizontalHeaderItem(4)
        item.setText(_translate("Form", "借出状态"))

        self.IdEdit.setText(_translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">{self.username}</span></p><p align=\"center\"><br/></p></body></html>"))
        self.StatusEdit.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Admin</span></p></body></html>"))

    def additem(self):
        # 添加教室信息
        StatusList = ['可借用','审批中','已借出']
        for i,x in enumerate(self.c):
            self.InfoTable.insertRow(i)
            btn = QPushButton('预定')
            btn.clicked.connect(lambda : self.click_btn(self.InfoTable.currentRow()))

            item = QTableWidgetItem(x['_id'])
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 0, QTableWidgetItem(item))

            item = QTableWidgetItem(x['name'])
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 1, QTableWidgetItem(item))

            item = QTableWidgetItem(str(x['seats']))
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 3, QTableWidgetItem(item))

            item = QTableWidgetItem(x['during'])
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 2, QTableWidgetItem(item))

            item = QTableWidgetItem(str(StatusList[x['status']]))
            item.setTextAlignment(Qt.AlignCenter)
            self.InfoTable.setItem(i, 4, QTableWidgetItem(item))

    def AddInfo(self):
        # 添加
        w = AddClassInfo()
        w.exec()

    def DelInfo(self):
        # 删除
        w = DelClassInfo()
        w.exec()

    def CorInfo(self):
        # 修改
        w = CorClassInfo()
        w.exec()

    def ApprInfo(self):
        # 审批
        print(4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Admin('hha')
    w.show()
    app.exit(app.exec_())