# Week 7 Q&A

## Problem 1

**Fill in the blanks in these statements about Transport layer services:**  
> 전송 계층 서비스에 대한 다음 문장의 빈칸을 채우시오.


- **A.** Client process has the **ephemeral** port number  
  > 클라이언트는 일반적으로 **임시 포트 번호(ephemeral port)** 를 사용합니다.  
  > 이 포트는 동적으로 할당되며, 클라이언트의 송신 시점마다 달라질 수 있습니다.  

- **B.** Server process has the **well-known** port number  
  > 서버는 **고정된 포트 번호(well-known port)** 를 사용하여 클라이언트가 접속할 수 있도록 합니다.  
  > 예: HTTP(80), HTTPS(443), FTP(21)  


- **C.** Encapsulation happens at the **sender** site and decapsulation happens at the **receiver** site  
  > **캡슐화(encapsulation)**: 송신 측에서 데이터를 TCP/UDP 세그먼트로 포장  
  > **역캡슐화(decapsulation)**: 수신 측에서 이를 해제하여 원본 데이터를 추출  

- **D.** After the host has been selected, the **port number** defines one of the processes on this particular host  
  > 동일한 호스트 내의 **개별 프로세스 식별자**로서 **포트 번호(port number)** 사용  

- **E.** Socket address: the combination of an **IP address** and a **port number**  
  > 전송 계층에서의 종단 식별자: **소켓 주소 (socket address)** = IP 주소 + 포트 번호  

---

## Problem 2

**Classify the following statements into Flow/Error/Congestion controls**  
> 다음 설명을 흐름 제어(Flow control), 오류 제어(Error control), 혼잡 제어(Congestion control) 중 하나로 분류하시오.


- **A. Managing the rate of data transmission between producer and consumer to prevent losing the data items at the consumer site**  
  > **Flow control**  
  - 수신자가 처리 가능한 속도보다 송신자가 너무 빠르게 보내지 않도록 **데이터 전송 속도 제어**  

- **B. Keeping track of lost and discarded packets and resending them**  
  > **Error control**  
  - **손실되거나 손상된 패킷을 재전송하는 메커니즘**  

- **C. The load on the network is greater than the capacity of the network**  
  > **Congestion control**  
  - 네트워크의 처리 용량을 초과하는 트래픽을 조절하여 **혼잡을 방지**  

- **D. Recognizing duplicate packets and discarding them**  
  > **Error control**  
  - 중복된 데이터가 수신될 경우 이를 식별하고 **버리는 오류 처리 방식**  

---

## Problem 3

**Which statements are True/False about Stop and Wait protocol?**  
> Stop-and-Wait 프로토콜에 대한 다음 설명의 진위를 판단하시오.


- **A. Connection-oriented protocol**  
  > **True**  
  - Stop-and-Wait는 송신자와 수신자가 **패킷마다 확인 응답(ACK)** 을 주고받는 방식으로, **논리적 연결 상태를 유지**함  
  - 따라서 **연결 지향적(connection-oriented)** 특성을 가짐

- **B. Uses both flow and error controls**  
  > **True**  
  - 수신자의 수신 능력을 초과하지 않도록 **흐름 제어(Flow control)** 제공  
  - 손실/손상된 패킷에 대해 재전송하는 **오류 제어(Error control)** 도 수행

- **C. Checksum is added to detect corrupted packets**  
  > **True**  
  - 패킷에 **체크섬(checksum)** 을 추가하여 데이터가 손상되었는지 검증  
  - 오류가 감지되면 재전송 필요

- **D. With flow control service, the sender uses a timer when it sends a packet to the receiver to detect the packet loss**  
  > **False**  
  - **타이머(timer)** 는 **패킷 손실을 탐지**하기 위한 것으로, 이는 **오류 제어(Error control)** 기능  
  - 흐름 제어와는 관련 없음

---

## Problem 4

**What are the total transmitted frames if we have to send 10 frames using Go-Back-N with the following conditions:**  
> Go-Back-N 방식으로 총 10개의 프레임을 전송할 때, 다음 조건에서 총 전송된 프레임 수를 구하시오.

- **Window size = 3**
- **Every 5th transmitted frame is lost**
- **Given frames: 1 2 3 4 5 6 7 8 9 10**


### 전체 시뮬레이션 요약

#### Part 1 (Frames 1~7 전송)

- 5번째로 전송한 **Frame 5가 손실**
- → ACK 못 받음 → **Frame 5부터 다시 전송**

#### Part 2 (Frames 5~9 전송 중)

- 10번째로 전송한 **Frame 7이 손실** (part 1에서 6-7, part 2에서 5-6-7 전송)
- → ACK 못 받음 → **Frame 7부터 다시 전송**

#### Part 3 (Frames 7~10 전송 중)

- 15번째로 전송한 **Frame 9가 손실** (part 2에서 8-9, part 3에서 7-8-9 전송)
- → ACK 못 받음 → **Frame 9부터 다시 전송**


### 최종 계산

- **총 전송된 프레임 수** = **18**  
- **손실된 프레임 수** = **3** (`Frame 5`, `Frame 7`, `Frame 9`)


> **Go-Back-N**에서는 **하나의 프레임이 손실되면 그 이후 모든 프레임 재전송**  
> 이로 인해 재전송 횟수가 많아지고 **전송 효율이 떨어질 수 있음**

---

## Problem 5

**Assume that, in Stop-and-Wait system, the bandwidth of the line is 0.2 Mbps, and 1 bit takes 50 milliseconds to make a round trip**

> Stop-and-Wait 방식에서 다음 조건이 주어졌을 때, 대역폭-지연 곱과 링크 활용률을 구하시오.


### A. What is the bandwidth-delay product?

> **0.2 Mbps × 50 ms = 10,000 bits**

- **대역폭 (Bandwidth)** = 0.2 Mbps = 0.2 * 10^6 bps  
- **왕복 지연 시간 (RTT)** = 50 ms = 50 * 10^(-3) sec  
- 계산:  
  
  ```
  BDP(Bandwidth-delay product) = Bandwidth * RTT 
                               = 0.2 * 10^6 bps * 50 * 10^(-3) sec = 10,000 bits
  ```
- 송신자는 ACK을 기다리는 동안 **최대 10,000비트**를 전송할 수 있음

### B. If the system data packets are 500 bits in length, what is the utilization percentage of the link?

> **500 / 10,000 = 0.05 → 5%**

- **실제 전송되는 유효 데이터량** = 500 bits  
- **링크가 활용 가능한 이론적 최대량** = 10,000 bits  
- 계산:  
  
    ```
    Utilization = (실제 전송되는 유효 데이터량) / (링크가 활용 가능한 이론적 최대량)
                = 500 bits / 10,000 bits
                = 0.05
                = 5%
    ```
- **링크 활용률 (Link utilization)** = 5%

> **Bandwidth-delay product**: 10,000 bits  
> **Link utilization**: 5% (Stop-and-Wait은 효율이 낮음)  
> Stop-and-Wait 방식은 왕복 지연 동안 **1개 패킷만 전송 가능** → BDP가 클수록 비효율 커짐

--- 

## Problem 6

**Answering TRUE/FALSE about protocols in the Transport layer**  
> 전송 계층에서 사용되는 프로토콜에 대한 설명의 진위를 판단하시오.

- **A. The Simple protocol is a connectionless protocol with neither flow control nor error control**  
  > **True**  
  - Simple protocol은 **연결 설정 없이 데이터만 전송**  
  - **흐름 제어도 없고, 오류 제어도 없음**  

- **B. The Stop-and-Wait protocol is actually a Go-Back-N protocol in which there are only two sequence numbers, and the send window size is 1 (i.e., m = 1 and 2ᵐ - 1 = 1)**  
  > **True**  
  - Stop-and-Wait은 **Go-Back-N의 특수한 경우**로 볼 수 있음  
  - **전송 윈도우 크기 = 1**, **시퀀스 번호는 0과 1만 사용**

- **C. In Selective-Repeat protocol, the size of the send window must be less than 2ᵐ; the size of the receive window is always 1.**  
  > **False**  
  - Selective-Repeat에서는 **송신 윈도우와 수신 윈도우 모두 최대 크기 = 2ᵐ⁻¹**  
  - 수신 윈도우가 항상 1이라는 설명은 **잘못됨**  

---

## Problem 7

**The Transport layer provides several important services for process-to-process communication between applications on different hosts. Which of the following are services provided by the Transport layer?**  
> 전송 계층이 서로 다른 호스트의 애플리케이션 간 **프로세스 간 통신**을 지원하기 위해 제공하는 주요 서비스는?

- **A. Flow control**  
  > **제공됨**  
  - 수신자가 감당할 수 있는 속도로만 전송되도록 제어  
  - → **송신자와 수신자의 처리 속도 불일치 방지**

- **B. Encapsulation and decapsulation**  
  > **제공됨**  
  - 응용 계층에서 받은 데이터를 **TCP/UDP 세그먼트로 캡슐화**,  
    수신 측에서 다시 원본 데이터로 **디캡슐화**

- **C. Multiplexing and demultiplexing**  
  > **제공됨**  
  - **멀티플렉싱(multiplexing)**: 여러 프로세스의 데이터를 하나로 묶어 전송  
  - **디멀티플렉싱(demultiplexing)**: 도착한 세그먼트를 올바른 프로세스로 전달

- **D. Path selection and routing across the network**  
  > X → **네트워크 계층(Network layer)의 역할**  
  - IP 라우팅 및 경로 설정은 전송 계층의 기능이 아님

- **E. Assigning MAC (Media Access Control Address) addresses to devices**  
  > X → **데이터 링크 계층(Data Link layer)의 기능**  
  - MAC 주소는 **물리 주소(Physical Address)** 로, 전송 계층과는 무관

--- 

## Problem 8

**Fill in the blanks to show the differences between host-to-host and process-to-process communication**  
> 호스트 간 통신(host-to-host)과 프로세스 간 통신(process-to-process)의 차이를 표로 정리하시오.


| Aspect              | Host-to-host communication                        | Process-to-process communication                             |
|---------------------|---------------------------------------------------|--------------------------------------------------------------|
| **Layer Involved**  | **Network Layer**                                 | **Transport Layer**                                          |
| **Main Purpose**    | 목적지 **호스트(컴퓨터)** 까지 메시지를 전달           | 목적지 **프로세스(프로그램)** 까지 메시지를 정확히 전달         |
| **Address Used**    | **IP 주소(IP address)** 사용                      | **포트 번호(port number)** 와 IP 주소를 함께 사용               |

> **Host-to-host**: IP 기반, 목적지는 컴퓨터 (네트워크 계층)  
> **Process-to-process**: 포트 기반, 목적지는 프로세스 (전송 계층)

--- 

## Problem 9

```http
HTTP/1.1 200 OK
Date: Tue, 07 Mar 2008 12:39:45 GMT
Server: Apache/2.0.52 (Fedora)
Last-Modified: Sat, 10 Dec 2005 18:27:46 GMT
ETag: "526c3-f22-a88a4c80"
Accept-Ranges: bytes
Content-Length: 3874
Keep-Alive: timeout=max=100
Connection: Keep-Alive
Content-Type: text/html; charset=ISO-8859-1

<!doctype html public "-//w3c//dtd html 4.0 transitional//en">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="GENERATOR" content="Mozilla/4.79 [en] (Windows NT 5.0; U Netscape)">
<title>CMPSCI 453 / 591 / NTU‑ST550A Spring 2005 homepage</title>
</head>
<body>
<h1>much more document text following here (not shown)</h1>
</body>
</html>
```

| 번호 | 메시지 구성요소 | 의미 |
|------|----------------|------|
| 1 | **Status line** `HTTP/1.1 200 OK` | 사용 **프로토콜 버전**(HTTP/1.1) 및 **상태 코드** 200 → 요청이 정상 처리됨 |
| 2 | `Date:` 헤더 | 서버가 **응답을 보낸 시각**(RFC 1123 형식) |
| 3 | `Server:` 헤더 | 서버 **소프트웨어 식별** (예: Apache 2.0.52 on Fedora) |
| 4 | `Last-Modified:` 헤더 | 리소스가 **마지막으로 수정된 시각** |
| 5 | `ETag:` 헤더 | 리소스 **버전을 식별**하는 고유 태그 → 캐싱/조건부 GET에 사용 |
| 6 | `Accept-Ranges:` 헤더 | 서버가 **바이트 범위 요청**(partial GET)을 지원함을 표시 |
| 7 | `Content-Length:` 헤더 | 본문의 **바이트 길이**(정확한 전송 크기) |
| 8 | `Keep-Alive:` 헤더 | **지속 연결** 파라미터(예: 타임아웃, 최대 요청 수) |
| 9 | `Connection:` 헤더 | `Keep-Alive` 지정 → **TCP 연결 유지** 의도 |
| 10 | `Content-Type:` 헤더 | 본문 **MIME 타입**(text/html) & **문자 인코딩**(ISO‑8859‑1) |
| 11 | `<!doctype …>` | HTML **문서 유형 선언** → HTML 4.0 Transitional |
| 12 | `<meta http-equiv="Content-Type">` | HTML 내부에서 다시 **문자 집합**(ISO‑8859‑1) 명시 |
| 13 | `<meta name="GENERATOR">` | HTML을 **생성한 도구** 표시 (Mozilla 4.79 Netscape) |
| 14 | `<title> … </title>` | 브라우저 탭에 나타날 **문서 제목** |
| 15 | `<h1> … </h1>` 등 이후 본문 | 실제 **콘텐츠 영역** (예시는 생략 부분이 있음) |

> 헤더(1~10)는 **전송 계층 위**에서 동작하는 HTTP 메타데이터  
> 11 이후는 **HTML 본문**—클라이언트 렌더링 대상