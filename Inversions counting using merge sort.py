def merge(a,b):
  arr=[]
  a=a[::-1]
  b=b[::-1]
  s=0
  while a and b:
    if a[-1]<b[-1]:arr+=[a.pop()]
    elif a[-1]>b[-1]:arr+=[b.pop()];s+=len(a)
    else:arr+=[a.pop()]
  while a:arr+=[a.pop()]
  while b:arr+=[b.pop()]
  return arr,s

def mergesort(a):
  n=len(a)
  if n==1:return a,0
  mid=len(a)//2
  left,p=mergesort(a[:mid])
  right,q=mergesort(a[mid:])
  a,k=merge(left,right)
  return a,p+q+k

#this function , returns the number of inversions in an array  , and the sorted array
#using merge sort
