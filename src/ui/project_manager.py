from PySide6.QtWidgets import *


from database.database import (
    get_projects,
    delete_project
)



class ProjectManager(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "مدیریت پروژه‌ها"
        )


        layout = QVBoxLayout()


        self.table = QTableWidget()


        self.table.setColumnCount(6)


        self.table.setHorizontalHeaderLabels(
            [
                "نام",
                "شهر",
                "زمین",
                "طبقات",
                "مصالح",
                "تاریخ"
            ]
        )


        layout.addWidget(
            self.table
        )


        delete_btn = QPushButton(
            "حذف پروژه"
        )


        delete_btn.clicked.connect(
            self.delete_selected
        )


        layout.addWidget(
            delete_btn
        )


        self.setLayout(
            layout
        )


        self.load_projects()



    def load_projects(self):

        projects = get_projects()


        self.table.setRowCount(
            len(projects)
        )


        for row, project in enumerate(projects):

            for col, value in enumerate(project[1:]):

                self.table.setItem(
                    row,
                    col,
                    QTableWidgetItem(
                        str(value)
                    )
                )



    def delete_selected(self):

        row = self.table.currentRow()


        if row >= 0:

            projects = get_projects()

            project_id = projects[row][0]


            delete_project(
                project_id
            )


            self.load_projects()