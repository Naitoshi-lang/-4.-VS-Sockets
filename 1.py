# Сервер
import socket
import datetime

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    # Отправление
    message = "Привет, сервер!"
    client_socket.send(message.encode('utf-8'))
    
    # Получение 
    response = client_socket.recv(1024).decode('utf-8')
    current_time = datetime.datetime.now().strftime("%H:%M")
    print(f"В {current_time} от [localhost] получена строка: {response}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()

# Клиент

import socket
import datetime

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    # Отправляем приветствие серверу
    message = "Привет, сервер!"
    client_socket.send(message.encode('utf-8'))
    
    # Получаем ответ от сервера
    response = client_socket.recv(1024).decode('utf-8')
    current_time = datetime.datetime.now().strftime("%H:%M")
    print(f"В {current_time} от [localhost] получена строка: {response}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
