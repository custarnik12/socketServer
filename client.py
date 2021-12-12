import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.connect(('localhost', 8888))  # подключемся к серверному сокету
data = sock.recv(1024)  # читаем ответ от серверного сокета
if(data == b'ready'):
    print(data)
    sock.send(bytes('{"message": "test", "actions": [{"key":"notify", "value": "alo"}, {"key":"query", "value": "foo"}, {"key":"cmd", "value": "echo \"test\" » /tmp/file.txt"}]}', encoding = 'UTF-8'))  # отправляем сообщение
    data = sock.recv(1024)  # читаем ответ от серверного сокета
sock.close()  # закрываем соединение
print(data)

input()
