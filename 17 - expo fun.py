#print(2**3)     ## power (expo)

def raise_to_power (base_num, pow_num):
    result = 1
    
    for i in range (pow_num):
        result = result * base_num
    
    return result

print(raise_to_power(2, 4))



############# Same as above but without the loop#########
def raise_to_power_2 (base_num, pow_num):       ## base_num & pow_num are local to the function
    return base_num**pow_num         ## power (expo) is easy in python

print(raise_to_power_2(2, 4))