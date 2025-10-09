
#building binary tree , and the function for processing queries

tree=[0]*(n*4)

def query(node,l,r,queryl,queryr):
  if l>queryr or queryl>r:return float('inf')
  if queryl<=l<=r<=queryr:return tree[node]
  mid=(l+r)//2
  return min(query(2*node+1,l,mid,queryl,queryr),query(2*node+2,mid+1,r,queryl,queryr))
 
def build(node,l,r):
  if l==r:tree[node]=arr[l]
  else:
    mid=(l+r)//2
    
    leftchild=2*node+1
    build(leftchild,l,mid)
    
    rightchild=2*node+2
    build(rightchild,mid+1,r)
    
    tree[node]=min(tree[leftchild],tree[rightchild])
