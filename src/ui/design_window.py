from PySide6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QPushButton,
    QLabel,
    QVBoxLayout
)

from architecture.building import Building


class DesignWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "طراحی اولیه ساختمان"
        )

        self.resize(
            500,
            500
        )


        main_layout = QVBoxLayout()


        form = QFormLayout()


        self.length = QLineEdit()

        self.width = QLineEdit()

        self.floors = QSpinBox()

        self.floors.setMinimum(1)

        self.floors.setMaximum(100)


        self.occupancy = QLineEdit()

        self.occupancy.setText("60")


        form.addRow(
            "طول زمین (متر)",
            self.length
        )

        form.addRow(
            "عرض زمین (متر)",
            self.width
        )

        form.addRow(
            "تعداد طبقات",
            self.floors
        )

        form.addRow(
            "سطح اشغال (%)",
            self.occupancy
        )


        main_layout.addLayout(
            form
        )


        button = QPushButton(
            "محاسبه"
        )

        button.clicked.connect(
            self.calculate
        )


        main_layout.addWidget(
            button
        )


        self.result = QLabel(
            "نتیجه محاسبات"
        )

        main_layout.addWidget(
            self.result
        )


        self.setLayout(
            main_layout
        )



    def calculate(self):

        building = Building(

            float(self.length.text()),

            float(self.width.text()),

            self.floors.value(),

            float(self.occupancy.text())

        )


        data = building.info()


        text = ""

        for key, value in data.items():

            text += f"{key}: {value}\n"


        self.result.setText(
            text
        )