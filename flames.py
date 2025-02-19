def flames_game(name1, name2):
    # Remove common letters from both names
    for letter in name1[:]:
        if letter in name2:
            name1 = name1.replace(letter, '', 1)
            name2 = name2.replace(letter, '', 1)
    
    # Combine the remaining letters
    combined_length = len(name1) + len(name2)
    
    # FLAMES acronym
    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    
    # Determine the relationship
    index = (combined_length % len(flames)) - 1
    
    return flames[index]

# Input names
name1 = input("Enter the first name: ").lower().replace(" ", "")
name2 = input("Enter the second name: ").lower().replace(" ", "")

# Get the result
result = flames_game(name1, name2)

# Output the result
print(f"The relationship between {name1.capitalize()} and {name2.capitalize()} is: {result}")