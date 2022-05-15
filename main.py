import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def vis(C):
    Z = C
    fig = plt.figure()
    ax1 = fig.add_subplot(131)
    ax1.set_xlabel('Столбец')
    ax1.set_ylabel('Строка')
    kku = ax1.imshow(Z)
    fig.colorbar(kku, ax=ax1)

    ax2 = fig.add_subplot(132, projection='3d')
    X, Y = np.meshgrid(np.linspace(1, len(C), len(C)), np.linspace(1, len(C), len(C)))
    ax2.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
    ax2.set_zlim(min([min(i) for i in Z]), max([max(i) for i in Z]))
    ax2.set_xlabel('Столбец')
    ax2.set_ylabel('Строка')
    ax2.set_zlabel('Значение')

    ax3 = fig.add_subplot(133)
    kkh = sns.ecdfplot(data=pd.DataFrame(np.transpose(C)), palette=f"ch:rot=-.25,hue=1,light=.75", ax=ax3)
    kkh.set_title('Градация значений по строкам')

    ax1.set_title('Тепловая карта')
    ax2.set_title('Объёмная тепловая карта')

    fig.set_figwidth(14)
    fig.set_figheight(5)
    plt.subplots_adjust(wspace=0.4)
    plt.show()


try:
    n = int(input("Задайте количество строк и столбцов > 3: "))
    while n < 4:
        n = int(input("Задайте количество строк и столбцов > 3: "))
    k = int(input("Задайте значение коэффициента k: "))
    A = np.random.randint(-10.0, 10.0, (n, n), dtype='int64')
    """A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if j == i or j == n-1-i:
                A[i][j] = 0
            else:
                A[i][j] = (n - i) * 10 + j"""
    F = np.copy(A)
    np.set_printoptions(precision=2, linewidth=200)
    print(f"----A----\n{A}\n\n----F----\n{F}\n\n")
    cond_e, cond_lines = 0, 1
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                cond_lines *= int(A[i][j])
            if i > (n // 2 - (n - 1) % 2) and j > (n // 2 - (n - 1) % 2) and j % 2 == 0 and A[i][j] == 0:
                cond_e += 1
    print(f"Количество нулей в нечетных столбцах Е = {cond_e}\nПроизведение чисел в нечетных строках = {cond_lines}\n")
    if cond_e * k > cond_lines:
        for i in range(n // 2):
            F[i] = F[i][::-1]
    else:
        for i in range(n // 2):
            for j in range(n // 2):
                F[i][j], F[n // 2 + n % 2 + i][n // 2 + n % 2 + j] = F[n // 2 + n % 2 + i][n // 2 + n % 2 + j], F[i][j]
    print(f"----F----\n{F}\n")
    if np.linalg.det(A) > sum(np.diagonal(F)):
        if np.linalg.det(F) == 0:
            print("Матрица F - вырожденная, невозможно провести вычисления")
        else:
            print(f"----A*AT – K * F-1----\n{np.matmul(A, np.transpose(A)) - np.linalg.inv(F) * k}")
            vis(np.matmul(A, np.transpose(A)) - np.linalg.inv(F) * k)
    else:
        if np.linalg.det(A) == 0:
            print("Матрица A - вырожденная, невозможно провести вычисления")
        else:
            print(f"----(A-1 +G-FТ)*K----\n{(np.linalg.inv(A) + np.tril(A) - np.transpose(F)) * k}")
            vis((np.linalg.inv(A) + np.tril(A) - np.transpose(F)) * k)
    print(f"Время выполнения: {time.process_time()}")

except ValueError:
    print("Введённые данные не являются числом")