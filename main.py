import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
from ui.lator_ui import Ui_kalkulator
from style.ui_style import stylesheet
from interaksi.identifikasi_string import eval_mtk, pisah_bilangan_negatif

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_kalkulator()
        self.ui.setupUi(self)
        self.ui.lineEdit.setAlignment(Qt.AlignRight)
        self.ui.lineEdit_2.setAlignment(Qt.AlignRight)
        self.setWindowIcon(QIcon("assets/calculator-icon-1.png"))
        
        # Menghubungkan semua tombol angka
        self.connect_buttons()

    def connect_buttons(self):
        # Membuat array dari tombol-tombol angka
        buttons = [getattr(self.ui, f"pushButton_{i}") for i in range(1, 20)]       
        for button in buttons:
            button.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        button = self.sender()
        text = button.text()
        
        if text == "=":
            # Menangani evaluasi ekspresi
            expression = self.ui.lineEdit.text()
            try:
                result = str(eval_mtk(expression))
                self.ui.lineEdit_2.setText(result.replace('.', ','))
            except Exception as e:
                self.ui.lineEdit_2.setText("Error")
        elif text == "AC":
            # Menangani penghapusan teks
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
        elif text == "⌫":
            # Menghapus satu karakter dari QLineEdit
            self.ui.lineEdit.setText(self.ui.lineEdit.text()[:-1])
        else:
            # Menambahkan teks tombol ke QLineEdit
            current_text = self.ui.lineEdit.text()
            current_text += text
            self.ui.lineEdit.setText(pisah_bilangan_negatif(current_text))
        
        

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(stylesheet)
    
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
