from name_function import get_formatted_name

print("Enter 'q' to quit")
while True:
    first = input("\nPlease give me a first name: ")
    if first.lower() == 'q':
        break
    last = input("Please give me a last name: ")
    if last.lower() == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.") 