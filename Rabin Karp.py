# --------------------- Rabin Karp Algorithm------------------------


# this code is a solution for CSES problem  https://cses.fi/problemset/hack/1753/entry/14973253/
# string matching

# s is the original string , t is the pattern
# This code calculates the number of occurences of t in s


def rabin_karp(s,t):
      n,m=len(s),len(t)
       
      if n<m:
        print(0)
        exit()
       
      # 2**61-1 is a very large prime number 
      # why ? the larger is the prime number , the less probability of collisions
      base,mod=30,2**60-1
      biggest=pow(base,m-1,mod)
      target,curr=0,0
      
      for i in range(m):
        target =( target * base + ord(t[i]) - 96) % mod
        curr=(curr * base  + ord(s[i])-96) % mod
       
      ans=1 if curr == target else 0
       
      for i in range(m,n):
        curr = curr - (ord(s[i-m])-96) * biggest # removing the first added character for every substring
        # here we have a substraction (-) , can curr have a negative vvalue ?
        # ==> yes it can , solution : negative % mod return always a posivtive value( in python but not in js)
        curr *= base 
        curr += ord(s[i])-96 # adding the new character 
        curr%=mod
        ans += 1 if curr == target else 0
      
      print('the number of occurences of  ' + t + ' in ' + s+' is '  ,ans)
  
s=input('enter the original string')
t=input('enter the pattern')
rabin_karp(s,t)
