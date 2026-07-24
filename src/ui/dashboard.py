from PySide6.QtWidgets import *


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()


        layout = QVBoxLayout()


        title = QLabel(
            "IranSmartBIM\nسامانه هوشمند طراحی ساختمان"
        )

        title.setStyleSheet(
            "font-size:28px;"
        )


        layout.addWidget(title)


        self.setLayout(layout)