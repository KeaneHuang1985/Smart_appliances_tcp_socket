import json

class SP_Json_Cmd:

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
        dict_function2 = { 'func' : "ATRMAXPOWERMEASUREMENTTHRESHOLD", 'val': 500.00}
        list_function.append(dict_function2)
        dict_functions ={'functions' : list_function}
        dict_data = {'data' :  dict_functions }
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)

    def Signal_Emit_Over_Current(self,targetDeviceId,int_msgid,bolresult):
        list_function = []
        dict_header = {'msgId':int_msgid,'sourceDeviceId':targetDeviceId,'msgType':"signalEmit"}
        dict_function = { 'func' : "SGN OVER CURRENT PROTECTION", 'val': bolresult}
        list_function.append(dict_function)
        dict_functions ={'functions' : list_function}
        dict_data = {'data' :  dict_functions }
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)


    def Disable_Power_Threshold(self,targetDeviceId,int_msgid):
        list_function = []
        dict_header = {
            'msgId'    :   int_msgid,
            'msgType'             :   "sendControlCommand",
            'targetDeviceId'           :   targetDeviceId
        }
        dict_function = { 'func' : "ATRMAXPOWERMEASUREMENTTHRESHOLD", 'val': "0.00"}
        list_function.append(dict_function)
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

    def System_Control(self,targetDeviceId,int_msgid,txtime):
        list_function = []
        dict_header = {
            'msgId'             :   int_msgid,
            'targetDeviceId'    :   targetDeviceId,
            'msgType'           :   "sendSystemControlCommand",
           
        }
        dict_function = { 'func' : "ATR_REPORT_PERIOD", 'val': txtime}
        list_function.append(dict_function)
        dict_functions ={'functions' : list_function}
        dict_data = {'data' :  dict_functions }
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)

    def identifyDevice(self,targetDeviceId,int_msgid):
        dict_header = {
            'msgId'    :   int_msgid,
            'msgType'             :   "identifyDevice",
            'targetDeviceId'           :   targetDeviceId
        }
        dict_data = {'data' : {}}
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)
