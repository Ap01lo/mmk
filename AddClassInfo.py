from PyQt5.QtWidgets    import *
from PyQt5.QtGui    import *
from PyQt5.QtCore   import *
from Match          import *
from ClassRoomCopy  import *
import sys

class AddClassInfo(QDialog):
    def __init__(self):
        super(AddClassInfo,self).__init__()
        self.setWindowTitle('增加教室数据')
        self.setFixedSize(250, 100)
        self.widget()
        self.setting()
    
    def widget(self):
        self.label_id = QLabel('id')
        self.label_people = QLabel('人数')
        self.edit_id = QLineEdit()
        self.edit_people = QLineEdit()
        self.btn_confirm = QPushButton('确认添加')

    def setting(self):
        layout = QGridLayout()

        self.label_id.setAlignment(Qt.AlignCenter)
        self.label_people.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(self.label_id, 0, 0, 1, 1)
        layout.addWidget(self.label_people, 1, 0, 1, 1)
        layout.addWidget(self.edit_id, 0, 1, 1, 2)
        layout.addWidget(self.edit_people, 1, 1, 1, 2)
        layout.addWidget(self.btn_confirm, 2, 1, 1, 1)
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AddClassInfo()
    w.show()
    sys.exit(app.exec_())