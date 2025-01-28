import random

def generate_random_flips(length):
    """
    Generate a random string of flips ('V' and 'H') of the specified length.
    
    Args:
        length (int): The length of the flip sequence.
        
    Returns:
        str: A random sequence of 'V' and 'H'.
    """
    return ''.join(random.choice(['V', 'H']) for _ in range(length))

def save_to_file(filename, content):
    """
    Save the given content to a file.
    
    Args:
        filename (str): The name of the file to save the content to.
        content (str): The content to save in the file.
    """
    with open(filename, "w") as file:
        file.write(content)
    print(f"Random flips saved to {filename}")

if __name__ == "__main__":
    # Specify the length of the random sequence
    length = 456  # You can adjust this value as needed
    
    # Generate the random flips
    random_flips = generate_random_flips(length)
    
    # Save the random flips to a file
    filename = "random_flips.txt"  # Specify the file name
    save_to_file(filename, random_flips)
