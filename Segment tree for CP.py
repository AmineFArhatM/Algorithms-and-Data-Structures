while 1:
      n,q=map(int,input().split())
      e=[0]*n + list(map(int,input().split()))
      for i in range(n-1,0,-1):
          e[i]=e[2*i]+e[2*i+1]
      print(e)
      for i in range(q):
          a,b,c=map(int,input().split())
          if a == 1:
              y=b+n-1
              d=c-e[y]
              while y >=1:
                  e[y]+=d
                  y=int(y/2)
          else:
              b+=n-1
              c+=n-1
              s=0
              while b <=c:
                  if b%2 == 1:
                      s+=e[b]
                      b+=1
                  if c %2 == 0:
                      s+=e[c]
                      c-=1
                  b,c=int(b/2),int(c/2)

