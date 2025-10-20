#-----------------Manachar's Algorithm--------------------

'''this algorithm is used to find the palindroms inside a string 
  it works similar to the Z algorithm
   !! it only finds palindrom with odd length 
  '''
  
  
'''
  p[i] : the length of the paindrom where the i th character is a palindrom
  center : center of the right most palindrom
  r : the edge of the right most palindrom '''
  
''' How it works ?
  if you are inside the right most palindrom , then part of (or all of your p[i] ) is calculated , so you do not 
  search before r . 
  '''
  

def manachar_algo(t):
  
  s='<+'+  '+'.join(t) + '+!' #adding '+' between charecters so even length pâlindroms can be found , exp baab becomes b+a+a+b(this algo finds only odd lengt palindroms)
  n=len(s)
  p=[0 for i in range(n)]
  pos,r=0,0
  center = 0
  i,j=0,0
  max_palindrom_length = 1 #we can always have a palindrom of length 1 that is the first character 
  for i in range(1,n-1):

    if i<=r:
      
      mirror = center - (i - center) #my mirror inside the right most palindrom 
      p[i]=min(p[mirror],r-i)
    
    while s[i+p[i]+1]==s[i-p[i]-1]:
      p[i]+=1
      
    if i+p[i]>r:
      r=i+p[i]
      center = i
    
    if p[i]>max_palindrom_length:
      max_palindrom_length=p[i]
      pos=i-p[i]+1#pos is the index of teft pos character of the palindrom !!inside the original string
      pos=(pos-1)//2

    
  return t[pos:pos+max_palindrom_length]

print(manachar_algo(input('Enter a string')))
