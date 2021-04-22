from PyQt5.QtWidgets    import *
from PyQt5.QtGui    import *
from PyQt5.QtCore   import *
from Match          import *
from ClassRoomCopy  import *
import sys

class CorClassInfo(QDialog):
    def __init__(self):
        super(CorClassInfo,self).__init__()
        self.setWindowTitle('增加教室数据')
        self.setFixedSize(250, 140)
        self.widget()
        self.setting()
    
    def widget(self):
        self.label_id = QLabel('id')
        self.label_people = QLabel('人数')
        self.label_status = QLabel('状态')
        self.edit_id = QLineEdit()
        self.edit_people = QLineEdit()
        self.edit_status = QLineEdit()
        self.btn_confirm = QPushButton('确认修改')

    def setting(self):
        layout = QGridLayout()

        self.label_id.setAlignment(Qt.AlignCenter)
        self.label_people.setAlignment(Qt.AlignCenter)
        self.label_status.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(self.label_id, 0, 0, 1, 1)
        layout.addWidget(self.label_people, 1, 0, 1, 1)
        layout.addWidget(self.label_status, 2, 0, 1, 1)


        layout.addWidget(self.edit_id, 0, 1, 1, 2)
        layout.addWidget(self.edit_people, 1, 1, 1, 2)
        layout.addWidget(self.edit_status, 2, 1, 1, 2)
        layout.addWidget(self.btn_confirm, 3, 1, 1, 1)
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CorClassInfo()
    w.show()
    sys.exit(app.exec_())