from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon
from GUI.style.style import CONST_SEARCH_WINDOW
from GUI.pop_window.pop_window import pop_window
from Logic.BaseDir import BD

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поиск пароля")
        self.setWindowIcon(QIcon(r"image\icon.webp"))
        self.setStyleSheet(CONST_SEARCH_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        text = QLabel(text="Введите название платформы")
        self.enter = QLineEdit()
        srh = QPushButton(text="Найти пароль")
        srh.clicked.connect(self.search)
        
        control_UI.addWidget(text)
        control_UI.addWidget(self.enter)
        control_UI.addWidget(srh)
        
        central_widget.setLayout(control_UI)
        self.setCentralWidget(central_widget)
        self.show()
        
    def search(self):
        try:
            plt = self.enter.text()
            sh = False
            psw = ''
            
            control = BD()
            data = control.all_table()
            
            for i in range(len(data)):
                if str(data[i][1]).lower() == plt.lower():
                    psw += data[i][3]
                    sh = True
                    break
                
            if sh == True:
                pop_window("Успех", f"Элимент найден. Ваш пароль: {psw}")
            else:
                pop_window("Неудача", "Возможно вы ввели неправильно название платформы")
        except:
            pop_window("Ошибка", "Нужный вам пароль не найден")