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
        socket.AF_INET, socket.SOCK_STREAM
    )  # AF_INET: IPv4, SOCK_STREAM: TCP
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)

    print(f"TCP server is ready (host: {server_host}, port: {server_port})")

    while True:
        # accept client connection
        conn, addr = server_socket.accept()
        print(f"[connection established] client: {addr}")

        # receive expression from client
        expression = conn.recv(1024).decode("utf-8")
        if not expression:
            conn.close()
            continue

        print(f"[received expression] {expression}")

        # compute expression
        result = compute_expression(expression)

        # send result
        conn.send(result.encode("utf-8"))
        print(f"[sent result] {result}")

        conn.close()


if __name__ == "__main__":
    main()
