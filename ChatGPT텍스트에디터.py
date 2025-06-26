import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox

class TextViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('텍스트 뷰어')
        self.setGeometry(100, 100, 800, 600)

        # 텍스트 에디터 위젯
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.setCentralWidget(self.text_edit)

        # 메뉴바
        menubar = self.menuBar()
        file_menu = menubar.addMenu('파일')

        open_action = QAction('열기', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        exit_action = QAction('종료', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "텍스트 파일 열기", "", "텍스트 파일 (*.txt);;모든 파일 (*)", options=options)
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                self.text_edit.setPlainText(text)
            except Exception as e:
                QMessageBox.critical(self, "오류", f"파일을 열 수 없습니다:\n{e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = TextViewer()
    viewer.show()  # 이 줄이 누락되어 창이 보이지 않았음
    sys.exit(app.exec_())  # 프로그램이 정상적으로 종료되도록 수정