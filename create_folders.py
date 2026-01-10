# Importing modules
import os

# Creating list of folders to create
list_of_dirs = ["01_Basics",            
"02_Arrays_and_Lists",    
"03_Linked_Lists",       
"04_Stacks_and_Queues",   
"05_Recursion",          
"06_Sorting_Searching",   
"07_Trees",              
"08_Graphs",             
"09_Dynamic_Programming"]

# Main Logic
def main():
    # Extracting per directory
    for dir in list_of_dirs:
        # Creating Directory
        os.makedirs(dir)


# Running the main function
if __name__ == "__main__":
    main()