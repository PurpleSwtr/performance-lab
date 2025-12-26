import sys

def find_path(array_size: int, step: int) -> str:
    """
    Функция для нахождения пути в круговом массиве
    
    Args:
        array_size (int): Размер массива (1..n)
        step (int): Длина обхода (шаг)
        
    Returns:
        str: Путь из первых элементов интервалов
    """
    
    # Сделал локальные переменные, потому что python работает с ними быстрее чем с глобальными (проверенно)
    # Ну и плюсом наименования переменных в функции более понятные
    n = array_size
    m = step

    if n <= 0 or m <= 0:
        return ""
    
    # Каждый интервал ВСЕГДА начинается с первого элемента 
    if m == 1:
        return "1"
    
    result = []
    current = 0
    
    while True:
        result.append(str(current + 1))
        current = (current + (m - 1)) % n
        
        if current == 0:
            break
    
    return ''.join(result)

if __name__ == "__main__":

    # На случай если в тестах будет попытка прогнать другое количество аргументов
    if len(sys.argv) != 5:
        print("Неверный ввод аргументов")
        sys.exit(1)
    
    try:
        n1, m1, n2, m2 = map(int, sys.argv[1:5])
        
        # Проверочка через генератор на все положительные числа
        if any(val <= 0 for val in (n1, m1, n2, m2)):
            raise ValueError("Все значения должны быть положительными")

        path1 = find_path(array_size = n1, step = m1)
        path2 = find_path(array_size = n2, step = m2)

        print(f"{path1}{path2}")
    
    except ValueError as e: 
        print(f"Ошибка: {e}")
        sys.exit(1)