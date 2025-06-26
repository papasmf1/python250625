# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#웹크롤링을 위한 선언
from bs4 import BeautifulSoup
#웹서버에 요청
import urllib.request


#디자인문서를 로딩(UI파일명 변경)
form_class = uic.loadUiType("DemoForm2.ui")[0]
#윈도우 클래스 정의(QDialog, QMainWindow클래스)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # UI 설정
    #슬롯메서드 추가
    def firstClick(self):
        #파일에 저장
        f = open("clien.txt", "wt", encoding="utf-8")
        #페이지처리(0부터 9까지)
        for i in range(0,10):
            url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
            print(url)
            data = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(data, "html.parser")
            list = soup.find_all("span", attrs={"data-role": "list-title-text"})
            for tag in list:
                title = tag.text.strip()
                print(title)
                f.write(title + "\n")

        f.close() 
        self.label.setText("중고장터 크롤링을 완료!")
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