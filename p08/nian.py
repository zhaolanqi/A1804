x=int(input())
ifx%4==0 and x%100!=0:
    print('闰年')
elif x%400==0:
    print('闰年')
else:
    print('平年')
