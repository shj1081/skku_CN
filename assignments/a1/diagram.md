# Assignment 1 Communication Flow Diagrams

## TCP Client-Server Communication

```mermaid
sequenceDiagram
    participant Client as C++ TCP Client
    participant Server as Python TCP Server
    participant File as result.txt
    
    Note over Client: Create TCP socket
    Note over Server: Create TCP socket<br/>with socket(AF_INET, SOCK_STREAM)<br/>Bind to port 12000<br/>Listen for connections
    
    Client->>Server: Connect to server
    
    Note over Client: Get expression from user<br/>(e.g., "10+5-3")
    Client->>Server: Send expression
    
    Note over Server: Receive expression<br/>Parse and calculate result<br/>without using eval()
    
    Server->>Client: Send calculation result
    
    Note over Client: Receive result
    Client->>File: Write "expression = result"
    
    Note over Client, Server: Connection closed
```

## UDP Client-Server Communication

```mermaid
sequenceDiagram
    participant Client as C++ UDP Client
    participant Server as Python UDP Server
    participant File as result.txt
    
    Note over Client: Create UDP socket
    Note over Server: Create UDP socket<br/>with socket(AF_INET, SOCK_DGRAM)<br/>Bind to port 12000
    
    Note over Client: Get expression from user<br/>(e.g., "10+5-3")
    Client->>Server: Send expression using sendto()
    
    Note over Server: Receive expression<br/>with recvfrom()<br/>Parse and calculate result<br/>without using eval()
    
    Server->>Client: Send calculation result using sendto()
    
    Note over Client: Receive result with recvfrom()
    Client->>File: Write "expression = result"
```

## Implementation Details

### TCP Version
- **Server (Python)**:
  - Creates a socket with `socket(AF_INET, SOCK_STREAM)`
  - Binds to the localhost (`127.0.0.1`) on port `12000`
  - Listens for client connections
  - Upon connection, receives expression, calculates result, sends back the result
  
- **Client (C++)**:
  - Creates a TCP socket
  - Connects to the server at `127.0.0.1:12000`
  - Gets user input for expression
  - Sends expression to server
  - Receives calculation result
  - Saves result to `result.txt`

### UDP Version
- **Server (Python)**:
  - Creates a socket with `socket(AF_INET, SOCK_DGRAM)`
  - Binds to the localhost (`127.0.0.1`) on port `12000`
  - Waits for datagrams from clients
  - Upon receipt, calculates result, sends back the result
  
- **Client (C++)**:
  - Creates a UDP socket
  - Gets user input for expression
  - Sends expression to server using `sendto()`
  - Receives calculation result using `recvfrom()`
  - Saves result to `result.txt`
