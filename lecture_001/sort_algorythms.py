def bubble_sort(data:list)-> list:
    """
Реализация алгоритма сортировки пузырьком с обработкой исключений
сортирует элементы данного списка по возрастанию и возвращает его.

"""
    print("Исходные данные ",data)
    try:
        assert isinstance(data,list)
    except AssertionError:
        print("[ОШИБКА] Аргумент функции должен являться списком")
        exit(1)
    for i in range(0,len(data)-1):
        for j in range(i,len(data)-1):
            try:
                if data[j] > data[j+1]:
                    data[j],data[j+1] = data[j+1],data[j]
            except TypeError:
                    print("[ОШИБКА] Для всех членов массива должны быть определены операции сравнения")
                    exit(2)

        print(data)
    return data

