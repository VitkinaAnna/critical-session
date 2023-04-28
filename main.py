import threading
import time
# Спільна змінна
shared_var = 0


# Створюємо м'ютекс
mutex = threading.Lock()

# Функція, яку буде виконувати кожен потік
def increment_shared_var():
    global shared_var
    for i in range(100000):
        # Захоплюємо м'ютекс
        mutex.acquire()
        shared_var += 1
        # Звільняємо м'ютекс
        mutex.release()

# Створюємо два потоки
thread1 = threading.Thread(target=increment_shared_var)
thread2 = threading.Thread(target=increment_shared_var)

# Запускаємо потоки
thread1.start()
thread2.start()

# Очікуємо завершення потоків
thread1.join()
thread2.join()

# Виводимо значення спільної змінної
print(shared_var)

# Виводимо час роботи
start_time = time.time()
end_time = time.time()
print(f"Час виконання : {(end_time - start_time)*100000000:.4f} секунд")
