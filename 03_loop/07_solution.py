while True:
  try:
    number = int(input("Enter value b/w 1 and 10: "))
  except ValueError:
    print("Invalid input, please enter an integer")
    continue
  if 1 <= number <= 10:
    print("Thanks")
    break
  print("Invalid number, try again")
