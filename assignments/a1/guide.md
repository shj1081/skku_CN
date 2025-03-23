# Homework 1

## Assignment Requirements

1. **Implement in Two Ways**

   - TCP-based Client-Server
   - UDP-based Client-Server

2. **Server and Client in Different Languages**

   - Example: Python server, C++ client

3. **Functionality**

   1. The client sends an expression, e.g., `10+5-3`
   2. The server receives the expression and parses it for calculation (do not use built-in libraries like `eval`)
   3. The server sends the calculation result back to the client
   4. The client saves the received result in `result.txt` in the format "expression and result"

4. **Network Information**

   - IP: `127.0.0.1` (localhost)
   - Port number: `12000`

5. **How to Run the Program**

   1. **Navigate to the Project Directory**:
      Open your terminal and change the directory to where your assignment files are located:

      ```bash
      cd /path/to/hw1
      ```

   2. **Compile the Code**:
      Use the `Makefile` to compile both the TCP and UDP client programs. Run the following command:

      ```bash
      make
      ```

      This will generate the executables `tcp-client.o` and `udp-client.o`.

   3. **Run the TCP Server**:
      Open a terminal window and run the TCP server:

      ```bash
      python3 tcp-server.py
      ```

      This will start the TCP server, which listens for incoming connections.

   4. **Run the TCP Client**:
      In another terminal window, run the TCP client:

      ```bash
      ./tcp-client.o
      ```

      Enter an expression when prompted (e.g., `10+5-3`). The client will send this expression to the server.

   5. **Check the Result**:
      After the server processes the expression, it will send back the result. The client will save the expression and the result in `result.txt`. You can check the contents of `result.txt` to see the output.

   6. **Run the UDP Server** (if needed):
      If you want to test the UDP functionality, open another terminal window and run the UDP server:

      ```bash
      python3 udp-server.py
      ```

   7. **Run the UDP Client**:
      In another terminal window, run the UDP client:
      ```bash
      ./udp-client.o
      ```
      Again, enter an expression when prompted. The UDP client will send the expression to the server and receive the result.

6. **Expression Limitations**
   - Only integers, addition (+), and subtraction (-) are included
   - Complex operations and parentheses are not considered

## Implementation Roadmap

1. **TCP Version**

   - **Server (Python)**
     1. Create a TCP socket with `socket(AF_INET, SOCK_STREAM)`
     2. Execute `bind` and `listen`, then wait for client connections
     3. Receive the client's expression string and parse/calculate it
     4. Send the result to the client
   - **Client (C++)**
     1. Initialize Winsock and create a TCP socket
     2. `connect` to the server
     3. Get the expression from the user and send it to the server
     4. Receive the result sent by the server and save it in `result.txt`

2. **UDP Version**
   - **Server (Python)**
     1. Create a UDP socket with `socket(AF_INET, SOCK_DGRAM)`
     2. `bind` and wait for datagram reception
     3. Receive the client's expression string, parse/calculate it
     4. Send the calculation result back using `sendto`
   - **Client (C++)**
     1. Initialize Winsock and create a UDP socket
     2. Use server IP/port information to `sendto`
     3. Receive the result sent by the server using `recvfrom`
     4. Save the result in `result.txt`
