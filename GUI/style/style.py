CONST_MAIN_WINDOW = """
QMainWindow {
    background-color: #121212;
    font-family: 'Arial', sans-serif;
    color: #ffffff;
}

QLabel {
    font-size: 22px;
    font-weight: bold;
    color: #ffffff;
    text-align: center;
    margin-bottom: 20px;
}

QPushButton {
    background-color: #333333;
    border: 2px solid #555555;
    border-radius: 8px;
    color: #ffffff;
    font-size: 16px;
    padding: 12px;
    cursor: pointer;
    transition: background-color 0.3s;
}

QPushButton:hover {
    background-color: #555555;
}

QVBoxLayout {
    margin: 30px;
    spacing: 12px;
}

QWidget#centralwidget {
    background-color: #1c1c1c;
    padding: 30px;
    border-radius: 10px;
}
"""


CONST_WINDOW = """
QMainWindow {
    background-color: #121212;
    font-family: 'Arial', sans-serif;
    color: #ffffff;
}

QLabel {
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    margin-bottom: 10px;
}

QLineEdit {
    background-color: #1c1c1c;
    border: 2px solid #333333;
    border-radius: 5px;
    color: #ffffff;
    padding: 8px;
    font-size: 16px;
    margin-bottom: 15px;
}

QPushButton {
    background-color: #333333;
    border: 2px solid #555555;
    border-radius: 8px;
    color: #ffffff;
    font-size: 16px;
    padding: 12px;
    cursor: pointer;
    transition: background-color 0.3s;
}

QPushButton:hover {
    background-color: #555555;
}

QVBoxLayout {
    margin: 30px;
    spacing: 12px;
}

QWidget#centralwidget {
    background-color: #1c1c1c;
    padding: 30px;
    border-radius: 10px;
}
"""


CONST_POPUP_WINDOW = """
QMessageBox {
    background-color: #1c1c1c;
    font-family: 'Arial', sans-serif;
    color: #ffffff;
}

QMessageBox QLabel {
    font-size: 18px;
    font-weight: normal;
    color: #ffffff;
    margin: 10px;
}

QMessageBox QPushButton {
    background-color: #333333;
    border: 2px solid #555555;
    border-radius: 5px;
    color: #ffffff;
    font-size: 16px;
    padding: 8px 16px;
    min-width: 80px;
    cursor: pointer;
    transition: background-color 0.3s;
}

QMessageBox QPushButton:hover {
    background-color: #555555;
}
"""


CONST_SEARCH_WINDOW = """
QMainWindow {
    background-color: #121212;
    font-family: 'Arial', sans-serif;
    color: #ffffff;
}

QLabel {
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    margin-bottom: 10px;
}

QLineEdit {
    background-color: #1c1c1c;
    border: 2px solid #333333;
    border-radius: 5px;
    color: #ffffff;
    font-size: 16px;
    padding: 8px;
}

QLineEdit:focus {
    border-color: #555555;
}

QPushButton {
    background-color: #333333;
    border: 2px solid #555555;
    border-radius: 8px;
    color: #ffffff;
    font-size: 16px;
    padding: 10px;
    cursor: pointer;
    transition: background-color 0.3s, border-color 0.3s;
}

QPushButton:hover {
    background-color: #555555;
    border-color: #777777;
}

QPushButton:pressed {
    background-color: #777777;
}

QVBoxLayout {
    margin: 20px;
    spacing: 15px;
}
"""
