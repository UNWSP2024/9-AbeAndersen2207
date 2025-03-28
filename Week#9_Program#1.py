#UNWSP Programming PythonCos2005DEsp25
#Program_1_Item Counter
#03.28.25
#Abraham. N. Andersen

def count_names(filename):
  """
  Counts the number of names in a file.

  Args:
    filename: The name of the file to read from.

  Returns:
    The number of names in the file, or None if there was an error.
  """
  try:
    with open(filename, 'r') as file:
      # Read all lines from the file and store them in a list
      lines = file.readlines()

      # The number of lines is the number of names
      num_names = len(lines)
      return num_names

  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None
  except Exception as e:
    print(f"An error occurred: {e}")
    return None