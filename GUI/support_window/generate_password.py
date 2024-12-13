from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from GUI.style.style import CONST_WINDOW
from PyQt6.QtGui import QIcon
from Logic.BaseDir import BD
from GUI.pop_window.pop_window import pop_window
import random
import string

class GeneratePassword(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генерация пароля")
        self.setStyleSheet(CONST_WINDOW)
        self.setWindowIcon(QIcon(r"image\icon.webp"))
        
        control_UI = QVBoxLayout()
        central_windget = QWidget()
        
        platworm_l = QLabel(text="Введите вашу платформу")
        username_l = QLabel(text="Введите ваше имя пользователя")
        
        self.platform = QLineEdit()
        self.username = QLineEdit()
        
        add = QPushButton(text="Добавить генерацию")
        add.clicked.connect(self.generate)
        
        control_UI.addWidget(platworm_l)
        control_UI.addWidget(self.platform)
        control_UI.addWidget(username_l)
        control_UI.addWidget(self.username)
        control_UI.addWidget(add)
        
        central_windget.setLayout(control_UI)
        self.setCentralWidget(central_windget)
        self.show()
        
    def generate(self):
        try:
            plt = self.platform.text()
            un = self.username.text()
            connect = BD()
            
            lowe = string.ascii_lowercase
            upper = string.ascii_uppercase
            num = "0123456789"
            special = "[]}{!@#$%^&*)(~'"
            all_symbol = lowe + upper + num + special
            psw = ''
            
            for i in range(0, 18):
                psw += random.choice(all_symbol)
                
            connect.insert_bd(plt, un, psw)
            
            pop_window("Успех", f"Пароль успешно сгенерирован и добавлен. Пароль: {psw}")
        except:
            pop_window("Ошибка", "Генерация пароля неудачна")