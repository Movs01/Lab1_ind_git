# импортируем библиотеку random для работы с рандомными числами
import random 

#Функция для генерации списка случайных целых чисел в заданном диапазоне.
def generateList(elementsAmount):
    try:
        if not isinstance(elementsAmount, int) or elementsAmount <= 0:
            raise ValueError("elementsAmount должен быть положительным целым числом")

        list = []
        for i in range(elementsAmount):
            list.append(random.randint(5, 1000))
        return list
    except ValueError as e:
        print("Ошибка:", e)

print(generateList(20))
