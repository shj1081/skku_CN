# Week 3 Q&A

## Problem 2

Which statements are True/False about Circuit Switched Networks (CSNs), and Packet Switched Networks (PSNs)?

회선 교환 네트워크와 패킷 교환 네트워크의 특징 중 옳은 것은?

---

```
In CSNs, a message is divided and grouped into units that are individually routed from the source to the destination
```

회선 교환 네트워크에서는 메시지가 작은 단위로 분할되어 각각의 단위가 독립적으로 목적지까지 경로를 선택하여 전송된다.

→ 패킷 교환 네트워크에 대한 설명이다. 회선 교환 네트워크는 전체 메시지를 한번에 전송한다.

```
Traditional telephone networks used PSNs since the networks are always available between the two end systems
```

전통적인 전화망은 패킷 교환 네트워크를 사용하고, 항상 두 end systems 간에 통신 경로가 있어야 한다.

→ 전통적인 전화망은 회선 교환 네트워크를 사용하고, 뒤의 설명은 회선 교환 네트워크에 대한 설명이다.

```
CSNs have better resource utilization because they have dedicated connections between the source and the destination
```

회선 교환 네트워크는 두 end systems 간에 전용 회선을 가지고 있어, 자원을 효율적으로 사용한다.

→ 회선 교환 네트워크는 두 end systems 간에 전용 회선 가지고 있는 것은 맞지만, 이로 인해 사용하지 않는 회선을 계속 연결하여 자원을 낭비하는 것이 문제이다. 패킷 교환 네트워크가 같은 채널이 여러 사용자에 의해 사용될 수 있기에 자원을 더 효율적으로 사용할 수 있다.

```
PSNs are suitable for data transmission
```

패킷 교환 네트워크는 데이터 전송에 적합하다.

→ 패킷 교환 네트워크에 대한 옳은 설명이다. 회선 교환 네트워크는 voice transmission 에 적합하고, 패킷 교환 네트워크는 data transmission 에 적합하다.

## Problem 3

| Abbrev. | Full form                                  | Generation | CS / PS                        |
| ------- | ------------------------------------------ | ---------- | ------------------------------ |
| AMPS    | Advanced Mobile Phone System               | 1G         | CS                             |
| GSM     | Global System for Mobile comm.             | 2G         | CS                             |
| CDMA    | Code Division Multiple Access              | 2G         | CS                             |
| EDGE    | Enhanced Data rates for GSM Evolution      | 2.5G       | CS (Voice and SMS) + PS (Data) |
| UMTS    | Universal Mobile Telecommunications System | 3G         | CS (Voice and SMS) + PS (Data) |
| LTE     | Long-Term Evolution                        | 4G         | PS                             |
| 5G NR   | 5G New Radio                               | 5G         | PS                             |

## Problem 4

Which of the following specific layers is/are not named in the TCP/IP model but is present in the OSI model?

어떤 계층이 TCP/IP 모델에는 없지만 OSI 모델에는 있는가?

---

→ TCP/IP의 application layer는 OSI의 application layer, **presentation layer, session layer** 의 기능을 수행한다.

## Problem 5

Relating to TCP/IP protocol suite, Correct layers ordering and fill respective identical object for each
layer in the following figure.

TCP/IP 프로토콜에 대해 각 계층의 순서와 identical object를 채워넣으시오.

---

![TCP/IP protocol suite](../screenshots/1.2.5.png)

1. application layer: message
2. transport layer: segment or user datagram
3. network layer: datagram
4. data link layer: frame
5. physical layer: bits

## Problem 6, 7

What is the address of physical layer in TCP/IP?

TCP/IP 물리 계층의 주소는?

Correct packet names and addresses ordering for each layer in the following figure.

각 계층의 패킷 이름과 주소 순서를 채워넣으시오.

---

![packet names and addresses ordering](../screenshots/1.2.6.png)

→ 물리 계층의 주소는 존재하지 않으며 각 계층의 패킷 이름과 주소 순서는 다음과 같다.

## Problem 8

What is achieved in circuit switching when resources are reserved between two communicating end systems?

회선 교환 네트워크에서 두 개의 통신 종단 시스템 간에 자원을 예약할 때 어떤 것이 달성되는가?

---

→ guranteed constant rate of transmission, reliability

즉, 전용 회선이 예약되어 전송 속도가 일정하고 신뢰성 있는 전송이 보장된다.

## Problem 9

In TCP/IP, a packet at the third layer carries data belonging to the (a) layer and the header belonging to the (b) layer.

TCP/IP 의 세 번째 계층에서 패킷은 (a) 계층의 데이터를 포함하고 헤더는 (b) 계층의 헤더를 포함한다.

---

→ 네트워크 계층의 패킷은 전송 계층(4계층)의 세그먼트(data)를 포함하고 헤더는 네트워크 계층(3계층)의 헤더를 포함한다.

즉, TCP/IP에서 data encapsulation은 데이터가 상위계층에서 하위 계층으로 이동할때, 하위 계층의 헤더가 상위 계층의 데이터에 추가된다.

## Problem 10

Devices including hubs, cables, and repeaters function at the (a) layer of the TCP/IP model, whereas routers operate at the (b) layer.

TCP/IP 모델의 (a) 계층에서 작동하는 장치는 허브, 케이블, 리피터이다. 반면에 라우터는 (b) 계층에서 작동한다.

---

→ 허브, 케이블, 리피터는 physical layer 에서 작동하고, 라우터는 network layer 에서 작동한다.
