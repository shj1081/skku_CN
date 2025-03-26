# Makefile for Assignment 1

# Compiler
CXX = g++

# Source files
TCP_CLIENT_SRC = tcp-client.cpp
UDP_CLIENT_SRC = udp-client.cpp

# Executables
TCP_CLIENT = tcp-client
UDP_CLIENT = udp-client
RESULT_FILE = result.txt

# Targets
all: $(TCP_CLIENT) $(UDP_CLIENT) # compile both tcp and udp clients

tcp: $(TCP_CLIENT_SRC)
	$(CXX) -o $(TCP_CLIENT) $(TCP_CLIENT_SRC)
	./$(TCP_CLIENT)

udp: $(UDP_CLIENT_SRC)
	$(CXX) -o $(UDP_CLIENT) $(UDP_CLIENT_SRC)
	./$(UDP_CLIENT)

clean:
	rm -f $(TCP_CLIENT) $(UDP_CLIENT) $(RESULT_FILE)

.PHONY: all clean
