from tkinter import *
##AUTHOR : LEV_NIKOLAYEVICH_MYSHKIN
##Sets and configure the windo of the library management systemto be opened
ws = Tk()
issue_S=  Tk()
ws.title("Library Management System")
ws.geometry('500x500')
ws.configure(bg="lightgrey")


##SETTING UP OF VARIABLE AND OTHER OBJECTS
global bookname
issued_book_dict = dict()
book_list = []
returned_books = dict()
issued_book_list =[]
global book_name_removed_for_dict
global holder_name_removed_for_dict 
##################
_text_ = Text(ws, width=50,height=10)
_text_.insert(END, "First box is for adding books, \n Second two for book name and borrower name and \nthrid two for returning book and issuer name \n Errors will be logged below")
_text_.pack()
#################
'''function defined for adding books y entering a name in given textbox'''
def add_book(): 
    book_name_for_list = get_book_from_user.get()  #get the name of book to be added and stores it in a variable
    Label (ws, text=f'{book_name_for_list}, added').pack() ## displays a label for  showing that the book is added
    book_list.append(book_name_for_list) #appends the input of book to list
    _text_.insert(END, f' \n{book_name_for_list}, is added in list of books')

'''function defined for listing books in a textbook when clciked'''
def listbook(): 
    book_list_text_tk = Text(ws)  ##Uses text widget to displaybooks
    book_list_text_tk.pack()
    for books in book_list:  ##iteraties thorugh the whole added book list to show available books
        book_list_text_tk.insert(END, books + '\n')
   
def issue_book_function(): 
        book_name_for_dict = str(bookname.get())  #stores the name of book that is borrowedto be stored in dict
        name_of_borrower = str(holdername.get())  #stores the name of borrower to be added in dict
        if book_name_for_dict in book_list :
            Label (ws ,text=f'{name_of_borrower}, has borrowed, {book_name_for_dict}').pack()
            issued_book_dict[f'{name_of_borrower}'] = book_name_for_dict   
            issued_book_list.append(book_name_for_dict)  
            print (issued_book_dict)  ## prints the dict in shell/terminal for cross-verfication
            _text_.insert(END, f' \n{book_name_for_dict}, is issued to {name_of_borrower}')
        else:
              _text_.insert(END, '\nNo such book exist to be borrowed', )
              print(book_list)

def list_issued_borrower():
        issued_books_text =Text(issue_S) ##this variable is for displaying text in tk
        issued_books_text.pack()
        _text_.insert(END, f' \nlisting issued borrowers ')
        for  issuedbooks in issued_book_dict:###iterated through the dict to display name of borrower
                issued_books_text.insert(END, issuedbooks + '\n' )
                issued_books_text.pack()
        for issued in issued_book_list:
              _text_.insert(END, issued ,'is issued')

def returned_books_function():
    book_name_removed_for_dict = (bookname_removed.get()) #This variable stores the value of book to be removed
    holder_name_removed_for_dict = (holdername_removed.get())##This stores the name to be remoev from issued holder list
    if book_name_removed_for_dict in issued_book_list:##Check if the entered book was borrowed or not
         issued_book_dict.pop(holder_name_removed_for_dict,book_name_removed_for_dict)
         Label (ws ,text=f'{holder_name_removed_for_dict}, has retuned, {book_name_removed_for_dict} and name removed from list of borrowed books').pack()
         returned_books[holder_name_removed_for_dict] = book_name_removed_for_dict   
         print (returned_books)
         _text_.insert(END, f' \n {holder_name_removed_for_dict} has returned {book_name_removed_for_dict}')
    else:
          _text_.insert(END, '\nNo such book exist to be returned/no such user hastaken book', )
          print(returned_books)


get_book_from_user=Entry(ws)  #get input from user abput adding books
get_book_from_user.pack() #rezies the input feild to small space

Button(ws , text="Add book", command=add_book).pack() #Button on ui for adding books
Button(ws,text="List books",command=listbook).pack() #Buttons on ui for showing list of books
          
bookname=Entry(ws) #method of data entry for getting book to be borrwed
holdername = Entry(ws)##getsname of holder and stores it in name of borrower
bookname.pack()
holdername.pack()

Button(ws , text="issue book", command=issue_book_function).pack()# displays button for issue book
Button(ws, text="List of holders",command=list_issued_borrower).pack()# displaybutton for showing the name of borrowers

bookname_removed=Entry(ws, text="Enter book name to be returned")##Displays input for bookname to be returned
holdername_removed = Entry(ws, text="Enter the name of the holder")##Displays holdername to be removed from issued list
bookname_removed.pack()
holdername_removed.pack()

Button(ws , text="[return] books", command=returned_books_function).pack()##Button for returning the book
Button(ws, text="[removes]List of holders",command=returned_books_function).pack()
ws.mainloop()

###Author - lev_nikolayevich_myskin