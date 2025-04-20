package supplementary.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class TCPClient {
    public static void main(String[] args) {
        try {
            // 서버에 연결
            Socket socket = new Socket("localhost", 9876);

            // 입출력 스트림 설정
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            // 서버에 메시지 전송
            String message = "안녕하세요, 서버!";
            out.println(message);

            // 서버로부터 응답 수신
            String response = in.readLine();
            System.out.println("서버로부터 수신: " + response);

            // 연결 종료
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}