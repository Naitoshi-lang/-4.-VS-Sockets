# Сервер


import socket
import datetime

def start_time_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12346))
    server_socket.listen(1)
    print("Сервер времени запущен и ожидает подключения...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        
        # Получение
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Получен запрос: {request} от {client_address[0]}")
        
        # Обрабатывание
        if request == "time":
            response = datetime.datetime.now().strftime("%H:%M:%S")
        elif request == "date":
            response = datetime.datetime.now().strftime("%Y-%m-%d")
        else:
            response = "Неизвестный запрос. Используйте 'time' или 'date'"
        
        # Отправление
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    start_time_server()




# Клиент

    import socket

def start_time_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12346))
    
    # Выбор пользователя
    while True:
        request = input("Введите 'time' для получения времени или 'date' для получения даты: ").strip().lower()
        if request in ['time', 'date']:
            break
        print("Неверный ввод. Попробуйте снова.")
    
    # Отправление
    client_socket.send(request.encode('utf-8'))
    
    # Получение
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Полученные данные: {response}")
    
    client_socket.close()

if __name__ == "__main__":
    start_time_client()
