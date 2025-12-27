import sys
import json

def build_report(tests_file: str, values_file: str, report_file: str) -> None:
    """
    Функция для заполнения значений в структуре тестов
    
    Args:
        tests_file: путь к файлу со структурой тестов
        values_file: путь к файлу со значениями тестов  
        report_file: путь для сохранения отчета
    """
    
    with open(values_file, 'r') as f:
        values_data = json.load(f)
    
    with open(tests_file, 'r') as f:
        tests_data = json.load(f)
    
    value_by_id = {}
    for item in values_data["values"]:
        value_by_id[item["id"]] = item["value"]
    
    def fill_node(node):
        if "id" in node and node["id"] in value_by_id:
            node["value"] = value_by_id[node["id"]]
        
        if "values" in node and isinstance(node["values"], list):
            for child in node["values"]:
                fill_node(child)
    
    fill_node(tests_data)
    
    with open(report_file, 'w') as f:
        json.dump(tests_data, f, indent=2)

if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise ValueError("Неверное количество аргументов")
        
        tests_file, values_file, report_file = map(str, sys.argv[1:4])
        
        build_report(tests_file, values_file, report_file)
        
        print(f"{report_file}")
    
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
        sys.exit(1)
    
    except json.JSONDecodeError:
        print("Ошибка в формате JSON")
        sys.exit(1)
    
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
