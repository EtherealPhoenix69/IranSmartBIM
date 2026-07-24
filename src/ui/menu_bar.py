from PySide6.QtGui import QAction

def create_menu(window):
    menubar = window.menuBar()

    file_menu = menubar.addMenu("فایل")
    project_menu = menubar.addMenu("پروژه")
    architecture_menu = menubar.addMenu("معماری")
    structure_menu = menubar.addMenu("سازه")
    quantity_menu = menubar.addMenu("متره")
    reports_menu = menubar.addMenu("گزارش")
    settings_menu = menubar.addMenu("تنظیمات")

    new_action = QAction("پروژه جدید", window)
    exit_action = QAction("خروج", window)

    file_menu.addAction(new_action)
    file_menu.addSeparator()
    file_menu.addAction(exit_action)

    exit_action.triggered.connect(window.close)

    return new_action