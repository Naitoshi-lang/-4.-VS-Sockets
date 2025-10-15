# Сервер
import socket
import datetime
import select

def start_async_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12347))
    server_socket.listen(5)
    server_socket.setblocking(False)
    
    print("Асинхронный сервер запущен...")
    
    inputs = [server_socket]
    outputs = []
    
    while True:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        
        for s in readable:
            if s is server_socket:
                # Новое подключение
                client_socket, client_address = server_socket.accept()
                client_socket.setblocking(False)
                inputs.append(client_socket)
                print(f"Новое подключение: {client_address}")
            else:
                # Данные от клиента
                try:
                    data = s.recv(1024)
                    if data:
                        message = data.decode('utf-8')
                        current_time = datetime.datetime.now().strftime("%H:%M")
                        print(f"В {current_time} от [{s.getpeername()[0]}] получена строка: {message}")
                        
                        # Отправляем ответ
                        response = "Привет, клиент!"
                        s.send(response.encode('utf-8'))
                    else:
                        # Соединение закрыто
                        inputs.remove(s)
                        s.close()
                except:
                    inputs.remove(s)
                    s.close()

if __name__ == "__main__":
    start_async_server()


# Клиент

import socket
import datetime
import select

def start_async_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12347))
    client_socket.setblocking(False)
    
    # Отправляем сообщение
    message = "Привет, сервер!"
    client_socket.send(message.encode('utf-8'))
    
    # Ожидаем ответ с таймаутом
    ready = select.select([client_socket], [], [], 10)
    if ready[0]:
        response = client_socket.recv(1024).decode('utf-8')
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(f"В {current_time} от [localhost] получена строка: {response}")
    else:
        print("Таймаут ожидания ответа")
    
    client_socket.close()

if __name__ == "__main__":
    start_async_client()
