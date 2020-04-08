import json

class Boiler_Json_Cmd:

    def __init__(self):
        pass
    
    def sendControlCommand(self,targetDeviceId,int_msgid,bolT_type):
        list_function = []
        dict_header = {
            'msgId'    :   int_msgid,
            'msgType'             :   "sendControlCommand",
            'targetDeviceId'           :   targetDeviceId
        }
        str_type = "OFF"

        if (bolT_type == True):
            str_type = "ON"      
        dict_function1 = { 'func' : "ATR_OPERATIONAL_STATUS", 'val': str_type}
        list_function.append(dict_function1)
        dict_functions ={'functions' : list_function}
        dict_data = {'data' :  dict_functions }
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)
    
    def Force_Read(self,targetDeviceId,int_msgid):

        dict_header = {
            'msgId'             :   int_msgid,
            'targetDeviceId'    :   targetDeviceId,
            'msgType'           :   "forceRead"   
        }
        dict_data = {'data' : {}}
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)
        
    def System_Control(self,targetDeviceId,int_msgid,intValue):
        list_function = []
        dict_header = {
            'msgId'    :   int_msgid,
            'targetDeviceId'           :   targetDeviceId,
            'msgType'             :   "sendSystemControlCommand"
        }
        dict_function1 = { 'func' : "ATR REPORT PERIOD", 'val': intValue}
        list_function.append(dict_function1)
        dict_functions ={'functions' : list_function}
        dict_data = {'data' :  dict_functions }
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)

