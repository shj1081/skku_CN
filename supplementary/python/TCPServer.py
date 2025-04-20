import socket

def start_tcp_server():
    # 소켓 객체 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 주소와 포트 바인딩
    server_address = ('localhost', 9876)
    server_socket.bind(server_address)
    
    # 연결 대기 상태로 설정
    server_socket.listen(1)
    print(f"TCP 서버가 {server_address}에서 시작되었습니다. 클라이언트 연결 대기 중...")
    
    try:
        while True:
            # 클라이언트 연결 수락
            client_socket, client_address = server_socket.accept()
            print(f"클라이언트가 연결되었습니다: {client_address}")
            
            try:
                # 데이터 수신
                data = client_socket.recv(1024).decode('utf-8')
                print(f"클라이언트로부터 수신: {data}")
                
                # 데이터 전송
                response = f"서버 응답: {data}"
                client_socket.sendall(response.encode('utf-8'))
                
            finally:
                # 클라이언트 소켓 종료
                client_socket.close()
                
    except KeyboardInterrupt:
        print("서버가 종료됩니다.")
    finally:
        # 서버 소켓 종료
        server_socket.close()

if __name__ == "__main__":
    start_tcp_server()