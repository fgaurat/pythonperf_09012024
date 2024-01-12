from main_table_window import Ui_mainWindow
from PySide6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from UserDAO import UserDAO

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self,dao:UserDAO):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.__dao = dao
        self.load_data()

    def load_data(self):
        users = list(self.__dao.findAll())
        self.tableWidget.setRowCount(len(users))
        
        for row_number,user in enumerate(users):
            self.tableWidget.setItem(row_number,0,QTableWidgetItem(str(user.id)))
            self.tableWidget.setItem(row_number,1,QTableWidgetItem(str(user.last_name)))
            self.tableWidget.setItem(row_number,2,QTableWidgetItem(str(user.first_name)))
            self.tableWidget.setItem(row_number,3,QTableWidgetItem(str(user.email)))

def main():
    app = QApplication([])
    dao = UserDAO('./formation.db')
    window = MainWindow(dao)
    window.show()
    app.exec()
if __name__ == '__main__':
    main()

