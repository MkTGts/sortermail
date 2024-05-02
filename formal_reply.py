from datetime import date, datetime

def rem_uns(wrt_stat=True):  # удаление адресов отписавшихся
    '''
    Если функции подать wrt_stat=True, записывает также статистику количества релевантных адресов на дату исполнения
    '''
    with open('data/imported/unsubs.txt', 'r', encoding='utf-8') as file:  # откр файл с отписками
        uns = file.readlines()  # список со строками из файла
        dct_uns = {}  # словарь под значения отписавшихся
        for st in uns:  # итерация по списку значений файла отписавшихся
            # приведение строки <<маил;имя>> к спику [маил, имя]
            s = st.strip().split(';')
            if len(s) == 2:  # если не пустая строка
                dct_uns[s[0]] = s[1]

    with open('data/file_new.txt', 'r', encoding='utf-8') as file:  # откр файл с андресами
        mails = file.readlines()
        dct_mails = {}
        for sm in mails:
            sq = sm.strip().split(';')
            if len(sq) == 2:
                dct_mails[sq[0]] = sq[1]
        print(len(dct_mails))

        for ku in dct_uns.keys():
            if ku in dct_mails.keys():
                print(ku)
                del dct_mails[ku]
        print(len(dct_mails))

    with open('data/file_new.txt', 'w', encoding='utf-8') as file:
        for k, v in dct_mails.items():
            file.write(k + ';' + v + '\n')
    
    if wrt_stat:
        stat_count(dct_mails)
    




def stat_count(dct_mails):
    '''
    Функция записывает результирующее количетсво адресов, после отсева с ошибками и отписавшихся
    В формате дата - кол-во
    '''
    with open('data/count_mail.txt', 'a+', encoding='utf-8') as file:
        s = f'{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}  -  {len(dct_mails)} адресов \n'
        file.write(s)
        print(s)
    

    
 


rem_uns()
