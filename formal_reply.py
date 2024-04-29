def rem_uns():  # удаление адресов отписавшихся 
    with open('data/imported/unsubs.txt', 'r', encoding='utf-8') as file:  # откр файл с отписками
        uns = file.readlines()
        dct_uns = {}
        for st in uns:
            s = st.strip().split(';')
            if len(s) == 2:
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

     
        

    #with open('data/imported/unsubs.txt', 'w', encoding='utf-8') as file:
        #for k,v in dct_uns.items():
            #file.write(f'{k};{v}')

rem_uns()