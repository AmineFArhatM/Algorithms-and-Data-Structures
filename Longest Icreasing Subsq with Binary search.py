#this code finds the longest increasing subsequence on an array using bs 
#O (n log(n) )
def find_LIS_using_BS(a):
  p=[a[0]]
  for x in a[1:]:
    if x>p[-1]:p.append(x)
    else:
      r,l=len(p)-1,-1
      while r-l>1:
        mid=(l+r)//2
        if p[mid]>=x:r=mid
        else:l=mid
      p[r]=x
  return p
print(find_LIS_using_BS(a))
