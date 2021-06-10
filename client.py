


import socket



class CLIENT:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.11", 30))
    clientName = None
    optionsDic = {:,:,:,:,:,:,:, }
    def __INIT__(self):
        openClient = True
        self.clientName = input('username: ')
        while openClient:
            options = input()
            action = self.optionsDic.get(options)
            action()

