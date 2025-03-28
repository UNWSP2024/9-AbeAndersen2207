#UNWSP Programming PythonCos2005DEsp25
#Program_2_Random Number Writer
#03.28.25
#Abraham. N. Andersen

import random

def write_random_numbers(filename, num_numbers):
  """
  Writes a specified number of random numbers to a file.

  Args:
    filename: The name of the file to write to.
    num_numbers: The number of random numbers to generate.
  """

  if num_numbers > 1000 or num_numbers < 1:
    print("Please enter a number between 1 and 1000.")
    return

  try:
    with open(filename, 'w') as file:
      for _ in range(num_numbers):
        random_number = random.randint(1, 500)
        file.write(str(random_number) + '\n')

    print(f"{num_numbers} random numbers have been written to {filename}")

  except Exception as e:
    print(f"Error: {e}")

while True:
  try:
    num_numbers = int(input("How many random numbers between 1 and 500 do you want to have writen (1-1000)? "))
    break #exit
  except ValueError:
    print("Invalid input. Please enter a number.")

filename = "random-numbers.txt"
write_random_numbers(filename, num_numbers)