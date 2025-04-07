import socket;(s:=socket.socket()).connect(("127.0.0.1",12000))
while 1:
    print(s.recv(500).decode(),end="")
    if (c:=input())[:4]=="exit":break
    s.send(c.encode())
s.close()