


import socket




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2055))

clientUserName = input('userName: ')

while True:
    msg=s.recv(32)
    resvmsg=(msg.decode("utf-8"))
    if resvmsg.split(':')[0] == clientUserName:
        print (" ")
    else:
        print(resvmsg)
    clientMessage =input(clientUserName +':  ')
    s.send(bytes(clientUserName+':'+clientMessage, "utf-8"))
