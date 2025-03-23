import re
import socket


def compute_expression(expr):
    # strip whitespace
    expr = expr.strip()

    # only use +, - (parsing with regex)
    tokens = re.split(r"(\+|\-)", expr)
    result = 0
    current_op = "+"  # default operator for first number

    for t in tokens:
        t = t.strip()
        if t == "" or t is None:
            continue

        # if operator, update current operator
        if t == "+" or t == "-":
            current_op = t
        else:
            # if number, convert to int and apply operation
            val = int(t)
            if current_op == "+":
                result += val
            else:
                result -= val
    return str(result)


def main():
    # predefined server host and port
    server_host = "127.0.0.1"
    server_port = 12000

    # create socket
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM
    )  # AF_INET: IPv4, SOCK_DGRAM: UDP
    server_socket.bind((server_host, server_port))

    print(f"UDP server is ready (host: {server_host}, port: {server_port})")

    while True:
        # receive expression from client
        message, clientAddress = server_socket.recvfrom(1024)
        expression = message.decode("utf-8")
        print(f"[client {clientAddress}] received expression: {expression}")

        # compute expression
        result = compute_expression(expression)

        # send result
        server_socket.sendto(result.encode("utf-8"), clientAddress)
        print(f"[client {clientAddress}] sent result: {result}")


if __name__ == "__main__":
    main()
