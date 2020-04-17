import json
import random
class Boiler_Json_Cmd:

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

