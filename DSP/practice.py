import sys
import serial
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class SensorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.serial_port = serial.Serial('COM3', 9600)  # Replace 'COM3' with your port

    def initUI(self):
        self.setWindowTitle("Sensor Data")
        self.layout = QVBoxLayout()
        self.label = QLabel("Waiting for sensor data...")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.startReading()

    def startReading(self):
        if self.serial_port.isOpen():
            while True:
                data = self.serial_port.readline().decode('utf-8').strip()
                self.label.setText(data)
                QApplication.processEvents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SensorUI()
    window.show()
    sys.exit(app.exec_())
