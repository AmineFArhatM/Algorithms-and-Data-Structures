#--------------------z algorithm------------------------------------

'''this is an algorithm used to calculate the number of occurences of a pattern inside a string'''
'''time complexity o(2*m) wheme m is the length of the original string'''


'what is z[i] : it is the length of the substring starting at s[i] that forms a prefix of the pattern string'
'what are l and r  : they are the start and end indexes of the previous box'
'what if there is no previous box ? then r<l'

def z_algo(originalstring,pattern):
  s=pattern + '&' +originalstring
  n=len(s)
  z=[0]*(n)
  l,r=0,0
  count=0
  for i in range(1,n):
    #I am i inside the box ? then i can update my z[i]
    if l<=i<=r:
      z[i] = min(r-i+1,z[i-l])
      
      
    while i+z[i]<n and s[i+z[i]]==s[z[i]]:
      z[i]+=1
      
    if z[i] == len(pattern):
      count += 1
    #if i am larger than the old box , then my value is the new box
    #Why the '-1' ? if my prefix matched 2 charcters , then , my l = i , and my r = i + z|i] is false because 
    #it means my box is i , i+1 , i+2 while it is only i and  i+1 or l = i and r = i+1  
    if i + (z[i] - 1) > r:
      l,r = i,i+z[i]-1
  return count


s=input('Enter original string:  ')
t=input('Enter pattern:  ')
print(z_algo(s,t))
    
    
