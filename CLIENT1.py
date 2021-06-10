
import socket


class CLIENT:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.11', 30))
        
    def __init__():
        while resvmsg != 'socket programming in python':
            msg= self.s.recv(32)
            resvmsg=(msg.decode("utf-8"))
            self.s.send(bytes("hello",'utf-8'))
    def command(self):
        com = False
        while com != True:
            userinput = input('send message or stop')
            if userinput == 'send':
                self.s.send(bytes("hello",'utf-8'))
            elif userinput == stop:
                com = True
    
client1 = ClIENT.__init__()
client1.command()
            
            
            
            
            