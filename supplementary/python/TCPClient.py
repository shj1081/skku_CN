import socket

def start_tcp_client():
    # 소켓 객체 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 서버 주소 설정
    server_address = ('localhost', 9876)
    
    try:
        # 서버에 연결
        client_socket.connect(server_address)
        print(f"서버 {server_address}에 연결되었습니다.")
        
        # 서버에 메시지 전송
        message = "안녕하세요, 서버!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"서버로 전송: {message}")
        
        # 서버로부터 응답 수신
        data = client_socket.recv(1024).decode('utf-8')
        print(f"서버로부터 수신: {data}")
        
    finally:
        # 소켓 종료
        client_socket.close()

if __name__ == "__main__":
    start_tcp_client()