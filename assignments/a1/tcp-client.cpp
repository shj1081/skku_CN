#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

#include <cstring>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

// predefined server host and port
const string SERVER_HOST = "127.0.0.1";
const int SERVER_PORT = 12000;

int main() {
    // Create socket (TCP)
    int clientSocket = socket(AF_INET, SOCK_STREAM, 0);  // AF_INET: IPv4, SOCK_STREAM: TCP
    if (clientSocket < 0) {
        cerr << "socket creation failed\n";
        return 1;
    }

    // Set server address
    sockaddr_in serverAddr;
    memset(&serverAddr, 0, sizeof(serverAddr));
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(SERVER_PORT);

    // inet_pton: convert IPv4 and IPv6 addresses from text to binary form
    if (inet_pton(AF_INET, SERVER_HOST.c_str(), &serverAddr.sin_addr) <= 0) {
        cerr << "failed to set server address\n";
        close(clientSocket);
        return 1;
    }

    // Connect to server
    if (connect(clientSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) < 0) {
        cerr << "failed to connect to server\n";
        close(clientSocket);
        return 1;
    }

    // Get expression input from user
    string expression;
    cout << "Enter an expression (e.g., 10+5-3): ";
    getline(cin, expression);

    // Send expression to server
    ssize_t sendSize = send(clientSocket, expression.c_str(), expression.size(), 0);
    if (sendSize < 0) {
        cerr << "failed to send expression\n";
        close(clientSocket);
        return 1;
    }

    // Receive result from server
    char buffer[1024];
    memset(buffer, 0, sizeof(buffer));
    ssize_t recvSize = recv(clientSocket, buffer, sizeof(buffer) - 1, 0);
    if (recvSize < 0) {
        cerr << "failed to receive result\n";
        close(clientSocket);
        return 1;
    } else if (recvSize == 0) {
        cerr << "server closed connection\n";
        close(clientSocket);
        return 1;
    }

    // Print result
    string result(buffer, recvSize);
    cout << "received result from server: " << result << endl;

    // Save expression and result to result.txt using ofstream
    ofstream outFile("result.txt");
    if (outFile.is_open()) {
        outFile << "Expression: " << expression << endl;
        outFile << "Result: " << result << endl;
        outFile.close();
        cout << "saved to result.txt" << endl;
    } else {
        cerr << "failed to create result.txt" << endl;
    }

    // Close socket
    close(clientSocket);

    return 0;
}
