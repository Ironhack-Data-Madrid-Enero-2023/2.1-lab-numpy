import numpy as np
a  = np.array([i for i in range(40)])
a.resize(2,4,5)
print(a)
'''for i in a:
    for j in i:
        for k in j:
            print('i: ',i,'\n','j: ',j,'\n','k: ',k,'\n')'''
print(a[1][2][3])
b = np.where(a<10,a,0)
print(b)