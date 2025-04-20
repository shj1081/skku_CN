import socket

def start_udp_client():
    # UDP 소켓 객체 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 서버 주소 설정
    server_address = ('localhost', 9876)
    
    try:
        # 메시지 전송
        message = "안녕하세요, UDP 서버!"
        client_socket.sendto(message.encode('utf-8'), server_address)
        print(f"서버로 전송: {message}")
        
        # 서버로부터 응답 수신
        data, server = client_socket.recvfrom(1024)
        print(f"서버로부터 수신: {data.decode('utf-8')}")
        
    finally:
        # 소켓 종료
        client_socket.close()

if __name__ == "__main__":
    start_udp_client()