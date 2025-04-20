package supplementary.java;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class UDPClient {
    public static void main(String[] args) {
        try {
            // create a UDP socket
            DatagramSocket clientSocket = new DatagramSocket();
            InetAddress serverAddress = InetAddress.getByName("localhost");

            // create a buffer for sending and receiving data
            byte[] sendData = new byte[1024];
            byte[] receiveData = new byte[1024];

            // message to be sent
            String message = "안녕하세요, UDP 서버!";
            sendData = message.getBytes();

            // create a datagram packet to send
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, serverAddress, 9876);

            // send the packet
            clientSocket.send(sendPacket);

            // create a datagram packet to receive
            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);

            // receive the packet
            clientSocket.receive(receivePacket);
            String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("서버로부터 수신: " + response);

            // close the socket
            clientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
