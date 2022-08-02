import random
import time

from multiprocessing import Pool
import multiprocessing

from Tiku import img_name


def img_name(num):
    # img_name = ''
    # for i in range(12):
    #     if i < 5:
    #         tmp = chr(random.randint(65, 90))
    #     else:
    #         tmp = random.randint(0, 9)
    #     img_name += str(tmp)
    #return img_name
    print(num)
if __name__=='__main__':
    p=Pool(3)
    for i in range(10):

        p.apply_async(img_name,args=[i,])
