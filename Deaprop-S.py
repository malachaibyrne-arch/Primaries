# Start of program ---

#Spacing and syntax --
TAB1 = '\n'
TAB2 = '\n\n'
TAB3 = '\n\n\n'
Tab4 = '\n\n\n\n'

## Libraries and module installs

import socket
from cryptography.fernet import Fernet

#Create the files for the secret Key.
try:
    #Attempt to open the Sec-Key file
    with open("secret.key", 'rb') as Key_File:
        key = Key_File.read()

except FileNotFoundError: #If the file is not there, create one and write it to the secret.key file.
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as Key_File:
        Key_File.write(key)

#Init the cypher engine -
Scrample = Fernet(key)

# Conigure the server for E2EE communication. ('def main')

def main():
    # Server-Side Config
    host = input(f'{TAB3} Host Address --> ')
    port = int(input("Port -->"))
    print("\nInitialising Server Configurations... ")
    print("\nInitialising Server Configurations:")
    print(TAB2 + "Host machine:" + host)
    print(f"Connection Bind: {port} \n\n")

    #Server's Calibration settigs ->>
    Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates an IPv4 TCP Socket.
    print("Socket Type: IPv4")
    Server_Socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allows for the reuse of ports if prg suddenly closes.
    print("\nPort Reuse: Allow")
    Server_Socket.bind((host, port)) # binds the host address and the port together
    print("Bind: Active... Initialization Success!" + TAB2)
    
    #recieving a connection
    Server_Socket.listen(5)  # queue up to 5 connection requests
    print(f"Server is listening on {host}:{port}...")
    conn, address = Server_Socket.accept()  # accept new connection
    print(TAB1 + "Connection from: " + str(address))

    # Bi-directional communication loop
    while True:
        # Receive encrypted data from client
        encrypted_data = conn.recv(1024)
        if not encrypted_data:
            break
        
        # Decrypt and display
        decrypted_message = Scrample.decrypt(encrypted_data).decode('utf-8')
        print(f"\nClient -> {decrypted_message}")

        # Send response back
        message = input(f"\nHost@{host}-> ")
        if message.lower() == 'exit':
            break
        
        encrypted_response = Scrample.encrypt(message.encode('utf-8'))
        conn.sendall(encrypted_response)

    conn.close()  # close the connection
    Server_Socket.close()  # close the listening socket


if __name__ == '__main__':
    main()

# End of program ---