import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

from database.database import initialize_database



def run():

    initialize_database()


    app = QApplication(sys.argv)


    window = MainWindow()

    window.show()


    sys.exit(
        app.exec()
    )