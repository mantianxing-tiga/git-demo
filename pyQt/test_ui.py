from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

class InfoCollect(object):
    def __init__(self) -> None:
        # 加载 UI 文件
        self.ui = QUiLoader().load('D:/personal/git-demo/pyQt/ui/test.ui')

        self.ui.button.clicked.connect(self.display_info)

    def display_info(self):
        info = self.ui.anharm_input.toPlainText()

        QMessageBox.about(
            self.ui,
            'input_info',
            info
        )

app = QApplication([])
info = InfoCollect()
info.ui.show()
app.exec_()