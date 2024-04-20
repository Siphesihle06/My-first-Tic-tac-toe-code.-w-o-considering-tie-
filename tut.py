Game = [[0,0,0],
       [0,0,0],
       [0,0,0,]]

#First move

print('   1  2  3 ')
Game[0][0] = 1
for count,row in enumerate(Game):
    print( count, row)

#second move

print('   1  2  3 ')
Game[0][1] = 1
for count,row in enumerate(Game):
    print( count, row)

#3rd move


print('   1  2  3 ') 
Game[0][2] = 1
for count,row in enumerate(Game):
    print( count, row)


#fourth possible move


print('  1   2  3')
Game[1][0] = 2
for count,row in enumerate(Game):
    print( count, row)

#fifth possible move

print('   1  2  3 ')
Game[1][1] = 0
for count,row in enumerate(Game):
    print( count, row)

#sixth possible move

print('   1  2  3 ')
Game[1][2] = 0
for count,row in enumerate(Game):
    print( count, row)

#seventh possible move

print('   1  2  3 ')
Game[2][0] = 0
for count,row in enumerate(Game):
    print( count, row)

#eighth possible move


print('   1  2  3 ')
Game[2][1] = 0
for count,row in enumerate(Game):
    print( count, row)

#nineth possible move

print('   1  2  3 ')
Game[2][2] = 2
for count,row in enumerate(Game):
    print( count, row)


#Check for rows


for row in Game:
    if Game[0][0] == Game[0][1] == Game[0][2] !=0:
        print('uwinile')

if Game[1][0] == Game[1][1] == Game[1][2] !=0:
    print('uwinile')

if Game[2][0] == Game[2][1] == Game[2][2] !=0:
     print('uwinile')

           

#Check for Columns


for col in Game:
    if Game[0][0] == Game[1][0] == Game[2][0] !=0:
        print('uwinile')


if Game[0][1] == Game[1][1] == Game[2][1] !=0:
    print('UWINILE')
if Game[0][2] == Game[1][2] == Game[2][2] !=0:
    print('UWINILE')
            
        
    
 #check for diagonals


for diag in Game:
    if Game[0][2] == Game[1][1] == Game[2][0] !=0:
        print('uwinile')

        if Game[0][0] == Game[1][1] == Game[2][2] !=0:
            print('uwinile')
#check for Tie


