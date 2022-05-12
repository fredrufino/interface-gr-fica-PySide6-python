#IMPORT MODULES
import sys
import os

#IMPORT QT CORE
from qt_core import *

#IMPORT PAGES
from gui.pages.ui_pages import Ui_application_pages 

#IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import *

#MAIN WIINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Curso de Python e PySide6")

        #SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        
        #TOGGLE BUTTON
        self.ui.toggle_button.clicked.connect(self.toggle_button)
        
        #HOME BUTTON
        self.ui.btn_1.clicked.connect(self.show_page_1)
        
        #WIDGETS BUTTON
        self.ui.btn_2.clicked.connect(self.show_page_2)
        
        #SETTINGS BUTTON
        self.ui.settings_btn.clicked.connect(self.show_page_3)
        
        #EXIBIR A APLICAÇÃO
        self.show()

    def show_page_1(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.Page_1)
        
    def show_page_2(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.Page_2)

    def show_page_3(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.Page_3)    

    def toggle_button(self):
        #GET MENU WIDTH
        menu_width = self.ui.left_menu.width()
        
        #CHECK WIDTH
        width = 50
        if menu_width == 50:
            width = 240

        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())