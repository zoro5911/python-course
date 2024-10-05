while True:
  a = input("Enter any value between 5 and 9 (or type 'quit'): ")
  if a == 'quit':
    break
  try:
    a = int(a)
    if (a<5 or a>9):
      raise ValueError("value must be between 5 and 9")
    else:
      print("Valid input")
      print(a)
  except ValueError as e:
    print(e)

