import socket

def create_socket():
    return socket.socket()

def connect_to_server(host, port=8080):
    try:
        s = create_socket()
        s.connect((host, port))
        print(f'Connected to chat server at {host}:{port}')
        return s
    except socket.error as e:
        print(f'Failed to connect to {host}:{port}')
        print(f"Error: {e}")
        return None

def receive_message(sock, buffer_size=1024):
    try:
        message = sock.recv(buffer_size).decode()
        print('Server:', message)
    except socket.error as e:
        print(f"Failed to receive message. Error: {e}")

def send_message(sock):
    message = input('>> ')
    if message.lower() == 'exit':
        sock.close()
        print('Disconnected from server.')
        return False
    try:
        sock.send(message.encode())
        print('Message sent.')
    except socket.error as e:
        print(f"Failed to send message. Error: {e}")
        return False
    return True

def main():
    host = input('Enter hostname or host IP: ')
    port = input('Enter port (default 8080): ')
    port = int(port) if port else 8080
    client_socket = connect_to_server(host, port)
    
    if client_socket:
        while True:
            receive_message(client_socket)
            if not send_message(client_socket):
                break

if __name__ == '__main__':
    main()