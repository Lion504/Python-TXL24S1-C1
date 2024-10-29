class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"Book Name:{self.name}, Author:{self.author}, {self.page_count} pages.")

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"Magazine Name:{self.name}, Chief Editor:{self.chief_editor}")


def main():
    publication_name = "Donald Duck"
    publication_chief_editor = "Aki Hyyppä"
    public_maga = Magazine(publication_name,publication_chief_editor)
    public_maga.print_information()

    publication_name = "Donald Duck"
    publication_author = "Rosa Liksom"
    publication_pages = 192
    public_book = Book(publication_name,publication_author, publication_pages)
    public_book.print_information()

if __name__ == "__main__":
    main()



