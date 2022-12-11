from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, \
    QBoxLayout, QVBoxLayout, QDateEdit, QDateTimeEdit, QAbstractSpinBox, QCalendarWidget

from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtGui import QIcon
import sys

class data_entry_application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nusery Logs")
        self.setWindowIcon(QIcon("/Users/Parit/Downloads/nursery.png"))
        self.setMinimumWidth(1200)

        self.thelayout = QVBoxLayout()
        self.thelayout.setSpacing(20)
        self.setLayout(self.thelayout)

        self.inituserinterface()

    def inituserinterface(self):
        partoflayout = {}
if __name__ == "__main__":
    application = QApplication(sys.argv)
    application.setStyleSheet('''

        QWidget {
            font-size: 30px;
        }      
      ''')

    my_application = data_entry_application()
    my_application.show()

    try:
        sys.exit(application.exec_())
    except:
        print("Closing Window")