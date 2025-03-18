import socket

SERVER_PORT = 9876

def tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost', SERVER_PORT))
        server_socket.listen(5)
        print(f"Servidor TCP escuchando en el puerto {SERVER_PORT}...")
        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Conexión establecida con: {client_address}")
                message = client_socket.recv(1024).decode()
                response = f"Respuesta del servidor: {message.upper()}"
                client_socket.sendall(response.encode())

tcp_server()