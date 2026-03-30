
         

'''
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
my_function_with_args ('asmaa','yyy')    
 
     
def grret(u ,n ):
    print('hello , %s, from function  %s ' %(u , n ))
grret ('asmaa', 'utut')    

'''
'''
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i in days:
    print (i)
'''
'''
sentence = 'Python is amazing'
for i in sentence:
    print (i)    
'''
'''
for i in range (30,120,6):
    print (i)    

i = 1
while  i <= 20:
    if i == 17:
        print ('yydy  %d ' %(i))
        break
    print (i)
    i += 1
   
c = 120 
while c <= 300 :
    print (c)
    c+=1
    if c == 180 :
        break
        print ('c = 180' )
else :
    print ('rtrt r')

def greet (name , age ):
    print ('hello ' , name , 'iam ', age ,'years old ' )    
greet(age = 33 , name = 'adam')    
 
def su (user , *values):
  
 
  print (min (values))
  print (max(values)-min(values))
  z= max(values)/min(values)
  y= sum(values)/len(values)
  x =  sum(values)/len(values)
  print ('user %s sucess ' %(user)    ,x )
  print ('user sucess' , user ,y )
  print ('user sucess' , user ,z )
  print (sum(values))
su  ('ahmed',10, 5, 2, 4,30)

import datetime 
print (datetime.datetime.now())
dt = datetime.datetime.now()
print (dt.strftime('%A %B %Y'))
'''
# Comparator هنا قمنا بتعريف كلاس إسمه
class Comparator:

    # بعدها تطبع القيمة الأكبر بينهما .b و a هنا قمنا بتعريف دالة تأخذ قيمتين عند إستدعائها و تخزنهما في الباراميترين
    def print_max(self, a, b):
        if a > b:
            print(a, 'is bigger')
        elif a < b:
            print(b, 'is bigger')
        else:
            print('They are equal')


# comparator إسمه Comparator هنا قمنا بإنشاء كائن من الكلاس
comparator = Comparator()

# و تمرير قيمتين لها حتى تطبع قيمة العدد الأكبر بينهما print_max() هنا قمنا باستدعاء الدالة
comparator.print_max(2, 6)