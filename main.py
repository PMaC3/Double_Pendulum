import sys
from PySide2.QtWidgets import QApplication, QLabel
import pyqtgraph as pg

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello World")
    label.show()
    sys.exit(app.exec_())
