import json


class LB_Json_Cmd:

    def __init__(self):
        pass
    #=========================================================#
    #           RGB Light / White Light Control               #
    #=========================================================#
    # LB_contor_Confige parameter description                 #
    # 0. ON/OFF : Bol                                         #
    # 1. White / RGB Control : 0(white), 1(RGB)               #
    # 2. TargetDeviD: str len == 22                           #
    # 3. msgId : int                                          #
    # 4. Brigthenss : int                                     #
    # 5. Brightness : bol                                     #
    # 6. Red value : int                                      #
    # 7. Green Value : int                                    #
    # 8. Blue Value : int                                     #
    #=========================================================#
    def sendControl_light_Switch_Command(self,confige):
        dict_header = {
            'msgId'            :   confige[3] ,
            'msgType'          :   "sendControlCommand",
            'targetDeviceId'   :   confige[2]
        }
        if (confige[0] == True):
            str_type = "ON"
        else:
            str_type = "OFF"
        dict_function = { 'func' : "ATR_OPERATIONAL_STATUS", 'val': str_type}   
        list_function = []
        list_function.append(dict_function)
        dict_functions ={'functions' : list_function}
        dict_data = {'data' :  dict_functions }
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)
    
    def sendControl_RGB_Brightness_Command(self,confige):
        list_function = []
        dict_header = {
            'msgId'             :   confige[3], # msg id
            'msgType'           :   "sendControlCommand",
            'targetDeviceId'    :   confige[2]  # Id
        }
        dict_function1 = { 'func' : "ATR_BRIGHTNESS", 'val': confige[4]}
        list_function.append(dict_function1)
        dict_functions ={'functions' : list_function}
        dict_data = {'data' :  dict_functions }
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)

    def sendControl_Color_White_Command(self,confige):
        list_function = []
        dict_header = {
            'msgId'             :   confige[3], # msg id
            'msgType'           :   "sendControlCommand",
            'targetDeviceId'    :   confige[2]  # Id
        }
        dict_function1 = { 'func' : "ATR_COLOR_WHITE", 'val': confige[4]}
        list_function.append(dict_function1)
        dict_functions ={'functions' : list_function}
        dict_data = {'data' :  dict_functions }
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)

    def sendControl_RGB_Setting_Command(self,confige):  
        dict_header = {
            'msgId'    :    confige[3],
            'msgType'             :   "sendControlCommand",
            'targetDeviceId'           :   confige[2]
        }
        list_function = []
        dict_ATR_COLOR_RED = { 'func' : "ATR_COLOR_RED", 'val': confige[6]}
        dict_ATR_COLOR_GREEN = { 'func' : "ATR_COLOR_GREEN", 'val': confige[7]}
        dict_ATR_COLOR_BLUE = { 'func' : "ATR_COLOR_BLUE", 'val': confige[8]}
        list_function.append(dict_ATR_COLOR_RED)
        list_function.append(dict_ATR_COLOR_GREEN)
        list_function.append(dict_ATR_COLOR_BLUE)
        dict_functions ={'functions' : list_function}
        dict_data = {'data' :  dict_functions }
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)
    
   
   


