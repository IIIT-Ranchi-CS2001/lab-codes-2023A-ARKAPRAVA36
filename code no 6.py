# initializing string
test_str = "houseofdragons"

# using naive method to get count
# counting e
count = 0

for i in test_str:
	if i == 'e':
		count = count + 1

# printing result
print("Count of e in houseofdragons is : "
	+ str(count))

