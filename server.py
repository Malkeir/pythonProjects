# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2055))
s.listen(5)

while True:
    clt, adr = s.accept()
    print(f"connection to {adr} established")
    clt.send(bytes(f"socket programming in python", "utf-8"))
    while True:
        msg=clt.recv(32)
        resvmsg=(msg.decode("utf-8"))
        print(resvmsg)
        clt.send(bytes(resvmsg, "utf-8"))
    