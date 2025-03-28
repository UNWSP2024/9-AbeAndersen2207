#UNWSP Programming PythonCos2005DEsp25
#Program_3_Average Numbers
#03.28.25
#Abraham. N. Andersen

def calculate_total(filename):
  """
  Reads numbers from a file, calculates their total, and handles errors.

  Args:
    filename: The name of the file to read from.
  """

  total = 0  # Start with zero

  try:
    with open(filename, 'r') as file:
      for line in file:
        try:
          number = int(line)
          total += number  # Adding
        except ValueError:
          print(f"Sorry Try Again. '{line.strip()}' is not a number. Skipping it.") #strip for good measure
    print(f"The total of the numbers in '{filename}' is: {total}")

  except FileNotFoundError:
    print(f"The file '{filename}' was not found.")

  except Exception as e:
    print(f"Something happened... {e}")

# Example usage:
filename = "numbers.txt"
calculate_total(filename)
