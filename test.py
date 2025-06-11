import socket
from Communicator import Communicator

class Server(Communicator):
    def __init__(self, ip, port):
        super().__init__(index=0, ip_address=ip)
        self.sock.bind((ip, port))
        self.sock.listen(2)
        print(f"[Server] Listening at {ip}:{port}")
        self.clients = []

    def accept_clients(self):
        for _ in range(2):  # 等待两个客户端连接
            conn, addr = self.sock.accept()
            print(f"[Server] Connected from {addr}")
            self.clients.append(conn)

    def run(self):
        for i in range(10):  # 进行3轮收发
            for idx, client in enumerate(self.clients):
                self.send_msg(client, ['MSG_FROM_SERVER', f'Hello Client {idx+1}, round {i+1}'])
                msg = self.recv_msg(client, 'MSG_FROM_CLIENT')
                print(f"[Server] Received from Client {idx+1}: {msg[1]}")

if __name__ == '__main__':
    server = Server('192.168.123.140', 5124)
    server.accept_clients()
    server.run()
