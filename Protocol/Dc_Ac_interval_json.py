import json

class Interval_set_Json_Cmd:

    def __init__(self):
        pass

    def sendSystemControlCommand_event1(self,targetDeviceId,int_msgid,tx,rx,bolactive):
        listDate = []
        dict_header = {'msgId':int_msgid,'msgType':"sendSystemControlCommand",'targetDeviceId':targetDeviceId}
        listDate.append({ 'func' : "ATR_REPORT_PERIOD", 'val': tx}) 
        listDate.append({ 'func' : "ATR WAKEUP PERIOD", 'val': rx}) 
        listDate.append({ 'func' : "ATR DEVICE ACTIVE", 'val': bolactive}) 
        dict_functions ={'functions' : listDate}
        dict_data = {'data' : dict_functions } 
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload,sort_keys=True,indent=2)
        
    def sendSystemControlCommand_event2(self,targetDeviceId,int_msgid,tx,rx):
        listDate = []
        dict_header = {'msgId':int_msgid,'msgType':"sendSystemControlCommand",'targetDeviceId':targetDeviceId}
        listDate.append({ 'func' : "ATR_REPORT_PERIOD", 'val': tx}) 
        listDate.append({ 'func' : "ATR WAKEUP PERIOD", 'val': rx}) 
        dict_functions ={'functions' : listDate}
        dict_data = {'data' : dict_functions } 
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload,sort_keys=True,indent=2)

    def sendSystemControlCommand_event3(self,targetDeviceId,int_msgid,tx):
        listDate = []
        dict_header = {'msgId':int_msgid,'msgType':"sendSystemControlCommand",'targetDeviceId':targetDeviceId}
        listDate.append({ 'func' : "ATR_REPORT_PERIOD", 'val': tx}) 
        dict_functions ={'functions' : listDate}
        dict_data = {'data' : dict_functions } 
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload,sort_keys=True,indent=2)

    def Set_Interval_contorl(self,Type,targetDeviceId,int_msgid,tx,rx,bolactive):
        if(Type == "WS" or Type == "MS"):
            strcmd = self.sendSystemControlCommand_event1(targetDeviceId,int_msgid,tx,rx,bolactive)
        if(Type == "SB" or Type == "TH"):
            strcmd = self.sendSystemControlCommand_event2(targetDeviceId,int_msgid,tx,rx)
        if(Type == "Boiler" or Type == "SP" or Type == "LB"):
            strcmd = self.sendSystemControlCommand_event3(targetDeviceId,int_msgid,tx)
        return strcmd

    
    