class BookDAO:

    def __init__(self):
        self.books = [
            {
                "title": "Naked in Death",
                "author": "J.D. Robb"
            },
            {
                "title": "Paradise Lost",
                "author": "John Milton"
            }
        ]

    def get_books(self):
        return self.books

    def add_book(self, book):
        self.books.append(book)
