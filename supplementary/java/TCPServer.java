package supplementary.java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class TCPServer {
    public static void main(String[] args) {
        ServerSocket serverSocket = null;

        try {

            // open a server socket on port 9876 and wait for a connection
            serverSocket = new ServerSocket(9876);

            while (true) {
                // accept a connection from a client
                Socket clientSocket = serverSocket.accept();

                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(new OutputStreamWriter(clientSocket.getOutputStream()));

                // read a message from the client
                String message = in.readLine();
                System.out.println("클라이언트로부터 수신: " + message);

                // send a response back to the client (echo)
                out.println("서버에서 응답: " + message);

                // close the output socket
                clientSocket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                // Now serverSocket is accessible here
                if (serverSocket != null && !serverSocket.isClosed()) {
                    serverSocket.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}