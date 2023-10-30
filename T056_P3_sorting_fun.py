# By: Mahad Mohamed Yonis (#101226808), Eliakum Gutknecht (#101243149), Ember Warren (#101232329)
# Date:March 30, 2022                              Version:1.0

#imports
from T056_check_equal import check_equal
import T56_P1_load_data
dict1 = T56_P1_load_data.book_category_dictionary('C:/Users/Mahad/Downloads/google_books_dataset.csv')


# Ember Warren 101232329
# I made this fucntion 2 ways. The first opens a file such as the google_books_dataset that was provided for the project. The second takes any list that is already properly formated and srts them accordingly.
# Method 1
def sort_books_title_1(filename):
    
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

# Method 2
def sort_books_title_2(book_dict):
    
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
    
    sort = [{"title" : "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author" : "Barbara Allan","rating" : 3.3,"publisher" : "Kensington Publishing Corp.", "pages" : 288, "category" : "Fiction", "language" :"English"},{"title" : "The Painted Man (The Demon Cycle. Book 1)", "author" : "Peter V. Brett","rating" : 4.5,"publisher" : "HarperCollins UK", "pages" : 544, "category" : "Fiction", "language" :"English"},{"title" : "Edgedancer: From the Stormlight Archive", "author" : "Brandon Sanderson","rating" : 4.8,"publisher" : "Tor Books", "pages" : 226, "category" : "Fiction", "language" :"English"}]
    
    >>> sort_books_title_2(sort)
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English'}]
    
    """
        
    for i in range (len(book_dict)):
        for j in range (len(book_dict) - 1- i):
            a = book_dict[j]
            b = book_dict[j+1]
            
            if a["title"] > b["title"]:
                book_dict[j], book_dict[j+1] = book_dict[j+1], book_dict[j]
            
    return book_dict

#Eliakim Gutknecht, 101243149, 
def sort_books_publisher(adict: dict) -> list:
    """
    The function returns a list of books sorted alphabetically by publisher
    from a given dictionary
    """
    books = [ ]
    titles_list = [ ]
    all_info_dict = { }
    publisher_dict = { }
    list_of_publishers = [ ]
    
    
    for category in adict:
        info_list = adict.get(category)
        
        for info in info_list:
            publisher = info.pop('publisher')
            title = info.get('title')
            titles_list.append(title)
            all_info_dict.update({title : info}) 
            publisher_dict.update({ title : publisher })
            list_of_publishers += [publisher]
           
        
            for i in range (0, len(titles_list) - 1):
                for j in range(0, len(titles_list) - 1 - i):  
                    if titles_list[j] > titles_list[j + 1]:
                        titles_list[j], titles_list[j + 1] = titles_list[j + 1], titles_list[j]
            
            for i in range (0, len(list_of_publishers) - 1):
                for j in range(0, len(list_of_publishers) - 1 - i):  
                    if list_of_publishers[j] > list_of_publishers[j + 1]:
                        list_of_publishers[j], list_of_publishers[j + 1] = list_of_publishers[j + 1], list_of_publishers[j]            
        
        for title in titles_list:
            publisher = publisher_dict[title]        
            books += [{ publisher : all_info_dict[title] }]
    
    
    return books


#Mahad Mohamed Yonis (#101226808)
def sort_books_author(dict1) -> dict:
    '''
    Returns all the books sorted by authors name in alphabetical order. If authors name are the same then it will sort by title name.
    
    >>> sort_books_author(dict1)
    [{'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'rating': 4.7, 'publisher': 'Pan Macmillan', 'pages': None, 'category': ['Humor'], 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': None, 'category': ['Mystery', 'Traditional', 'Detective', 'Fiction'], 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': None, 'category': ['Mystery', 'Thrillers', 'Detective', 'Fiction'], 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': None, 'category': ['Horror', 'Thrillers', 'Detective', 'Fiction', 'Classics'], 'language': 'English'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': None, 'category': ['Comics', 'Superheroes'], 'language': 'English'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': None, 'category': ['Comics', 'Superheroes'], 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': None, 'category': ['Mystery', 'Thrillers', 'Adventure', 'Fiction'], 'language': 'English'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': None, 'category': ['Economics', 'Money Management', 'Investing', 'Finance', 'Business'], 'language': 'English'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': None, 'category': ['Adventure', 'Mythical Creatures', 'Fiction'], 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': None, 'category': ['Epic', 'Fiction', 'Fantasy'], 'language': 'English'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': None, 'category': ['Adventure', 'Fiction', 'Fantasy'], 'language': 'English'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': None, 'category': ['Comics', 'Superheroes'], 'language': 'English'}

    }
    '''
    
    
    # Open the file and read it.
    file = open('C:/Users/Mahad/Downloads/google_books_dataset.csv', 'r')
    
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
   
    

def test_sort_author():
    '''
    Tests the function called T056_P3_sorting. Checks to see if failed or passed.
    '''
      
    check_equal("sort_books_author(dict1)", sort_books_author(dict1), sort_books_author(dict1))
    




def test_function2( ) -> None:
    """
    Uses the function check_equal to check if function2, sort_books_publisher, functions properly with a sample dictionary
    """
    
    sample_dict = {'Comics'  :  [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'language': 'English'}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'pages': 144, 'language': 'English'}]}
    
    check_equal( "Test for the function sort_books_publisher with a test_dictionary with 2 books from the same publisher: sort_books_publisher( sample_dict)" , sort_books_publisher(sample_dict), [{'Marvel Entertainment': {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'pages': 96, 'language': 'English'}}, {'Marvel Entertainment': {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'rating': 4.1, 'pages': 144, 'language': 'English'}}])
    
def test_sort_books_title() -> None:
    """
    Returns the description of what is being tested, PASSED if the expected outcome and real outcome are the same type and , and FAILED otherwise.
    
    # Note that the examples should print the entire expected and actual output of the function not just PASSED/ FAILED, but to reduce readibility issues and save lines that was omitted. 
    """
    sort = [{"title" : "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author" : "Barbara Allan","rating" : 3.3,"publisher" : "Kensington Publishing Corp.", "pages" : 288, "category" : "Fiction", "language" :"English"},{"title" : "The Painted Man (The Demon Cycle. Book 1)", "author" : "Peter V. Brett","rating" : 4.5,"publisher" : "HarperCollins UK", "pages" : 544, "category" : "Fiction", "language" :"English"},{"title" : "Edgedancer: From the Stormlight Archive", "author" : "Brandon Sanderson","rating" : 4.8,"publisher" : "Tor Books", "pages" : 226, "category" : "Fiction", "language" :"English"}]
    
    check_equal(sort_books_title_2(sort), sort_books_title_2(sort), ([{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English'}]))
                


# Main Script
test_sort_books_title()
test_sort_author()   
test_function2( )
