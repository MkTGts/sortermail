import csv


def importable(file_old='data/imported/file1.csv', names='True') -> list:  # если True, то только с именами, False - все строки
    with open(file_old, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=';')
        res_list = {}
        c = 0
        for i in file_reader:
            c += 1
            #st = i[0].split(';')
            if names:
                if i[4] != '""':
                    res_list[i[3]] = i[4]
            else:
                res_list[i[3]] = i[4]
        print(c, len(res_list))
        return res_list

def writer_list(res_list=importable(names=False), file_name='data/file_new.txt') -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        f = True
        for em, name in res_list.items():
            if f:
                f = False
                continue
            else:
                file.write(em.strip('"') + ';' + name.strip('"').capitalize() + '\n')

writer_list()


    



    
    
    
        
        