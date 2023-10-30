# Mahad Mohamed Yonis (#101226808), Ember Warren (#101232329), Eliakim Gutknecht (#101243149), Aditi Keertani (#101202033)
# Date:April 6, 2022                              Version:1.0
#The functions required to make P4 Task 2: Final Team Code work

#Imports
import string
from typing import List


def book_category_dictionary(filename) -> dict:
    '''
    Returns all the books sorted by category.
    
    >>> book_category_dictionary('C:/Users/Mahad/Downloads/google_books_dataset.csv')
    "Fiction":[ {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery",
        "author": " Barbara Allan",
        "language ": "English",
        "rating": 3.3,
        "publisher": " Kensington Publishing Corp.",
        "pages": 288
        },
        {another element},
        ...
        ],
    "Biography":[ {"title": "The Nightshift Before Christmas: Festive hospital
        diaries from the author of million-copy hit",
        "author": " Adam Kay",
        "language": "English",
        "rating": 4.7,
        "publisher": "Pan Macmillan"
        "page": 112
        },
        {another element},
        ...],
    ....
    }
    '''
    #create an empty dictionary called books.
    books = {}
    
    # Open the file and read it.
    file = open(filename, 'r')
    
    #Skip the first line of the file since its just the headers.
    next(file)
    
    #For loop to go through each line
    for tab in file:
    
    #Split each tab in the excel to its own index
        line = tab.split(",")

        lst1 = []
        
    #Taking out the category column.
        category = line.pop(5)
        
        # Creating a temporary dictionary with all the information about the book
    
        temp_dictionnary = {"title": line[0],
                            "author": line[1],
                            "rating":line[2],
                            "publisher": line[3],
                            "pages": line [4],
                            "language": line[5].rstrip("\n")}
        
        
        rating = temp_dictionnary["rating"]
        pages = temp_dictionnary["pages"]
        
        # Converting Rating from String to float then updating the dictionnary
        if rating != "N/A":
            new_rating = float(rating)
            temp_dictionnary.update({"rating" : new_rating})
            
        # Converting number of pages from string to int then updating the dictionnary
        if pages != "N/A":
            new_pages = int(pages)
            temp_dictionnary.update({"pages" : new_pages})
            
        # Adding the temporary dictionnary into the list     
        lst1.append(temp_dictionnary)

    
    
        if category in books:
            books[category] += (lst1)
        else:
            books.update({category: lst1})
    
        #Close File
    file.close()
    return books



#Dictionnary that is used where all books are stored.
dict1 = book_category_dictionary('google_books_dataset.csv')



# Function add book
def add_book(dict1: dict, details: tuple) -> dict:
    '''
    Returns the updated dictionary and prints a message stating, “The book has been added
    correctly” or “There was an error adding the book”.
    
    >>> add_book(dict1, ('Mahad', 'Toukaleh', '9.9', 'Productions', '900', 'Investing', 'English')) 
    [...]
    The Book has been added correctly
    
    >>> add_book(dict1, ('Mahad', 'Toukaleh', '9.9', 'Productions', '900', 'daaaaa', 'English')) 
    [...]
    There was an error adding the book.

    >>> add_book(dict1, ('Mahad', 'Toukaleh', '9.9', 'Productions', '900', 'Fiction', 'English')) 
    [...]
    The Book has been added correctly
    
    '''
    
    
    title = str(details[0])
    author = str(details[1])
    rating = float(details[2])
    publisher = str(details[3])
    pages = int(details[4])
    category = str(details[5])
    language = str(details[6])
    
    details = (title, author, rating, publisher, pages, category, language)

    
    for key in dict1.copy():
        if key == category:
            temp_book = {"title": str(details[0]), "author": str(details[1]), "rating": float(details[2]), "publisher": str(details[3]), "pages": int(details[4]), "language": str(details[5])}
            dict1[key].append(temp_book)
    
    
    if temp_book in dict1[category]:
        print("\nThe Book has been added correctly")
    else:
        print("\nThere was an error adding the book")
        
    
    return len(dict1)


#Function Remove Book
def remove_book(title: str, category: str, dict1: dict) -> dict:
    """
    Returns an updated dictionary and prints a message depending on if the book was found or not.
    The dictionary must be ordered in a way so that the key is the category and the value is the book title.
    
    some_dict = {'bookcat 1' : 'book title 1', 'bookcat 2' : 'book title 2'}
    >>> remove_book ('bookcat 1', 'book title 1', some_dict)
    The book has been removed correctly
    {'bookcat 2': 'book title 2'}
    
    some_dict = {'bookcat 1' : 'book title 1', 'bookcat 2' : 'book title 2'}
    >>> remove_book ('bookcat 3', 'book title 1', some_dict)
    There was an error removing the book. Book not found
    {'bookcat 1' : 'book title 1', 'bookcat 2' : 'book title 2'}
    
    some_dict = {'bookcat 1' : 'book title 1', 'bookcat 2' : 'book title 2'}
    >>> remove_book ('bookcat 1', 'book title 4', some_dict)
    There was an error removing the book. Book not found
    {'bookcat 1' : 'book title 1', 'bookcat 2' : 'book title 2'}
    """
    
    error = True
    
    for i in dict1.values():
        for j in i:
            if title == j['title'] and category in dict1.keys():
                error = False
                j.clear()
                    
    
    if error == True:
        print("There was an error removing the book")
    
    else:
        print("Book removed successfully")           
            
            
    return dict1    



#Function 3 to get books by category
def get_books_by_category(data_source: str, category_wanted: str) -> dict:
    
    """
    The function returns all of the given books as well as the author of the books for a given category.
    Precondition: Text file must be in the same format of title, author, and then category in the 6th place. The infrmation must also be seperated by commas.
    
    >>>get_books_by_category('google_books_dataset.csv',comics)
    The category Comics has 7 books. This is the lists of books: 
    Book 1 : Deadpool Kills the Marvel Universe by Cullen Bunn 
    Book 2 : Young Justice Vol. 1 by Art Baltazar 
    Book 3 : Ultimate Spider-Man Vol. 11: Carnage by Brian Michael Bendis 
    Book 4 : Immortal Hulk Vol. 1: Or Is He Both? by Al Ewing 
    Book 5 : Watchmen (2019 Edition) by Alan Moore 
    Book 6 : The Joker by Brian Azzarello 
    Book 7 : Venomized by Cullen Bunn 
    """
    
    #Reads the file and skips the first line
    books = []
    file = open(data_source, 'r')
    next(file)
    i = 0
    
    #Reads each line in the file, takes out string "\n", and splits it into tabs, seperated by commas       
    for line in file: 
        updated_line = line.strip("\n")
        tab = updated_line.split(',')
        category = tab.pop(5)
        
        
    #Counts the number of books in the category and retrieves the wanted information    
        if category == category_wanted:
            i += 1
            adictionary =  {'Title' : tab[0], 'Author' : tab[1] }
            books += [ ['Book' , i , ':' ,  adictionary['Title'] , 'by' , adictionary['Author'] ]] 
            
    
     #Creates the message that will be displayed at the end       
    message = [ 'The category' , category_wanted , 'has' , i , 'books. This is the lists of books:' ] 
    for words in message:
        words = str(words)
        print(words, end = " ")
        
    for book in books:
        print("")
        for words in book:
            words = str(words)
            print(words, end = " ")
            
    
    return len(books)

#Function 4 to get books by rate
def get_books_by_rate(dict1:dict, exprate: int)-> str:
    """
    The function returns the number of books for the given rate.
    
    >>>x=get_books_by_rate(dictionary1, 3)
    print(x)
    there are 8 books whose rate is between 3 and 4
    Book 1 : Antiques Roadkill: A Trash 'n' Treasures Mystery Barbara Allan
    Book 2 : Bring Me Back B A Paris
    Book 3 : Mrs. Pollifax Unveiled Dorothy Gilman
    Book 4 : How to Understand Business Finance: Edition 2 Bob Cinnamon
    Book 5 : The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further Alvin Hall
    Book 6 : Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything Steven D. Levitt
    Book 7 : The Infinite Game Simon Sinek
    Book 8 : Selling 101: What Every Successful Sales Professional Needs to Know Zig Ziglar
    8

    """
    keys = dict1.keys()
    keys = list(keys)
    books=[]
    for jj in range(len(keys)):
        for book in dict1[keys[jj]]:
            r = book['rating']
            t = book['title']
            au = book['author']
            
            isSame=False  
            if r!= 'N/A' and r>=exprate and r<exprate+1:
                for aBook in books:
                #checking if book is already present in the books list
                    if aBook['title']==t and aBook['author']==au:
                        isSame=True
                if isSame==False:#book is not present in the list    
                    books.append({'title': book['title'], 'author':book['author']})
                         
    total=len(books)
    print('there are', total, 'books whose rate is between', exprate, 'and', exprate+1)
    i=1
    for aBook in books:
        print('Book', i, ':',aBook['title'], aBook['author'])
        i+=1
    return total

#Function 5 to get books by title
def get_books_by_title(dict1:dict, title: str)-> str:
    """
    The function returns a Boolean variable which is True if the title exists in the dictionary;
otherwise, it returns False. Additionally, the function prints a message stating, “The book has
been found” or “The book has NOT been found”. 

     >>>get_books_by_title(dictionary1, 'Bring Me Back')
     The book has been found 
     True

    """

    isPresent=False

    for key in dict1:
            for values in dict1[key]:
                for index in values:
                    if values[index] == title:
                        isPresent = True


    if isPresent is True:
        print("The book has been found ")
    else:
        print("The book has NOT been found")

    return isPresent



# Function 6: get_books_by_author
def get_books_by_author(filename: str, get_author:str):
    
    """
    Returns each book the author for get_author has published from the filename as well as the rating of the book and the total number of books published. Note that the same book in a different category counts as a single book.
    
    filename = {John Doe's book, John Doe, 3.3, Kensington Publishing Corp., 288, Fiction, English
                Jane Doe's book, Jane Doe, 4.8, Kensington Publishing Corp., 288, Fiction, English
                John Doe's book, John Doe, 3.3, Kensington Publishing Corp., 288, Mystery, English}
    >>> x = get_books_by_author('filename', 'John Doe')
    The author Barbara Allan has published the following books:
    book 1 : John Doe's book, rate: 3.3
    """
    
    lst1 = [] # Starts with an empty list
    num = 1 # set count to 1 for the first book published by author
    with open (filename, 'r') as file: # Opens and reads the dictionary.
        lines = file.readlines()
        for line in lines:
            tab = line.split(',') # Splits the dictionary into individual lines 
            if get_author in tab: # for each time the authors name is in the dictionary        
                lst1.append((tab[0],tab[2])) # add the book and rating to the lst
        print ("The author", get_author, "has published the following books:") # Prints a message.
        for item in list(set(lst1)): # Removes repeated book titles 
            print ("book", num, ":", item[0], ", rate:", item[1],) # Prints the book number, title and rating
            num += 1 # book count goes up by 1
            
    total_books = num-1
    return total_books


#Function 7 to get books by publisher
def get_books_by_publisher(data_source: str, publisher_wanted: str) -> dict:

    """
    The function returns all of the given books as well as the author of the books from a given publisher.
    Precondition: Text file must be in the same format of title, author, and publisher as the 4th place. The infrmation must also be seperated by commas.

    >>>get_books_by_publisher('google_books_dataset.csv', 'Kensington Publishing Corp.')
    The publisher Kensington Publishing Corp. has published the following books: 
    Book 1 : Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan 
    Book 2 : Antiques Knock-Off by Barbara Allan 

    """

    #Reads the file and skips the first line
    books = []
    book_names = set()
    file = open(data_source, 'r')
    next(file)
    number_of_books = 0

    #Reads each line in the file, takes out string "\n", and splits it into tabs, seperated by commas
    for line in file: 
        updated_line = line.strip("\n")
        tab = updated_line.split(',')
        publisher = tab.pop(3)
        title = tab[0]
#Counts the number of books produced by a publisher and retrieves the wanted information
        if publisher == publisher_wanted:
            if title not in book_names:
                number_of_books += 1
                adictionary =  {'Title' : tab[0], 'Author' : tab[1] }
                info = [ ['Book' , number_of_books , ':' ,  adictionary['Title'] , 'by' , adictionary['Author'] ]]

            check_duplicate = info[0][3]
            if check_duplicate not in book_names:
                book_names.add(check_duplicate)
                books += info



     #Creates the message that will be displayed at the end
    message = [ 'The publisher' , publisher_wanted , 'has published the following books:' ] 
    for words in message:
        words = str(words)
        print(words, end = " ")

    for book in books:
        print("")
        for words in book:
            words = str(words)
            print(words, end = " ")



    return number_of_books

#function 8 get all categories for book title
def get_all_categories_for_book_title(dict1: dict, title: str) -> int:
    '''
    The function returns the number of categories associated with the given title.
    
    >>> get_all_categories_for_book_title(dict1, 'Bring Me Back')
    The Book Title Bring Me Back belongs to the following categories: 
    Category 1 : Fiction
    Category 2 : Crime
    Category 3 : Thrillers
    
    >>> get_all_categories_for_book_title(dict1, "Antiques Roadkill: A Trash 'n' Treasures Mystery")
    The Book Title Antiques Roadkill: A Trash 'n' Treasures Mystery belongs to the following categories: 
    Category 1 : Mystery
    Category 2 : Fiction
    Category 3 : Detective
    
    >>> get_all_categories_for_book_title(dict1, 'The Mysterious Affair at Styles')
    The Book Title The Mysterious Affair at Styles belongs to the following categories: 
    Category 1 : Classics
    Category 2 : Thrillers
    Category 3 : Horror
    Category 4 : Fiction
    Category 5 : Detective
    '''
    
    print("\nThe Book Title", title, "belongs to the following categories: ")
    
    temp_set = set()
    
    count = 0
    
    for key in dict1:
        for values in dict1[key]:
            for index in values:
                if values[index] == title:
                    category = key
                    count +=1
                    temp_set.add(category)
    
    
    count = 0               
    for i in temp_set:
        count +=1
        print("Category", count,': ' +  i)
        
    return count




def sort_books_title(filename):
    
    """
    Takes an input dictionary book_dict, converts into a list that formats it to 
    
    {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery",
    "author": " Barbara Allan",
    "language ": "English",
    "rating": 3.3,
    "publisher": " Kensington Publishing Corp.",
    " category": [" Fiction", "Comedy"]
    "pages": 288} 
    
    and returns an updated dictionary that sorts the books alphabetically by title. *Note : Book titles must be capitalised in order to be sorted properly. 
    
    >>> sort_books_title_1('/Users/emberwarren/Downloads/google_books_dataset')
    [{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'rating': 'George R.R. Martin', 'publisher': '4.5', 'pages': 'HarperCollins UK', 'category': '864', 'language': 'Fiction'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'rating': 'George R.R. Martin', 'publisher': '4.5', 'pages': 'HarperCollins UK', 'category': '864', 'language': 'Fantasy'}] 
    # The entire dataset will output, but to save space in the docstring I shortened it.
    """    
    
    book_dict = []
    filepath = open(filename, 'r')
    
    next (filepath)
    for tab in filepath:
        
        line = tab.split(',')
        
        temp_dict = {"title": line[0],"rating":line[1], "publisher": line[2], "pages": line [3], "category": line[4], "language": line[5].rstrip("\n")}
          
        book_dict.append(temp_dict)
        
        for i in range (len(book_dict)):
            for j in range (len(book_dict) - 1- i):
                a = book_dict[j]
                b = book_dict[j+1]
                
                if a["title"] > b["title"]:
                    book_dict[j], book_dict[j+1] = book_dict[j+1], book_dict[j]
                
    return book_dict    



def sort_books_publisher(dict1) -> dict:
    '''
   The function returns a list of books sorted alphabetically by publisher, and 
   then sorts the books made by the author alphabetically by title.
    '''
    
    
    # Open the file and read it.
    file = open('google_books_dataset.csv', 'r')
    
    #Skip the first line of the file since its just the headers.
    next(file)
    lst1 = []
    categories = []
    #For loop to go through each line
    for tab in file:
    
    #Split each tab in the excel to its own index
        line = tab.split(",")
        
        
        
        # Creating a temporary dictionary with all the information about the book
    
        temp_dictionnary = {"title": line[0],
                            "author": line[1],
                            "rating":line[2],
                            "publisher": line[3],
                            "pages": line[4],
                            "category": line[5],
                            "language": line[6].rstrip("\n")}
        
        title = temp_dictionnary["title"]
        author = temp_dictionnary["author"]
        rating = temp_dictionnary["rating"]
        publisher = temp_dictionnary["publisher"]
        pages = temp_dictionnary["pages"]
        category = temp_dictionnary["category"]
        language = temp_dictionnary["language"]
        
        # Converting Rating from String to float then updating the dictionnary
        if rating != "N/A":
            new_rating = float(rating)
            temp_dictionnary.update({"rating" : new_rating})
            
        # Converting number of pages from string to int then updating the dictionnary
        if pages != "N/A":
            new_pages = int(pages)
            temp_dictionnary.update({"pages" : new_pages})
            
            
        lst1.append(temp_dictionnary)
        
    
    lst2 = []
    categories = []
     
        
    for i in dict1:
        for j in dict1[i]:
            equal = False
            
            for details in lst2:
        
                if details.get('title') == j.get('title'): 
                    equal = True

            if equal == False:
                non_dupes = set()
                
                for same_category in dict1:
                    
                    for same_book in dict1.get(same_category):
                        
                            if same_book.get('title') == j.get('title'): 
                                non_dupes.add(same_category)
                                
                categories = list(non_dupes) 
                
                
                lst2.append({'title': j.get('title'), 'author': j.get('author'), 'rating': j.get('rating'), 'publisher': j.get('publisher'), 'pages': j.get(pages), 'category': categories, 'language': j.get('language')})
    
              
    
    for i in range(len(lst2)):
        for j in range(len(lst2) - 1 - i):
            first = lst2[j]
            second = lst2[j + 1]
                    
            if first["publisher"] > second["publisher"]:
                lst2[j], lst2[j+1] = lst2[j + 1], lst2[j]  
            
            if first['publisher'] == second['publisher']:
                lst2[j], lst2[j+1] = lst2[j + 1], lst2[j]

       
    file.close
    return lst2



def sort_books_author(dict1) -> dict:
    '''
    Returns all the books sorted by authors name in alphabetical order. If authors name are the same then it will sort by title name.
    
    >>> sort_books_author(dict1)
    [{'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'rating': 4.7, 'publisher': 'Pan Macmillan', 'pages': None, 'category': ['Humor'], 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': None, 'category': ['Mystery', 'Traditional', 'Detective', 'Fiction'], 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': None, 'category': ['Mystery', 'Thrillers', 'Detective', 'Fiction'], 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': None, 'category': ['Horror', 'Thrillers', 'Detective', 'Fiction', 'Classics'], 'language': 'English'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': None, 'category': ['Comics', 'Superheroes'], 'language': 'English'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': None, 'category': ['Comics', 'Superheroes'], 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': None, 'category': ['Mystery', 'Thrillers', 'Adventure', 'Fiction'], 'language': 'English'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': None, 'category': ['Economics', 'Money Management', 'Investing', 'Finance', 'Business'], 'language': 'English'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': None, 'category': ['Adventure', 'Mythical Creatures', 'Fiction'], 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': None, 'category': ['Epic', 'Fiction', 'Fantasy'], 'language': 'English'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': None, 'category': ['Adventure', 'Fiction', 'Fantasy'], 'language': 'English'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': None, 'category': ['Comics', 'Superheroes'], 'language': 'English'}

    }
    '''
    
    
    # Open the file and read it.
    file = open('google_books_dataset.csv', 'r')
    
    #Skip the first line of the file since its just the headers.
    next(file)
    lst1 = []
    categories = []
    #For loop to go through each line
    for tab in file:
    
    #Split each tab in the excel to its own index
        line = tab.split(",")
        
        
        
        # Creating a temporary dictionary with all the information about the book
    
        temp_dictionnary = {"title": line[0],
                            "author": line[1],
                            "rating":line[2],
                            "publisher": line[3],
                            "pages": line[4],
                            "category": line[5],
                            "language": line[6].rstrip("\n")}
        
        title = temp_dictionnary["title"]
        author = temp_dictionnary["author"]
        rating = temp_dictionnary["rating"]
        publisher = temp_dictionnary["publisher"]
        pages = temp_dictionnary["pages"]
        category = temp_dictionnary["category"]
        language = temp_dictionnary["language"]
        
        # Converting Rating from String to float then updating the dictionnary
        if rating != "N/A":
            new_rating = float(rating)
            temp_dictionnary.update({"rating" : new_rating})
            
        # Converting number of pages from string to int then updating the dictionnary
        if pages != "N/A":
            new_pages = int(pages)
            temp_dictionnary.update({"pages" : new_pages})
            
            
        lst1.append(temp_dictionnary)
        
    
    lst2 = []
    categories = []
     
        
    for i in dict1:
        for j in dict1[i]:
            equal = False
            
            for details in lst2:
        
                if details.get('title') == j.get('title'): 
                    equal = True

            if equal == False:
                non_dupes = set()
                
                for same_category in dict1:
                    
                    for same_book in dict1.get(same_category):
                        
                            if same_book.get('title') == j.get('title'): 
                                non_dupes.add(same_category)
                                
                categories = list(non_dupes) 
                
                
                lst2.append({'title': j.get('title'), 'author': j.get('author'), 'rating': j.get('rating'), 'publisher': j.get('publisher'), 'pages': j.get(pages), 'category': categories, 'language': j.get('language')})
    
              
    
    for i in range(len(lst2)):
        for j in range(len(lst2) - 1 - i):
            first = lst2[j]
            second = lst2[j + 1]
                    
            if first["author"] > second["author"]:
                lst2[j], lst2[j+1] = lst2[j + 1], lst2[j]  
            
            if first['author'] == second['author']:
                lst2[j], lst2[j+1] = lst2[j + 1], lst2[j]

       
    file.close
    return lst2    




def sort_books_ascending_rate(booksdict):
    # Open the file and read it.
    file = open('google_books_dataset.csv', 'r')
    
    #Skip the first line of the file since its just the headers.
    next(file)
    lst1 = []
    categories = []
    #For loop to go through each line
    for tab in file:
    
    #Split each tab in the excel to its own index
        line = tab.split(",")
        
        
        
        # Creating a temporary dictionary with all the information about the book
    
        temp_dictionnary = {"title": line[0],
                            "author": line[1],
                            "rating":line[2],
                            "publisher": line[3],
                            "pages": line[4],
                            "category": line[5],
                            "language": line[6].rstrip("\n")}
        
        title = temp_dictionnary["title"]
        author = temp_dictionnary["author"]
        rating = temp_dictionnary["rating"]
        publisher = temp_dictionnary["publisher"]
        pages = temp_dictionnary["pages"]
        category = temp_dictionnary["category"]
        language = temp_dictionnary["language"]
        
        # Converting Rating from String to float then updating the dictionnary
        if rating != "N/A":
            new_rating = float(rating)
            temp_dictionnary.update({"rating" : new_rating})
            
        # Converting number of pages from string to int then updating the dictionnary
        if pages != "N/A":
            new_pages = int(pages)
            temp_dictionnary.update({"pages" : new_pages})
            
            
        lst1.append(temp_dictionnary)
        
    lst2 = []
    categories = []
     
        
    for i in dict1:
        for j in dict1[i]:
            equal = False
            
            for details in lst2:
        
                if details.get('title') == j.get('title'): 
                    equal = True

            if equal == False:
                non_dupes = set()
                
                for same_category in dict1:
                    
                    for same_book in dict1.get(same_category):
                        
                            if same_book.get('title') == j.get('title'): 
                                non_dupes.add(same_category)
                                
                categories = list(non_dupes) 
                
                
                lst2.append({'title': j.get('title'), 'author': j.get('author'), 'rating': j.get('rating'), 'publisher': j.get('publisher'), 'pages': j.get(pages), 'category': categories, 'language': j.get('language')})
    
              
    
    for i in range(len(lst2)):
        for j in range(len(lst2) - 1 - i):
            first = lst2[j]
            second = lst2[j + 1]
            
            
            if first["rating"] == 'N/A':
                first['rating'] = 0
                
            if second["rating"] == 'N/A':
                second['rating'] = 0
                    
            if first["rating"] > second["rating"]:
                lst2[j], lst2[j+1] = lst2[j + 1], lst2[j]  
            
            if first['rating'] == second['rating']:
                lst2[j], lst2[j+1] = lst2[j + 1], lst2[j]
    
            if first["rating"] == 0:
                first['rating'] = 'N/A'
                
            if second["rating"] == 0:
                second['rating'] = 'N/A'
                
        file.close
    return lst2        
    
    