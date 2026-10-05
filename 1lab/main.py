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

    is_not_correct = True
    alphabet = "12345"
    while is_not_correct:
        print("Введите координаты лампы в подобном формате!\nВвод: x y | Пример: 3 2 - Вводите без знаков препинания, только через пробел!")
        value = input("Выключить лампу по координатам: ")

        for char in ",.":
            value = value.replace(char, " ")

        coords = [int(coord) for coord in value.split() if coord in alphabet]

        if (
            len(coords) == 2 and 
            1 <= coords[0] <= 5 and 
            1 <= coords[1] <= 5
        ):
            is_not_correct = False
            return coords
        else:
            print("Некорректный ввод, повторите операцию!")

    raise NotImplementedError(
        "Реализуйте лабораторную 1 своего варианта (поле variant в student.json)"
    )


if __name__ == "__main__":
    main()
