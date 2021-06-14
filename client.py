


import socket




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2055))

msg=s.recv(32)
resvmsg=(msg.decode("utf-8"))
print(resvmsg)

while True:
    clientMessage =input("Message:  ")
    s.send(bytes(clientMessage, "utf-8"))
