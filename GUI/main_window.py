from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from GUI.style.style import CONST_MAIN_WINDOW
from GUI.support_window.save_password import SaveWindow
from GUI.support_window.generate_password import GeneratePassword
from Logic.BaseDir import BD
import csv
from GUI.pop_window.pop_window import pop_window
from GUI.support_window.password_search import SearchWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер паролей")
        self.setStyleSheet(CONST_MAIN_WINDOW)
        self.setWindowIcon(QIcon(r"image\icon.webp"))
        
        self.save = None
        self.generate = None
        self.search = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        text = QLabel(text="Выберите действие")
        
        creating_a_record = QPushButton(text="Сохранить пароль")
        creating_a_record.clicked.connect(self.save_window)
        
        generate_password = QPushButton(text="Сгенерировать пароль")
        generate_password.clicked.connect(self.generate_window)
        
        see_all_passwords = QPushButton(text="Просмотр паролей")
        see_all_passwords.clicked.connect(self.all_see)
        
        find_the_password = QPushButton(text="Найти пароль по платформе")
        find_the_password.clicked.connect(self.search_window)
        
        control_UI.addWidget(text, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(creating_a_record)
        control_UI.addWidget(generate_password)
        control_UI.addWidget(see_all_passwords)
        control_UI.addWidget(find_the_password)
        
        central_widget.setLayout(control_UI)
        self.setCentralWidget(central_widget)
        self.show()
        
    def save_window(self):
        self.save = SaveWindow()
        
    def generate_window(self):
        self.generate = GeneratePassword()
        
    def all_see(self):
        try:
            path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", '', "CSV Files (*.csv)")
        
            with open(path, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(["id", "platform", "username", "password"])
        
            see_rec = BD()
        
            data = see_rec.all_table()
        
            for i in range(len(data)):
                temp = list(data[i])
            
                with open(path, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(temp)
            pop_window("Успех", "Мы успешно запсали данные в файл")
        except:
            pop_window("Ошибка", "Запись паролей провалена")
            
    def search_window(self):
        self.search = SearchWindow()