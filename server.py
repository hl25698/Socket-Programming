import socket
import threading
import random

# Server configuration
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
client_name = "Client of Hannah"
server_name = "Server of Hannah"


# Handle single client connection
def handle_client(client_socket, server_socket):
    try:
        # Receive client data
        data = client_socket.recv(1024).decode()
        print("[Server]: Received data from client")
        if not data:
            return
        
        # Extract client data
        try:
            client_name, client_number = data.split(":")
            client_number = int(client_number)
        except ValueError:
            print("[Error]: not enough values to unpack (expected 2, got 1)")
            client_socket.close()
            return

        # Check if client number is out of range
        if not (1 <= client_number <= 100):
            print("[Error]: Client number out of range. Terminating server.")
            errormsg = "Number out of range. Terminating server."
            client_socket.send(errormsg.encode())
            print("[Server]: Sent error message to client")
            client_socket.close()
            server_socket.close()
            raise SystemExit

        # Print client data
        print(f"\n[Client Name]: {client_name}")
        print(f"[Server Name]: {server_name}")

        # Generate random number
        server_number = random.randint(1, 100)
        print(f"[Client Number]: {client_number}")
        print(f"[Server Number]: {server_number}")
        print(f"[Sum]: {client_number + server_number}")

        # Send sum to client
        response = f"{client_name}:{server_number}"
        client_socket.send(response.encode())
        print("[Server]: Sent sum to client")

        # Close client connection
        client_socket.close()
        print("[Server]: Closed client connection")
    except ValueError:
        print("[Error]: Invalid data received from client. Terminating server.")
        client_socket.close()

# Main server function
def start_server():
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"{server_name}")
    print(f"[Server Started]: Listening on {SERVER_HOST}:{SERVER_PORT}")

    try:
        # Accept client connections
        while True:
            try:
                client_socket, client_address = server_socket.accept()
                print("[Server]: Accepted connection from client")
                client_thread = threading.Thread(target=handle_client, args=(client_socket, server_socket))
                client_thread.start()
            except OSError:
                break
    except SystemExit:
        print("[Server Terminated]")
    finally:
        server_socket.close()
        print("[Server]: Closed server socket")

# Start server
if __name__ == "__main__":
    start_server()