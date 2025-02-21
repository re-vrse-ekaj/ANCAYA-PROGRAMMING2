# ANCAYA-PROGRAMMING2
# Contact Address Book

This Python script allows users to store and look up contact information. It allows for entering multiple contacts with a name and phone number, and later lets you search for a contact by name.

## Features
- Allows users to input a number of contacts.
- Stores the contact names and numbers in a dictionary.
- Provides functionality to look up the phone number by name.

## Requirements
- Python 3.x

## Usage

### Running the Script
1. Execute the script.
2. You will be prompted to enter the number of contacts you want to save.
3. Enter the name and phone number for each contact.
4. Once all contacts are saved, you can search for a specific contact by name.
5. If the name exists in the address book, the associated phone number will be displayed. Otherwise, it will print a "name not found" message.

### Example Flow:

Enter a number of contacts: 3 enter your name: John enter your number: 1234567890 enter your name: Alice enter your number: 9876543210 enter your name: Bob enter your number: 5555555555 {'John': 1234567890, 'Alice': 9876543210, 'Bob': 5555555555}

Lookup name: Alice number: 9876543210

### Code Explanation
- The script first asks for the number of contacts to be added (`dami`).
- Then, it collects the contact names and numbers using a `for` loop and stores them in the dictionary `address_book`.
- Finally, it prompts the user to look up a contact name. If the name exists in the dictionary, the script displays the phone number associated with that name; otherwise, it notifies that the name wasn't found.

## How to Run
1. Make sure you have Python 3.x installed on your machine.
2. Copy the code into a Python file (e.g., `address_book.py`).
3. Open your terminal or command prompt.
4. Run the script using:

## Notes
- The phone numbers are stored as integers in the dictionary.
- This script is intended for educational purposes and works in a simple, text-based interface.
