import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QMessageBox

class FoodOrderingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set window title
        self.setWindowTitle('Food Ordering App')

        # Create layout
        layout = QVBoxLayout()

        # Create a label
        self.label = QLabel('Select your food items:')
        layout.addWidget(self.label)

        # Create a list widget for food items
        self.food_list = QListWidget()
        self.food_items = ['Pizza', 'Burger', 'Pasta', 'Salad', 'Sushi']
        self.food_list.addItems(self.food_items)
        layout.addWidget(self.food_list)

        # Create a submit button
        self.submit_button = QPushButton('Submit Order')
        self.submit_button.clicked.connect(self.submit_order)
        layout.addWidget(self.submit_button)

        # Set layout to the window
        self.setLayout(layout)

    def submit_order(self):
        selected_items = self.food_list.selectedItems()
        if selected_items:
            ordered_food = [item.text() for item in selected_items]
            QMessageBox.information(self, 'Order Submitted', f'You have ordered: {", ".join(ordered_food)}')
        else:
            QMessageBox.warning(self, 'No Selection', 'Please select at least one food item.')

def main():
    app = QApplication(sys.argv)
    food_ordering_app = FoodOrderingApp()
    food_ordering_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
