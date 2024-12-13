from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from GUI.style.style import CONST_WINDOW
from PyQt6.QtGui import QIcon
from Logic.BaseDir import BD
from GUI.pop_window.pop_window import pop_window

class SaveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сохрание пароля")
        self.setStyleSheet(CONST_WINDOW)
        self.setWindowIcon(QIcon(r"image\icon.webp"))
        
        control_UI = QVBoxLayout()
        central_windget = QWidget()
        
        platworm_l = QLabel(text="Введите вашу платформу")
        username_l = QLabel(text="Введите ваше имя пользователя")
        password_l = QLabel(text="Введите ваш пароль")
        
        self.platform = QLineEdit()
        self.username = QLineEdit()
        self.password = QLineEdit()
        
        add = QPushButton(text="Добавить пароль")
        add.clicked.connect(self.add_password)
        
        control_UI.addWidget(platworm_l)
        control_UI.addWidget(self.platform)
        control_UI.addWidget(username_l)
        control_UI.addWidget(self.username)
        control_UI.addWidget(password_l)
        control_UI.addWidget(self.password)
        control_UI.addWidget(add)
        
        central_windget.setLayout(control_UI)
        self.setCentralWidget(central_windget)
        self.show()
        
    def add_password(self):
        control = BD()
        
        try:
            plt = self.platform.text()
            un = self.username.text()
            psw = self.password.text()
            
            control.insert_bd(plt, un, psw)
            pop_window("Успех", "Пароль успешно сохранен")
        except:
            pop_window("Неудача", "Пароль не был сохранен")
            