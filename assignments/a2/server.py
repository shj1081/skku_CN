import socket
import threading
import os
import math
import re

HOST = ""  # can accept any IP address
PORT = 12000
HISTORY_FILE = "history.html"
VALID_OPERATORS = {"+", "-", "*", "/"}


def calculate_expression(expr_str: str) -> float:

    original_expr = expr_str

    expr = expr_str.lower().replace("of", "").strip()

    if not expr:
        raise ValueError("Empty expression.")

    sqrt_pattern = r"sqrt\s+(-?\d+(\.\d+)?)"
    square_pattern = r"square\s+(-?\d+(\.\d+)?)"

    replacements = {}
    replacement_count = 0

    while re.search(sqrt_pattern, expr):
        match = re.search(sqrt_pattern, expr)
        num_str = match.group(1)

        try:
            num = float(num_str)
            if num < 0:
                raise ValueError(
                    f"Cannot calculate square root of a negative number: {num}"
                )
            result = math.sqrt(num)

            placeholder = f"__PLACEHOLDER_{replacement_count}__"
            replacements[placeholder] = result
            expr = expr[: match.start()] + placeholder + expr[match.end() :]
            replacement_count += 1

        except ValueError as e:
            if "negative" in str(e):
                raise e
            raise ValueError(f"Invalid number format in sqrt operation: {num_str}")

    while re.search(square_pattern, expr):
        match = re.search(square_pattern, expr)
        num_str = match.group(1)

        try:
            num = float(num_str)
            result = num * num

            placeholder = f"__PLACEHOLDER_{replacement_count}__"
            replacements[placeholder] = result
            expr = expr[: match.start()] + placeholder + expr[match.end() :]
            replacement_count += 1

        except ValueError:
            raise ValueError(f"Invalid number format in square operation: {num_str}")

    for placeholder, value in replacements.items():
        expr = expr.replace(placeholder, str(value))

    if not re.fullmatch(r"[0-9+\-*/.\s]+", expr):
        raise ValueError(f"Invalid characters in expression: {expr}")

    def tokenize(expression):
        tokens = []
        i = 0

        while i < len(expression):
            if expression[i].isspace():
                i += 1
                continue

            if expression[i].isdigit() or expression[i] == ".":
                num_start = i
                while i < len(expression) and (
                    expression[i].isdigit() or expression[i] == "."
                ):
                    i += 1
                try:
                    tokens.append(float(expression[num_start:i]))
                except ValueError:
                    raise ValueError(
                        f"Invalid number format: {expression[num_start:i]}"
                    )
                continue

            if expression[i] in "+-*/":
                if expression[i] == "-" and (not tokens or isinstance(tokens[-1], str)):
                    num_start = i
                    i += 1
                    while i < len(expression) and (
                        expression[i].isdigit() or expression[i] == "."
                    ):
                        i += 1
                    if i > num_start + 1:
                        try:
                            tokens.append(float(expression[num_start:i]))
                        except ValueError:
                            raise ValueError(
                                f"Invalid number format: {expression[num_start:i]}"
                            )
                    else:
                        tokens.append(expression[num_start])
                else:
                    tokens.append(expression[i])
                    i += 1
                continue

            raise ValueError(f"Unexpected character: {expression[i]}")

        return tokens

    tokens = tokenize(expr)

    if not tokens:
        raise ValueError("Empty expression after parsing.")

    if isinstance(tokens[0], str) and tokens[0] != "-":
        raise ValueError("Expression cannot start with an operator.")

    if isinstance(tokens[-1], str):
        raise ValueError("Expression cannot end with an operator.")

    for i in range(len(tokens) - 1):
        if (
            isinstance(tokens[i], str)
            and isinstance(tokens[i + 1], str)
            and tokens[i + 1] != "-"
        ):
            raise ValueError("Invalid consecutive operators.")

    if len(tokens) == 1:
        if isinstance(tokens[0], float):
            return tokens[0]
        raise ValueError("Invalid expression.")

    def calculate(tokens_list):
        i = 1
        while i < len(tokens_list):
            if not isinstance(tokens_list[i], str):
                i += 1
                continue

            if tokens_list[i] == "*":
                if (
                    i == 0
                    or i == len(tokens_list) - 1
                    or isinstance(tokens_list[i - 1], str)
                    or isinstance(tokens_list[i + 1], str)
                ):
                    raise ValueError("Invalid expression format.")
                tokens_list[i - 1] = tokens_list[i - 1] * tokens_list[i + 1]
                tokens_list.pop(i)
                tokens_list.pop(i)
            elif tokens_list[i] == "/":
                if (
                    i == 0
                    or i == len(tokens_list) - 1
                    or isinstance(tokens_list[i - 1], str)
                    or isinstance(tokens_list[i + 1], str)
                ):
                    raise ValueError("Invalid expression format.")
                if abs(tokens_list[i + 1]) < 1e-10:
                    raise ZeroDivisionError("Division by zero.")
                tokens_list[i - 1] = tokens_list[i - 1] / tokens_list[i + 1]
                tokens_list.pop(i)
                tokens_list.pop(i)
            else:
                i += 1

        result = tokens_list[0]
        i = 1
        while i < len(tokens_list):
            if not isinstance(tokens_list[i], str):
                raise ValueError("Invalid expression format.")

            if tokens_list[i] == "+":
                if i == len(tokens_list) - 1 or isinstance(tokens_list[i + 1], str):
                    raise ValueError("Invalid expression format.")
                result += tokens_list[i + 1]
            elif tokens_list[i] == "-":
                if i == len(tokens_list) - 1 or isinstance(tokens_list[i + 1], str):
                    raise ValueError("Invalid expression format.")
                result -= tokens_list[i + 1]
            else:
                raise ValueError(f"Unexpected operator: {tokens_list[i]}")
            i += 2

        return result

    try:
        return calculate(tokens)
    except Exception as e:
        raise type(e)(f"{str(e)} in expression: {original_expr}")


def append_to_history(text, result):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{text} = {result}\n")


def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")
    try:
        conn.sendall(
            b"Welcome to TCP Calculator Server!\nEnter expression or GET filename:\n"
        )
        while True:
            data = conn.recv(1024)
            if not data:
                break

            text = data.decode("utf-8", errors="ignore").strip()
            if not text:
                conn.sendall(b"Enter expression or GET filename:\n")
                continue

            if text.startswith("GET"):
                parts = text.split()
                if len(parts) == 2:
                    filename = parts[1]
                    if os.path.exists(filename):
                        with open(filename, "r", encoding="utf-8") as f:
                            content = f.read()
                        response = f"HTTP/1.1 200 OK\r\n\r\n{content}"
                    else:
                        response = "HTTP/1.1 404 File Not Found\r\n"
                    response += "\r\nEnter expression or GET filename:\r\n"
                    conn.sendall(response.encode("utf-8"))
                else:
                    conn.sendall(
                        b"HTTP/1.1 400 Bad Request\r\n\r\nEnter expression or GET filename:\r\n"
                    )
            else:
                try:
                    result = calculate_expression(text)
                    append_to_history(text, result)
                    conn.sendall(
                        f"Result = {result}\r\n\r\nEnter expression or GET filename:\r\n".encode(
                            "utf-8"
                        )
                    )
                except Exception as e:
                    err = (
                        f"Error: {str(e)}\r\n\r\nEnter expression or GET filename:\r\n"
                    )
                    conn.sendall(err.encode("utf-8"))
    finally:
        conn.close()
        print(f"[DISCONNECTED] {addr}")


def main():
    print("[START] Server is starting...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"[LISTENING] on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(
                target=handle_client, args=(conn, addr), daemon=True
            ).start()


if __name__ == "__main__":
    main()
