def merge(a,b):
  arr=[]
  a=a[::-1]
  b=b[::-1]
  s=0
  while a and b:
    if a[-1]<b[-1]:arr+=[a.pop()]
    else:arr+=[b.pop()]
  while a:arr+=[a.pop()]
  while b:arr+=[b.pop()]
  return arr

def mergesort(a):
  n=len(a)
  if n==1:return a
  mid=len(a)//2
  left=mergesort(a[:mid])
  right=mergesort(a[mid:])
  a=merge(left,right)
  return a
