import os
import sys
import re
import IPy
import socket
import random
import time
# import 
import Protocol.Boiler_json as Boiler_json
import Protocol.Light_Bubl_json as Light_Bubl_json
import Protocol.Smart_Plug_json as Smart_Plug_json
import Protocol.Gengeral as Gengeral
import Protocol.Dc_Ac_interval_json as interval_set
import Protocol.tcp as tcp_socket
from threading import Timer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
#from Ui_untitled1 import Ui_MainWindow
from UI.Ui_MainUI import Ui_MainWindow

clientsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
clientsock.settimeout(5)
Disable_encryption = "38313139373435313133313534313230D4DDB986B58E2B1A938551E6975B9C334148CD48B3F58919CBF4CD3592450242DEE896FE8B724758ACA2482819ECE42CB68B94E260F1428A645F592D8BDB294D95B0940D7EBB74AD39AA84EF670F8F4938313139373435313133313534313230" 

class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.buffsize = 1024 # 接收資料的快取大小
        self.ip = "" # inite IP
        self.setupUi(self)
        self.CreateItems()
        self.CreateSignalSlot()
        self.int_Max_number_node = 4097 # Node number hex 1001
        self.My_Gengral = Gengeral.Gengeral_Function()
        self.My_SP = Smart_Plug_json.SP_Json_Cmd()
        self.My_LB = Light_Bubl_json.LB_Json_Cmd()
        self.My_tcp_clinet = tcp_socket.tcp_socket_clinet()
        self.MY_Interval = interval_set.Interval_set_Json_Cmd()
        self.bolDisable_encryption = False
        self.bolable_Rec = True

    def CreateItems(self): # 設置 Timer 
        t = Timer(5.0,self.Label_Time_Sheet) # python therad timer 
        t.start()

    def CreateSignalSlot(self):  # 設定線槽
        #== TCP Socket === 
        self.btn_connect.clicked.connect(self.Fn_Socket_Connect)        #Connect TCP Socket
        self.btn_close.clicked.connect(self.Fn_Socket_Disconnect)       #Disconnet TCP Socket
        #== Gengeral function 
        self.btn_ac_find.clicked.connect(self.Fn_Find_dev)              # find dev
        self.btn_ota_available.clicked.connect(self.Fn_OTA_Available)   # OTA Available
        self.btn_force_read_all.clicked.connect(self.Fn_ForceReadAll)   # ForceReadall
        self.btn_start_rssi_scan.clicked.connect(self.Fn_startRssiScan) # Start Rssi Scan 
        self.btn_remove_dev.clicked.connect(self.Fn_Remove_devices)     # remove Dev
        self.btn_add_dev.clicked.connect(self.Fn_add_devices)           # add dev
        self.btn_set_interval.clicked.connect(self.Fn_Interval_Set)     # Set Interval 
        self.btn_clear.clicked.connect(self.Fn_Text_Clear_Send_Rec)     # Clear Text
        self.btn_send_json.clicked.connect(self.Fn_send_json)           #Send msg form TCP Socket
        self.btn_read_list.clicked.connect(self.Fn_mesh_dev_store)      #update devices list
        self.cb_Generated_id.currentTextChanged.connect(self.Fn_Updata_Info)
        #====== SP / boiler =======
        self.btn_sp_on.clicked.connect(self.Fn_General_ON)              # General ON
        self.btn_sp_off.clicked.connect(self.Fn_General_OFF)            # General OFF
        self.btn_SP_OPC.clicked.connect(self.Fn_OPC_status_Contorl)     # OPC
        #====== LB =======
        self.dial_red.valueChanged.connect(self.ChangeColorRed)       # Horizontal slider red
        self.dial_green.valueChanged.connect(self.ChangeColorGreen)   # Horizontal slider green
        self.dial_blue.valueChanged.connect(self.ChangeColorBlue)     # Horizontal slider blue 
        self.dial_br.valueChanged.connect(self.ChangeBrightness)              # Horizontal slider Brightness 
        self.dial_rgb_br.valueChanged.connect(self.ChangeRGBBrightness)       # Horizontal slider Brightness 
        self.btn_lb_rgb_light_setting.clicked.connect(self.Fn_LB_RGB_Setting) # Setting RGB Color
        self.btn_lb_rgb_brightness.clicked.connect(self.Fn_LB_RGB_Brightness) # Setting RGB Brightness 
        self.btn_lb_white_brghtness.clicked.connect(self.Fn_White_Brightnes)  # Setting White Brightness
        self.btn_lb_light_off.clicked.connect(self.Fn_LB_General_OFF)         # Light OFF
        self.btn_lb_light_on.clicked.connect(self.Fn_LB_General_ON)           # Light ON
        # Light bulb Auto RGB Test
        self.btn_auto_rgb_test.clicked.connect(self.Fn_LB_Auot_RGB_Test)        # color test
        self.btn_auto_rgb_br_test.clicked.connect(self.Fn_LB_Auto_RGB_BR_Test)  # brghtness test
        self.btn_auto_LB_Switch.clicked.connect(self.Fn_LB_Auto_Switch_Test)    # Genral ON OFF
        # SP and Boiler Auto Test 
        self.btn_sp_boiler_auot_Switch.clicked.connect(self.Fn_Auto_Switch_Test) # Genral ON OFF

    def TCP_Conn_Enable_GB(self,bolresult): # UI Contrl 
        if(bolresult == True):
            self.GB_LB.setEnabled(True)
            self.GB_SP.setEnabled(True)
            self.GB_Commom.setEnabled(True)
            self.GB_Setting.setEnabled(True)
            self.btn_send_json.setEnabled(True)
            self.btn_connect.setEnabled(False)
            self.label_tcp_socket_state.setText("Connect")
        else:
            self.GB_SP.setEnabled(False)
            self.GB_Commom.setEnabled(False)
            self.GB_LB.setEnabled(False)
            self.GB_Setting.setEnabled(False)
            self.btn_send_json.setEnabled(False)
            self.btn_connect.setEnabled(True)
            self.label_tcp_socket_state.setText("Disconnect")
        
    def Fn_Socket_Connect(self):
        self.ip = self.lineEdit.text()
        if(self.My_tcp_clinet.init_socket_clinet() == True):
            if(self.My_tcp_clinet.TCP_socket_Clinet_Connect(self.ip)):
                self.Fn_mesh_dev_store()      # update devices list
                self.TCP_Conn_Enable_GB(True)
            else:
                self.label_tcp_socket_state.setText("Connect Socket Fail")
        else:
            self.label_tcp_socket_state.setText("Init Socket Fail")
    
    def Fn_Socket_Disconnect(self):
        self.My_tcp_clinet.TCP_socket_Clinet_Disconnect()
        self.TCP_Conn_Enable_GB(False)
    
    def Fn_send_json(self):
        strdata = self.textEdit_Send.toPlainText() # 獲得輸入欄的內容
        self.textEdit_Send.clear() # 清除輸入內容
        if(len(strdata)>0):
            if(self.My_tcp_clinet.TCP_socket_Clinet_Send(strdata)):
                bolresult = self.My_tcp_clinet.TCP_socket_Clinet_Rec()
                if(bolresult != False):
                    self.textEdit_rec.setText(self.My_Gengral.rec_parser_sort_json(bolresult))
                        
    def Fn_mesh_dev_store(self):
        ListDate,self.int_Max_number_node = self.My_Gengral.Read_Dev_list(self.ip)
        if(ListDate != False):
            self.cb_Generated_id.clear()
            self.cb_Generated_id.addItems(ListDate)

    def Fn_Updata_Info(self):
        self.label_type.setText(self.Get_Generated_ID(2))
        self.label_mac.setText(self.Get_Generated_ID(3))
        self.label_targetid.setText(self.Get_Generated_ID(1))

    # common function             
    def Fn_Find_dev(self):          # 1-> find dev 
        self.Fn_Common_function(1) 
    def Fn_OTA_Available(self):     # 2-> OTA Available
        self.Fn_Common_function(2)
    def Fn_ForceReadAll(self):      # 4-> Force Read All 
        self.Fn_Common_function(3) 
    def Fn_startRssiScan(self):     # 5-> start Rssi Scan
        self.Fn_Common_function(4) 
    def Fn_Remove_devices(self):    # 6 -> Remove devices
        self.Fn_Common_function(5) 
    def Fn_add_devices(self):       # 7 -> add devices
        self.Fn_Common_function(6) 
    def Fn_Interval_Set(self):      # 8 -> interval Setting    
        self.Fn_Common_function(7) 

    def Fn_Common_function(self,ievent):
        if(ievent == 1 or ievent == 2 or ievent == 3 or ievent == 4 or ievent == 5):
            strcmd = self.My_Gengral.Commom_Cmd(self.Get_Generated_ID(1),ievent)
        if(ievent == 6):
            strcmd,self.int_Max_number_node = self.My_Gengral.addDevice(
                self.Get_Generated_ID(1),
                self.int_Max_number_node,
                self.lineEdit_onboard_mac.text(),
                self.lineEdit_Report_interval.text()
                )
        if(ievent == 7):
            bolaction = True
            if(self.cb_Action.isChecked == False):
                bolaction = False
            strcmd = self.MY_Interval.Set_Interval_contorl(
                self.Get_Generated_ID(2),
                self.Get_Generated_ID(1),
                self.spinBox_tx.value(),
                self.spinBox_rx.value(),
                bolaction
                )
        self.TCP_Clinet_Send(strcmd)

    def Fn_General_ON(self):
        self.Fn_General_Ctrl(True,self.Get_Generated_ID(1))
    def Fn_General_OFF(self):
        self.Fn_General_Ctrl(False,self.Get_Generated_ID(1))
    def Fn_General_Ctrl(self,Switch,strid):           
        self.TCP_Clinet_Send(self.My_SP.sendControlCommand(strid,Switch))    

    def Fn_Auto_Switch_Test(self):
        offset = 0 
        index = self.spinBox_sp_boiler_value.value()
        while(offset < index ):
            self.Fn_General_Ctrl(True,self.Get_Generated_ID(1))
            time.sleep(3)
            self.Fn_General_Ctrl(False,self.Get_Generated_ID(1))
            offset += 1
            
    # SP OPC Control 
    def Fn_OPC_status_Contorl(self):
        if(self.cb_sp_enable.isChecked()):
            self.TCP_Clinet_Send(self.My_SP.Power_Threshold(self.Get_Generated_ID(1),True,self.spinBox_sp_power.value()))
        else:
            self.TCP_Clinet_Send(self.My_SP.Power_Threshold(self.Get_Generated_ID(1),False,0))
        
    # Light Blub Horizontal slider control RGB and Brightness value*                                                   
    def ChangeColorRed(self):                       
        self.label_red_val.setText(str(self.dial_red.value()))
    def ChangeColorGreen(self):
        self.label_green_val.setText(str(self.dial_green.value()))
    def ChangeColorBlue(self):
        self.label_blue_val.setText(str(self.dial_blue.value()))
    def ChangeBrightness(self):
        self.lb_pb_brightness.setValue(self.dial_br.value())
        self.label_white_br.setText(str(self.dial_br.value()))
    def ChangeRGBBrightness(self):
        self.lb_pb_rgbbrightness.setValue(self.dial_rgb_br.value())

    # Setting Light Bulb Config value* 
    def Fn_LB_Light_Ctrl(self,confige,ievent):
        if(len(confige)==0):
            return      
        else:
            if(ievent == 1):    # ievent 1 : ON/OFF                      
                strcmd = self.My_LB.sendControl_light_Switch_Command(confige)        
            if(ievent == 2):    # ievent 2 : Setting RGB Brightness              
                strcmd = self.My_LB.sendControl_RGB_Brightness_Command(confige)                                       
            if(ievent == 3):    # ievent 3 : Setting RGB color                 
                strcmd = self.My_LB.sendControl_RGB_Setting_Command(confige) 
            if(ievent == 4):    # ievent 4 : Setting White Brightness
                strcmd = self.My_LB.sendControl_Color_White_Command(confige)
        self.TCP_Clinet_Send(strcmd)
        print(strcmd)
   
    # Create LB Cmd 
    def Fn_LB_General_OFF(self):
        self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige(False,0,self.lb_pb_brightness.value(),self.Get_Generated_ID(1),self.dial_red.value(),self.dial_green.value(),self.dial_blue.value()),1)
    def Fn_LB_General_ON(self):
        self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige(True,0,self.lb_pb_brightness.value(),self.Get_Generated_ID(1),self.dial_red.value(),self.dial_green.value(),self.dial_blue.value()),1)
    def Fn_LB_RGB_Brightness(self):
        self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige(False,1,self.lb_pb_rgbbrightness.value(),self.Get_Generated_ID(1),self.dial_red.value(),self.dial_green.value(),self.dial_blue.value()),2)
    def Fn_LB_RGB_Setting(self):
        self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige(False,1,self.lb_pb_rgbbrightness.value(),self.Get_Generated_ID(1),self.dial_red.value(),self.dial_green.value(),self.dial_blue.value()),3)
    def Fn_White_Brightnes(self):
        self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige(False,0,self.lb_pb_brightness.value(),self.Get_Generated_ID(1),self.dial_red.value(),self.dial_green.value(),self.dial_blue.value()),4)

    def Fn_LB_Auto_Switch_Test(self):
        offset = 0  
        index = int(self.spinBox_LB_Count.value())
        targetid = self.Get_Generated_ID(1)
        while(offset < index):
            print("Test Count:" + str(offset))
            self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige(False,0,100,targetid,255,255,255),1)
            time.sleep(3)
            self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige(True,0,100,targetid,255,255,255),1)
            time.sleep(3)
            offset +=1
        self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige_for_Auto_test(targetid,100,255,255,255),3)


    def Fn_LB_Auto_RGB_BR_Test(self):
        offset = 1
        index = 100
        targetid = self.Get_Generated_ID(1)
        self.bolable_Rec = False

        while(offset < index):
            self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige_for_Auto_test(targetid,offset,255,255,100),3)
            time.sleep(1)
            offset += 10
            offset = offset if offset < 100 else 100
        offset = 1 

        while(offset < index):
            self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige_for_Auto_test(targetid,offset,255,100,255),3)
            time.sleep(1)
            offset += 10
            offset = offset if offset < 100 else 100
        offset = 1 
    
        while(offset < index):
            self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige_for_Auto_test(targetid,offset,100,255,255),3)
            time.sleep(1)
            offset += 10
            offset = offset if offset < 100 else 100
        offset = 1 

    def Fn_LB_Auot_RGB_Test(self):
        offset = 1
        index = 255
        targetid = self.Get_Generated_ID(1)
        self.bolable_Rec = False
        while(offset < index):
            self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige_for_Auto_test(targetid,100,255,offset,0),3)
            time.sleep(1)
            offset += 10
            offset = offset if offset < 255 else 255
        offset = 1
        while(offset < index):
            self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige_for_Auto_test(targetid,100,0,255,offset),3)
            time.sleep(1)
            offset += 10
            offset = offset if offset < 255 else 255
        offset = 1
        while(offset < index):
            self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige_for_Auto_test(targetid,100,offset,0,255),3)
            time.sleep(1)
            offset += 10
            offset = offset if offset < 255 else 255
        offset = 1 
        self.Fn_LB_Light_Ctrl(self.My_LB.LB_Confige_for_Auto_test(targetid,100,255,255,255),3)

    def Fn_Text_Clear_Send_Rec(self):
        self.textEdit_rec.setText("")
        self.textEdit_send.setText("")

    def Update_Text_Send_Rec_Text(self,payload):
        self.textEdit_send.setText("")
        self.textEdit_rec.setText("")
        self.textEdit_send.setText(payload)

    def Label_Time_Sheet(self):
        self.label_Time.setText(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))

    def TCP_Clinet_Send(self,data):
        try:
            self.My_tcp_clinet.TCP_socket_Clinet_Send(data)
            self.Update_Text_Send_Rec_Text(time.strftime("%Y-%m-%d %H:%M:%S:\r\n", time.localtime()) + self.My_Gengral.rec_parser_sort_json(data) +'\n\r')
            recvdata = self.My_tcp_clinet.TCP_socket_Clinet_Rec()
            self.textEdit_rec.insertPlainText( time.strftime("%Y-%m-%d %H:%M:%S :\r\n", time.localtime()) + self.My_Gengral.rec_parser_sort_json(recvdata) + '\n\r')
        except socket.error as msg:
            Timesheet = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
            self.textEdit_rec.insertPlainText(Timesheet + " Error Result: " + str(msg) + '\n\r')

    def Get_Generated_ID(self,itype):
        '''
        itype option target id = 1,dev type = 2, mac = 3
        '''
        if(itype == 1): # Target id
            pattern = r"(?<=GenID\:)\w{22}"
        if(itype == 2): # dev type
            pattern = r"(?<=Type\:)\w+"
        if(itype == 3): # mac 
            pattern = r"(?<=Mac\:)\w{12}"
        try:
            if(len(self.lineEdit_Generated.text()) == 22 ):
                strid = self.lineEdit_Generated.text()
            else:
                temp_id = re.findall(pattern,self.cb_Generated_id.currentText())     
                strid = temp_id[0]
            return strid
        except Exception as msg:
            print(str(msg)) 
            return 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())


  
