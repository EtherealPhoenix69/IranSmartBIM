from PySide6.QtWidgets import QMainWindow

from ui.dashboard import Dashboard
from ui.project_dialog import ProjectDialog
from ui.design_window import DesignWindow
from ui.project_manager import ProjectManager

from database.models import Project
from core.project_manager import save_project


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "IranSmartBIM - نسخه 0.2"
        )

        self.resize(
            1200,
            800
        )

        self.setCentralWidget(
            Dashboard()
        )

        self.create_menu()
        self.create_toolbar()


    def create_menu(self):

        menu = self.menuBar()


        file_menu = menu.addMenu("فایل")


        new_project = file_menu.addAction(
            "پروژه جدید"
        )


        exit_action = file_menu.addAction(
            "خروج"
        )


        new_project.triggered.connect(
            self.new_project
        )


        exit_action.triggered.connect(
            self.close
        )


        project_menu = menu.addMenu(
            "پروژه"
        )


        manager_action = project_menu.addAction(
            "مدیریت پروژه‌ها"
        )


        manager_action.triggered.connect(
            self.show_projects
        )


        architecture_menu = menu.addMenu(
            "معماری"
        )


        design_action = architecture_menu.addAction(
            "طراحی ساختمان جدید"
        )


        design_action.triggered.connect(
            self.open_design
        )


        menu.addMenu("سازه")
        menu.addMenu("متره و برآورد")
        menu.addMenu("گزارش‌ها")
        menu.addMenu("تنظیمات")


    def create_toolbar(self):

        toolbar = self.addToolBar(
            "ابزارها"
        )


        action = toolbar.addAction(
            "طراحی ساختمان"
        )


        action.triggered.connect(
            self.open_design
        )


    def new_project(self):

        dialog = ProjectDialog()


        if dialog.exec():


            project = Project(

                dialog.name.text(),

                dialog.city.text(),

                float(dialog.area.text()),

                dialog.floors.value(),

                dialog.material.currentText()

            )


            save_project(project)



    def show_projects(self):

        self.project_window = ProjectManager()

        self.project_window.show()



    def open_design(self):

        self.design_window = DesignWindow()

        self.design_window.show()