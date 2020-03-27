import os
import sys
import re
import IPy
import socket
import time
import Protocol.Boiler_json as Boiler_json
import Protocol.Light_Bubl_json as Light_Bubl_json
import Protocol.Smart_Plug_json as Smart_Plug_json
import Protocol.Gengeral as Gengeral
import Protocol.Dc_Ac_interval_json as interval_set
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
        self.buffsize = 1024  # 接收資料的快取大小
        self.setupUi(self)
        self.CreateItems()
        self.CreateSignalSlot()
        self.msgid = 1
        self.tempmsgid = 0
        self.ip = ""
        self.int_Max_number_node = 4097
        self.My_Gengral = Gengeral.Gengeral_Function()
        self.My_SP = Smart_Plug_json.SP_Json_Cmd()
        self.My_LB = Light_Bubl_json.LB_Json_Cmd()
        self.MY_Interval = interval_set.Interval_set_Json_Cmd()

    # 設置 Timer 
    def CreateItems(self):  
        # python therad timer 
        t = Timer(5.0,self.Label_Time_Sheet)
        t.start()

    # 設定線槽 
    def CreateSignalSlot(self):
        #== TCP Socket === 
        self.btn_connect.clicked.connect(self.Fn_Socket_Connect)        #Connect TCP Socket
        self.btn_close.clicked.connect(self.Fn_socket_disconnect)       #Disconnet TCP Socket
        self.btn_send_json.clicked.connect(self.Fn_send_json)           #Send msg form TCP Socket
        self.btn_read_mesh_dev.clicked.connect(self.Fn_mesh_dev_store)
        #== Gengeral function 
        self.btn_ac_find.clicked.connect(self.Fn_Find_dev)              # find dev
        self.btn_ota_available.clicked.connect(self.Fn_OTA_Available)   # OTA Available
        self.btn_ready_for_ota.clicked.connect(self.Fn_Ready_OTA)       # Ready_OTA
        self.btn_force_read_all.clicked.connect(self.Fn_ForceReadAll)   # ForceReadall
        self.btn_start_rssi_scan.clicked.connect(self.Fn_startRssiScan) # Start Rssi Scan 
        self.btn_remove_dev.clicked.connect(self.Fn_Remove_devices)     # remove Dev
        self.btn_add_dev.clicked.connect(self.Fn_add_devices)           # add dev
        self.btn_set_interval.clicked.connect(self.Fn_Interval_Set)
        #====== SP / boiler =======
        self.btn_sp_on.clicked.connect(self.Fn_General_ON)              # General ON
        self.btn_sp_off.clicked.connect(self.Fn_General_OFF)            # General OFF
        self.btn_SP_OPC.clicked.connect(self.Fn_OPC_status_Contorl)     # OPC
        #====== LB =======
        self.lb_hz_red_color.valueChanged.connect(self.ChangeColorRed)       # Horizontal slider red
        self.lb_hz_green_color.valueChanged.connect(self.ChangeColorGreen)   # Horizontal slider green
        self.lb_hz_blue_color.valueChanged.connect(self.ChangeColorBlue)     # Horizontal slider blue 
        self.lb_hz_brightness.valueChanged.connect(self.ChangeBrightness)    # Horizontal slider Brightness 
        self.btn_lb_rgb_light_setting.clicked.connect(self.Fn_LB_RGB_Setting)# Setting RGB Color
        self.btn_lb_rgb_brightness.clicked.connect(self.Fn_LB_RGB_Brightness)# Setting RGB Brightness 
        self.btn_lb_white_brghtness.clicked.connect(self.Fn_White_Brightnes) # Setting White Brightness
        self.btn_lb_light_off.clicked.connect(self.Fn_LB_General_OFF)        # Light OFF
        self.btn_lb_light_on.clicked.connect(self.Fn_LB_General_ON)          # Light ON

    # UI Contrl 
    def TCP_Conn_Enable_GB(self,bolresult):
        if(bolresult == True):
            self.GB_LB.setEnabled(True)
            self.GB_SP.setEnabled(True)
            self.GB_Commom.setEnabled(True)
            self.btn_send_json.setEnabled(True)
            self.btn_connect.setEnabled(False)
            self.btn_read_mesh_dev.setEnabled(True)
            self.label_tcp_socket_state.setText("Connect")
        else:
            self.GB_SP.setEnabled(False)
            self.GB_Commom.setEnabled(False)
            self.btn_send_json.setEnabled(False) 
            self.btn_connect.setEnabled(False)
            self.btn_read_mesh_dev.setEnabled(False)
            self.label_tcp_socket_state.setText("Disconnect")

    #========================================#
    #   TCP Socket Function and ssh  connect #
    #========================================#
    def Fn_Socket_Connect(self):  
        if(self.is_ip(self.lineEdit.text())):
            self.TCP_Clinet_Connect(self.ip)
            self.TCP_Clinet_Send(Disable_encryption)
            self.TCP_Conn_Enable_GB(True)
        else:
            print("Tcp socket Connect Fail")
       
    def TCP_Clinet_Connect(self,addr_ip):
        addr = (addr_ip,9090)
        try:
            clientsock.connect(addr)
            return True
        except socket.error as msg:
            print('Failed to Socket connect , Error msg:' + str(msg))
            return False

    def Fn_send_json(self):
        senddata = self.textEdit_Send.toPlainText() # 獲得輸入欄的內容
        self.textEdit_Send.clear() # 清除輸入內容
        if(len(senddata)>0):
            self.TCP_Clinet_Send(senddata)

    def Fn_socket_disconnect(self):
        clientsock.close()
        self.TCP_Conn_Enable_GB(False)
    
    def Fn_mesh_dev_store(self):
        SSh_Read_dev_Store = Gengeral.Gengeral_Function()
        ListDate,self.int_Max_number_node = SSh_Read_dev_Store.Read_Dev_list(self.ip)
        if(ListDate == False):
            return
        else:
            self.cb_Generated_id.clear()
            self.cb_Generated_id.addItems(ListDate)

    # common function             
    def Fn_Find_dev(self):
        self.update_msgid_count()
        self.Fn_Common_function(1) # 1-> find dev
    def Fn_OTA_Available(self):
        self.update_msgid_count()
        self.Fn_Common_function(2) # 2-> OTA Available
    def Fn_Ready_OTA(self):
        self.update_msgid_count()
        self.Fn_Common_function(3) # 3-> Ready OTA 
    def Fn_ForceReadAll(self):
        self.update_msgid_count()
        self.Fn_Common_function(4) # 4-> Force Read All 
    def Fn_startRssiScan(self):
        self.update_msgid_count()
        self.Fn_Common_function(5) # 5-> Force Read All 
    def Fn_Remove_devices(self):
        self.update_msgid_count()
        self.Fn_Common_function(6) # 6 -> Remove devices
    def Fn_add_devices(self):
        self.update_msgid_count()
        self.Fn_Common_function(7) # 7 -> add devices
    def Fn_Interval_Set(self):
        self.update_msgid_count()
        self.Fn_Common_function(8) # 8 -> interval Setting

    def Fn_Common_function(self,ievent):
        if(ievent == 1):
            strcmd = self.My_Gengral.identifyDevice(self.Get_Generated_ID(),self.tempmsgid)
        if(ievent == 2):
            strcmd = self.My_Gengral.OtaAvailable(self.Get_Generated_ID(),self.tempmsgid)
        if(ievent == 3):
            strcmd = self.My_Gengral.readyForOta(self.Get_Generated_ID(),self.tempmsgid)
        if(ievent == 4):
            strcmd = self.My_Gengral.forceReadAll(self.Get_Generated_ID(),self.tempmsgid)
        if(ievent == 5): 
            strcmd = self.My_Gengral.startRssiScan(self.tempmsgid)
        if(ievent == 6): 
            strcmd = self.My_Gengral.removeDevice(self.Get_Generated_ID(),self.tempmsgid)
        if(ievent == 7):
            strcmd,self.int_Max_number_node = self.My_Gengral.addDevice(
                self.Get_Generated_ID(),
                self.tempmsgid,
                self.int_Max_number_node,
                self.lineEdit_onboard_mac.text(),
                self.lineEdit_Report_interval.text()
                )

        if(ievent == 8):
            bolaction = True
            if(self.cb_Action.isChecked == False):
                bolaction = False
            strcmd = self.MY_Interval.Set_Interval_contorl(
                self.Get_Type(),
                self.Get_Generated_ID(),
                self.tempmsgid,
                self.lineEdit_tx.text(),
                self.lineEdit_rx.text(),
                bolaction
                )

        self.TCP_Clinet_Send(strcmd)

    def Get_Generated_ID(self):
        if(len(self.lineEdit_Generated.text()) == 22 ):
            strid = self.lineEdit_Generated.text()
        else:
            print(self.cb_Generated_id.currentText())
            temp_id = re.findall(r"(?<=GenID\:)\w{22}",self.cb_Generated_id.currentText())     
            strid = temp_id[0]
        return strid   

    def Get_Type(self):
        if(len(self.lineEdit_Generated.text()) == 22 ):
            strType = self.lineEdit_Generated.text()
        else:
            print(self.cb_Generated_id.currentText())
            Type = re.findall(r"(?<=Type\:)\w+",self.cb_Generated_id.currentText())     
            strType = Type[0]
        return strType   



    def Fn_General_ON(self):
        self.Fn_General_Ctrl(True,self.Get_Generated_ID())
    def Fn_General_OFF(self):
        self.Fn_General_Ctrl(False,self.Get_Generated_ID())
    def Fn_General_Ctrl(self,Switch,strid):
        if(len(strid) == 22 ):
            self.update_msgid_count()                
            self.TCP_Clinet_Send(self.My_SP.sendControlCommand(strid,self.tempmsgid,Switch))  # SP cmd to TCP Send   
        else:
            print("Generated_ID Len Error ")
    # SP OPC Control 
    def Fn_OPC_status_Contorl(self):
        self.update_msgid_count()
        if(self.rb_sp_enable.isChecked == True):
            self.TCP_Clinet_Send(self.My_SP.Signal_Emit_Over_Current(self.Get_Generated_ID(),self.tempmsgid,True))
        else:
            self.TCP_Clinet_Send(self.My_SP.Signal_Emit_Over_Current(self.Get_Generated_ID(),self.tempmsgid,False))
            
        

    # Light Blub Horizontal slider control RGB and Brightness value*                                                   
    def ChangeColorRed(self):                       
        pos = self.lb_hz_red_color.value()
        self.label_red.setText("Red: " + str(pos))   
    def ChangeColorGreen(self):
        pos = self.lb_hz_green_color.value()
        self.label_green.setText("Green:" + str(pos))
    def ChangeColorBlue(self):
        pos = self.lb_hz_blue_color.value()
        self.label_blue.setText("Blue:" + str(pos))
    def ChangeBrightness(self):
        pos = self.lb_hz_brightness.value()
        self.lb_pb_brightness.setValue(pos)
    def update_msgid_count(self):
        self.tempmsgid = self.msgid 
        self.msgid+=1

    # Setting Light Bulb Config value* 
    def LB_Confige(self,bolswitch,itype,bolBrightness):
        self.update_msgid_count()
        LB_contor_confige = [
                            bolswitch,
                            itype,
                            self.Get_Generated_ID(),
                            self.tempmsgid,
                            self.lb_pb_brightness.value(),
                            bolBrightness,
                            self.lb_hz_red_color.value(),
                            self.lb_hz_green_color.value(),
                            self.lb_hz_blue_color.value()
        ]
        return LB_contor_confige

    def Fn_LB_General_OFF(self):
        self.Fn_LB_Light_Ctrl(self.LB_Confige(False,0,False),1)
    def Fn_LB_General_ON(self):
        self.Fn_LB_Light_Ctrl(self.LB_Confige(True,0,False),1)
    def Fn_LB_RGB_Brightness(self):
        self.Fn_LB_Light_Ctrl(self.LB_Confige(False,1,True),2)
    def Fn_LB_RGB_Setting(self):
        self.Fn_LB_Light_Ctrl(self.LB_Confige(False,1,False),3)
    def Fn_White_Brightnes(self):
        self.Fn_LB_Light_Ctrl(self.LB_Confige(False,0,True),4)

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
            
    def Update_Text_Send_Rec_Text(self,payload):
        self.textEdit_send.setText("")
        #self.textEdit_rec.setText("")
        self.textEdit_send.setText(payload)

    def Label_Time_Sheet(self):
        self.label_Time.setText(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()))

    def TCP_Clinet_Send(self,data):
        try:
            self.Update_Text_Send_Rec_Text(time.strftime("%Y-%m-%d %H:%M:%S : ", time.localtime()) + data)
            clientsock.send(data.encode())  # 傳送訊息
            #recvdata = clientsock.recv(self.buffsize).decode('utf-8')  # 接收訊息，格式轉換
            #self.textEdit_rec.insertPlainText( time.strftime("%Y-%m-%d %H:%M:%S : ", time.localtime()) + recvdata + '\n\r')
        except socket.error as msg:
            print('Socket Error : %s ' %str(msg))
            #Timesheet = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
            #self.textEdit_rec.insertPlainText(Timesheet + " Error Result: " + str(msg) + '\n\r')

    def is_ip(self,ipAddr):
        try:
            IPy.IP(ipAddr)
            self.ip =  ipAddr
            return True
        except Exception as e:
            print("Error msg:" + str(e) )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())


  
