str='12bbb500cc5dd1200'
# n=len(string1)
temp='0'
sum = 0
for i in range(len(str)):
 if str[i].isdigit():
  temp=temp+str[i]
 else:
  sum+=int(temp)
  temp='0'

sum+=int(temp)

print(sum)

# s="njnc152ncsk54kj15"                                  
# l=['0','1','2','3','4','5','6','7','8','9']
# sum=0
# for i in s:
#  if(i in l):
#   sum=sum+int(i)
#  else:
#   pass
# print(sum)