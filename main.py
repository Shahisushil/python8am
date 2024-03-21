# # # name = 'Sushil'
# # # age = 40
# # # email = 'shahisushil98@gmail.com'
# # # phone = 9767547742
# # # address = 'Gyaneshwor'
# # # print(f"My name is {name} My age is {age} My email is {email} My phone number is {phone} My address  {address}")
# # # print ("hello python")

# # # data=[
# # #     [12,34,56,78,97]
# # #     [67,87,[[[600]],900],12,34,54]
# # # ]
# # # print (data[1][4])

# # # data=[
# # #     [34,56,78],
# # # #     [55,77,88]
# # # # ]

# # # data[0].pop(0)
# # # data[1].pop(2)
# # # print(data)


# # # data=[
# # #     [34,56,78],
# # #     [55,77,88]
# # # ]


# # # data[0].insert(1,200)
# # # data[1].insert(2,500)
# # # print(data)


# # # data[0].append(500)
# # # data[1].append(500)
# # # print(data)

# # # data[0].pop(1)
# # # data[1].pop(2)
# # # print(data)

# # # p= input ( "Enter p")
# # # t= input ("Enter t")
# # # r= input ("Enter r")
# # # p= int (p)
# # # t= int (t)
# # # r= int (r)
# # # print (p*t*r/100)          

# # data=[
# #     ['ram','sita','gita'],
# #     ['nepal',['india'],'china'],
# #     {'name':"hari"}

# # ]

# # print(data[0][0])
# # print(data[1][1][0])
# # print(data[2]["name"])


# students=[
#     {
#         'name':"ram",
#         "country":[
#             {
#                 'cname':"nepal",
#                 'capital':"ktm"
#             },
#             {
#                 'cname':"india",
#                 'capital':"delhi"
#             }
#         ]
        
#     },
#     {
#         'name':"sita",
#         "country":[
#             {
#                 'name':"nepal",
#                 'capital':"ktm"
#             },
#             {
#                 'name':"china",
#                 'capital':"beijing"
#             }
#         ]
#     }
# ]

# print (students[1]["name"])
# print(students[1]["country"][0]['name'])
# print(students[1]["country"][0]["capital"])

# WAP to enter age and check if the person is eligible to vote or not
# 18<not eligible
# 40>not eligible

# age=int(input('enter you age:'))
# if age<18 or age<40:
#     print('not eligible for vote')
# else:
#     print('eligible for vote')


# WRITE A PROGRAM (WAP) to enter any number and check if the number divisible by 3 and 5 or not

# num=int(input('Enter any number' ))
# if num%3==0 and num%5==0:
#     print('Divisible by 3 and 5')
# else:
#     print('not divisible by 3 and 5')

    

# #     find the greatest number among 3 numbers
# #     x=5
# #     y=6
# #     z=7

# num=int(input('greatest number among 3 numbers'))
# if x>y or x<y or 

# # # find the greatest number among 3 numbers
# # x=5
# # y=6
# # z=7
# # if (x>=y) and (x>=z):
# #     greatest = x
# # elif(y>-x) and (y>=z):
# #     greatest =y
# # else:
# #     greatest =z
# #     print("The greatest number is",greatest)




# # # #     WAP to enter five subject marks calculate the total, percentage and grade
# # # 45< fail
# # # 45> and 60< C
# # # 60> and 75< B
# # # 75> and 90< A
# # # 90> and 100< A+

# # print("Enter the marks of 5 subjects::")


# subject_1 = float (input ("enter sub1 :"))
# subject_2 = float (input ("enter sub2 :"))
# subject_3 = float (input ("enter sub3 :"))
# subject_4 = float (input ("enter sub4 :"))
# subject_5 = float (input ("enter sub5 :"))


# total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
# pre=total/5

# if pre >=90 and pre < 100:
#     grade ='A+'
# elif pre >=75 and pre < 90:
#     grade ='A'
# elif pre >=60 and pre <  75:
#     grade ='B'
# elif pre >=45 and pre < 60:
#     grade = 'C'
    
# else: 
#     grade = 'fail'


# print("total",total)
# print("percentage",pre)
# print("grade",grade)

# users=[
#     ['admin','admin002'],
#     ['ram','ram123'],
# ]

# username = input('Enter username : ')
# password = input('Enter password :')

# if users[0][0]==username and users[0][1]==password:
#     print('Welcome',username)
# elif users[1][0]==username and users[1][1]==password:
#     print('welcome',username)
# else:
#     print('invalid username or password')

    

# print("==========Welcome to ATM==========")
# pin_code=1234
# amount=10000
# pin=int(input('Enter your pin code: '))
# if pin==pin_code:
#         print('1. Check Balance')
#         print('2. Withdraw Money')
#         option=int(input('Enter your option:'))
#         if option==1:
#             print ('You balance is :',amount)
#         elif option==2:
#             new_amount=int(input('Enter the amount: '))
#             if new_amount<=amount:
#                 n=amount-new_amount
#                 print('Please collect your cash')
#                 print('withdrawn amount:',new_amount)
#                 print('Your new balance is: ',n)
#             else:
#                 print('Insufficient balance')
#         else:
#             print('Invalid option')
    
# else:
#      print('Invalid pin code')


