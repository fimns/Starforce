import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random
from math import *

#libpaths = QApplication.libraryPaths() 
#libpaths.append("C:\\Users\fimns\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\PyQt5\Qt\plugins") 
#QApplication.setLibraryPaths(libpaths)

class SeWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setGeometry(200,200,1100,400)
        self.setWindowTitle("aa")
        
class MyWindow(QMainWindow):
    Acc = 0
    Temp1 = "Temp"
    Temp2 = "Temp"
    Temp3 = "Temp"
    Temp4 = "Temp"
    S_Save = 0
    M_Save = 0
    L_Save = 0
    M = 100
    S = 100
    Sunday = 1.0
    Event15 = 0
    Event2 = 0
    Pay = [[110800,220500,330300,440000,549800,659600,769300,879100,988800,1098600,4448200,5625900,6982900,8529400,10275700,24462200,28812500,33620400,38904500,44683300,50974700,57796700,65166700,73102200,81620200,0,0],[136000,271000,406000,541000,676000,811000,946000,1081000,1216000,1351000,5470800,6919400,8588400,10490600,12638500,30087200,35437900,41351400,47850600,54958200,62969400,71087200,80152000,89912300,100389000,0,0],[164800,328700,492500,656400,820200,984000,1147900,1311700,1475600,1639400,6639400,8397300,10422900,12731500,15338200,36514500,43008300,50185100,58072700,66698700,76090000,86273300,97274600,109120000,121834900],[321000,641000,961000,1281000,1601000,1921000,2241000,2561000,2881000,3201000,12966500,16400100,20356300,24865300,29956500,71316500,83999600,98016700,113422300,130270000,148612400,168501500,189988600,213124000,237957700,0,0]]
    Suc = [0.95,0.9,0.85,0.85,0.8,0.75,0.7,0.65,0.6,0.55,0.45,0.35,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.03,0.02,0.01,0,0]
    Des = [0,0,0,0,0,0,0,0,0,0,0,0,0,0.007,0.014,0.014,0.021,0.021,0.021,0.028,0.028,0.07,0.07,0.194,0.294,0.396,0,0]
    Res = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Ev_30 = 0
    StarCatch = 0
    Ev_10 = 0
    Ev_2 = 0
    rnd = 0
    Tax = 1
    P_Des = 18
    Destination = 25
    Lv = 0
    MVP = 0
    PC = 0
    
    def __init__(self):
        
        self.Acc = 20000
        super().__init__()
        self.GroupWindow()
        self.LabelWindow()
        self.ButtonWindow()
        self.TextWindow()
        self.StatusWindow()
        self.CheckWindow()
        self.RadioWindow()
        self.setGeometry(200,200,1100,400)
        self.setWindowTitle("스타포스")
    
    def ButtonWindow(self):
        self.Bt_Calc = QPushButton("계산",self)
        self.Bt_Calc.clicked.connect(self.Calc)
        self.Bt_Calc.move(750,350)
        self.Bt_Quit = QPushButton("종료",self)
        self.Bt_Quit.clicked.connect(QCoreApplication.instance().quit)
        self.Bt_Quit.move(870,350);
        
    def Ref(self):
        self.Temp1 = self.Text_M.text()
        self.Temp2 = self.Text_S.text()
        self.Temp3 = self.Text_D.text()
        self.Temp4 = self.Text_L.text()
        self.S_Save = int(self.Temp2)
        self.M_Save = int(self.Temp1)
        self.Lv = int(self.Temp4)

        self.Destination = int(self.Temp3)
        
        for i in range(0,27) :
            self.Res[i] = 0
    
    def StatusWindow(self):
        self.Bar = QStatusBar(self)
        self.setStatusBar(self.Bar)
    def GroupWindow(self):
        self.Group_Des = QGroupBox("파괴방지",self)
        self.Group_Des.move(690,30)
        self.Group_Des.resize(180,120)
        self.Group_Sunday = QGroupBox("선데이 메이플",self)
        self.Group_Sunday.move(690,190)
        self.Group_Sunday.resize(320,120)
        self.Group_MVP = QGroupBox("MVP등급",self)
        self.Group_MVP.move(880,30)
        self.Group_MVP.resize(160,150)
        
    def Sunday30(self):
        self.Sunday = (-1 * self.Sunday) + 1.7
        #print(self.Sunday)
    def Sunday15(self):
        self.Event15 = (self.Event15 * -1) + 1
    
    def Sunday2(self):
        self.Event2 = self.Event2 * -1 + 1
        
    def CheckWindow(self):
        self.Chk_Star = QCheckBox("스타캐치",self)
        self.Chk_Star.move(520,30)
        self.Chk_Star.stateChanged.connect(self.ChangeStarCatch)
        self.Chk_Pc = QCheckBox("PC방",self)
        self.Chk_Pc.move(520,70)
    
        self.Chk_Sunday30 = QCheckBox("스타포스 강화 비용 30% 할인",self)
        self.Chk_Sunday30.move(710,210)
        self.Chk_Sunday30.resize(300,30)
        self.Chk_Sunday15 = QCheckBox("5,10,15성에서 성공확률 100%",self)
        self.Chk_Sunday15.move(710,240)
        self.Chk_Sunday15.resize(300,30)
        self.Chk_Sunday2 = QCheckBox("10성 이하 강화 성공시 1+1 강화",self)
        self.Chk_Sunday2.move(710,270)
        self.Chk_Sunday2.resize(300,30)
        
        self.Chk_Pc.stateChanged.connect(self.Set_PC)
        self.Chk_Sunday30.stateChanged.connect(self.Sunday30)
        self.Chk_Sunday15.stateChanged.connect(self.Sunday15)
        self.Chk_Sunday2.stateChanged.connect(self.Sunday2)
        
    def Set_PC(self):
        if self.PC == 0 :
            self.PC = 0.05
        else:
            self.PC = 0
    def RadioWindow(self):
        self.Radio_Des1517 = QRadioButton("15성 ~ 17성",self)
        self.Radio_Des1517.move(710,50)
        self.Radio_Des1517.resize(200,30)
        self.Radio_Des1217 = QRadioButton("12성 ~ 17성",self)
        self.Radio_Des1217.move(710,80)
        self.Radio_Des1217.resize(200,30)
        self.Radio_Des0 = QRadioButton("파괴방지 없음",self)
        self.BT_GroupA = QButtonGroup(self)
        self.BT_GroupA.addButton(self.Radio_Des1517)
        self.BT_GroupA.addButton(self.Radio_Des1217)
        self.BT_GroupA.addButton(self.Radio_Des0)
        
        self.Radio_MVP_Bronze = QRadioButton("MVP브론즈",self)
        self.Radio_MVP_Bronze.move(900,50)
        self.Radio_MVP_Bronze.resize(120,30)
        self.Radio_MVP_Silver = QRadioButton("MVP실버",self)
        self.Radio_MVP_Silver.move(900,80)
        self.Radio_MVP_Silver.resize(120,30)
        self.Radio_MVP_Gold = QRadioButton("MVP골드",self)
        self.Radio_MVP_Gold.move(900,110)
        self.Radio_MVP_Gold.resize(120,30)
        self.Radio_MVP_Dia = QRadioButton("MVP다이아",self)
        self.Radio_MVP_Dia.move(900,140)
        self.Radio_MVP_Dia.resize(120,30)
        self.Radio_MVP_Bronze.setChecked(True)
        
        self.Radio_Des0.move(710,110)
        self.Radio_Des0.resize(200,30)
        self.Radio_Des0.setChecked(True)
        
        
        self.Radio_Des1517.clicked.connect(self.Prev_Des)
        self.Radio_Des1217.clicked.connect(self.Prev_Des)
        self.Radio_Des0.clicked.connect(self.Prev_Des)
        self.Radio_MVP_Bronze.clicked.connect(self.Set_MVP)
        self.Radio_MVP_Silver.clicked.connect(self.Set_MVP)
        self.Radio_MVP_Gold.clicked.connect(self.Set_MVP)
        self.Radio_MVP_Dia.clicked.connect(self.Set_MVP)
    
    def Set_MVP(self):
        if self.Radio_MVP_Bronze.isChecked():
            self.MVP = 0
        elif self.Radio_MVP_Silver.isChecked():
            self.MVP = 0.03
        elif self.Radio_MVP_Gold.isChecked():
            self.MVP = 0.05
        elif self.Radio_MVP_Dia.isChecked():
            self.MVP = 0.1
    def Prev_Des(self):
        if self.Radio_Des0.isChecked():
            self.P_Des = 18
        elif self.Radio_Des1217.isChecked():
            self.P_Des = 12
        elif self.Radio_Des1517.isChecked():
            self.P_Des = 15
        #print(self.P_Des)
        

    def ChangeStarCatch(self):
        if self.StarCatch == 0 :
            self.StarCatch = 1
        else :
            self.StarCatch = 0
    
    def Calc(self):
        self.Ref()
        if self.Lv == 140:
            self.Lv = 0
        elif self.Lv == 150:
            self.Lv = 1
        elif self.Lv == 160:
            self.Lv = 2
        elif self.Lv == 200:
            self.Lv = 3
        else:
            self.Bar.showMessage("레벨제는 140, 150, 160, 200 만 가능")
            return
        for i in range(1,self.Acc+1) :
            self.Bar.showMessage(str(round(i/self.Acc*100,2))+"%")
            f = 0
            self.S = self.S_Save
            self.M = self.M_Save
            if self.S <= 17 and self.S >= self.P_Des :
                self.Tax = 1
            else :
                self.Tax = 0
            tmt = 1 - self.PC - self.MVP
            while self.S < self.Destination and self.M - (self.Pay[self.Lv][self.S]*self.Sunday * self.Tax) - (self.Pay[self.Lv][self.S]*self.Sunday*tmt) >= 0 :

                self.rnd = random.random()
               # print(tmt)
                    
                self.M = self.M - (self.Pay[self.Lv][self.S]*self.Sunday * self.Tax) - (self.Pay[self.Lv][self.S]*self.Sunday*tmt)
                if self.Event15 == 1 and (self.S == 5 or self.S == 10 or self.S == 15) :
                    self.rnd = 0
                if self.rnd <= (self.Suc[self.S] + (self.StarCatch*0.045)) or f == 2 :
                    self.S = self.S + 1
                    if self.Event2 == 1 and self.S <= 10 :
                        self.S = self.S + 1
                    f = 0
                elif 1-self.rnd <=self.Des[self.S] and (self.S < self.P_Des or self.S > 17):
                    self.S = 26
                    self.M = -1
                else:
                    if(self.S > 5 and self.S != 5 and self.S != 10 and self.S != 15 and self.S != 20) :
                        self.S = self.S - 1
                        f = f + 1
                
                if self.S <= 17 and self.S >= self.P_Des :
                     self.Tax = 1
                else :
                     self.Tax = 0
                
            
            self.Res[self.S] = self.Res[self.S] + 1
        
        #print(self.Res[0]/self.Acc)
        self.Lb_S0.setText("0성 확률  " + str(round(self.Res[0]/self.Acc*100,2))+"%")
        self.Lb_S1.setText("1성 확률  " + str(round(self.Res[1]/self.Acc*100,2))+"%")
        self.Lb_S2.setText("2성 확률  " + str(round(self.Res[2]/self.Acc*100,2))+"%")
        self.Lb_S3.setText("3성 확률  " + str(round(self.Res[3]/self.Acc*100,2))+"%")
        self.Lb_S4.setText("4성 확률  " + str(round(self.Res[4]/self.Acc*100,2))+"%")
        self.Lb_S5.setText("5성 확률  " + str(round(self.Res[5]/self.Acc*100,2))+"%")
        self.Lb_S6.setText("6성 확률  " + str(round(self.Res[6]/self.Acc*100,2))+"%")
        self.Lb_S7.setText("7성 확률  " + str(round(self.Res[7]/self.Acc*100,2))+"%")
        self.Lb_S8.setText("8성 확률  " + str(round(self.Res[8]/self.Acc*100,2))+"%")
        self.Lb_S9.setText("9성 확률  " + str(round(self.Res[9]/self.Acc*100,2))+"%")
        self.Lb_S10.setText("10성 확률  " + str(round(self.Res[10]/self.Acc*100,2))+"%")
        self.Lb_S11.setText("11성 확률  " + str(round(self.Res[11]/self.Acc*100,2))+"%")
        self.Lb_S12.setText("12성 확률  " + str(round(self.Res[12]/self.Acc*100,2))+"%")
        self.Lb_S13.setText("13성 확률  " + str(round(self.Res[13]/self.Acc*100,2))+"%")
        self.Lb_S14.setText("14성 확률  " + str(round(self.Res[14]/self.Acc*100,2))+"%")
        self.Lb_S15.setText("15성 확률  " + str(round(self.Res[15]/self.Acc*100,2))+"%")
        self.Lb_S16.setText("16성 확률  " + str(round(self.Res[16]/self.Acc*100,2))+"%")
        self.Lb_S17.setText("17성 확률  " + str(round(self.Res[17]/self.Acc*100,2))+"%")
        self.Lb_S18.setText("18성 확률  " + str(round(self.Res[18]/self.Acc*100,2))+"%")
        self.Lb_S19.setText("19성 확률  " + str(round(self.Res[19]/self.Acc*100,2))+"%")
        self.Lb_S20.setText("20성 확률  " + str(round(self.Res[20]/self.Acc*100,2))+"%")
        self.Lb_S21.setText("21성 확률  " + str(round(self.Res[21]/self.Acc*100,2))+"%")
        self.Lb_S22.setText("22성 확률  " + str(round(self.Res[22]/self.Acc*100,2))+"%")
        self.Lb_S23.setText("23성 확률  " + str(round(self.Res[23]/self.Acc*100,2))+"%")
        self.Lb_S24.setText("24성 확률  " + str(round(self.Res[24]/self.Acc*100,2))+"%")
        self.Lb_S25.setText("25성 확률  " + str(round(self.Res[25]/self.Acc*100,2))+"%")
        self.Lb_S26.setText("파괴 확률  " + str(round(self.Res[26]/self.Acc*100,2))+"%")
        
    
    def TextWindow(self):
        self.Text_M = QLineEdit("0",self)
        self.Text_M.move(200,30)
        self.Text_M.resize(120,30)
        self.Text_S = QLineEdit("0",self)
        self.Text_S.move(200,70)
        self.Text_S.resize(50,30)
        self.Text_D = QLineEdit("25",self)
        self.Text_D.move(430,30)
        self.Text_D.resize(50,30)
        self.Text_L = QLineEdit("0",self)
        self.Text_L.move(430,70)
        self.Text_L.resize(50,30)
        
    def LabelWindow(self):
        self.Lb_L = QLabel("레벨제",self)
        self.Lb_L.move(360,70)
        self.Lb_D = QLabel("목표",self)
        self.Lb_D.move(360,30)
        self.Lb_M = QLabel("보유 메소",self)
        self.Lb_M.move(50,30)
        self.Lb_S = QLabel("시작 스타포스",self)
        self.Lb_S.move(50,70)
        self.Lb_S.resize(200,30)
        self.Lb_S0 = QLabel("0성 확률",self)
        self.Lb_S0.move(50,120)
        self.Lb_S0.resize(160,30)
        self.Lb_S1 = QLabel("1성 확률",self)
        self.Lb_S1.move(50,150)
        self.Lb_S1.resize(160,30)
        self.Lb_S2 = QLabel("2성 확률",self)
        self.Lb_S2.move(50,180)
        self.Lb_S2.resize(160,30)
        self.Lb_S3 = QLabel("3성 확률",self)
        self.Lb_S3.move(50,210)
        self.Lb_S3.resize(160,30)
        self.Lb_S4 = QLabel("4성 확률",self)
        self.Lb_S4.move(50,240)
        self.Lb_S4.resize(160,30)
        self.Lb_S5 = QLabel("5성 확률",self)
        self.Lb_S5.move(50,270)
        self.Lb_S5.resize(160,30)
        self.Lb_S6 = QLabel("6성 확률",self)
        self.Lb_S6.move(50,300)
        self.Lb_S6.resize(160,30)
        self.Lb_S7 = QLabel("7성 확률",self)
        self.Lb_S7.move(200,120)
        self.Lb_S7.resize(160,30)
        self.Lb_S8 = QLabel("8성 확률",self)
        self.Lb_S8.move(200,150)
        self.Lb_S8.resize(160,30)
        self.Lb_S9 = QLabel("9성 확률",self)
        self.Lb_S9.move(200,180)
        self.Lb_S9.resize(160,30)
        self.Lb_S10 = QLabel("10성 확률",self)
        self.Lb_S10.move(200,210)
        self.Lb_S10.resize(160,30)
        self.Lb_S11 = QLabel("11성 확률",self)
        self.Lb_S11.move(200,240)
        self.Lb_S11.resize(160,30)
        self.Lb_S12 = QLabel("12성 확률",self)
        self.Lb_S12.move(200,270)
        self.Lb_S12.resize(160,30)
        self.Lb_S13 = QLabel("13성 확률",self)
        self.Lb_S13.move(200,300)
        self.Lb_S13.resize(160,30)
        self.Lb_S14 = QLabel("14성 확률",self)
        self.Lb_S14.move(360,120)
        self.Lb_S14.resize(160,30)
        self.Lb_S15 = QLabel("15성 확률",self)
        self.Lb_S15.move(360,150)
        self.Lb_S15.resize(160,30)
        self.Lb_S16 = QLabel("16성 확률",self)
        self.Lb_S16.move(360,180)
        self.Lb_S16.resize(160,30)
        self.Lb_S17 = QLabel("17성 확률",self)
        self.Lb_S17.move(360,210)
        self.Lb_S17.resize(160,30)
        self.Lb_S18 = QLabel("18성 확률",self)
        self.Lb_S18.move(360,240)
        self.Lb_S18.resize(160,30)
        self.Lb_S19 = QLabel("19성 확률",self)
        self.Lb_S19.move(360,270)
        self.Lb_S19.resize(160,30)
        self.Lb_S20 = QLabel("20성 확률",self)
        self.Lb_S20.move(360,300)
        self.Lb_S20.resize(160,30)
        self.Lb_S21 = QLabel("21성 확률",self)
        self.Lb_S21.move(520,120)
        self.Lb_S21.resize(160,30)
        self.Lb_S22 = QLabel("22성 확률",self)
        self.Lb_S22.move(520,150)
        self.Lb_S22.resize(160,30)
        self.Lb_S23 = QLabel("23성 확률",self)
        self.Lb_S23.move(520,180)
        self.Lb_S23.resize(160,30)
        self.Lb_S24 = QLabel("24성 확률",self)
        self.Lb_S24.move(520,210)
        self.Lb_S24.resize(160,30)
        self.Lb_S25 = QLabel("25성 확률",self)
        self.Lb_S25.move(520,240)
        self.Lb_S25.resize(160,30)
        self.Lb_S26 = QLabel("파괴 확률",self)
        self.Lb_S26.move(520,270)
        self.Lb_S26.resize(160,30)
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    secondwindow = SeWindow()
    secondwindow.show();
    app.exec_()