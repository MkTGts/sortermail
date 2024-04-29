import csv


def importable(file_old='data/imported/file1.csv', names='True') -> list:  # если True, то только с именами, False - все строки
    with open(file_old, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=',')
        res_list = []
        c = 0
        for i in file_reader:
            c += 1
            st = i[0].split(';')
            if names:
                if st[4] != '""' and [st[3], st[4]] not in res_list:
                    res_list.append([st[3], st[4]])
            else:
                res_list.append([st[3], st[4]])
        print(c, len(res_list))
        return res_list

def writer_list(res_list=importable(names=False), file_name='data/file_new.txt') -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        for lst in res_list[1:]:
            file.write(lst[0].strip('"') + ';' + lst[1].strip('"').capitalize() + '\n')

writer_list()





    



    
    
    
        
        