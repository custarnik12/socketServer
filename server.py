import socket
import json
import logging
import os
logging.basicConfig(filename="server.log", level=logging.INFO) #логи
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.bind(('', 8888))  # связываем сокет с портом
sock.listen(10)  # сколько соединений
print('Server is running, please, press ctrl+c to stop')
while True:
    conn, addr = sock.accept()  # принимаем конекты
    conn.send(b"ready") # готовы слушать
    logging.info('connected:', addr)  # инфа о подключении
    data = conn.recv(1024)  # принимаем данные от клиента, по 1024 байт
    data = data.decode('utf-8')
    try:
        res = json.loads(str(data)) #парсим
        conn.send(b"OK")
    except ValueError  as e:
        conn.send(b"ERR")
        logging.exception("VALID_ERR")
    conn.close()  # закрываем соединение
    logging.info(res["message"])
    for i in res["actions"]:
        if i["key"]=="cmd":
            os.system(i["value"])
