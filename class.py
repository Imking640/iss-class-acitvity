def find_cube_pairs(target):                    # a colon was missing here so i added a colon
    solutions = []                              # a colon was present here which was unnecessary hence removed
    max_num = round(target ** (1/3))            # *** is not the correct exponentiation operator . we use ** 

    for a in range(1, max_num + 1):             # here ranges was written instead of range 
        for b in range(a, max_num + 1):
            if a**3 + b**3 == target:           # use ** instead of *** for exponentiation and targ was undefined so use target instead of targ
                solutions.append((a, b))        #sol was undefined so used solutions and semicolon was unnecessary
    return solutions

pairs = find_cube_pairs(1729)               # a comma was present here , removed that

print("Valid cube pairs for 1729:")
for a, b in pairs:                          # changed pair to pairs and added a colon
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")    #here ** 2 was given earlier but we are calculating cube hence **3 i used


# THIS PROGRAM FINDS PAIRS (A,B) SUCH THAT A^3 + B^3 = TARGET WHICH IN OUR CASE IS 1729
