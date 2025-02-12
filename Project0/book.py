from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'id':1, 'title':'Python-Full Stack', 'author':'Sachin Gupta','rating':4.5},   
    {'id':2, 'title':'Django-Full Stack', 'author':'Veronica','rating':5},
     {'id':3, 'title':'Stock Market', 'author':'Sachin Gupta','rating':4.5},
    {'id':4, 'title':'FastAPI-Full Stack', 'author':'Sam','rating':5},
     {'id':5, 'title':'Engineer-?', 'author':'Sachin Gupta','rating':4.5},
]


@app.get('/book')
def home():
    return BOOKS

book_author=[]
@app.get('/book/author') 
def get_book_by_author(author: str ): # query Parameter
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            print("..", book.get('author'))
            print("....................",book['author'])
            # book_author.append(book)
            # print(book_author)
            # return book_author
            return book

@app.get('/book/{title}') # Path parameter
def get_book_by_title(title: str):
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold():
            return book
        

