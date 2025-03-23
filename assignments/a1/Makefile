# Makefile for Assignment 1

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17

# Source files
TCP_CLIENT_SRC = tcp-client.cpp
UDP_CLIENT_SRC = udp-client.cpp

# Executables
TCP_CLIENT = tcp-client.out
UDP_CLIENT = udp-client.out
RESULT_FILE = result.txt

# Targets
all: tcp udp

tcp: $(TCP_CLIENT_SRC)
	$(CXX) $(CXXFLAGS) -o $(TCP_CLIENT) $(TCP_CLIENT_SRC)

udp: $(UDP_CLIENT_SRC)
	$(CXX) $(CXXFLAGS) -o $(UDP_CLIENT) $(UDP_CLIENT_SRC)

clean:
	rm -f $(TCP_CLIENT) $(UDP_CLIENT) $(RESULT_FILE)

.PHONY: all clean
