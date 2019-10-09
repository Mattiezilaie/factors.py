# Author: Mahtab Zilaie
# Date: 10/9/19
# Description: asks the user to enter an integer,
# then prints a list of all positive integers
# that divide that number evenly,
# excluding itself and 1, in ascending order.



num_1 = int(input("Please enter a positive integer: "))
print('The factors of', num_1, 'are:')

for i in range(1, num_1+ 1,):
   if i == num_1:
       continue
   elif i == 1:
       continue
   elif num_1%i==0:
       print(i)