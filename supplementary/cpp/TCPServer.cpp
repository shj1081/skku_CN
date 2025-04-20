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

    // 소켓 생성
    SOCKET serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == INVALID_SOCKET) {
        std::cerr << "소켓 생성 실패" << std::endl;
#ifdef _WIN32
        WSACleanup();
#endif
        return 1;
    }

    // 서버 주소 설정
    sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(9876);  // 포트 번호

    // 바인딩
    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        std::cerr << "바인딩 실패" << std::endl;
        closesocket(serverSocket);
#ifdef _WIN32
        WSACleanup();
#endif
        return 1;
    }

    // 리스닝 시작
    if (listen(serverSocket, 5) == SOCKET_ERROR) {
        std::cerr << "리스닝 실패" << std::endl;
        closesocket(serverSocket);
#ifdef _WIN32
        WSACleanup();
#endif
        return 1;
    }

    std::cout << "TCP 서버가 시작되었습니다. 클라이언트 연결 대기 중..." << std::endl;

    // 클라이언트 연결 수락
    sockaddr_in clientAddr;
    socklen_t clientAddrSize = sizeof(clientAddr);
    SOCKET clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &clientAddrSize);

    if (clientSocket == INVALID_SOCKET) {
        std::cerr << "연결 수락 실패" << std::endl;
        closesocket(serverSocket);
#ifdef _WIN32
        WSACleanup();
#endif
        return 1;
    }

    std::cout << "클라이언트가 연결되었습니다: "
              << inet_ntoa(clientAddr.sin_addr) << std::endl;

    // 데이터 수신
    char buffer[1024] = {0};
    int bytesReceived = recv(clientSocket, buffer, sizeof(buffer), 0);

    if (bytesReceived > 0) {
        std::cout << "클라이언트로부터 수신: " << buffer << std::endl;

        // 데이터 전송
        std::string response = "서버 응답: ";
        response += buffer;
        send(clientSocket, response.c_str(), response.length(), 0);
    }

    // 소켓 종료
    closesocket(clientSocket);
    closesocket(serverSocket);

// 윈속 정리 (Windows에서만 필요)
#ifdef _WIN32
    WSACleanup();
#endif

    return 0;
}