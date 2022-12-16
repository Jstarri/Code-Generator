print("Welcome to AJ's Code Generator")

while True:  
    str = input("What value do you want to turn into a print statement: ")
    print(str)
    
    next_generation = input("Let's do another string? (yes/no): ")
    if next_generation == 'yes':
        continue
    if next_generation == 'no':
        print("Goodbye!")
        break

    else:
        print("Invalid Input")