from names import make_full_name, extract_given_name, extract_family_name

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    full_name = make_full_name(given_name=first_name, family_name=last_name)
    ex_first_name = extract_given_name(full_name)
    ex_last_name = extract_family_name(full_name)

    print(f'\nFirst name: {ex_first_name}\nLast name: {ex_last_name}\n')    
if __name__ == "__main__":
    main()