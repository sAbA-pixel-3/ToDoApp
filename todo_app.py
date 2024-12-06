import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox, QListWidgetItem
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont 



class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 300)

        self.tasks = []

        self.layout = QVBoxLayout()

        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Tasks")
        self.delete_button = QPushButton("Delete Task")
        self.task_list = QListWidget()

        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.task_list)

        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task) 

        self.task_list.itemChanged.connect(self.toggle_task_completion) 

        self.setLayout(self.layout)

    def add_task(self):
        task = self.input_field.text()
        if task:
            task_item = QListWidgetItem(task)
            task_item.setFlags(task_item.flags() | Qt.ItemIsUserCheckable)
            task_item.setCheckState(Qt.Unchecked) 

            self.task_list.addItem(task_item) 
            self.input_field.clear()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            for item in selected_items:
                self.task_list.takeItem(self.task_list.row(item)) 

    def toggle_task_completion(self, item):
        if item.checkState() == Qt.Checked:
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font) 
        else:
            font = item.font()
            font.setStrokeOut(False)
            item.setFont(font) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())







