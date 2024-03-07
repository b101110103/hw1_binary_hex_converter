while True:
    
    num = int(input('Please input a number between 0 to 255:'))
    
    #界定範圍
    if not 0 <= num <= 255:
        print('This number is not in range.')
        break
    
    blist = [] 
    binary = ''
    
    #判斷完各個位數後，把0或1放到blist當中
    for i in range(7,-1,-1):    
        if num >= 2**i:
            blist.append(1)
            num -= 2**i
        else:
            blist.append(0)
    
    #把blist轉換成string
    for i in range(len(blist)):
        binary += str(blist[i])
    
    #再轉換成正整數以消除前面的0
    binary = int(binary)
    
    print('The binary form:', binary)
    
    pre = blist[0]*8 + blist[1]*4 + blist[2]*2 + blist[3]*1
    post = blist[4]*8 + blist[5]*4 + blist[6]*2 + blist[7]*1
    
    hlist = ['A','B','C','D','E','F']
    
    #10到15的數字在十六進位裡是字母
    if 10 <= pre <= 15:
        pre = str(hlist[pre-10])
    if 10 <= post <= 15:
        post = str(hlist[post-10])
    
    #因為可能有字母，所以用string
    pre = str(pre)
    post = str(post)
    
    #消除第一位數的0
    if pre == '0':
        print('The hexadecimal form:', post)
    else:
        print('The hexadecimal form:', pre + post)
    
    break