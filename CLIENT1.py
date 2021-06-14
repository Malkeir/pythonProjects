
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2030))
        
while resvmsg != 'socket programming in python':
    msg= self.s.recv(32)
    resvmsg=(msg.decode("utf-8"))
    self.s.send(bytes("hello",'utf-8'))

       
            
            
            
            
            