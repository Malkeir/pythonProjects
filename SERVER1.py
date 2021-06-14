# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket


class COMSSERVER:

    def ComsInit(message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), 55))
        s.listen(5)
        while True:
                clt, adr = s.accept()
                print(f"connection to {adr} established")
                clt.send(bytes(f"socket programming in python", "utf-8"))
                msg = s.recv(32)

    def recieveInformation(self,LISTOFINFO):
        while ms != 'hi':
            msg = s.recv(32)
            ms = msg.decode("utf-8")
        return True


serv = COMSSERVER.ComsInit('connected')

if (serv.recieveInformation()):
    print('message recieved')