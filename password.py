#password
times = 3
while times <= 3 and times > 0 :
    real_password = 'a123456'
    password = input('請輸入密碼: ')
    if real_password == password:
        print('登入成功!')
        break
    else:
        times = times - 1
        if times == 2:
            print('密碼錯誤還有',times, '次機會')
        elif times == 1:
            print('密碼錯誤還有',times, '次機會')
        else:
            break

    