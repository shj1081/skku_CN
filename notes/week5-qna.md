# Week 5 Q&A

## Problem 1

To define a web page, what kind of identifier(s) do we need?

> 웹 페이지를 정의하기 위해 어떤 종류의 식별자가 필요한가요?

- **Protocol**: 웹 페이지에 접속하기 위한 방식 (예: `http`, `https`)
- **Host**: 서버의 IP 주소 또는 도메인 이름 (예: `www.example.com`)
- **Port**: 서버 애플리케이션과 통신하기 위해 사용하는 16비트 숫자 (예: `80`, `443`)
- **Path**: 서버 내부에서 요청된 파일의 위치 및 이름 (예: `/index.html`)

---

## Problem 2

Name three types of web documents and describe their differences.

> 웹 문서의 세 가지 종류는 무엇인지 말하고 이들 간의 차이점을 설명하세요.

Which languages are used in those web documents?

> 각각의 웹 문서 유형에서 어떤 언어가 사용되나요?

| **Type**              | **Description**                                                                               | **Used Languages**           |
| --------------------- | --------------------------------------------------------------------------------------------- | ---------------------------- |
| **Static Documents**  | 내용이 고정되어 있으며 서버에 미리 저장됨.<br>클라이언트는 해당 문서의 복사본만 받을 수 있음. | HTML, XML, XSL 등            |
| **Dynamic Documents** | 브라우저가 요청할 때마다 **서버가 생성**하는 문서.                                            | CGI, JSP, ASP, ColdFusion 등 |
| **Active Documents**  | 클라이언트 측에서 **스크립트나 프로그램이 실행되는 문서**.                                    | JavaScript, Java Applet      |

---

## Problem 3

What is the main difference between non-persistent and persistent connections in HTTP?

> HTTP에서 비지속 연결과 지속 연결의 주요 차이점은 무엇인가요?

What are the HTTP versions used in non-persistent and persistent connections?

> 각 연결 방식에 사용되는 HTTP 버전은 무엇인가요?

What kinds of connections do most modern browsers like Chrome, Firefox, and Microsoft Edge use?

> 크롬, 파이어폭스, 엣지 등 현대 브라우저들이 사용하는 연결 방식은 무엇인가요?

| **속성 (Attribute)**    | **Non-persistent connections**        | **Persistent connections**                               |
| ----------------------- | ------------------------------------- | -------------------------------------------------------- |
| **Connection behavior** | 각 요청/응답마다 새로운 TCP 연결 생성 | 응답 후에도 연결을 열어두고 추가 요청을 처리함           |
| **HTTP version**        | HTTP 1.0                              | HTTP 1.1                                                 |
| **Browser usage**       | —                                     | 대부분의 현대 브라우저가 사용 (Chrome, Firefox, Edge 등) |

**Non-persistent**

- 한 개의 요청을 처리할 때마다 **새로운 TCP 연결**을 설정하고 응답 후 종료함
- 오버헤드가 크고 비효율적이며 **HTTP 1.0에서 사용됨**

**Persistent**

- 한번 연결된 TCP 소켓을 통해 **여러 요청과 응답**을 처리함
- 성능이 향상되며 **HTTP 1.1 이상에서 기본 동작**
- `Connection: keep-alive`가 명시적이거나 암묵적으로 설정됨

---

## Problem 4

**In HTTP, the first line in a request message is called a **\_\_\_\_** line; the first line in the response message is called the **\_\_\_\_** line.**

> HTTP에서 요청 메시지의 첫 번째 줄은 무엇이라고 하고, 응답 메시지의 첫 번째 줄은 무엇이라고 하나요?

- **Request line**: 클라이언트가 서버에 요청할 때 사용되는 HTTP 요청 메시지의 첫 줄  
  예:

  ```
  GET /index.html HTTP/1.1
  ```

- **Status line**: 서버가 응답할 때 사용하는 HTTP 응답 메시지의 첫 줄  
  예:

  ```
  HTTP/1.1 200 OK
  ```

---

## Problem 5

A. A user requests a web page that consists of some text and three images. For this page, the client will send one request message and receive four response messages.

> 사용자가 텍스트와 이미지 3개로 구성된 웹 페이지를 요청하면, 클라이언트는 요청 메시지 1개를 보내고 응답 메시지 4개를 받는다.

> **False**
>
> - 클라이언트는 각 리소스(텍스트 1 + 이미지 3)에 대해 **4개의 요청**을 전송해야 하며, 각 요청에 대해 **각각의 응답**을 받는다.
> - 따라서 **요청도 4개, 응답도 4개**이다.

B. Two distinct Web pages (e.g., `/research.html`, `/students.html`) can be sent over the same persistent connection.

> 서로 다른 두 웹 페이지도 하나의 **지속 연결(persistent connection)** 을 통해 전송될 수 있다.

> **True**
>
> - HTTP 1.1부터는 연결을 유지하여 다수의 요청과 응답을 한 연결로 처리 가능하다.

C. With non-persistent connections, it is possible for a single TCP segment to carry two distinct HTTP request messages.

> 비지속 연결에서도 하나의 TCP 세그먼트로 2개의 요청을 보낼 수 있다.

> **False**
>
> - **Non-persistent HTTP**에서는 요청 하나당 연결 하나가 사용된다.
> - 두 개의 HTTP 요청은 절대로 하나의 TCP 세그먼트에 포함될 수 없다.

D. The `Date:` header in the HTTP response message indicates when the object in the response was last modified.

> HTTP 응답 메시지의 `Date:` 헤더는 객체가 마지막으로 수정된 시점을 나타낸다.

> **False**
>
> - `Date:` 헤더는 **응답이 생성된 시간**을 나타냄.
> - **마지막 수정 시점**을 나타내는 것은 `Last-Modified:` 헤더임.

E. HTTP response messages never have an empty message body.

> HTTP 응답 메시지는 항상 메시지 바디를 가진다.

> **False**
>
> - HTTP 응답은 **상황에 따라 바디가 비어있을 수 있다.**  
>   예: `204 No Content`, `304 Not Modified` 등

---

## Problem 6

**To successfully access the initial landing page of our lab’s website [`http://monet.skku.ac.kr/main/`](http://monet.skku.ac.kr/main/), which range of HTTP status codes would you typically expect to receive?**

> 연구실 웹사이트의 초기 메인 페이지에 성공적으로 접속하려면, 보통 어떤 범위의 HTTP 상태 코드를 받게 되나요?

- A. 100–199 (Informational responses)
- **B. 200–299 (Successful responses) (정답)**
- C. 300–399 (Redirection messages)
- D. 400–499 (Client error responses)
- E. 500–599 (Server error responses)

| 범위    | 설명                               | 예시                                                   |
| ------- | ---------------------------------- | ------------------------------------------------------ |
| 100–199 | **정보 제공** (요청은 계속 진행됨) | `100 Continue`                                         |
| 200–299 | **요청 성공**                      | `200 OK`, `201 Created`                                |
| 300–399 | **리다이렉션 필요**                | `301 Moved Permanently`, `302 Found`                   |
| 400–499 | **클라이언트 오류**                | `404 Not Found`, `403 Forbidden`                       |
| 500–599 | **서버 오류**                      | `500 Internal Server Error`, `503 Service Unavailable` |

- 웹 페이지 접속이 정상적으로 완료되었다면, 서버는 일반적으로 **`200 OK`** 상태 코드를 반환

---

## Problem 7

Did you notice the “Not secure” label in the video of Wireshark?

> Wireshark 영상에서 웹사이트 주소창에 "Not secure(보안되지 않음)"이라는 문구가 보였나요?

A. What is the reason for this?

> 왜 이런 문구가 뜨는 걸까요?

**The website is using `http` instead of `https`. `http` does not have Secure Socket Layer (SSL).**

> 해당 웹사이트가 https가 아닌 http를 사용하고 있기 때문입니다.  
> `http`는 암호화되지 않은 프로토콜이며, SSL/TLS 기반의 보안 계층이 없어 정보가 평문으로 전송됩니다.

B. Can we change it to secure?

> 이를 보안 연결로 바꿀 수는 없을까요?

**Yes, by incorporating an SSL certificate on the domain.**

> 가능합니다. 도메인에 SSL 인증서를 설치하면 HTTPS 기반 통신으로 전환할 수 있습니다.

C. Is it worth doing so?

> 굳이 그럴 필요가 있을까요?

**Yes, it's worth implementing HTTPS for improved security and trustworthiness.**

> HTTPS를 사용하는 것은 매우 중요합니다.
> 민감한 데이터를 다룰 때 보안성과 신뢰성이 높아지고, 검색 엔진 최적화(SEO) 측면에서도 유리합니다.

| 항목           | HTTP                    | HTTPS                                |
| -------------- | ----------------------- | ------------------------------------ |
| 암호화         | 평문 전송               | SSL/TLS로 암호화                     |
| 기본 포트      | 80                      | 443                                  |
| 신뢰성         | 낮음 (패킷 스니핑 가능) | 높음 (SSL 인증)                      |
| SEO 영향       | 없음                    | 검색 순위에 긍정적 영향              |
| 주요 사용 사례 | 공개 정보 제공 사이트   | 로그인, 결제 등 보안 요구되는 사이트 |

---

## Problem 8

A. HTTP/1.0 uses persistent connections

> HTTP/1.0은 지속 연결(persistent connection)을 사용한다.

> **False**
>
> - HTTP/1.0은 non-persistent connection을 사용
> - 즉, 요청-응답마다 새로운 TCP 연결이 생성됨

B. HTTP/1.1 relies on TCP so it must establish handshaking process for every request

> HTTP/1.1은 TCP 위에서 동작하므로, 매 요청마다 핸드셰이크 과정을 거쳐야 한다.

> **False**
>
> HTTP/1.1도 TCP 위에서 동작하지만, 하나의 연결로 여러 요청을 처리할 수 있기 때문에 매 요청마다 새로운 핸드셰이크는 필요하지 않음
> (단, 연결이 끊기면 다시 핸드셰이크가 필요)

C. HTTP/2 reduces the latency by using UDP protocol which allows multiple streams onto a single UDP connection

> HTTP/2는 UDP 프로토콜을 사용하여 여러 스트림을 하나의 UDP 연결에서 처리함으로써 지연을 줄인다.

> **False**
>
> - HTTP/2는 여전히 TCP를 사용하며,
> - stream multiplexing을 통해 단일 연결에서 다수의 스트림을 병렬 처리하여 지연 시간을 줄임

D. HTTP/3 integrates a transport layer protocol – QUIC in application layer instead of using it from the transport layer (like previous HTTP versions do)

> HTTP/3는 QUIC이라는 전송 계층 프로토콜을 애플리케이션 계층에 통합하여 사용한다.

> **False**
>
> - HTTP/3는 전송 계층 프로토콜인 QUIC을 사용하는 것은 맞지만
> - QUIC은 애플리케이션 계층에 통합된 것이 아닌, 전송 계층에서 작동하는 프로토콜입니다.

| HTTP 버전 | 연결 방식                    | 프로토콜 | 특징 요약                                     |
| --------- | ---------------------------- | -------- | --------------------------------------------- |
| HTTP/1.0  | 비지속 연결 (단일 요청-응답) | TCP      | 요청마다 새로운 TCP 연결                      |
| HTTP/1.1  | 지속 연결                    | TCP      | 하나의 TCP 연결로 여러 요청 처리 (Keep-Alive) |
| HTTP/2    | 지속 연결 + 멀티플렉싱       | TCP      | 여러 요청을 동시에 처리 (stream 기반)         |
| HTTP/3    | 지속 연결 + 멀티플렉싱       | QUIC     | TCP 대신 QUIC 사용, 빠른 연결 성립            |

---

## Problem 9

A. Electronic mail (or E-mail) allows users to exchange messages and is considered a one-way transaction

> 전자메일(E-mail)은 사용자 간의 메시지 교환을 가능하게 하며, 단방향 트랜잭션으로 간주된다.

> **True**
>
> - 이메일은 기본적으로 요청-응답 방식이 아닌, 발신자 → 수신자의 단방향 메시지 전달 구조
> - 수신자가 응답하려면 별도의 메일을 다시 작성해야 하므로 트랜잭션 관점에서는 단방향

B. There are two types of UA (User Agent): command-driven UA and GUI-based UA

> 사용자 에이전트(UA)에는 명령어 기반(command-driven)과 GUI 기반 두 종류가 있다.

> **True**
>
> - command-driven UA: `mutt`, `pine` 같은 텍스트 기반 CLI 에이전트
> - GUI-based UA: Outlook, Thunderbird 같이 GUI 환경에서 사용하는 에이전트

C. The process of transferring a mail message occurs in three phases: Connection establishment, Message Transfer, and Connection termination

> 이메일 메시지 전송 과정은 다음의 세 단계로 구성된다: 연결 설정, 메시지 전송, 연결 종료

> **True**
>
> - 이메일을 전송할 때 SMTP는 TCP 연결을 열고, 메시지를 전송한 후 연결을 닫음
> - 이 과정은 세 단계로 명확히 나뉘며, SMTP 통신의 기본 구조

D. SMTP, POP3 and IMAP are stateless protocols. They maintain and store the past information for further uses.

> SMTP, POP3, IMAP은 상태 없는(stateless) 프로토콜이며, 과거 정보를 저장하여 이후에 재사용하지 않는다.

> **False**
>
> - 세 프로토콜은 모두 stateful
> - SMTP: 세션 중 발신자·수신자·본문 상태를 유지
> - POP3/IMAP: 클라이언트와 메일 서버 간의 세션을 유지하며, 사용자의 읽음 여부, 동기화 상태 등을 기억

---

## Problem 10

A. In the DNS hierarchy, a top-level domain (TLD) represents the first stop after the root zone. TLD in the domain www.google.com is **`.com`**

> DNS 계층 구조에서 최상위 도메인(TLD)은 루트 영역 이후의 첫 번째 level 을 의미하며, `www.google.com`의 TLD는 `.com`

B. **Primary** server manages and updates the zone file while **secondary** server retrieves and stores zone information from another server.

> - **Primary 서버**는 존(zone) 파일을 관리하고 갱신하는 역할을 하며, authoritative zone을 직접 관리
> - **Secondary 서버**는 Primary로부터 존 정보를 가져와 보관, 복제본만 유지하며 변경 권한은 없음

C. The process of storing previously resolved DNS queries to speed up future lookups is called **caching**

> - 이전에 수행된 DNS 질의 결과를 저장하여 향후 조회 속도를 높이는 과정은 `캐싱(caching)`
> - DNS Resolver나 브라우저는 이 캐싱을 통해 반복적인 DNS 요청을 줄여 성능을 향상

D. A resource record is a 5-tuple structure: consisting of the following fields:

**Domain name, Type, Class, TTL, Value**

> 리소스 레코드는 5개의 필드로 구성된 구조
>
> - 도메인 이름 (Domain Name)
> - 타입 (Type: A, AAAA, MX, etc.)
> - 클래스 (Class: IN 등)
> - TTL (Time To Live)
> - 값 (Value: IP 주소 또는 다른 도메인)

E. The default port number for DNS queries is **53**

> DNS 질의를 위한 **기본 포트 번호는 53번**으로, TCP/UDP 모두에서 사용되며, 일반적으로 UDP로 전송됨 (TCP는 zone transfer나 큰 응답 시 사용)

---

## Problem 11

Complete the following TCP server and client structure

> TCP 서버와 클라이언트가 통신하기 위해 사용하는 소켓 프로그래밍의 단계별 함수

![flow diagram for TCP communication](../screenshots/2.5.5.png)

**Server 측:**

1. `socket()`

   > 소켓 (listening socket) 생성. `socket(AF_INET, SOCK_STREAM, 0)`

2. `bind()`

   > 로컬 주소(IP, Port)를 소켓에 할당.

3. `listen()`

   > 해당 포트에서 들어오는 연결을 수신할 준비.

4. `accept()`

   > 클라이언트가 연결 요청을 하면 그것을 수락하고 새로운 소켓 (connected socket)을 리턴.

5. `receive()`

   > 클라이언트로부터 요청 데이터 수신.

6. `send()`
   > 응답 데이터 전송.

**Client 측:**

1. `socket()`

   > 소켓 생성.

2. `connect()`

   > 서버의 IP, 포트에 연결 요청.

3. `send()`

   > 요청 데이터 전송.

4. `receive()`
   > 서버로부터 응답 수신.
