
b = raw_input ("enter a floating point number: ")
b_float = float (b)
n = raw_input ("enter a natural number: ")
n_int = int (n)
print b_float**(n_int+1)/(b_float-1)
total_sum = 1
i = 1
while i<= n_int :
    total_sum = total_sum + b_float**i
    i += 1
print total_sum
