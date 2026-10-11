from shapes import Rectangle, Square, Circle, Triangle, Hexagon

while True:
  print("Welcome to your area calculator!")
  print("What would you like to calculate the area of today?")
  print("1. Rectangle")
  print("2. Square")
  print("3. Circle")
  print("4. Triangle")
  print("5. Hexagon")

  choice = input("Enter the number of your choice (or 'q' to quit): ")
  breakpoint()

  if choice == "1":
    try:
      width = float(input("Enter the width of the rectangle: "))
      height = float(input("Enter the height of the rectangle: "))
    except ValueError:
      print("Invalid input. Please enter a valid number.")
      input("Press Enter to return to the main menu...")
      continue
    
    breakpoint()
    print("The area of the rectangle is:", round(Rectangle(width, height).area(), 2))
    input("Press Enter to return to the main menu...")

  elif choice == "2":
    try:
      side_length = float(input("Enter the side length of the square: "))
    except ValueError:
      print("Invalid input. Please enter a valid number.")
      input("Press Enter to return to the main menu...")
      continue

    print("The area of the square is:", round(Square(side_length).area(), 2))
    input("Press Enter to return to the main menu...")

  elif choice == "3":
    try:
      radius = float(input("Enter the radius of the circle: "))
    except ValueError:
      print("Invalid input. Please enter a valid number.")
      input("Press Enter to return to the main menu...")
      continue
    
    print("The area of the circle is:", round(Circle(radius).area(), 2))
    input("Press Enter to return to the main menu...")

  elif choice == "4":
    try:
      base = float(input("Enter the base of the triangle: "))
      height = float(input("Enter the height of the triangle: "))
    except ValueError:
      print("Invalid input. Please enter a valid number.")
      input("Press Enter to return to the main menu...")
      continue

    print("The area of the triangle is:", round(Triangle(base, height).area(), 2))
    input("Press Enter to return to the main menu...")

  elif choice == "5":
    try:
      side_length = float(input("Enter the side length of the hexagon: "))
    except ValueError:
      print("Invalid input. Please enter a valid number.")
      input("Press Enter to return to the main menu...")
      continue

    print("The area of the hexagon is:", round(Hexagon(side_length).area(), 2))
    input("Press Enter to return to the main menu...")

  elif choice.lower() == "q":
    print("Thank you for using the area calculator. Goodbye!")
    break

  else:
    print("Invalid choice. Please try again.")
    input("Press Enter to return to the main menu...")