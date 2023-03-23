'''
29.	Формируется матрица F следующим образом: если в С количество нулей в нечетных столбцах в области 2 больше,
чем сумма чисел по периметру области 4, то поменять в В симметрично области 1 и 3 местами, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего вычисляется выражение: А*(F+А)-K* FT . Выводятся по мере формирования А, F и все матричные операции последовательно.
'''

import random

def printm(matrix):
    matrix1 = list(map(list, zip(*matrix)))
    for i in range(len(matrix1)):
        k = len(max(list(map(str, matrix1[i])), key=len))
        matrix1[i] = [f'{elem:{k}d}' for elem in matrix1[i]]
    matrix1 = list(map(list, zip(*matrix1)))
    for row in matrix1:
        print(*row)
    print()

print("Введите число для задания размерности квадратной матрицы(не менее 4)")
N = int(input())
print("Введите число <K> ")
K = int(input())

if N < 4:
    print("Вы ввели слишком маленькую размерность матрицы")
    exit(0)

print("Матрица А")
matrixA = [[random.randint(-10, 10) for i in range(N)] for j in range(N)]
printm(matrixA)
print("-------------------")


matrixC = [[0 for i in range((N//2))] for j in range((N//2))]
if N % 2 == 0:
    for i in range(0, N // 2, 1):
        for j in range(N // 2, N):
            matrixC[i][j-N//2] = matrixA[i][j]
else:
    for i in range(0, N // 2, 1):
        for j in range(N // 2, N):
            matrixC[i][j-N//2-1] = matrixA[i][j]
print("Подматрица C")
printm(matrixC)
print("-------------------")


matrixF = [[elem for elem in raw] for raw in matrixA]
print("Начальная матрица F")
printm(matrixF)
print("-------------------")

l1 = N//2
ch = []  # числа второй области по нечетным столбцам
summ = 0  # сумма чисел по пириметру четвертой области

if l1 == 2:  # если матрица С размерностью 2x2
    ch.append(matrixC[0][0])
    ch.append(matrixC[0][1])
    summ = matrixC[1][0]+matrixC[1][1]

if l1 == 3:  # если матрица С размерностью 3x3
    ch.append(matrixC[0][0])
    ch.append(matrixC[0][2])
    summ = matrixC[2][0]+matrixC[2][1]+matrixC[2][2]+matrixC[1][1]

if l1 == 4:  # cумма 4 области по пириметру если матрица С размерностью 4x4
    summ = matrixC[3][3]+matrixC[3][2]+matrixC[3][1]+matrixC[3][0]+matrixC[2][1]+matrixC[2][2]

dl = 1
dl1 = 2
n = 1
if l1 > 3: # если матрица размерностью 4x4 и более
    if l1 % 2 == 0: # если матрица четной размерности
        for i in range(0, len(matrixC[0])//2, 2):
            for j in range(0, dl):
                ch.append(matrixC[j][i])
            dl += 2
        for i in range(len(matrixC[0])-2, (len(matrixC[0])//2)-1, -2):
            for j in range(0, dl1):
                ch.append(matrixC[j][i])
            dl1 += 2

    else:  # если матрица нечетной размерности
        for i in range(0, (len(matrixC[0])//2)+1, 2):
            for j in range(0, dl):
                ch.append(matrixC[j][i])
            dl += 2
        dl=1
        for i in range(len(matrixC[0])-1, (len(matrixC[0])//2), -2):
            for j in range(0, dl):
                ch.append(matrixC[j][i])
            dl += 2


dl = l1
dl1 = l1
if l1 > 4:
    if l1 % 2 == 0:
        for i in range(0, dl):
            summ += matrixC[dl-1][i]
        for i in range(1, dl//2):
            for j in range(dl-2, dl-1):
                summ += matrixC[j][i]
                dl -= 1
        for i in range(dl1-2, dl1//2-1, -1):
            for j in range(dl1 - 2, dl1 - 1):
                summ += matrixC[j][i]
                dl1 -= 1
    else:
        for i in range(0, dl):
            summ += matrixC[dl-1][i]
        for i in range(1, dl//2+1):
            for j in range(dl-2, dl-1):
                summ += matrixC[j][i]
                dl -= 1
        for i in range(dl1-2, dl1//2, -1):
            for j in range(dl1 - 2, dl1 - 1):
                summ += matrixC[j][i]
                dl1 -= 1


zero = 0
for i in range(len(ch)):
    if int(ch[i]) == 0:
        zero += 1
print("Количество нулей в нечетных столбцах 2-ой области =", zero, "\n", "-------------------")
print("Сумма чисел по пириметру 4-ой области =", summ, "\n", "-------------------")


matrixB = [[0 for i in range((N//2))] for j in range((N//2))]
if N % 2 == 0:
    for i in range(0, N // 2, 1):
        for j in range(0, N // 2, 1):
            matrixB[i][j-N//2] = matrixA[i][j]
else:
    for i in range(0, N // 2, 1):
        for j in range(0, N // 2, 1):
            matrixB[i][j-N//2] = matrixA[i][j]
print("Подматрица B в матрице А")
printm(matrixB)
print("-------------------")


matrixB1 = [[elem for elem in raw] for raw in matrixB]
matrixF1 = [[elem for elem in raw] for raw in matrixF]
dl = 1
dl1 = 1
if zero > summ: #Если в С количество нулей в нечетных столбцах в области 2 больше,чем сумма чисел по периметру области 4, то поменять в В симметрично области 1 и 3 местами
    if l1 % 2 == 0:
        for i in range(0, l1 // 2, 1):
            for j in range(0, dl, 1):
                matrixF[i][j] = matrixB[i][l1 - 1 - j]
                matrixF[i][l1 - 1 - j] = matrixB[i][j]
            dl += 1
        for i in range(l1 - 1, l1 // 2 - 1, -1):
            for j in range(0, dl1, 1):
                matrixF[i][j] = matrixB[i][l1 - 1 - j]
                matrixF[i][l1 - 1 - j] = matrixB[i][j]
            dl1 += 1
    else:
        for i in range(0, l1 // 2 + 1, 1):
            for j in range(0, dl, 1):
                matrixF[i][j] = matrixB[i][l1 - 1 - j]
                matrixF[i][l1 - 1 - j] = matrixB[i][j]
            dl += 1
        for i in range(l1 - 1, l1 // 2 - 1, -1):
            for j in range(0, dl1, 1):
                matrixF[i][j] = matrixB[i][l1 - 1 - j]
                matrixF[i][l1 - 1 - j] = matrixB[i][j]
            dl1 += 1
    print("Колличество нулей больше, чем сумма чисел по пириметру.\n Заменяем симетрично области 1 и 3 в подматрице В.\n", "--------------")
    print("Матрица F с заменёнными симетрично областями 1 и 3 в подматрице В.\n")
    printm(matrixF)
    print("--------------")
else:  # Иначе С и Е поменять местами несимметрично
    if N % 2 == 0:
        for i in range(0, N//2, 1):
            for j in range(N // 2, N, 1):
                matrixF[i][j] = matrixF1[i+N//2][j]
                matrixF[i+N//2][j] = matrixF1[i][j]
    else:
        for i in range(0, N//2, 1):
            for j in range(N // 2 + 1, N, 1):
                matrixF[i][j] = matrixF1[i + (N // 2) + 1][j]
                matrixF[i + N//2 + 1][j] = matrixF1[i][j]
    print("Колличество нулей меньше или равно сумме чисел по пириметру.\n Заменяем несиметрично подматрицы С и Е\n", "--------------")
    print("Матрица F с заменёнными несиметрично подматрицами С и Е.\n")
    printm(matrixF)
    print("--------------")


matrixFT = [[elem for elem in raw] for raw in matrixF]
for i in range(N):
        for j in range(N):
            matrixFT[i][j] = matrixF[j][i]
print("Транспонированная матрица F")
printm(matrixFT)
print("-------------------")


matrix_F_plus_A = [[elem for elem in raw] for raw in matrixF]
for i in range(N):  # F+A
        for j in range(N):
            matrix_F_plus_A[i][j] = matrixF[i][j] + matrixA[i][j]
print("Матрица F+A")
printm(matrix_F_plus_A)
print("-------------------")


matrixAFA = [[elem for elem in raw] for raw in matrixF]
for i in range(N):  # A*(F+A)
        for j in range(N):
            matrixAFA[i][j] = matrixA[i][j] * matrix_F_plus_A[i][j]
print("Матрица A*(F+A)")
printm(matrixAFA)
print("-------------------")


matrixFTK = [[elem for elem in raw] for raw in matrixF]
for i in range(N):  # K*FT
        for j in range(N):
            matrixFTK[i][j] = matrixFT[i][j] * K
print("Матрица K*FT")
printm(matrixFTK)
print("-------------------")


matrixFinal = [[elem for elem in raw] for raw in matrixF]
for i in range(N):  # A*(A+F)-K*FT
        for j in range(N):
            matrixFinal[i][j] = matrixAFA[i][j] - matrixFTK[i][j]
print("Итоговая матрица А*(F+А)-K*FT")
printm(matrixFinal)
print("Работа программы завершена")