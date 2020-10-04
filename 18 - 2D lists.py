###### 2D lists ######
###### arrays inside an array ######

number_grid = [
    [1, 2, 3],      # row 0
    [4, 5, 6],      # row 1
    [7, 8, 9],      # row 2
    [0]             # row 3
]

print(number_grid[2])       # prints row 2



############ Nested For loop ##########

for row in number_grid:     ## for loop 1 - loop count defined by number of rows
    for col in row:         ## for loop 2 - loop count defined by number of cols
        print(col)

