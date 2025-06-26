# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#디자인문서를 로딩(UI파일명 변경)
form_class = uic.loadUiType("DemoForm2.ui")[0]
#윈도우 클래스 정의(QDialog, QMainWindow클래스)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 설정
    #슬롯메서드 추가
    def firstClick(self):
        self.label.setText("첫번째 버튼 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭했음")        
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭했음~~")

#진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    demoForm = DemoForm()  # DemoForm 객체 생성
    demoForm.show()  # 윈도우 보여주기
    app.exec_()  # 이벤트 루프 실행