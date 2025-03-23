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
    // Create socket (UDP)
    int clientSocket = socket(AF_INET, SOCK_DGRAM, 0);  // AF_INET: IPv4, SOCK_DGRAM: UDP
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

    // Get expression input from user
    string expression;
    cout << "Enter an expression (e.g., 10+5-3): ";
    getline(cin, expression);

    // Send expression to server (sendto)
    ssize_t sendSize = sendto(clientSocket,
                              expression.c_str(),
                              expression.size(),
                              0,
                              (struct sockaddr*)&serverAddr,
                              sizeof(serverAddr));
    if (sendSize < 0) {
        cerr << "failed to send expression\n";
        close(clientSocket);
        return 1;
    }

    // Receive result from server (recvfrom)
    char buffer[1024];
    memset(buffer, 0, sizeof(buffer));
    socklen_t addrLen = sizeof(serverAddr);
    ssize_t recvSize = recvfrom(clientSocket,
                                buffer,
                                sizeof(buffer) - 1,
                                0,
                                (struct sockaddr*)&serverAddr,
                                &addrLen);
    if (recvSize < 0) {
        cerr << "failed to receive result\n";
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
