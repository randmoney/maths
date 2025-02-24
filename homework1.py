import re

def determinant(matrix):
    """Вычисление определителя матрицы (без использования сторонних библиотек)."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for col in range(n):
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(minor)
    return det

def cramer_solver(A, b):
    """Решение СЛАУ методом Крамера без использования сторонних библиотек."""
    n = len(A)
    det_A = determinant(A)
    
    if det_A == 0:
        raise ValueError("Система не имеет единственного решения (определитель равен 0).")
    
    solutions = []
    for i in range(n):
        A_i = [row[:] for row in A]
        for j in range(n):
            A_i[j][i] = b[j]
        solutions.append(determinant(A_i) / det_A)
    
    return solutions

def parse_equation(equation):
    """Парсинг уравнения в коэффициенты матрицы и свободный член."""
    equation = equation.replace(" ", "")
    sides = equation.split("=")
    left_side = sides[0]
    right_side = complex(sides[1])
    
    terms = re.findall(r'[+-]?\d*\.?\d*[+-]?\d*j?', left_side)
    terms = [complex(term) if 'j' in term or any(c.isdigit() for c in term) else 0 for term in terms]
    
    return terms, right_side

# Ввод уравнений с клавиатуры
n = int(input("Введите количество уравнений: "))
A = []
b = []

print("Введите уравнения в формате (a+bi) + (c+di) = e+fi:")
for _ in range(n):
    equation = input()
    coefficients, free_term = parse_equation(equation)
    A.append(coefficients)
    b.append(free_term)

solution = cramer_solver(A, b)
print("Решение системы:", solution)