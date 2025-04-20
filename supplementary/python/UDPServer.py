import socket

def start_udp_server():
    # UDP 소켓 객체 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 주소와 포트 바인딩
    server_address = ('localhost', 9876)
    server_socket.bind(server_address)
    
    print(f"UDP 서버가 {server_address}에서 시작되었습니다. 패킷 대기 중...")
    
    try:
        while True:
            # 데이터 수신
            data, client_address = server_socket.recvfrom(1024)
            message = data.decode('utf-8')
            print(f"클라이언트 {client_address}로부터 수신: {message}")
            
            # 응답 전송
            response = f"서버 응답: {message}"
            server_socket.sendto(response.encode('utf-8'), client_address)
            
    except KeyboardInterrupt:
        print("서버가 종료됩니다.")
    finally:
        # 서버 소켓 종료
        server_socket.close()

if __name__ == "__main__":
    start_udp_server()