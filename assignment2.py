def count_digits(number):
    number = abs(number)
    if number < 10:
        return 1
    return 1 + count_digits(number // 10)
    
def count_tag_from_file(file_path, tag):
    with open(file_path, 'r') as file:
        html = file.read()

    return count_tag(html, tag)

    
def count_tag(html, tag):
    if not html:
        return 0

    open_tag = '<' + tag + '>'
    close_tag = '</' + tag + '>'
    if open_tag in html and close_tag in html:
        end_index = html.index(close_tag) + len(close_tag)
        
        return 1 + count_tag(html[end_index:], tag)
    else:
        return 0
        
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 0:
        return 0
    else:
        max_val = find_max(lst[1:])
        return max_val if max_val > lst[0] else lst[0]

def count_normalized_columns():
    print("Counting normalized columns...")

while True:
    print("""
1. Count Digits
2. Find Max
3.1. Count Tags
3.2. Count Normalized Columns
4. Exit
    """)

    choice = input("Please choose an option: ")

    if choice == "1":
         number_str = input("Enter an integer: ")
         number = int(number_str)
         count = count_digits(number)
         print(count)
         break
    elif choice == "2":
        user_input = input("Please enter a list of numbers separated by space: ")
        user_list = [int(item) for item in user_input.split()]
        print("User list:", user_list)
        max_value = find_max(user_list)
        print(max_value)
        break
    elif choice == "3.1":
        file_path = input("Enter your file path")
        tag = input("Enter tag")
        count = count_tag_from_file(file_path, tag) 
        print(count);
        break
    elif choice == "3.2":
        count_normalized_columns()
        break
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        break


