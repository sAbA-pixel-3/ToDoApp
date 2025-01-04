import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QCalendarWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App with Calendar")
        self.setGeometry(100, 100, 600, 400)

        self.tasks = {}

        # Main layout
        self.layout = QVBoxLayout()

        # Calendar
        self.calendar = QCalendarWidget()
        self.layout.addWidget(self.calendar)

        # Task input field and buttons
        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.delete_button = QPushButton("Delete Task")

        # Horizontal layout for input and buttons
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.add_button)
        input_layout.addWidget(self.delete_button)

        self.layout.addLayout(input_layout)

        # Task list
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Connect buttons
        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)

        # Update tasks when the calendar date changes
        self.calendar.selectionChanged.connect(self.load_tasks_for_date)

        # Set layout
        self.setLayout(self.layout)

    def add_task(self):
        task = self.input_field.text()
        if task:
            selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")

            # Create a task item
            task_item = QListWidgetItem(task)
            task_item.setFlags(task_item.flags() | Qt.ItemIsUserCheckable)
            task_item.setCheckState(Qt.Unchecked)

            # Add task to the current date's list
            if selected_date not in self.tasks:
                self.tasks[selected_date] = []
            self.tasks[selected_date].append(task_item)

            # Update task list widget
            self.load_tasks_for_date()

            # Clear the input field
            self.input_field.clear()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if selected_items:
            selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
            for item in selected_items:
                self.task_list.takeItem(self.task_list.row(item))
                if selected_date in self.tasks:
                    self.tasks[selected_date].remove(item)

    def load_tasks_for_date(self):
        selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        self.task_list.clear()
        if selected_date in self.tasks:
            for task_item in self.tasks[selected_date]:
                self.task_list.addItem(task_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_()) 