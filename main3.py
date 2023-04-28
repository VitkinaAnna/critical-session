import random
import concurrent.futures
import time

# Розміри матриць
n = 2
m = 2
k = 2

# Заповнення матриць випадковими числами
#A = [[random.randint(1, 10) for j in range(m)] for i in range(n)]
#B = [[random.randint(1, 10) for j in range(k)] for i in range(m)]

A = [[1, 2], [3, 4]]
B = [[1, 2], [3, 4]]
start_time = time.time()

# Виведення початкових матриць
print("Матриця A:")
for row in A:
    print(row)
print("\nМатриця B:")
for row in B:
    print(row)

print ("")

# Функція для обчислення одного елементу
def multiply_element(i, j):
    result = sum(A[i][x] * B[x][j] for x in range(m))
    print(f"[{A[i][j]}, {B[j][i]}] = {result}")
    return result


# Створюємо пул потоків
with concurrent.futures.ThreadPoolExecutor(max_workers=((n) *(k))) as executor:
    # Додаємо задачі на обчислення елементів
    futures = [executor.submit(multiply_element, i, j) for i in range(n) for j in range(k)]

    # Очікуємо завершення всіх задач
    concurrent.futures.wait(futures)

# Матриця С

C = [[0 for j in range(k)] for i in range(n)]
for i in range(n):
    for j in range(k):
        C[i][j] = sum(A[i][x] * B[x][j] for x in range(m))

print("\nМатриця С")
for row in C:
    print(row)


end_time = time.time()
print(f"Час виконання з n*k потоками: {(end_time - start_time)*1000000:.4f} секунд")