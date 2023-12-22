from random import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFormLayout, QLineEdit, QPushButton


class DiceSimulation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dice Simulation")

        self.main_widget = QWidget()
        self.layout = QVBoxLayout()

        self.label1 = QLabel("Сколько кубиков?")
        self.layout.addWidget(self.label1)
        self.lineEdit1 = QLineEdit()
        self.layout.addWidget(self.lineEdit1)

        self.label2 = QLabel("Сколько бросков?")
        self.layout.addWidget(self.label2)
        self.lineEdit2 = QLineEdit()
        self.layout.addWidget(self.lineEdit2)

        self.button = QPushButton("Запустить")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.run_simulation)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def run_simulation(self):
        kol = int(self.lineEdit1.text())
        br = int(self.lineEdit2.text())

        data = []
        for l in range(br):
            count = 0
            for i in range(kol):
                a = randint(1, 6)
                count += a
            data.append(count)
            if l % 1000 == 0:
                print(f'{l // 1000} из {br // 1000}')

        data.sort()

        result = "Результаты бросков: " + str(data) + "\n"
        result += "Вероятности выпадения суммы значений кубиков:\n"
        for h in range(kol, (kol * 6) + 1):
            gg = data.count(h)
            result += f'Вероятность выпадения {h}: {gg / br * 100}%\n'

        self.result_label.setText(result)


if __name__ == "__main__":
    app = QApplication([])
    window = DiceSimulation()
    window.resize(100,200)
    window.show()
    app.exec()