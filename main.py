from collections import Counter
filename = "books/frankenstein.txt"
def main():
        
    with open(filename) as f:
        content = f.read()
    words = content.split()
    words_count = len(words)
    letter_counts = Counter(char for char in content.lower() if char.isalpha())

    
    print(f"--- Begin report of {filename} ---")
    print(f"--- {words_count} words found in the text ---\n")
    for letter, count in sorted(letter_counts.items()):
        print(f"{letter}: was found {count} times")
    
    print("--- End report ---")

main()


