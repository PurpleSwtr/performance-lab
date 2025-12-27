import sys

def min_moves(nums: list[int]) -> int | str:
    """
    Функция для вычисления минимального количества ходов
    для приведения всех элементов массива к одному числу.
    
    Args:
        nums: список целых чисел
        
    Returns:
        int: минимальное количество ходов, если <= 20
        str: сообщение об ошибке, если > 20
    """
    
    # Сделал локальные переменные для скорости
    n = len(nums)
    
    if n == 0:
        return 0
    
    # Самый оптимальный целевой элемент — медиана массива
    nums_sorted = sorted(nums)
    median = nums_sorted[n // 2]
    
    # Минимальное количество ходов
    total_moves = 0
    for num in nums:
        total_moves += abs(num - median)
    
    # Проверил ограничение в 20 ходов как указали в задании
    if total_moves <= 20:
        return total_moves
    else:
        return "20 ходов недостаточно для приведения всех элементов массива к одному числу"

if __name__ == "__main__":
    
    try:
        # На случай если в тестах будет попытка прогнать другое количество аргументов
        if len(sys.argv) != 2:
            raise ValueError("Неверное количество аргументов")
        
        # Тут уж не стал бойлерплейтить, и принимать аргументы через мапу
        file_path = sys.argv[1]
        
        numbers = []
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    numbers.append(int(line))
        
        result = min_moves(numbers)
        
        print(result)
    
    except FileNotFoundError:
        print(f"Файл не найден")
        sys.exit(1)
    
    except ValueError as e:
        print(f"Ошибка в значениях: {e}")
        sys.exit(1)
    
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)