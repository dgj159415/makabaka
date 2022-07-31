import math

list=[4,1,34,555,276,54,6,89,9,98,453]
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


print(s4_love(b))
