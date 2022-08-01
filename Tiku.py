import math
list=[25,5,32,50,13,35,2]
a='dugaojian'
b={45:32,3:98,24:89}
#输出a+b
def s1_love(a,b):
    return a+b
#冒泡排序
def s2_love(list):
    if len(list)<2:
        return list
    else:
        for i in range(0,len(list)-1):
            for j in range(i+1,len(list)):
                if(list[i]>list[j]):
                    a=list[i]
                    list[i]=list[j]
                    list[j]=a
                else:
                    pass
    return list
#倒序输出字符串
def s3_love(a):
    b=''
    for i in range(0,len(a)):
        b=b+a[-1-i]
    return b
#输入字典的键，并且排序
def s4_love(b):
    list=[]
    for i in b.keys():
        list.append(i)
    list.sort()
    return list
#输出奇数位的字符串
def s5_love(a):
    b=''
    for i in range(0,len(a)):
        if i%2==0:
            b=b+a[i]
        else:
            pass
    return b
#输入100以内素数，中间用逗号隔开，最后一位不隔开
def s6_love():
    str1=''
    for i in range(2,101):
        if i==2:
            str1=str1+str(i)+' '
            continue
        else:
            aaa=True
            for j in range(2,i):
                if i%j==0:
                    aaa=False
                else:
                    continue
            if aaa:
                if i==100:
                    str1 = str1 + str(i)
                else:
                    str1 = str1 + str(i) + ' '
    print(str1)
#输出矩形的面积和周长
def s7_love(a,b):
    print(str(a*b)+' '+str(2*(a+b)))
#输出列表的中位数
def s8_love(list):
    list.sort()
    if (len(list)%2==0):
        print((list[int(len(list)/2)]+list[int(len(list)/2)-1])/2)
    else:
        print(list[math.ceil(len(list)/2-1)])

#输出两个数的最大公约数
def s9_love(a,b):
    if a<b:
        pan=True
        for i in range(a,1,-1):
            if b%i==0:
                if a%i==0:
                    print(i)
                    pan=False
                    break
                else:
                    continue
            else:
                pass
        if pan:
            print(1)
    else:
        pan=True
        for i in range(b,1,-1):
            if a%i==0:
                if b%i==0:
                    print(i)
                    pan=False
                    break
                else:
                    continue
            else:
                pass
        if pan:
            print(1)
#输出两个数的最小公倍数
def s10_love(a,b):
    if a>b:
        for i in range(a,a*b+1):
            if i%b==0:
                if i%a==0:
                    print(i)
                    break
                else:
                    continue
    else:
        for i in range(b,a*b+1):
            if i%a==0:
                if i%b==0:
                    print(i)
                    break
                else:
                    continue

def s11_love(list):
    print(list)
    sum1=0
    sum2=0
    sum3=0
    sum4=1
    for i in list:
        sum4=sum4*i
        #判断0的个数
        if i%10==0:
            b=i
            while b%10==0:
                sum1=sum1+1
                b=b/10
        else:
            pass
        #判断5的个数
        if i%5==0:
            c = i
            if c%10==0:
                while c % 10 == 0:
                    c = c/ 10
                    if c%10!=0:
                        if c%5==0:
                            sum2=sum2+1
            else:
                sum2=sum2+1
        #判断2的个数
        if i%2==0:
            if i%10==0:
                d=i
                while d % 10 == 0:
                    d = d / 10
                    if d % 10 != 0:
                        if d % 2 == 0:
                            while d%2==0:
                                d=d/2
                                sum3 = sum3 + 1


            else:
                e=i
                while e % 2 == 0:
                    e = e / 2
                    sum3 = sum3 + 1
    if sum2<sum3:
        if sum2==0:
            print(sum1+sum2)
        else:
            print(sum1+sum2+1)
    else:
        print(sum1+sum3)
    print(sum1,sum2,sum3)
    print(sum4)
s11_love(list)
