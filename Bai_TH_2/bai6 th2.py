print("sinh vien:Nguyen Xuan Vu MSV:235752021610011")

j=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print (','.join(j))
