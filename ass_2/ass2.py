# python file for assignment 2 
# code from the jupyter notebook

user_inputs = []
MAX_TRY = 11

for i in range(1, MAX_TRY):

    while True:
        try:
            user_input = input("Please enter an integer:")
            in_input = int(user_input)
            break
        except:
            print("Please retry (only integer accepted)")
    user_inputs.append(user_input)   
    print(f"You have entered integer #{i}:", user_input)

ints = [int(item) for item in user_inputs] #cast each element into an integer 

print("Overall, you have entered:", ints) #display looks cleaner after casting

ints.sort(reverse = True)

print("The minimum is:", ints[9])
print("The maximum is:", ints[0])

the_max = ints[0] 
the_min = ints[9]
print("The range is:", the_max - the_min)

# Python program to find sum of elements in list
sum = 0 
# Iterate each element in list
# and add them in variale sum
for ele in range(0, len(ints)):
    sum += ints[ele]
mean = sum / 10
print("The mean is:", mean)

sum_diff = 0
for ele in range(0, len(ints)):
    sum_diff += (ints[ele] - mean) ** 2
var = sum_diff / 9

# Format variance to display only 2 decimals
variance = "The variance is: {:.2f}"
print(variance.format(var))

# Get standard deviation by raising variance to .5 power
stan_dev = var ** .5

# Format standard deviation to 2 decimals 
stand_dev = "The standard deviation is: {:.2f}"
print(stand_dev.format(stan_dev))