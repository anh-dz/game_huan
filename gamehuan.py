from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtMultimedia import QSound
import random, sys

def getnum(x): # !Tạo số
    def check(lis1, lis2):
        for i in range(3):
            for j in range(3):
                if lis1[i] == lis2[j]:
                    return False
        return True #CÁI NÀY ĐỂ CHO ĐẸP

    if x:
        while True: #ĐỌC CC
            lis_right = [random.randint(0,9),random.randint(0,9),random.randint(0,9)]
            if (len(set(lis_right))==3): #CÓ LÀM MỚI CÓ ĂN
                ans = sum(lis_right)
                break

        while True:
            lis_wrong = []
            for i in range(3):
                lis_wrong.append(random.choice([i for i in range(0,9) if i not in lis_right]))
            if (len(set(lis_wrong))==3) and sum(lis_wrong) != ans:
                if check(lis_right, lis_wrong):
                    break
    else:
        while True: #ĐỌC CC
            lis_right = [random.randint(-9,9),random.randint(-9,9),random.randint(-9,9)]
            if (len(set(lis_right))==3): #CÓ LÀM MỚI CÓ ĂN
                ans = sum(lis_right)
                break

        while True:
            lis_wrong = []
            for i in range(3):
                lis_wrong.append(random.choice([i for i in range(-9,9) if i not in lis_right]))
            if (len(set(lis_wrong))==3) and sum(lis_wrong) != ans:
                if check(lis_right, lis_wrong):
                    break

    user = lis_right+lis_wrong
    random.shuffle(user)
    return ans, user

def check_ans():
    if sum(lis) == ans:
        return True
    else:
        return False

def next_ans_temp(self):
    Ui_Form.next_ans(self)

class Ui_Form(object): #MAIN
    def setupUi(self, Form):
    	#SETUP
        Form.setObjectName("Form")
        Form.resize(728, 499)
        Form.setStyleSheet("background: rgb(0, 0, 0)")
        self.time = QtWidgets.QLabel(Form)
        self.time.setGeometry(QtCore.QRect(440, 90, 200, 31))
        self.time.setObjectName("time")
        self.time_title = QtWidgets.QPushButton(Form)
        self.time_title.setGeometry(QtCore.QRect(600, 90, 50, 31))
        self.time_title.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 35px;color: white}")
        self.time_title.setObjectName("time_title")
        self.play = QtWidgets.QPushButton(Form)
        self.play.setGeometry(QtCore.QRect(270, 270, 259, 50))
        self.play.setStyleSheet("QPushButton{font: bold;background-color: white;font-size: 36px;color: black;border-radius: 15px}")
        self.play.setObjectName("play")
        self.how_to = QtWidgets.QPushButton(Form)
        self.how_to.setGeometry(QtCore.QRect(270, 200, 259, 50))
        self.how_to.setStyleSheet("QPushButton{font: bold;background-color: white;font-size: 36px;color: black;border-radius: 15px}")
        self.how_to.setObjectName("how_to")
        self.home = QtWidgets.QPushButton(Form)
        self.home.setGeometry(QtCore.QRect(40, 440, 81, 31))
        self.home.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 24px;color: white}")
        self.home.setObjectName("home")
        self.howto = QtWidgets.QTextBrowser(Form)
        self.howto.setEnabled(True)
        self.howto.setGeometry(QtCore.QRect(60, 130, 611, 281))
        self.howto.setOpenLinks(False)
        self.howto.setObjectName("howto")
        self.howto.setStyleSheet("border: 3px solid white")
        self.ans1 = QtWidgets.QPushButton(Form)
        self.ans1.setGeometry(QtCore.QRect(40, 220, 111, 81))
        self.ans1.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans1.setObjectName("ans1")
        self.ans2 = QtWidgets.QPushButton(Form)
        self.ans2.setGeometry(QtCore.QRect(300, 220, 111, 81))
        self.ans2.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans2.setObjectName("ans2")
        self.ans3 = QtWidgets.QPushButton(Form)
        self.ans3.setGeometry(QtCore.QRect(560, 220, 111, 81))
        self.ans3.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans3.setObjectName("ans3")
        self.ans4 = QtWidgets.QPushButton(Form)
        self.ans4.setGeometry(QtCore.QRect(40, 340, 111, 81))
        self.ans4.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans4.setObjectName("ans4")
        self.ans5 = QtWidgets.QPushButton(Form)
        self.ans5.setGeometry(QtCore.QRect(300, 340, 111, 81))
        self.ans5.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans5.setObjectName("ans5")
        self.ans6 = QtWidgets.QPushButton(Form)
        self.ans6.setGeometry(QtCore.QRect(560, 340, 111, 81))
        self.ans6.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans6.setObjectName("ans6")
        self.target = QtWidgets.QLabel(Form)
        self.target.setGeometry(QtCore.QRect(0, 0, 729, 78))
        self.target.setObjectName("target")
        self.score_title = QtWidgets.QPushButton(Form)
        self.score_title.setGeometry(QtCore.QRect(540, 440, 91, 31))
        self.score_title.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 24px;color: white}")
        self.score_title.setObjectName("score_title")
        self.score = QtWidgets.QPushButton(Form)
        self.score.setGeometry(QtCore.QRect(640, 440, 81, 31))
        self.score.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 24px;color: white}")
        self.score.setObjectName("score")
        self.tagert = QtWidgets.QPushButton(Form)
        self.tagert.setGeometry(QtCore.QRect(620, 0, 112, 79))
        self.tagert.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 63px;color: white}")
        self.tagert.setObjectName("tagert")
        self.infor = QtWidgets.QPushButton(Form)
        self.infor.setGeometry(QtCore.QRect(0, 0, 721, 491))
        self.infor.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 60px;color: white}")
        self.infor.setObjectName("infor")

        #CLICK
        self.home.clicked.connect(self.home_run)
        self.how_to.clicked.connect(self.howto_run)
        self.play.clicked.connect(self.play_run)
        self.play.clicked.connect(self.next_ans)
        self.ans1.clicked.connect(self.ans1_run)
        self.ans2.clicked.connect(self.ans2_run)
        self.ans3.clicked.connect(self.ans3_run)
        self.ans4.clicked.connect(self.ans4_run)
        self.ans5.clicked.connect(self.ans5_run)
        self.ans6.clicked.connect(self.ans6_run)

        #RUN
        self.home.click()
        QSound.play("huanrose.wav")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        app.setWindowIcon(QtGui.QIcon('huanrose.jpg'))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GAME HUẤN"))
        self.time.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:15pt; font-weight:600; color:#ffffff;\">BAY MÀU?</span></p></body></html>"))
        self.play.setText(_translate("Form", "LÀM THÔI!!"))
        self.how_to.setText(_translate("Form", "HƯỚNG DẪN"))
        self.home.setText(_translate("Form", "NHÀ"))
        self.howto.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">GAME HUẤN PHIÊN BẢN 1.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">CHÀO MỪNG</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">HƯỚNG DẪN: CÓ LÀM MỚI CÓ ĂN</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">KẾT THÚC HƯỚNG DẪN</span></p></body></html>"))
        self.ans1.setText(_translate("Form", "0"))
        self.ans2.setText(_translate("Form", "0"))
        self.ans3.setText(_translate("Form", "0"))
        self.ans4.setText(_translate("Form", "0"))
        self.ans5.setText(_translate("Form", "0"))
        self.ans6.setText(_translate("Form", "0"))
        self.target.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">GAME HUẤN</span></p></body></html>"))
        self.score_title.setText(_translate("Form", "ĐÃ LÀM"))
        self.score.setText(_translate("Form", "0"))
        self.tagert.setText(_translate("Form", "0"))

    #FUNCTION
    def home_run(self): #HOME_MAIN
        global st
        st = 0
        self.score.setVisible(False)
        self.score_title.setVisible(False)
        self.time.setVisible(False)
        self.time_title.setVisible(False)
        self.howto.setVisible(False)
        self.ans1.setVisible(False)
        self.ans2.setVisible(False)
        self.ans3.setVisible(False)
        self.ans4.setVisible(False)
        self.ans5.setVisible(False)
        self.ans6.setVisible(False)
        self.play.setVisible(True)
        self.how_to.setVisible(True)
        self.infor.setVisible(False)

    def howto_run(self):
        self.how_to.setVisible(False)
        self.play.setVisible(False)
        self.howto.setVisible(True)

    def play_run(self):
        global num, misson
        num = 0
        misson = random.randint(50,1000)
        self.infor.setText(f"NHIỆM VỤ: {str(misson)}")
        self.infor.setVisible(True)
        QtTest.QTest.qWait(1000)
        self.infor.setVisible(False)
        self.score.setText(str(num))
        self.how_to.setVisible(False)
        self.play.setVisible(False)
        self.time.setVisible(True)
        self.time_title.setVisible(True)
        self.score.setVisible(True)
        self.score_title.setVisible(True)
        self.ans1.setVisible(True)
        self.ans2.setVisible(True)
        self.ans3.setVisible(True)
        self.ans4.setVisible(True)
        self.ans5.setVisible(True)
        self.ans6.setVisible(True)

    def next_ans(self):
    	#NEXT_ANS
        global ans, non_ans, user, lis, lily, st
        lily = 0
        st = 1
        lis = []
        if num<11:
            ans, user = getnum(True)
        else:
            ans, user = getnum(False)
        if num==10:
            self.infor.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white}")
            self.infor.setText("KHÔNG PHẢI ĂN ĐẦU BUỒI NỮA")
            self.infor.setVisible(True)
            QtTest.QTest.qWait(1000)
            self.infor.setVisible(False)
            self.infor.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 60px;color: white}")
        if num==100:
            self.infor.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white}")
            self.infor.setText("TIẾP TỤC CỐ GẮNG")
            self.infor.setVisible(True)
            QtTest.QTest.qWait(1000)
            self.infor.setVisible(False)
            self.infor.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 60px;color: white}")
        if num==misson:
            self.infor.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white}")
            self.infor.setText("HOÀN THÀNH NHIỆM VỤ")
            self.infor.setVisible(True)
            QtTest.QTest.qWait(2000)
            self.infor.setText("XỨNG ĐÁNG LÀ CON CỦA ĐẢNG")
            QtTest.QTest.qWait(3000)
            QSound.play("win.wav")
            self.infor.setText("NHẬN HUÂN CHƯƠNG THẦY HUẤN")
            QtTest.QTest.qWait(2000)
            self.home.click()
            self.infor.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 60px;color: white}")

        self.ans1.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans2.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans3.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans4.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans5.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        self.ans6.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
        
        self.tagert.setText(str(ans))
        self.ans1.setText(str(user[0]))
        self.ans2.setText(str(user[1]))
        self.ans3.setText(str(user[2]))
        self.ans4.setText(str(user[3]))
        self.ans5.setText(str(user[4]))
        self.ans6.setText(str(user[5]))

        #TIME
        for i in range(9,0,-1):
            self.time_title.setText(str(i))
            QtTest.QTest.qWait(1000)
            if st==0:
                break

        #TIME_OUT
        if st==1:
            self.infor.setText("NGU NHƯ BÒ")
            self.infor.setVisible(True)
            lis.clear()
            QSound.play("wrong.wav")
            QtTest.QTest.qWait(1000)
            self.infor.setVisible(False)
            self.home.click()

    #ANS
    def ans1_run(self):
        global lily, num
        if lis.count(user[0]) == 0:
       	    lily+=1
       	    self.ans1.setStyleSheet("QPushButton{font: bold;background-color: white;font-size: 40px;color: black;border: 1px solid white}")
            lis.append(user[0])
            if lily == 3: 
                if check_ans():
                    self.infor.setText("TỐT")
                    self.infor.setVisible(True)
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    num+=1
                    self.score.setText(str(num))
                    next_ans_temp(self)
                else:
                    self.infor.setText("TỐN CƠM TỐN GẠO")
                    self.infor.setVisible(True)
                    QSound.play("wrong.wav")
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    self.home.click()
        else:
            lily-=1
            self.ans1.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
            lis.remove(user[0])

    def ans2_run(self):
        global lily, num
        if lis.count(user[1]) == 0:
       	    lily+=1
       	    self.ans2.setStyleSheet("QPushButton{font: bold;background-color: white;font-size: 40px;color: black;border: 1px solid white}")
            lis.append(user[1])
            if lily == 3: 
                if check_ans():
                    self.infor.setText("DỎI")
                    self.infor.setVisible(True)
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    num+=1
                    self.score.setText(str(num))
                    next_ans_temp(self)
                else:
                    self.infor.setText("TỐN CƠM TỐN GẠO")
                    self.infor.setVisible(True)
                    QSound.play("wrong.wav")
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    self.home.click()
        else:
            lily-=1
            self.ans2.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
            lis.remove(user[1])

    def ans3_run(self):
        global lily, num
        if lis.count(user[2]) == 0:
       	    lily+=1
       	    self.ans3.setStyleSheet("QPushButton{font: bold;background-color: white;font-size: 40px;color: black;border: 1px solid white}")
            lis.append(user[2])
            if lily == 3: 
                if check_ans():
                    self.infor.setText("CÓ LÀM MỚI CÓ ĂN")
                    self.infor.setVisible(True)
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    num+=1
                    self.score.setText(str(num))
                    next_ans_temp(self)
                else:
                    self.infor.setText("TỐN CƠM TỐN GẠO")
                    self.infor.setVisible(True)
                    QSound.play("wrong.wav")
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    self.home.click()
        else:
            lily-=1
            self.ans3.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
            lis.remove(user[2])

    def ans4_run(self):
        global lily, num
        if lis.count(user[3]) == 0:
       	    lily+=1
       	    self.ans4.setStyleSheet("QPushButton{font: bold;background-color: white;font-size: 40px;color: black;border: 1px solid white}")
            lis.append(user[3])
            if lily == 3: 
                if check_ans():
                    self.infor.setText("RỎI")
                    self.infor.setVisible(True)
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    num+=1
                    self.score.setText(str(num))
                    next_ans_temp(self)
                else:
                    self.infor.setText("TỐN CƠM TỐN GẠO")
                    self.infor.setVisible(True)
                    QSound.play("wrong.wav")
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    self.home.click()
        else:
            lily-=1
            self.ans4.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
            lis.remove(user[3])

    def ans5_run(self):
        global lily, num
        if lis.count(user[4]) == 0:
       	    lily+=1
       	    self.ans5.setStyleSheet("QPushButton{font: bold;background-color: white;font-size: 40px;color: black;border: 1px solid white}")
            lis.append(user[4])
            if lily == 3: 
                if check_ans():
                    self.infor.setText("TỐT")
                    self.infor.setVisible(True)
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    num+=1
                    self.score.setText(str(num))
                    next_ans_temp(self)
                else:
                    self.infor.setText("TỐN CƠM TỐN GẠO")
                    self.infor.setVisible(True)
                    QSound.play("wrong.wav")
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    self.home.click()
        else:
            lily-=1
            self.ans5.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
            lis.remove(user[4])

    def ans6_run(self):
        global lily, num
        if lis.count(user[5]) == 0:
       	    lily+=1
       	    self.ans6.setStyleSheet("QPushButton{font: bold;background-color: white;font-size: 40px;color: black;border: 1px solid white}")
            lis.append(user[5])
            if lily == 3:
                if check_ans():
                    self.infor.setText("TỐT")
                    self.infor.setVisible(True)
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    num+=1
                    self.score.setText(str(num))
                    next_ans_temp(self)
                else:
                    self.infor.setText("TỐN CƠM TỐN GẠO")
                    self.infor.setVisible(True)
                    QSound.play("wrong.wav")
                    QtTest.QTest.qWait(1000)
                    self.infor.setVisible(False)
                    self.home.click()
        else:
            lily-=1
            self.ans6.setStyleSheet("QPushButton{font: bold;background-color: black;font-size: 40px;color: white;border: 1px solid white}")
            lis.remove(user[5])

#START
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())
