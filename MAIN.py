import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox,
                             QDialog, QLabel, QLineEdit, QDialogButtonBox, QTabWidget)
from PyQt6.QtCore import Qt
import pandas as pd
import numpy as np


class ConstantInputDialog(QDialog):
    def __init__(self, constants, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter Constants")
        self.constants = constants
        self.inputs = {}

        layout = QVBoxLayout()

        for name, value in constants.items():
            label = QLabel(f"{name}:")
            input_field = QLineEdit(str(value))
            self.inputs[name] = input_field
            layout.addWidget(label)
            layout.addWidget(input_field)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_values(self):
        values = {}
        for name, input_field in self.inputs.items():
            try:
                values[name] = float(input_field.text())
            except ValueError:
                values[name] = 0.0
        return values


class ExcelTableEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agricultural Model Calculator")
        self.setGeometry(100, 100, 1200, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create tab widget
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # Add control buttons
        self.button_layout = QVBoxLayout()

        self.load_button = QPushButton("Load Excel File")
        self.load_button.clicked.connect(self.load_excel)
        self.button_layout.addWidget(self.load_button)

        self.edit_constants_button = QPushButton("Edit Constants")
        self.edit_constants_button.clicked.connect(self.edit_constants)
        self.button_layout.addWidget(self.edit_constants_button)

        self.calculate_button = QPushButton("Calculate Model")
        self.calculate_button.clicked.connect(self.calculate_model)
        self.button_layout.addWidget(self.calculate_button)

        self.save_button = QPushButton("Save Results")
        self.save_button.clicked.connect(self.save_results)
        self.button_layout.addWidget(self.save_button)

        self.layout.addLayout(self.button_layout)

        # Initialize data structures
        self.sheets = {}
        self.table_widgets = {}
        self.current_data = {}

        # Define constants from the model
        self.constants = {
            "Урожайность (ц/га)": 11.4,
            "Себестоимость 1 ц (руб)": 1882.82,
            "Коэффициент выхода сырья (маслосемена)": 0.95,
            "Коэффициент себестоимости сырья": 1.4,
            "Коэффициент выхода готовой продукции": 0.8,
            "Коэффициент товарности": 0.98,
            "Цена маслосемян (руб)": 3841,
            "Цена масла подсолнечного (руб)": 8607,
            "Таможенная пошлина (руб)": 300
        }

        # Initialize with empty table
        self.add_sheet("Empty", pd.DataFrame())

    def add_sheet(self, name, dataframe):
        if name in self.table_widgets:
            return

        table = QTableWidget()
        table.setRowCount(dataframe.shape[0])
        table.setColumnCount(dataframe.shape[1])

        # Set headers
        table.setHorizontalHeaderLabels(list(dataframe.columns))
        if not dataframe.empty:
            table.setVerticalHeaderLabels(list(dataframe.index.astype(str)))

        # Fill data
        for i in range(dataframe.shape[0]):
            for j in range(dataframe.shape[1]):
                item = QTableWidgetItem(str(dataframe.iloc[i, j]))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                table.setItem(i, j, item)

        self.table_widgets[name] = table
        self.sheets[name] = dataframe
        self.tab_widget.addTab(table, name)

    def load_excel(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls)")

        if file_path:
            try:
                # Read all sheets from Excel
                excel_data = pd.read_excel(file_path, sheet_name=None)

                # Clear existing tabs
                for i in range(self.tab_widget.count()):
                    self.tab_widget.removeTab(0)
                self.table_widgets = {}
                self.sheets = {}

                # Add each sheet as a tab
                for sheet_name, df in excel_data.items():
                    self.add_sheet(sheet_name, df)

                # Store the loaded data
                self.current_data = excel_data

                QMessageBox.information(self, "Success", "Excel file loaded successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load Excel file: {str(e)}")

    def edit_constants(self):
        dialog = ConstantInputDialog(self.constants, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.constants = dialog.get_values()

    def calculate_model(self):
        if not self.current_data:
            QMessageBox.warning(self, "Warning", "No data loaded. Please load an Excel file first.")
            return

        try:
            # Get data from the "Регулирующий блок" sheet
            reg_block = self.current_data.get("Регулирующий блок", pd.DataFrame())

            # Get data from the "Управляющий блок" sheet
            control_block = self.current_data.get("Управляющий блок", pd.DataFrame())

            # Get data from the "Модель последняя" sheet
            model = self.current_data.get("Модель последняя", pd.DataFrame())

            # Apply constants
            yield_per_ha = self.constants["Урожайность (ц/га)"]
            cost_per_centner = self.constants["Себестоимость 1 ц (руб)"]
            output_coef = self.constants["Коэффициент выхода сырья (маслосемена)"]
            cost_coef = self.constants["Коэффициент себестоимости сырья"]
            final_output_coef = self.constants["Коэффициент выхода готовой продукции"]
            marketability_coef = self.constants["Коэффициент товарности"]
            seed_price = self.constants["Цена маслосемян (руб)"]
            oil_price = self.constants["Цена масла подсолнечного (руб)"]
            customs_duty = self.constants["Таможенная пошлина (руб)"]

            # Calculate based on the model (simplified example)
            # This would be replaced with the actual calculations from the model

            # Example calculation for output (column 3 in Регулирующий блок)
            if not reg_block.empty and len(reg_block.columns) > 2:
                sown_area = reg_block.iloc[0, 2]  # Посевная площадь
                calculated_output = sown_area * yield_per_ha

                # Update the table
                if "Регулирующий блок" in self.table_widgets:
                    table = self.table_widgets["Регулирующий блок"]
                    if table.rowCount() > 2 and table.columnCount() > 2:
                        item = QTableWidgetItem(str(round(calculated_output, 2)))
                        table.setItem(2, 2, item)

            # More complex calculations would go here based on the actual model formulas

            QMessageBox.information(self, "Success", "Model calculations completed!")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to calculate model: {str(e)}")

    def save_results(self):
        if not self.current_data:
            QMessageBox.warning(self, "Warning", "No data to save.")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Results", "", "Excel Files (*.xlsx)")

        if file_path:
            try:
                # Create a writer object
                writer = pd.ExcelWriter(file_path, engine='openpyxl')

                # Save each sheet
                for sheet_name, table in self.table_widgets.items():
                    # Convert table data back to DataFrame
                    rows = table.rowCount()
                    cols = table.columnCount()

                    data = []
                    for row in range(rows):
                        row_data = []
                        for col in range(cols):
                            item = table.item(row, col)
                            row_data.append(item.text() if item else "")
                        data.append(row_data)

                    # Get headers
                    headers = []
                    for col in range(cols):
                        headers.append(table.horizontalHeaderItem(col).text() if table.horizontalHeaderItem(
                            col) else f"Column {col}")

                    df = pd.DataFrame(data, columns=headers)
                    df.to_excel(writer, sheet_name=sheet_name, index=False)

                writer.close()
                QMessageBox.information(self, "Success", "Results saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save results: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExcelTableEditor()
    window.show()
    sys.exit(app.exec())
