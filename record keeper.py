from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout, QDateEdit

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon

import sys 
import csv

class data_entry_application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nursery Logs")
        self.setWindowIcon(QIcon("nursery.png"))
        self.setMinimumWidth(1200)

        self.thelayout = QVBoxLayout()
        self.thelayout.setSpacing(20)
        self.setLayout(self.thelayout)

        self.inituserinterface()

        self.reset()



    def inituserinterface(self):
        partoflayout = {}
        
        partoflayout["DateTime"] = QHBoxLayout()
        self.thelayout.addLayout(partoflayout["DateTime"])

        self.birth_date = QLabel("Birth Date: ")
        self.edit_date = QDateEdit()
        self.edit_date.setCalendarPopup(True)

        self.label_nationality = QLabel("Nationality: ")
        self.edit_nationality = QLineEdit()

        partoflayout["DateTime"].addWidget(self.birth_date, 0, alignment=Qt.AlignRight)
        partoflayout["DateTime"].addWidget(self.edit_date, 5)
        partoflayout["DateTime"].addWidget(self.label_nationality, 0, alignment=Qt.AlignRight)
        partoflayout["DateTime"].addWidget(self.edit_nationality, 5)

        partoflayout["names"] = QHBoxLayout()
        self.thelayout.addLayout(partoflayout["names"])

        self.labelguardian_name = QLabel("Guardian's Name: ")
        self.edit_guardian_name = QLineEdit()

        self.labelchild_name = QLabel("Child's Name: ")
        self.edit_child_name = QLineEdit()

        partoflayout["names"].addWidget(self.labelguardian_name, 0, alignment=Qt.AlignRight)
        partoflayout["names"].addWidget(self.edit_guardian_name, 5)
        partoflayout["names"].addWidget(self.labelchild_name, 0, alignment=Qt.AlignRight)
        partoflayout["names"].addWidget(self.edit_child_name, 5)

        partoflayout["tuition"] = QHBoxLayout()
        self.thelayout.addLayout(partoflayout["tuition"])

        self.amount = QLabel("Number of Months: ")
        self.months_attending = QLineEdit()
        self.months_attending.returnPressed.connect(self.tuitioncost)

        self.fee = QLabel("Tuition Fee:")
        self.cost = QLabel()
        self.cost.setText("--> Enter Amount of Months (5000 THB/Month)")
        
        partoflayout["tuition"].addWidget(self.amount, 0, alignment=Qt.AlignRight)
        partoflayout["tuition"].addWidget(self.months_attending, 5)
        partoflayout["tuition"].addWidget(self.fee, 0, alignment=Qt.AlignRight)
        partoflayout["tuition"].addWidget(self.cost, 5)
        
        partoflayout["buttons"] = QHBoxLayout()
        self.thelayout.addLayout(partoflayout["buttons"])

        enterbutton = QPushButton("Enter", clicked=self.adding_entry)
        partoflayout["buttons"].addWidget(enterbutton)

        resetbutton = QPushButton("Reset", clicked=self.reset)
        partoflayout["buttons"].addWidget(resetbutton)

        closebutton = QPushButton("Exit")
        closebutton.clicked.connect(application.quit)
        partoflayout["buttons"].addWidget(closebutton)

        self.status = QLabel()
        self.status.setStyleSheet("""  
            font-size: 23px;
            color: #282C34;
        """)
        

    def tuitioncost(self):
        value = self.months_attending.text()
        integer = int(value) * 5000
        self.cost.setText(f"{integer} THB")

    def reset(self):
        self.edit_date.setDate(QDate.currentDate())
        self.edit_child_name.clear()
        self.edit_nationality.clear()
        self.edit_guardian_name.clear()
        self.amount.clear()
        self.cost.setText("--> Enter Amount of Months (5000 THB/Month)")
    def adding_entry(self):
        records = [
            self.edit_date.text(),
            self.edit_nationality.text(),
            self.edit_guardian_name.text(),
            self.edit_child_name.text(),
            self.months_attending.text(),
            self.cost.text()
        ]

        self.reset()

        print(records)

        with open(r"/Users/Parit/Desktop/PyP/PyP/naharuethaibabyhome.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(records)
            
if __name__ == "__main__":
    application = QApplication(sys.argv)
    application.setStyleSheet('''

        QWidget {
            font-size: 15px;
        }      
      ''')

    my_application = data_entry_application()
    my_application.show()

    try:
        sys.exit(application.exec_())
    except:
        print("Closing Window")