#password
times = 3
while times > 0 :
    times = times - 1
    real_password = 'a123456'
    password = input('請輸入密碼: ')
    if real_password == password:
        print('登入成功!')
        break
    else:
        if times > 0:
            print('密碼錯誤還有',times, '次機會')
        else:
            print('密碼錯誤')

    