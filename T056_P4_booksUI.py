# Mahad Mohamed Yonis (#101226808), Ember Warren (#101232329), Eliakim Gutknecht (#101243149), Aditi Keertani (#101202033)
# Date:April 6, 2022                              Version:1.0
list_of_commands = ['L', 'A', 'R', 'G', 'GCT', 'S','M']

#imports
import T056_P4_functions as p4
import string
from typing import List

def menu():
    #Menu function that displays all of the functions
    
    print("The Available Commands Are:")
    print("1- L)oad data")
    print("2- A)dd book")
    print("3- R)emove book")
    print("4- G)et books")
    print("    T)itle  R)ate  A)uthor  P)ublisher  C)ategory")
    print("5- GCT) Get All Categories for book Title")
    print("6- S)ort books")
    print("    T)itle  R)ate  P)ublisher  A)uthor")
    print("7- Q)uit")
    
    return ''

def user_input():
    #Function that takes all of the input and controls the commands
    
    first_command = True
    main_commands = True
    
    
    
    while first_command == True:
        input1 = input("Please enter your first command (Press M for menu): ")
        input1 = input1.upper()
        
        if input1 == 'L':
            filename = input("Please enter filename to read: ")
            dict1 = p4.book_category_dictionary(filename)
            dict2 = p4.sort_books_title(filename)
            first_command = False
            print(dict1)
            
        elif input1 == 'M':
            print(menu())
        
        elif input1 == 'Q':
            first_command = False
            main_commands = False
            
        elif input1 in list_of_commands:
            print("File not loaded")
    
        else:
            print("No such command")
     
    
    
    while main_commands == True:
        user_input = input("Please type in your command: ")
        user_input = user_input.upper()
        
        if user_input == 'L':
            filename = input("Please enter filename to read: ")
            dict1 = p4.book_category_dictionary(filename)
            dict2 = p4.sort_books_title('google_books_dataset.csv')

        elif user_input == 'M':
            print(menu())
            
        elif user_input == 'A':
            file_input = input("Enter the title of book to be added: ")       
            if file_input not in dict1.keys():
                    enter_info = input("Enter the details of the book to be added: ")
                    # Example of enter_info input : ['author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'category': 'Fiction', 'language': 'English']
                    print ("The Book has been added correctly")
                    dict1.update({file_input : enter_info})
                    print (dict1)
            else:
                    print ("Book already in dictionary")
            print ('\n')
            
        
        elif user_input == "R":
            title = input("Enter the title of the book you wish to remove: ")
            category = input("Enter the category of the book you wish to remove: ")
            removing_book = p4.remove_book(title, category, dict1)
            print(removing_book)
            
            """
            file_input = input("Enter the title of book to be removed: ")
            for item in dict2:
                    if file_input in item.values():
                            book_category = input("Enter the category of the book to be removed: ")
                            if book_category in item.values():  
                                    dict2.remove(item)
                                    print (dict2)
                                    print ("Book successfully removed.")
                                    break
                            else: print ('book not found')
                            break
                            
                    else:
                            print ("book not found") 
                            break
            """
                
        elif user_input == 'G':
            subcommand = input("How do you want to get books by? ")
            subcommand = subcommand.upper()
            
            if subcommand == 'T':
                title = input("What is the name of the book you are looking for?\n ")
                books_by_title = p4.get_books_by_title(dict1, title)
                print(books_by_title)
                
            elif subcommand == 'R':
                rating = int(input("What is the rating of the book you are looking for? \n"))
                books_by_rate = p4.get_books_by_rate(dict1, rating)   
                print(books_by_rate)
            
            elif subcommand == 'A':
                author = input("What is the name of the author? \n")
                books_by_author = p4.get_books_by_author('google_books_dataset.csv', author)
                print(books_by_author)
                
            elif subcommand == 'P':
                publisher = input("Which publisher do you desire? ")
                books_by_publisher = p4.get_books_by_publisher(filename, publisher)
                print(books_by_publisher)
            
            elif subcommand == 'C':
                category = input('Which category do you desire? ')
                books_by_category = p4.get_books_by_category(filename, category)
                print(books_by_category)
            
            elif subcommand == 'Q':
                main_commands = False
            
            else:
                print("No such command")
        
            
        elif user_input == 'GCT':
            title = input("Enter a books title: ")
            all_categories_for_book_title = p4.get_all_categories_for_book_title(dict1, title)
        
        elif user_input == 'S':
            subcommand = input("How do you want to sort? ")
            subcommand = subcommand.upper()
            
            
            if subcommand == 'T':
                print('Sorting by title')
                sort_by_titles = p4.sort_books_title(filename)
                print(sort_by_titles)
                
            elif subcommand == 'R':
                print('Sorting by rate')
                sort_books_rate = p4.sort_books_ascending_rate(dict1)
                print(sort_books_rate)
            
            elif subcommand == 'P':
                print('Sorting by publisher')
                sorting_books_by_publisher = p4.sort_books_publisher(dict1)
                print(sorting_books_by_publisher)
            
            elif subcommand == 'A':
                print('Sorting by author')
                sort_books_by_author = p4.sort_books_author(dict1)
                print(sort_books_by_author)
            
            elif subcommand == 'Q':
                main_commands = False
            
            else:
                print('No such sorting method. Please try again.')            
    
        
        elif user_input == 'Q':
            main_commands = False
        
        elif user_input not in list_of_commands:
            print("No such command")

    
    
    
    
    print('You have quit the program. Have a good day!')
        
user_input()