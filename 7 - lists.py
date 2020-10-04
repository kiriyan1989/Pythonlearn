friends = ["Kevin", "Karen", "Jim", ]

#print(friends[0:3])
#print(friends[-1])

#change first item on the list to Mike
friends[1] = "Mike"
#print(friends[1])


#####List Functions#####

lucky_numbers = [1, 4, 6, 90, 7, 30]

friends.extend(lucky_numbers)

#print(friends)


friends.insert(1, "Kelley")

friends.append("Dilshan")


friends.insert(0, "Kelley")

#remove Mike from the list
friends.remove("Mike")

#remove Mike from the list
#friends.clear()

#remove last item
#friends.pop()

#print(friends.index("Dilshan"))

## assending order to numbers in the list. We can sort mixed list (numbers and string)
lucky_numbers.reverse 

friends2 = lucky_numbers.copy()

print(friends2)


#we can sort assending order
#friends.sort()
#print(friends)

