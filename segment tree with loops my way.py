def build():
  q=[(0,0,n-1)]
  for node,l,r in q:
    if l!=r:
      mid=(l+r)//2
      q+=[(2*node+1,l,mid),(2*node+2,mid+1,r)]
  for node,l,r in q[::-1]:
    if l==r:tree[node]=a[l]
    else:
      tree[node]=min(tree[2*node+1],tree[2*node+2])
  
 
 
def query(ql,qr):
  q=[(0,0,n-1)]
  ans=inf
  while q:
    node,l,r=q.pop()
    if ql<=l<=r<=qr:ans=min(ans,tree[node])
    elif not(ql>r or l>qr):
      mid=(l+r)//2
      q+=[(2*node+1,l,mid),(2*node+2,mid+1,r)]
  return ans
