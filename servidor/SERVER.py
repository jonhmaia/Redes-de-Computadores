import socket
import os

# Obtém o diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.join(current_dir, "root_folder")

# Cria um socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))  # Altera a porta para 8080
server_socket.listen(1)  # Espera por conexões

print("Servidor pronto para receber conexões...")
print("Acesse o servidor em: http://localhost:8080/")  # Imprime o link de acesso

while True:
    # Aceita uma nova conexão
    client_socket, client_address = server_socket.accept()

    # Recebe a requisição HTTP
    request = client_socket.recv(1024).decode()

    # Analisa a requisição para determinar o arquivo solicitado
    if request.startswith("GET"):
        file_requested = request.split()[1]
        if file_requested == "/":
            file_requested = "/index.html"

        file_path = os.path.join(root_folder, file_requested[1:])  # Remove a barra inicial do caminho
        print("Solicitado:", file_path)  # Adiciona esta linha para debug

        try:
            # Tenta abrir o arquivo solicitado
            with open(file_path, "rb") as file:
                content = file.read()

            # Cria a resposta HTTP com sucesso
            response = "HTTP/1.1 200 OK\r\n\r\n".encode() + content
        except FileNotFoundError:
            # Se o arquivo não for encontrado, retorna o erro 404 Not Found
            response = "HTTP/1.1 404 Not Found\r\n\r\n".encode() + b"404 Not Found"

        # Envia a resposta de volta ao cliente
        client_socket.sendall(response)

    # Fecha o socket do cliente
    client_socket.close()
