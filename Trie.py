def update_trie(x,trie):
  curr =trie
  for c in x:
    #set default here is very important
    #if the character exitst in the current dectionnary , then curr will become that characters own dictionnary 
    #else; otherwise , setdedault adds that character to te dictionnary and then gives it a dictionnary as a value 
    # ===> key = caracter : value = dictionnary 
    curr = curr.setdefault(c,{})
  curr[-1] = True
  #now curr has the dictionnary of the last character of the string 
  #we add to that dictionnary -1:True identifiying the end of the string
  
  
#this function is used to check if there is a string  p equals to a string s
def check(s,trie):
  curr = trie
  for x in s:
    if x in curr:curr=curr[x]
    else :return False
  if -1 in curr :return True
  else:return False
  #check the end of the similar string if it is -1
  
  
#time complexity for check O(n log n) where n is the length of s
#time complexity for update-tris is o(m log m) where m is the sum of lengths of all strings
  

#PRO TIP:
#using ord(character) is faster

trie = {}
l = ['abcd' , 'amine','xyz']
for x in l:update_trie(x,trie)
target = 'xyz'
print('does target exist in l ?',check(target,trie))


  
  
