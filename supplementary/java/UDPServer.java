package supplementary.java;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class UDPServer {
    public static void main(String[] args) {
        DatagramSocket serverSocket = null;

        try {
            // UDP 소켓 생성
            serverSocket = new DatagramSocket(9876);
            byte[] receiveData = new byte[1024];

            System.out.println("UDP 서버가 시작되었습니다. 포트: 9876");

            while (true) {
                // 수신용 데이터그램 패킷 생성
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);

                // 패킷 수신
                serverSocket.receive(receivePacket);
                String message = new String(receivePacket.getData(), 0, receivePacket.getLength());

                // 클라이언트 정보
                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();

                System.out
                        .println("클라이언트 [" + clientAddress.getHostAddress() + ":" + clientPort + "]로부터 수신: " + message);

                // 응답 준비
                String response = "서버 응답: " + message;
                byte[] sendData = response.getBytes();

                // 응답 패킷 생성 및 전송
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, clientAddress, clientPort);
                serverSocket.send(sendPacket);

                // 새 수신을 위해 receiveData 배열 초기화
                receiveData = new byte[1024];
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            // 소켓 정리
            if (serverSocket != null && !serverSocket.isClosed()) {
                serverSocket.close();
            }
        }
    }
}
