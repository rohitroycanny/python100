s = input("Enter")
vowels = ('aeiouAEIOU')  
for x in s:
   if x in vowels:
       s = s.replace(x,'')   
print(s)