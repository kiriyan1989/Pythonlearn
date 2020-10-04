is_male = False
is_tall = True

if is_male and is_tall:          # and operator
    print("you are a tall male")

elif is_male and not(is_tall):
    print("you are a short male")

elif not(is_male) and (is_tall):
    print("you are not male,  but tall")

else:
    print("you are NOT a male and NOT tall")