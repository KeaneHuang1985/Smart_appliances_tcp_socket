import json
import random
class SP_Json_Cmd:

    def __init__(self):
        pass
    
    def sendControlCommand(self,targetDeviceId,bolT_type):
        list_function = []
        dict_header = {
            'msgId'    :   random.randint(0,999),
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

    def Power_Threshold(self,targetDeviceId,bolresult,intpower):
        list_function = []
        dict_header = {'msgId':random.randint(0,999),'msgType':"sendControlCommand",'targetDeviceId':targetDeviceId}

        if(bolresult == True):
            list_function.append({'func' : "ATR_OPERATIONAL_STATUS", 'val': "False"})
            list_function.append({'func' : "ATR_MAX_POWER_MEASUREMENT_THRESHOLD", 'val':float(intpower)})
        if(bolresult == False):
            list_function.append({'func' : "ATR_MAX_POWER_MEASUREMENT_THRESHOLD", 'val':intpower})
        
        dict_functions ={'functions' : list_function}
        dict_data = {'data' :  dict_functions }
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)

