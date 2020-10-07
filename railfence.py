def encode_rail_fence_cipher(string, n):
    matrix_c = len(string)
    matrix_r = n
    flow_flag = True
    row_p = 0
    matrix = [["\n" for _ in range(matrix_c)] for _ in range(matrix_r)]
    for c in range(matrix_c):
        if c == 0:
            row_p = 0
            matrix[row_p][c] = string[c]
            row_p +=1
        else :
            if row_p < matrix_r-1 and flow_flag: 
                matrix[row_p][c] = string[c]
                row_p += 1
            elif row_p == matrix_r-1 and flow_flag :
                matrix[row_p][c] = string[c]
                row_p -= 1
                flow_flag = False
                pass
            elif row_p > 0 and not flow_flag:
                matrix[row_p][c] = string[c]
                row_p -= 1
            elif row_p ==0 and not flow_flag : 
                matrix[row_p][c] = string[c]
                row_p += 1
                flow_flag = True
    result = []
    for i in range(n): 
        for j in range(len(string)): 
            if matrix[i][j] != '\n': 
                result.append(matrix[i][j]) 
    return("" . join(result)) 
   
               
def decode_rail_fence_cipher(string, n):
    matrix_c = len(string)
    matrix_r = n
    flow_flag = True
    row_p,counter = 0,0
    result = []
    matrix = [["\n" for _ in range(matrix_c)] for _ in range(matrix_r)]
    for c in range(matrix_c):
        if c == 0:
            row_p = 0
            matrix[row_p][c] = '*'
            row_p +=1
        else :
            if row_p < matrix_r-1 and flow_flag: 
                matrix[row_p][c] = '*'
                row_p += 1
            elif row_p == matrix_r-1 and flow_flag :
                matrix[row_p][c] = '*'
                row_p -= 1
                flow_flag = False
                pass
            elif row_p > 0 and not flow_flag:
                matrix[row_p][c] = '*'
                row_p -= 1
            elif row_p ==0 and not flow_flag : 
                matrix[row_p][c] = '*'
                row_p += 1
                flow_flag = True
                
    for y in range(matrix_r) :
         for x in range(matrix_c):
                if matrix[y][x] == '*':
                    matrix[y][x] = string[counter]
                    counter+=1
                    
    for c in range(matrix_c):
        if c == 0:
            flow_flag = True
            row_p = 0
            result.append(matrix[0][0])
            row_p +=1
        else :
            if row_p < matrix_r-1 and flow_flag and matrix[row_p][c] != '*': 
                result.append(matrix[row_p][c]) 
                row_p += 1
            elif row_p == matrix_r-1 and flow_flag and matrix[row_p][c] != '*' :
                result.append(matrix[row_p][c]) 
                row_p -= 1
                flow_flag = False
            elif row_p > 0 and not flow_flag and matrix[row_p][c] != '*':
                result.append(matrix[row_p][c]) 
                row_p -= 1
            elif row_p ==0 and not flow_flag and matrix[row_p][c] != '*': 
                result.append(matrix[row_p][c]) 
                row_p += 1
                flow_flag = True
    return ( "".join(result)) 
