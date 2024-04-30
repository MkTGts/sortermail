import csv

if input():  # Если 1: True - подается .csv, Если 0: False - подается .txt
    flag = True
    file_old = 'data/imported/file1.csv'
else:  
    flag = False
    file_old = 'data/imported/status_ok.txt'

# если names True, то только с именами, False - все строки
def importable(file_old, names=False, flag=False) -> list:
    '''
    Функция достает из csv файла эмаил и имя
    Если подается names=True, то возвращает только те у которых указано имя
    Если False все подряд
    '''
    with open(file_old, 'r', encoding='utf-8') as file:
        res_dict = {}  # словаьр под выходные значения
        c = 0  # cчетчик собранных значений
        print(flag)

        if flag:  # если .csv
            file_reader = csv.reader(file, delimiter=';')
            for i in file_reader:  # итарация по обекту из csv файла
                if not c:
                    #print(i)
                    c += 1
                    continue
                else:
                    if names:  # если отбираем только с заполненными именами
                        if i[4] != '""':
                            res_dict[i[3]] = i[4]
                    else:  # если все подряд
                        res_dict[i[3]] = i[4]
                    c += 1  # прибавляет к счетчику

        else:  # если .txt
            file_reader = file.readlines()  # достает из файла
            for st in file_reader:  # итерирует по списку строк из файла
                s = st.strip().split(';')  # преобразует строку в список посредствам разделителя ;
                if len(s) == 2:  # если строка не пустая
                    res_dict[s[0]] = s[1]
                    c += 1  # прибавляет к счетчику2



        print(c, len(res_dict))
        return res_dict
        
            



def writer_list(res_list=importable(file_old), file_name='data/file_new.txt') -> None:
    '''
    Функция записывает в файл file_name значения res_list
    По дефолту то что функция importable достала из csv файла
    '''
    with open(file_name, 'w', encoding='utf-8') as file:
        for em, name in res_list.items():  # итерация по переданным значениям
            file.write(em.strip('"') + ';' +
                       name.strip('"').capitalize() + '\n')  # запись строки


writer_list()
