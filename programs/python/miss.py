miss = [1,2,3,4,5,8,10]

lis = [n1+1 for n1,n2 in zip(miss,miss[1:]) if n2-n1 != 1]
print(lis)
