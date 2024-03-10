for i in range(int(input())):
    n=input()
    z,o=n.count('0'),n.count('1')
    if z>o:
        print('LOSE')
    else:
        print('WIN')
  