#ifdef _WIN32
#include <winsock2.h>
#include <ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")
#else
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>
#define SOCKET int
#define INVALID_SOCKET -1
#define SOCKET_ERROR -1
#define closesocket close
#endif

#include <cstring>
#include <iostream>
#include <string>

int main() {
// 윈속 초기화 (Windows에서만 필요)
#ifdef _WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup 실패" << std::endl;
        return 1;
    }
#endif

    // UDP 소켓 생성
    SOCKET clientSocket = socket(AF_INET, SOCK_DGRAM, 0);
    if (clientSocket == INVALID_SOCKET) {
        std::cerr << "소켓 생성 실패" << std::endl;
#ifdef _WIN32
        WSACleanup();
#endif
        return 1;
    }

    // 서버 주소 설정
    sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(9876);                      // 서버 포트 번호
    inet_pton(AF_INET, "127.0.0.1", &serverAddr.sin_addr);  // 서버 IP 주소

    // 메시지 전송
    const char* message = "안녕하세요, UDP 서버!";
    int serverAddrSize = sizeof(serverAddr);

    sendto(clientSocket, message, strlen(message), 0,
           (struct sockaddr*)&serverAddr, serverAddrSize);

    std::cout << "서버로 전송: " << message << std::endl;

    // 응답 수신
    char buffer[1024] = {0};
    sockaddr_in fromAddr;
    socklen_t fromAddrSize = sizeof(fromAddr);

    int bytesReceived = recvfrom(clientSocket, buffer, sizeof(buffer), 0,
                                 (struct sockaddr*)&fromAddr, &fromAddrSize);

    if (bytesReceived > 0) {
        std::cout << "서버로부터 수신: " << buffer << std::endl;
    }

    // 소켓 종료
    closesocket(clientSocket);

// 윈속 정리 (Windows에서만 필요)
#ifdef _WIN32
    WSACleanup();
#endif

    return 0;
}