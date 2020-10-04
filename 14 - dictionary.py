monthconversion = {
    1:'Janauary',
    2:'February',
    '03':'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':'July',
    '08':'August',
    '09':'September',
    '10':'October',
    '11':'November',
    '12':'December',
    "year" : 2020
}

print(monthconversion["10"])

print(monthconversion.get(2))

print(monthconversion.get('year', "not valid key"))    #get function allows default value

