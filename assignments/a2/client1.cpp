#include <iostream>
#include <string>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    const char* server_ip = "127.0.0.1";
    int port = 12000;

    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        std::cerr << "Socket creation failed\n";
        return 1;
    }

    sockaddr_in server_addr = {};
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    inet_pton(AF_INET, server_ip, &server_addr.sin_addr);

    if (connect(sock, (sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        std::cerr << "Connection failed\n";
        return 1;
    }

    char buffer[2048];
    int len = recv(sock, buffer, sizeof(buffer) - 1, 0);
    if (len > 0) {
        buffer[len] = 0;
        std::cout << buffer;
    }

    while (true) {
        std::string input;
        std::getline(std::cin, input);
        if (input == "exit") break;

        input += '\n';
        
        send(sock, input.c_str(), input.length(), 0);
        len = recv(sock, buffer, sizeof(buffer) - 1, 0);
        if (len <= 0) break;

        buffer[len] = 0;
        std::cout << buffer;
    }

    close(sock);
    return 0;
}
