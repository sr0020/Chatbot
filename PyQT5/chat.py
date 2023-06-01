# 0427 / 0601
from PyQt5.QtWidgets import *
import pandas as pd
import openai
from PyQt5 import uic
import os
import sys

# openai
OPENAI_API_KEY = "" # https://platform.openai.com/ 해당 사이트에서 키 다운로드
openai.api_key = OPENAI_API_KEY
model = 'gpt-3.5-turbo'

class secondWindow(QDialog):
    def __init__(self, text):
        super().__init__()
        self.text = text
        qtCreatorFile = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "secondwindow.ui")
        self.Ui_MainWindow, self.QtBaseClass = uic.loadUiType(qtCreatorFile)
        self.initUI()
        self.show()

    def initUI(self):
        self.ui = self.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText(self.text)
        # self.home.clicked.connect(self.Home) # 

    # def Home(self):
    #     self.close()

class Chat(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.show()

        self.resize(500, 120)
        self.setWindowTitle("Chatbot")

        # 버튼, 결과
        self.question = QLineEdit()
        self.enter = QPushButton("Enter")
        self.cancel = QPushButton("Cancel")

        # 레이아웃
        input_lay = QHBoxLayout()
        input_lay.addWidget(self.question)

        btn_lay = QHBoxLayout()
        btn_lay.addWidget(self.enter)
        btn_lay.addWidget(self.cancel)

        self.main_lay = QVBoxLayout()
        self.main_lay.addLayout(input_lay)
        self.main_lay.addLayout(btn_lay)

        self.setLayout(self.main_lay)
        self.enter.clicked.connect(self.main)
        self.cancel.clicked.connect(self.close)

        self.enter.clicked.connect(self.buttonEvent)
        self.show()

    def main(self):
        query = str(self.question.text())

        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": query} 
        ]

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )

        self.answer = response['choices'][0]['message']['content']
        print(self.answer)

        # to txt
        f = open("chat.txt", "w")
        f.write(self.answer)

        f.close()
        
        # text = self.answer
        # sw = secondWindow(text)
        # sw.exec_()
    
    def buttonEvent(self):
        text = self.answer 
        sw = secondWindow(text) 
        sw.exec_()

if __name__ == "__main__":
    app = QApplication([])
    dialog = Chat()
    dialog.show()
    app.exec_()
    print("Done")