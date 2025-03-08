# -*- coding: utf-8 -*-
"""Copy 22201990of Lab 3 - 2D Matrix [PYTHON].ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cdfITj6OYCLoaDkfgkVaH4ULDSBV9rPU

**Instructions to Follow (Failing to follow these will result mark deductions).**
1. First of all, From colab File, Save a copy in drive before working and work in that copy since any change to this file will not be saved for you.
2. You can not use any built-in function except len()

3. You can not use any other python collections except array (e.g: tuple, dictionaries etc.).

4. We will initialize a new array using numpy library. We have to mention the fixed size during initialization. There might be 4 approaches.

 i. arr = np.array([None] * 10) #Initializing an array length 10 with values None.

 ii. arr = np.array([0] * 10) #Initializing an array length 10 with values zero.

 iii. arr = np.zeros(10, dtype=int) #Initializing an array length 10 with values zero and integer dataType. By default, dtype is float.

 iv. arr = np.array([10, 20, 30, 40]) #Initializing an array length 4 with the values.
"""

# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

"""You will see the status Accepted after completion if your code is correct.

If your function is wrong you will see wrong [correction percentage]

Do not change the driver code statements. You can only change the input values to test your code.
"""

#DO NOT CHANGE THE CODE BELOW
#You must run this cell to print matrix and for the driver code to work
def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))

# Task 01: Zigzag Walk
def walk_zigzag(floor):
    m,n=floor.shape
    for col in range(n):
        if col %2 ==0:
            for row in range(m):

                if row % 2==0:
                    print(floor[row,col],end=" ")
    else:
        for row in range(m-1, -1, -1):
           if row % 2 == 0:
            print(floor[row,col],end=" ")
    print()
#DO NOT CHANGE THE CODE BELOW
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0'],
                  ['1' , '4' , '2' , '8' , '6']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9 1
# 1 2
# 4 7 2
# 4 9
# 1 8 6
print('################')
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9
# 1 2
# 4 7
# 4 9
# 1 8

#Task 02: Decryption Process

def decrypt_matrix(matrix):
    number_col = len(matrix[0])
    col_sums = []

    for col in range(number_col):
        col_sum = 0
        for row in range(len(matrix)):
            col_sum += matrix[row][col]

        col_sums += [col_sum]

    result = [0] * (len(col_sums) - 1)

    for i in range(1, len(col_sums)):
        result[i - 1] = col_sums[i] - col_sums[i - 1]

    return result

#DO NOT CHANGE THE CODE BELOW
matrix=np.array([[1,3,1],
                 [6,4,2],
                 [5,1,7],
                 [9,3,3],
                 [8,5,4]
                 ])

returned_array=decrypt_matrix(matrix)
print(returned_array)
#This should print [-13, 1]

# Task 03: Row Rotation Policy of BRACU Classroom
def row_rotation(exam_week, seat_status):

#To Do
    rows=len(seat_status)
    rotation= exam_week % rows

    rotated_seat_status= [None]*rows

    for i in range(rows):
        current_stat=(i+rotation)% rows
        rotated_seat_status[current_stat]=seat_status[i]

    pos_aa=5
    aa_row= (pos_aa+rotation)% rows+1

    for row in  rotated_seat_status:
        for s in row:
            print(s,end=" ")
        print()
    return aa_row
#DO NOT CHANGE THE CODE BELOW
seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                  ['F' , 'G' , 'H' , 'I' , 'J'],
                  ['K' , 'L' , 'M' , 'N' , 'O'],
                  ['P' , 'Q' , 'R' , 'S' , 'T'],
                  ['U' , 'V' , 'W' , 'X' , 'Y'],
                  ['Z' , 'AA' , 'BB' , 'CC' , 'DD']])
exam_week=3
print_matrix(seat_status)
print()

row_number=row_rotation(exam_week, seat_status) #This should print modified seat status after rotation and return the row number
print(f'Your friend AA will be on row {row_number}') #This should print Your friend AA will be on row 2

#Task 04: Matrix Compression

def compress_matrix(mat):
  #TO DO
  rows,cols=mat.shape
  comp=np.zeros((rows//2,cols//2,),dtype=int)
  for i in range(0,rows,2):
    for j in range(0,cols,2):
        comp[i//2][j//2]=(mat[i][j] + mat[i][j + 1] +mat[i + 1][j] + mat[i + 1][j + 1])
  return comp

#DO NOT CHANGE THE CODE BELOW
matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
print("...............")
returned_array=compress_matrix(matrix)
print_matrix(returned_array)
#This should print

#|  14  |  22 |
#--------------
#|  2  |  10  |
#--------------

#Task 05: Game Arena

def play_game(arena):
  #TO DO
    total_points=0
    rows=len(arena)
    col=len(arena[0])

    for i in range(rows):
        for j in range(col):
            if arena[i][j]%50==0:
                if arena[i][j]!=0:
                    player_points=0
                    if i-1>=0 and arena[i-1][j]==2:
                        player_points+=1
                    if i+1< rows and arena[i+1][j]==2:
                        player_points+=1
                    if j+1< col and arena[i][j+1]==2:
                        player_points+=1
                    total_points+=player_points*2
    if  total_points>=10:
        print("points Gained:",total_points,"Your team has survived the game.")
    else:
         print("points Gained:",total_points,"Your team out.")
#DO NOT CHANGE THE CODE BELOW
arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 6. Your team is out.
print(".....................")
arena=np.array([[0,2,2,0,2],
                [1,50,2,1,100],
                [2,2,2,0,2],
                [0,200,2,0,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 14. Your team has survived the game.