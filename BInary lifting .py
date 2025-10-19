#-------------Binary lifting-------------


#this technic is used on rooted trees in order to find the i-th partent of a node
#It is similar to sparce table 

#lets suppose we have an array parent where parent[i]=x means that x is the direct parent of a  node
#this can be easily built using Dfs or Bfs

#lets then build the binary lifting table


from math import log2
def buil_binary_lifting(parent,root):
  n=len(parent)
  maxi=int(log2(n))
  
  #for every node i , let  up[i]=[ 1 first parent , 2nd parent , 4thparent , 8thparent ... ] 
  up=[[None for i in range(maxi)]for j in range(n)]
  
  #setting the first direct parent for every node
  for i in range(n):up[i][0]=parent[i]
  
  #it is obvious that all parents of the root are the root itself
  parent[root]=[root for i in range(maxi)]
  
  #my second parent is my first parent's first parent
  #my fourth parent is my second parent's second parent (2+2=4)
  #my eigth parent is my 4th parent's fourth parent  (4+4=8) 
  #.......
  for i in range(1,maxi):
    for j in range(n):
      lastparent=up[i][j-1]
      parent[i][j]=parent[lastparent][j-1]

      
  return up

#finding the xth parent of a node
def find_ith_parent(node,x):
  
  # x can be represented as 2**a + 2**b +2**c.. ex 5 = 2**0 + 2**2
  # looping over all these bits , going up 2**a , then 2**b then 2**c... till we have climed up x parent
  for i in range(int(log2(x))+1):
    bit=2**i
    if x&bit:
      node=parent[node][i]
  return node
  
  


  
  
