
from PyQt5.QtWidgets    import *
from PyQt5.QtGui    import *
from PyQt5.QtCore   import *
from ClassRoomCopy  import *
import sys
from User2ClassRoom import *

class Info(QDialog):
    def __init__(self,username):
        super(Info,self).__init__()
        self.username = username
        self.setFixedSize(400,300)
        self.setWindowTitle('已借用')
        self.initUI()
        self.addItem()

    def initUI(self):
        layout = QFormLayout()
        self.Appr_list = QListWidget()
        # self.Appr_list.itemDoubleClicked.connect(self.appr)
        layout.addWidget(self.Appr_list)
        self.setLayout(layout)

    def addItem(self):
        self.u = User2ClassRoom().ShowAll()
        StatusList = ["可借用","审批中","已借出"]
        title = '借用者'.center(14,' ')+'事件'.center(14,' ')+'教室'.center(13,' ')+'时段'.center(25,' ')+'状态'
        item = QListWidgetItem(title)
        self.Appr_list.addItem(item)
        for x in self.u:
            l = ClassRoom(x['_id']).PullClassroom()
            if x['user_id'] == self.username:
                line = x['user_id'].ljust(14,' ') + l.id.ljust(12,' ') + l.name.ljust(12,' ') + l.during.ljust(20,' ')+StatusList[l.status]
                item = QListWidgetItem(line)
                # item.setTextAlignment(Qt.AlignCenter)
                self.Appr_list.addItem(item)

    # def appr(self):
        # info = self.Appr_list.currentItem().text()
        # _id = info[14:21]
        # c = ClassRoom(_id).PullClassroom()
        # ClassRoom(_id,c.seats,status=0).PushClassroom()
        # User2ClassRoom(_id).Delete()
        # curItem = self.Appr_list.currentRow()
        # self.Appr_list.takeItem(curItem)
        # QMessageBox.information(self, '归还结果', '已经成功归还!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ApprInfo()
    w.exec()