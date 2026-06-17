import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        """Initializes the journal manager with a target text file."""
        self.filename = filename

    def add_entry(self):
        """Option 1: Appends a new entry with a timestamp to the file using 'a' mode."""
        entry_text = input("\nEnter your journal entry:\n")
        
  
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        formatted_entry = f"{timestamp}\n{entry_text}\n\n"
        
        try:
            # Using 'a' mode to append new data 
            with open(self.filename, "a") as file:
                file.write(formatted_entry)
            print("\nEntry added successfully!")
        except PermissionError:
            print("\nError: Permission denied. Cannot write to the file.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

    def view_all_entries(self):
        """Option 2: Reads and displays all entries from the text file using 'r' mode."""
        if not os.path.exists(self.filename):
            print("\nOutput (If the file does not exist):")
            print("No journal entries found. Start by adding a new entry!")
            return

        try:
            with open(self.filename, "r") as file:
                content = file.read().strip()
            
            if not content:
                print("\nOutput (If the file does not exist):")
                print("No journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:")
                print("------------------------------")
                print(content)
        except PermissionError:
            print("\nError: Permission denied. Cannot read the file.")

    def search_entry(self):
        """Option 3: Searches for specific terms or dates inside the file."""
        keyword = input("\nEnter a keyword or date to search: ").strip()
        
        if not os.path.exists(self.filename):
            print("\nOutput (If no match is found):")
            print(f"No entries were found for the keyword: {keyword}")
            return

        try:
            0.with open(self.filename, "r") as file:
                # Read entire file contents
                content = file.read()
            

            entries = [entry.strip() for entry in content.split("\n\n") if entry.strip()]
            
            matching_entries = []
            for entry in entries:
                if keyword.lower() in entry.lower():
                    matching_entries.append(entry)
            
            if matching_entries:
                print("\nOutput (If a match is found):")
                print("Matching Entries:")
                print("------------------------------")
                for match in matching_entries:
                    print(match)
                    print() # Extra spacing matching expected output format
            else:
                print("\nOutput (If no match is found):")
                print(f"No entries were found for the keyword: {keyword}")
                
        except PermissionError:
            print("\nError: Permission denied. Cannot access file for searching.")

    def delete_all_entries(self):
        """Option 4: Clears out data by removing/deleting the file storage."""
        if not os.path.exists(self.filename):
            print("\nOutput (If the file does not exist):")
            print("No journal entries to delete.")
            return

        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
        if confirm == 'yes':
            try:
                # Delete the physical file entirely
                os.remove(self.filename)
                print("\nOutput (If the file is deleted successfully):")
                print("All journal entries have been deleted.")
            except PermissionError:
                print("\nError: Permission denied. File is open elsewhere or restricted.")
        else:
            print("\nDeletion canceled.")


def main():
    # Instantiate the JournalManager object
    manager = JournalManager("journal.txt")
    
    while True:
        # Display Menu matching requirements
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        
        user_input = input("\nUser Input:\n").strip()
        
        if user_input == "1":
            manager.add_entry()
        elif user_input == "2":
          
            if not os.path.exists(manager.filename):
                print("\nOutput:")
                print("Error: The journal file does not exist. Please add a new entry first.")
            else:
                manager.view_all_entries()
        elif user_input == "3":
            manager.search_entry()
        elif user_input == "4":
            manager.delete_all_entries()
        elif user_input == "5":
            print("\nOutput:")
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            # Handle invalid choice inputs gracefully
            print("\nOutput:")
            print("Invalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
        
        
                       
