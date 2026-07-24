from PySide6.QtGui import QAction

def create_toolbar(window):

    toolbar = window.addToolBar("Main")

    new_project = QAction("پروژه جدید", window)

    save_project = QAction("ذخیره", window)

    toolbar.addAction(new_project)

    toolbar.addAction(save_project)

    return new_project