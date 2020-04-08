import json

dict_data = {'data' : {}}

class IPcam_Json_Cmd:

    def __init__(self):
        pass

    def P2P_SESSION_AUTHORIZATION(self):
        dict_data = {'auth':'/auth','events':'/events'}
        dict_Payload ={'baseUrl':'ipcam.arcelikiot .com','endpoints': dict_data}
        return json.dumps(dict_Payload)

    def Conn_to_Cloud(self):
        dict_Payload = { 'secondaryToken' : "qwe564wetqwe564y" }
        return json.dumps(dict_Payload,sort_keys=True,indent=2)
        
    def sendSystemControlCommand(self,targetDeviceId,int_msgid,iInterval):
        listDate = []
        dict_header = {'msgId':int_msgid,'msgType':"sendSystemControlCommand",'targetDeviceId':targetDeviceId}
        listDate.append({ 'func' : "”CMD_START_RECORDING", 'val': iInterval}) 
        dict_functions ={'functions' : listDate}
        dict_data = {'data' : dict_functions } 
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)

    def newOtaAvailable(self,targetDeviceId,int_msgid,otaDownloadUrl):
        dict_header = {'msgId':int_msgid,'msgType':"newOtaAvailable",'targetDeviceId':targetDeviceId}
        dict_data_Payload = {'otaDownloadUrl' : otaDownloadUrl}
        dict_data = {'data' : dict_data_Payload } 
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)
    
    def Force_Read_Configuration(self,targetDeviceId,int_msgid):
        dict_header = {'msgId':int_msgid,'msgType':'configurationForceRead','targetDeviceId':targetDeviceId}
        dict_Payload = {'header': dict_header , 'payload' : dict_data }
        return json.dumps(dict_Payload)

    def sendConfigurationCommand(self,targetDeviceId,int_msgid,list_Config):
        # Config about ipcam
        list_config_data = self.Config_date_payload(list_Config) 
        if(list_config_data == False):
            return False
        else:  
            dict_header = {'msgId':int_msgid,'msgType':"newOtaAvailable",'targetDeviceId':targetDeviceId} 
            dict_data = {'data' : list_config_data } 
            dict_Payload = {'header': dict_header , 'payload' : dict_data }
            return json.dumps(dict_Payload)

    def Config_date_payload(self,list_Config):
        list_config_data = []
        if(len(list_Config) == 8):
            list_config_data.append({'config': 'ATR_CAMERA_DAY_NIGHT_MODE','val': list_Config[0]})
            list_config_data.append({'config': 'ATR_CAMERA_SPEAKER_VOLUME','val': list_Config[1]})
            list_config_data.append({'config': 'ATR_CAMERA_MICROPHONE_VOLUME','val': list_Config[2]})
            list_config_data.append({'config': 'ATR_CAMERA_TAKE_SNAPSHOT_IF_EVENT_OCCURS','val': list_Config[3]})
            list_config_data.append({'config': 'ATR_CAMERA_RECORD_VIDEO_IF_EVENT_OCCURS','val': list_Config[4]})
            list_config_data.append({'config': 'ATR_CAMERA_SET_RECORDING_VIDEO_CHANNEL','val': list_Config[5]})
            list_config_data.append({'config': 'ATR_CAMERA_RECORD_TO_SDCARD','val': list_Config[6]})
            list_config_data.append({'config': 'ATR_CAMERA_SAVE_SNAPSHOT_TO_SDCARD','val': list_Config[7]})
            return list_config_data
        else:
            return False
        


