import socket


def main():
    s = socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 50007))
    s.listen(0)
    conn_socket, address_info = socket.accept


if __name__ == '__main__':
    main()
