def lcs(str1, str2):
    matrix= [[0 for _ in range((len(str1)))] for _ in range(len(str2))]
    for row, cha2 in enumerate(str2):
        for col, cha1 in enumerate(str1):
            left, top, diag= 0, 0, 0
            if row!=0:
                top= matrix[row-1][col]
            if col!=0:
                left= matrix[row][col-1]
            if cha1!= cha2:
                matrix[row][col]=max(left, top)
            else:
                if row>0 and col>0:
                    diag= matrix[row-1][col-1]
                matrix[row][col]=diag+1
    return matrix[len(str2)-1][len(str1)-1]


## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')