import paramiko
import re
import json
import random

class Gengeral_Function:

    def __init__(self):
        self.dict_data = {'data' : {}}
        
    def Commom_msgType(self,imsgevent):
        if(imsgevent == 1):
            return 'identifyDevice'
        if(imsgevent == 2):
            return 'otaAvailable'
        if(imsgevent == 3):
            return 'forceReadAll'
        if(imsgevent == 4):
            return 'startRssiScan'
        if(imsgevent == 5):
            return 'removeDevice'

    def Commom_Cmd(self,targetDeviceId,imsgevent):
        dict_header = {
            'msgId':random.randint(0,999),
            'msgType':self.Commom_msgType(imsgevent), # return msg Type
            'targetDeviceId':targetDeviceId
            } 
        dict_Payload = {'header': dict_header , 'payload' : self.dict_data }
        return json.dumps(dict_Payload)

    def addDevice(self,targetDeviceId,Nodeid,addr_mac,txinterval):
        int_id = Nodeid + 1
        dict_header = {'msgId':random.randint(0,999),'msgType':"addDevice",'targetDeviceId':targetDeviceId}
        dict_dev_info = {  'id' :  hex(int_id)[2:] , 'key' : addr_mac , 'reportInterval' : txinterval}
        dict_dev = {  'device' : dict_dev_info }
        dict_data = {'data' : dict_dev } 
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload),int_id

    def Type_Number_to_Dev_name(self,Typenumber):  
        if(Typenumber == "9591"):
            return "TH"
        if(Typenumber == "9573"):
            return "SB"
        if(Typenumber == "9565"):
            return "MS"
        if(Typenumber == "9568"):
            return "WS"
        if(Typenumber == "9593"):
            return "Boiler"
        if(Typenumber == "9564"):
            return "SP"
        if(Typenumber == "9563"):
            return "LB"
        return False

    def Read_Dev_list(self,Addr_ip):
        Result = self.SSH_Connect_Read_mesh_dev_store(Addr_ip)
        if(Result == False):
            print("Read_mesh_dev_store Fail")
            return False,0
        else:
            List_dev,Max_number_Node = self.parser_dev_info(Result)
            if(List_dev == False):
                print("Not Dev info")
            else:
                for i in range(len(List_dev)):
                    print("No " + str(i) + ": " + List_dev[i])
                return List_dev,int(Max_number_Node,16)
        
    def SSH_Connect_Read_mesh_dev_store(self,Addr_ip):
        try:
            temp = paramiko.SSHClient()
        except paramiko.SSHException as Error:
            print("Error Code:" + str(Error))
            temp.close()
            return False

        temp.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        temp.connect(hostname= Addr_ip, username="root", password="I@T6tw9!+?") 
        ssh_stdin, ssh_stdout, ssh_stderr= temp.exec_command('cat /etc/config/mesh_dev_store') 
        strcmd = ''.join(ssh_stdout.readlines())
        temp.close()
        if(len(strcmd)>0):
            return strcmd
        else:
            return False
       
    def parser_dev_info(self,strlog):
        list_dev = []
        strDev = ""
        listtemp = strlog.splitlines()    
        Find_Max_Node = "1001"
        for i in range(len(listtemp)):
            listData = re.findall(r"\w+",listtemp[i]) 
            if(len(listData[5]) == 4):
                strResult = self.Type_Number_to_Dev_name(listData[5]) # return Type name if not tyep return false
                if(strResult == False):
                    continue
                else:
                    strDev = "Type:" + strResult + ","
                    if(len(listData[1]) == 22):
                        strDev = strDev + "GenID:" + listData[1] +","
                        if(len(listData[0]) == 12):
                            strDev = strDev + "Mac:" + listData[0]
                            list_dev.append(strDev)
                            if(len(listData[4]) == 4):
                                Find_Max_Node = hex(self.Fin_Max_Node(Find_Max_Node,listData[4]))                                     
        if(len(list_dev) == 0):
            return False
        else:
            return list_dev,Find_Max_Node

    def Fin_Max_Node(self,Max_number_Node,Compare):
        Max_Node = int(Max_number_Node,16)
        Compare_node = int(Compare,16)
        if(Max_Node > Compare_node):
            return Max_number_Node
        else:
            return Compare_node

    def rec_parser_sort_json(self,data):
        try:
            m = json.loads(data)
            n = json.dumps(m,sort_keys=True,indent=3)
            return n 
        except Exception as Error:
            print("Error at Rec_parser:" + str(Error))
            return str(data)
            

    

    
        
            
                
        
            
            