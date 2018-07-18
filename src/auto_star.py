# -*- coding:utf-8 -*-
import os
import time

error_flags = False

if __name__ == '__main__':
    try_time = 0
    while(error_flags == False):
        try_time = try_time+1
        time.sleep(1)
        print "第"+str(try_time)+"次尝试"
        time.sleep(3)
        os.system('python2.7 ./get_actor_works.py')
    print "第"+str(try_time)+"次尝试","任务结束"
