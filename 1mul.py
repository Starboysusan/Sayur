
'''
1)
Print the following using loop
1*1=1
1*2=2
1*3=3
1*4=4
1*5=5'''


multiply=1
for mul in range(1,6):
    print(multiply,"*",mul,"=",multiply*mul)


'''
2)
print the following using two loop'''


for multiplyr in range(1,4):
    for  num in range(1,6):
        print(multiplyr,"*",num,"=",multiplyr*num)



'''
3)
print the following using two loop
My Table
Tabel  1
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
**********
Tabel  2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
**********
Tabel  3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
**********
End of table
'''
format='*'
print("My Table")
for multipler in range(1,4):
    print("Tabel ",multipler)
    for num in range(1,6):
        print(multipler,"*",num,"=",multipler*num)
    print(f'{format*10}')
print("End of table")

'''
4)
print the following
My Tables
Table  10
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
**********
Table  8
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
**********
Table  6
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
**********
Table  4
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
**********
Table  2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
**********
End of table
'''

print("My Tables")
for multiplyer in range(10,0,-2):
    print("Table ",multiplyer)
    for num in range(1,6):
        print(multiplyer,"*",num,"=",multiplyer*num)
    print(f'{format*10}')
print("End of table")


'''
5)
Print the following
My Tables
Tabel  1
Easy numbers
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10
Advanced numbers
1 * 11 = 11
1 * 12 = 12
1 * 13 = 13
1 * 14 = 14
1 * 15 = 15
1 * 16 = 16
1 * 17 = 17
1 * 18 = 18
1 * 19 = 19
1 * 20 = 20
**********
Tabel  2
Easy numbers
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
Advanced numbers
2 * 11 = 22
2 * 12 = 24
2 * 13 = 26
2 * 14 = 28
2 * 15 = 30
2 * 16 = 32
2 * 17 = 34
2 * 18 = 36
2 * 19 = 38
2 * 20 = 40
**********
Tabel  3
Easy numbers
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30
Advanced numbers
3 * 11 = 33
3 * 12 = 36
3 * 13 = 39
3 * 14 = 42
3 * 15 = 45
3 * 16 = 48
3 * 17 = 51
3 * 18 = 54
3 * 19 = 57
3 * 20 = 60
**********
End of table'''


print("My Tables")
for multipler in range(1,4):
    print("Tabel ",multipler)
    print("Easy numbers")
    for num in range(1,11):
        print(multipler,"*",num,"=",multipler*num)
    print("Advanced numbers")
    for num in range(11,21):
        print(multipler,"*",num,"=",multipler*num)
    print(f'{format*10}')
print("End of table")



'''
6)
Enter the multiper number:1
Enter 1 for basic/n2 for advance /n 3 for both3
My Tables 1
Basic numbers
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10
Advanced numbers
1 * 11 = 11
1 * 12 = 12
1 * 13 = 13
1 * 14 = 14
1 * 15 = 15
1 * 16 = 16
1 * 17 = 17
1 * 18 = 18
1 * 19 = 19
1 * 20 = 20
**********
End of table
'''


number=int(input("Enter the multiper number:"))
choice=int(input("Enter 1 for basic/n2 for advance /n 3 for both"))
print("My Tables",number)
if(choice>0):
    if(choice==1 or choice==3):
        print("Basic numbers")
        for num in range(1,11):
            print(number,"*",num,"=",number*num)
        print("Advanced numbers")
        for num in range(11,21):
            print(number,"*",num,"=",number*num)
        print(f'{format*10}')
# if(choice==3):
#     print("Basic numbers")
#     for num in range(1,11):
#         print(multipler,"*",num,"=",multipler*num)
#     print("Advanced numbers")
#     for num in range(11,21):
#         print(multipler,"*",num,"=",multipler*num)
#     print(f'{format*10}')
else:
    print("Ivalid choice")
print("End of table")


for multiplyr in range(1,4):
    for  num in range(1,6):
        print(multiplyr,"*",num,"=",multiplyr*num)
