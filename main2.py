import threading

# Задана спільна змінна
shared_var = 0

# Кількість змінних, на які буде розбита спільна змінна
num_sub_vars = 10

# Список менших змінних
sub_vars = [0] * num_sub_vars

# Створюємо м'ютекс
mutex = threading.Lock()

# Функція, яку буде виконувати кожен потік
def increment_sub_var(sub_var_index):
    global shared_var
    for i in range(1000):
        # Захоплюємо м'ютекс
        mutex.acquire()
        sub_vars[sub_var_index] += 1
        shared_var = int(sum(sub_vars)/num_sub_vars)
        # Звільняємо м'ютекс
        mutex.release()

# Створюємо потоки для кожної меншої змінної
threads = []
for i in range(num_sub_vars):
    thread = threading.Thread(target=increment_sub_var, args=(i,))
    threads.append(thread)

# Запускаємо потоки
for thread in threads:
    thread.start()

# Очікуємо завершення потоків
for thread in threads:
    thread.join()

# Виводимо значення спільної змінної
print(shared_var)
