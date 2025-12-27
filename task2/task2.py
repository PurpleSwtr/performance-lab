import sys
import math

def check_points(ellipse_file: str, points_file: str) -> None:
    """
    Функция для определения положения точек относительно эллипса
    
    Args:
        ellipse_file (str): Путь к файлу с параметрами эллипса
        points_file (str): Путь к файлу с координатами точек
        
    Returns:
        None: Функция выводит результаты в stdout
    """
    
    with open(ellipse_file, 'r') as f:
        center_line = f.readline().strip().split()
        radii_line = f.readline().strip().split()
        
        x0, y0 = float(center_line[0]), float(center_line[1])
        a, b = float(radii_line[0]), float(radii_line[1])
    
    with open(points_file, 'r') as f:
        points = []
        for line in f:
            if line.strip():
                x, y = map(float, line.strip().split())
                points.append((x, y))

    for x, y in points:
        value = ((x - x0) ** 2) / (a ** 2) + ((y - y0) ** 2) / (b ** 2)
        
        if math.isclose(value, 1.0):
            print(0)
        elif value < 1:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    
    try:
        # На случай если в тестах будет попытка прогнать другое количество аргументов
        if len(sys.argv) != 3:
            raise ValueError("Неверное количество аргументов")

        ellipse_file, points_file = map(str, sys.argv[1:3])
        
        check_points(ellipse_file=ellipse_file, points_file=points_file)
    
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e.filename}")
        sys.exit(1)
    
    except ValueError as e:
        print(f"Ошибка в значениях: {e}")
        sys.exit(1)
    
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)