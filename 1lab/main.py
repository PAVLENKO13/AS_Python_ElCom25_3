"""Лабораторная 1.

Текст задания:
https://github.com/hilleri123/AS_Python/blob/master/1lab/task.md

Запуск из корня репозитория:
    python3 1lab/main.py
    pytest
"""


def main():
    print("hello world")
    def input_data() :
    '''
    Проверка корректности вводимых значений. Принимаются исключительно [1;5]. Возвращает координаты в списке (Готов)
    '''
    import random

def create_solvable_board():
    """Генерирует гарантированно решаемое поле 5x5."""
    # Начинаем с полностью выключенного поля (все '.')
    board = [['.' for _ in range(5)] for _ in range(5)]
    
    # Делаем от 10 до 20 случайных нажатий, чтобы запутать поле
    # Поскольку ходы обратимы, полученная позиция точно имеет решение
    num_presses = random.randint(10, 20)
    for _ in range(num_presses):
        r = random.randint(0, 4)
        c = random.randint(0, 4)
        toggle(board, r, c)
        
    # Если случайно получилось полностью пустое поле, генерируем заново
    if is_victory(board):
        return create_solvable_board()
        
    return board

def toggle(board, r, c):
    """Переключает выбранную клетку и ее ортогональных соседей."""
    directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            board[nr][nc] = '.' if board[nr][nc] == '*' else '*'

def print_board(board):
    """Красиво выводит поле с координатами."""
    print("\n    1 2 3 4 5")
    for i, row in enumerate(board):
        print(f"  {i + 1} {' '.join(row)}")
    print()

def is_victory(board):
    """Проверяет, все ли лампы выключены."""
    for row in board:
        if '*' in row:
            return False
    return True

def play_game():
    print("=== ИГРА «ВЫКЛЮЧИ СВЕТ» ===")
    print("Цель: выключить все лампы (* -> .)")
    print("Генерация гарантированно решаемой позиции...")
    
    board = create_solvable_board()
    moves_count = 0
    
    while True:
        print_board(board)
        print(f"Сделано ходов: {moves_count}")
        
        user_input = input("Введите координаты (строка столбец, например, 3 2) или 'exit' для выхода: ").strip()
        
        if user_input.lower() == 'exit':
            print("Выход из игры.")
            break
            
        parts = user_input.split()
        if len(parts) != 2:
            print("Ошибка! Введите ровно два числа через пробел.")
            continue
            
        try:
            row, col = int(parts[0]), int(parts[1])
        except ValueError:
            print("Ошибка! Координаты должны быть числами.")
            continue
            
        # Проверка границ 1..5
        if not (1 <= row <= 5 and 1 <= col <= 5):
            print("Ошибка! Координаты должны быть в диапазоне от 1 до 5.")
            continue
            
        # Выполняем ход (переводим индексы пользователя 1..5 в индексы массива 0..4)
        toggle(board, row - 1, col - 1)
        moves_count += 1
        
       

if __name__ == "__main__":
    play_game()


    raise NotImplementedError(
        "Реализуйте лабораторную 1 своего варианта (поле variant в student.json)"
    )


if __name__ == "__main__":
    main()
