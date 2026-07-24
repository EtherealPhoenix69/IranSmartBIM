from PySide6.QtWidgets import *


class ProjectDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "پروژه جدید"
        )


        layout = QFormLayout()


        self.name = QLineEdit()

        self.city = QLineEdit()

        self.area = QLineEdit()

        self.floors = QSpinBox()

        self.material = QComboBox()

        self.material.addItems(
            [
            "اقتصادی",
            "متوسط",
            "با کیفیت"
            ]
        )


        layout.addRow(
            "نام پروژه",
            self.name
        )

        layout.addRow(
            "شهر",
            self.city
        )

        layout.addRow(
            "متراژ زمین",
            self.area
        )

        layout.addRow(
            "تعداد طبقات",
            self.floors
        )

        layout.addRow(
            "کیفیت مصالح",
            self.material
        )


        button = QPushButton(
            "ذخیره"
        )

        button.clicked.connect(
            self.accept
        )


        layout.addWidget(button)


        self.setLayout(layout)