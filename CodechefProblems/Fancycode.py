for i in range(int(input())):
    a = list(map(str,input().split()))
    for i in a:
        i.lower()
        if i == 'not':
            print('Real Fancy')
            break
    else:
        print('regularly fancy')