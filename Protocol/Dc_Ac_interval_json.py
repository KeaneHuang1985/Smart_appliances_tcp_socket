import json
import random
class Interval_set_Json_Cmd:

    def __init__(self):
        pass

    def sendSystemControlCommand_event1(self,targetDeviceId,tx,rx,bolactive):
        listDate = []
        dict_header = {'msgId':random.randint(0,999),'msgType':"sendSystemControlCommand",'targetDeviceId':targetDeviceId}
        listDate.append({ 'func' : "ATR_REPORT_PERIOD", 'val': tx}) 
        listDate.append({ 'func' : "ATR_WAKEUP_PERIOD", 'val': rx}) 
        listDate.append({ 'func' : "ATR_DEVICE_ACTIVE", 'val': bolactive}) 
        dict_functions ={'functions' : listDate}
        dict_data = {'data' : dict_functions } 
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)
        
    def sendSystemControlCommand_event2(self,targetDeviceId,tx,rx):
        listDate = []
        dict_header = {'msgId':random.randint(0,999),'msgType':"sendSystemControlCommand",'targetDeviceId':targetDeviceId}
        listDate.append({ 'func' : "ATR_REPORT_PERIOD", 'val': tx}) 
        listDate.append({ 'func' : "ATR_WAKEUP_PERIOD", 'val': rx}) 
        dict_functions ={'functions' : listDate}
        dict_data = {'data' : dict_functions } 
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)

    def sendSystemControlCommand_event3(self,targetDeviceId,tx):
        listDate = []
        dict_header = {'msgId':random.randint(0,999),'msgType':"sendSystemControlCommand",'targetDeviceId':targetDeviceId}
        listDate.append({ 'func' : "ATR_REPORT_PERIOD", 'val': tx}) 
        dict_functions ={'functions' : listDate}
        dict_data = {'data' : dict_functions } 
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)

    def Set_Interval_contorl(self,Type,targetDeviceId,tx,rx,bolactive):
        if(Type == "WS" or Type == "MS"):
            strcmd = self.sendSystemControlCommand_event1(targetDeviceId,tx,rx,bolactive)
        if(Type == "SB" or Type == "TH"):
            strcmd = self.sendSystemControlCommand_event2(targetDeviceId,tx,rx)
        if(Type == "Boiler" or Type == "SP" or Type == "LB"):
            strcmd = self.sendSystemControlCommand_event3(targetDeviceId,tx)
        return strcmd

    
    