import socket

# Client configuration
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001

def start_client():
    client_name = "Client of Hannah"
    server_name = "Server of Hannah"
    
    # Get user input
    client_number = int(input("Enter an integer (1-100): "))

    # Print client name and input number
    print(f"Client Name: {client_name}")
    print(f"Client Number: {client_number}")

    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try: 
        # Print client name and input number

        print(f"Connecting to server at {SERVER_HOST}:{SERVER_PORT}...")
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("[Client]: Connected to server")

        # Send client data
        message = f"{client_name}:{client_number}"
        client_socket.send(message.encode())
        print("[Client]: Sent data to server")

        # Receive server data
        server_data = client_socket.recv(1024).decode()
        print("[Client]: Received data from server")

        # Check if server sent an error message
        if "Terminating server" in server_data:
            print(f"[Error from server]: {server_data}")
        else:
            # Extract server data
            client_name, server_number = server_data.split(":")
            server_number = int(server_number)

            # Print server data
            print(f"\n[Client Connected]: {client_name}")
            print(f"[Server Name]: {server_name}")
            print(f"[Client Number]: {client_number}")
            print(f"[Server Number]: {server_number}")
            print(f"[Sum]: {client_number + server_number}")

    except Exception as e:
        print(f"[Error]: {e}")
    finally:
        # Close client connection        
        client_socket.close()
        print("[Client]: Closed client connection")

# Start client
if __name__ == "__main__":
    start_client()