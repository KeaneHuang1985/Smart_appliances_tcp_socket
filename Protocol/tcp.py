import IPy
import socket
import os
import sys
class tcp_socket_clinet:

    def __init__(self):
        self.clientsock = ""
        self.GPIB_Dev = ""
        self.buffsize = 1024
        self.Disable_encryption = "38313139373435313133313534313230D4DDB986B58E2B1A938551E6975B9C334148CD48B3F58919CBF4CD3592450242DEE896FE8B724758ACA2482819ECE42CB68B94E260F1428A645F592D8BDB294D95B0940D7EBB74AD39AA84EF670F8F4938313139373435313133313534313230"
        self.port = 9090
        
    def init_socket_clinet(self):
        try:
            self.clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
            self.clientsocket.settimeout(5)
            return True
        except socket.error as msg:
            print("init Socket Error msg:"+ str(msg))
            return False

    def is_ip(self,ipAddr):
        try:
            IPy.IP(ipAddr)
            return True
        except Exception as msg:
            print("IP format Error result:" + str(msg) )
            return False

    def TCP_socket_Clinet_Connect(self,addr_ip):
        try:
            if(self.is_ip(addr_ip) == True):
                addr = (addr_ip,self.port)
                self.clientsocket.connect(addr)
                self.clientsocket.send(self.Disable_encryption.encode())
                return True
        except socket.error as msg:
            print('Failed to Socket connect , Error msg:' + str(msg.strerror))
            return False
    
    def TCP_socket_Clinet_Disconnect(self):
        try:
            self.clientsocket.close()
            return True
        except socket.error as msg:
            print("Socket Error msg:" +str(msg))
            return False
    
    def TCP_socket_Clinet_Send(self,data):
        '''
        Return Send msg Result 
        '''
        try:
            self.clientsocket.send(data.encode())  # 傳送訊息
            return True   
        except socket.error as msg:
            print('TCP Socket Clinet Error : %s ' %str(msg))
            return False
    
    def TCP_socket_Clinet_Rec(self):
        '''
        Return 
        '''
        try:
            rec_data = self.clientsocket.recv(self.buffsize).decode('utf-8')  # 接收訊息，格式轉換
            return rec_data
        except socket.error as msg:
            print("Socket Error :  " + str(msg))
            return False
            