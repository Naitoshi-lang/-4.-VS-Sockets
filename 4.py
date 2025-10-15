#Сервер

import socket
import datetime
import select

def start_async_time_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12348))
    server_socket.listen(5)
    server_socket.setblocking(False)
    
    print("Асинхронный сервер времени запущен...")
    
    inputs = [server_socket]
    
    while True:
        readable, _, exceptional = select.select(inputs, [], inputs, 1)
        
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
                        request = data.decode('utf-8')
                        print(f"Получен запрос: {request} от {s.getpeername()[0]}")
                        
                        # Обрабатываем запрос
                        if request == "time":
                            response = datetime.datetime.now().strftime("%H:%M:%S")
                        elif request == "date":
                            response = datetime.datetime.now().strftime("%Y-%m-%d")
                        else:
                            response = "Неизвестный запрос"
                        
                        # Отправляем ответ
                        s.send(response.encode('utf-8'))
                    
                    # Закрываем соединение после ответа
                    inputs.remove(s)
                    s.close()
                    
                except Exception as e:
                    print(f"Ошибка: {e}")
                    inputs.remove(s)
                    s.close()
        
        # Обработка исключений
        for s in exceptional:
            inputs.remove(s)
            s.close()

if __name__ == "__main__":
    start_async_time_server()



#Клиент


import socket
import select

def start_async_time_client():
    # Пользователь выбирает запрос
    while True:
        request = input("Введите 'time' для получения времени или 'date' для получения даты: ").strip().lower()
        if request in ['time', 'date']:
            break
        print("Неверный ввод. Попробуйте снова.")
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12348))
    client_socket.setblocking(False)
    
    # Отправляем запрос
    client_socket.send(request.encode('utf-8'))
    
    # Ожидаем ответ
    ready = select.select([client_socket], [], [], 10)
    if ready[0]:
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Полученные данные: {response}")
    else:
        print("Таймаут ожидания ответа")
    
    client_socket.close()

if __name__ == "__main__":
    start_async_time_client()
