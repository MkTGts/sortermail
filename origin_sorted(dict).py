import csv


# если True, то только с именами, False - все строки
def importable(file_old='data/imported/file1.csv', names=True) -> list:
    '''
    Функция достает из csv файла эмаил и имя
    Если подается names=True, то возвращает только те у которых указано имя
    Если False все подряд
    '''
    with open(file_old, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=';')
        res_dict = {}  # словаьр под выходные значения
        c = 0  # cчетчик собранных значений
        for i in file_reader:  # итарация по обекту из csv файла
            if not c:
                continue
            else:
                if names:  # если отбираем только с заполненными именами
                    if i[4] != '""':
                        res_dict[i[3]] = i[4]
                else:  # если все подряд
                    res_dict[i[3]] = i[4]
            c += 1  # прибавляет к счетчику
        print(c, len(res_dict))
        return res_dict


def writer_list(res_list=importable(names=False), file_name='data/file_new.txt') -> None:
    '''
    Функция записывает в файл file_name значения res_list
    По дефолту то что функция importable достала из csv файла
    '''
    with open(file_name, 'w', encoding='utf-8') as file:
        for em, name in res_list.items():  # итерация по переданным значениям
            file.write(em.strip('"') + ';' +
                       name.strip('"').capitalize() + '\n')  # запись строки


writer_list()
