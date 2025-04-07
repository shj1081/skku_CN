make:
	g++ client1.cpp -o client1
	gcc client2.c -o client2

run-server:
	python3 server.py

run-client1:
	g++ client1.cpp -o client1 && ./client1

run-client2:
	gcc client2.c -o client2 && ./client2

clean:
	rm -f client1
	rm -f client2
	rm -f history.html
	
