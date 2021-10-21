# form1.py
# form1.up(화면단) + form1.py(로직을 수행)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 화면을 로딩
form_class = uic.loadUiType("form1.ui")[0]

#윈도우 클래를 정의
class DemoForm(Qdialog, form_class):
    def __ini__(sef):
        super().__init__()
        self.setupUI(self)
        self.label.setText("첫번째 Qt데모")

#진입점을 체크(직접 모듈을 실행했는지 여부)
if __name__=="__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()