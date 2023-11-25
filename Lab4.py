import sys
from PyQt5 import QtWidgets
import csv
from datetime import datetime

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Dataset Annotation App')

        self.date_input = QtWidgets.QLineEdit(self)
        self.date_input.setPlaceholderText('Введите дату в формате ДД.ММ.ГГГГ')
        
        self.get_data_button = QtWidgets.QPushButton('Получить данные', self)
        self.get_data_button.clicked.connect(self.get_data)

        self.annotation_button = QtWidgets.QPushButton('Создать файл аннотации', self)
        self.annotation_button.clicked.connect(self.create_annotation_file)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.date_input)
        vbox.addWidget(self.get_data_button)
        vbox.addWidget(self.annotation_button)

        self.setLayout(vbox)

    def get_data(self):
        date_str = self.date_input.text()
        try:
            date = datetime.strptime(date_str, '%d.%m.%Y')
            data = self.get_data_from_csv(date)
            if data:
                QtWidgets.QMessageBox.information(self, 'Данные', f"Данные для {date_str}: {data}")
            else:
                QtWidgets.QMessageBox.information(self, 'Данные', 'Данные для данной даты не найдены.')
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Неверный формат даты. Используйте ДД.ММ.ГГГГ')

    def get_data_from_csv(self, date):
        with open('dataset.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if len(row) >= 4:
                    row_date = datetime.strptime(row[0], '%d.%m.%Y')
                    if row_date == date:
                        return row[1:]
        return None

    def create_annotation_file(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку')
        if folderpath:
            annotation_filename = f'annotation_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
            with open(f'{folderpath}/{annotation_filename}', 'w') as annotation_file:
                # Записываем информацию о пути к исходному датасету
                annotation_file.write(f"Путь к исходному датасету: {folderpath}\n")
                
                # Добавляем данные из исходного датасета в файл аннотации
                with open('dataset.csv', 'r') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    annotation_file.write("Данные исходного датасета:\n")
                    for row in csv_reader:
                        annotation_file.write(','.join(row) + '\n')

                # Добавьте здесь дополнительные сведения, если нужно
                annotation_file.write(f"Дата создания аннотации: {datetime.now()}\nДругая информация: ...")

            QtWidgets.QMessageBox.information(self, 'Успех', f"Файл аннотации создан: {annotation_filename}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
