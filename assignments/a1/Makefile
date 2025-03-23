# Makefile for Assignment 1

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17

# Source files
TCP_CLIENT_SRC = tcp-client.cpp
UDP_CLIENT_SRC = udp-client.cpp

# Executables
TCP_CLIENT = tcp-client.o
UDP_CLIENT = udp-client.o

# Targets
all: tcp-client.o udp-client.o

tcp: $(TCP_CLIENT_SRC)
	$(CXX) $(CXXFLAGS) -o $(TCP_CLIENT) $(TCP_CLIENT_SRC)

udp: $(UDP_CLIENT_SRC)
	$(CXX) $(CXXFLAGS) -o $(UDP_CLIENT) $(UDP_CLIENT_SRC)

clean:
	rm -f $(TCP_CLIENT) $(UDP_CLIENT)

.PHONY: all clean
