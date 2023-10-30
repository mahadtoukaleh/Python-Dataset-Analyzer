# Eliakim Gutknecht (#101243149) (Created)
#Reviewed By: Mahad Mohamed Yonis (101226808), Ember Warren (#101232329),  Aditi Keertani (#101202033)
# Date:April 12, 2022                              Version:1.0

def book_category_dictionary(filename) -> dict:
    '''
    Returns the dictionary with no duplicate books.
    
    >>> book_category_dictionary('google_books_dataset.csv')
    
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Fiction', 'language': 'English'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'category': 'Fiction', 'language': 'English'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'category': 'Fiction', 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'category': 'Fiction', 'language': 'English'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'category': 'Fiction', 'language': 'English'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'category': 'Fiction', 'language': 'English'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'rating': 4.0, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Fiction', 'language': 'English'}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Trace of Vice (a Keri Locke Mystery Book #3)', 'author': 'Blake Pierce', 'rating': 4.8, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'category': 'Fiction', 'language': 'English'}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208, 'category': 'Fiction', 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 1216, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'category': 'Fiction', 'language': 'English'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fiction', 'language': 'English'}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'rating': 4.4, 'publisher': 'Morgan Rice', 'pages': 250, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'category': 'Fiction', 'language': 'English'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226, 'category': 'Fiction', 'language': 'English'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'rating': 4.3, 'publisher': 'Minotaur Books', 'pages': 60, 'category': 'Fiction', 'language': 'English'}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'rating': 4.3, 'publisher': 'Macmillan', 'pages': 1728, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'category': 'Fiction', 'language': 'English'}],

    '''
    
    
    #create an empty dictionnary called books.
    books = {}
    no_dup = {}
    list_of_titles_category = []
    number = 0
    dup_num = 0
    t = 0
    
    # Open the file and read it.
    file = open(filename, 'r')
    
    #Skip the first line of the file 
    next(file)
    
    
    for tab in file:
    
    #Split each tab in the excel to its own index
        line = tab.split(",")

        lst1 = []
        
   
        
        # Creating a temporary dictionnary with all the information about the book
    
        temp_dictionnary = {"title": line[0],
                            "author": line[1],
                            "rating":line[2],
                            "publisher": line[3],
                            "pages": line [4],
                            "category": line [5],
                            "language": line[6].rstrip("\n")}
        
        
        rating = temp_dictionnary["rating"]
        pages = temp_dictionnary["pages"]
        category = temp_dictionnary["category"]
        title = temp_dictionnary["title"]
        
        # Converting Rating from String to float then updating the dictionnary
        if rating != "N/A":
            new_rating = float(rating)
            temp_dictionnary.update({"rating" : new_rating})
            
        # Converting number of pages from string to int then updating the dictionnary
        if pages != "N/A":
            new_pages = int(pages)
            temp_dictionnary.update({"pages" : new_pages})
            
           
        lst1.append(temp_dictionnary)
        

        if [title, category] not in list_of_titles_category:
            if category in no_dup:
                no_dup[category] += (lst1)
                number += 1
                
            else:
                no_dup.update({category: lst1}) 
                number += 1

        list_of_titles_category += [[title, category]]
    
    
    
    
            
        #CLose File
    file.close()
    
    print('number:', number)
    #print('dup #:', dup_num)
    #print ('t:', t)
    print(list_of_titles_category)

    return no_dup

a = book_category_dictionary('google_books_dataset.csv')
print(a)
