class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        return f"Book Name:{self.name} \nAuthor:{self.author} \nPages:{self.page_count} pages\n"

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        return f"Magazine Name:{self.name} \nChief Editor:{self.chief_editor}\n"


def main():
    publication_name = "Donald Duck"
    publication_chief_editor = "Aki Hyyppä"
    public_maga = Magazine(publication_name,publication_chief_editor)
    print("Magazine List:")
    print(public_maga.print_information())

    publication_name = "Donald Duck"
    publication_author = "Rosa Liksom"
    publication_pages = 192
    public_book = Book(publication_name,publication_author, publication_pages)
    print("Book List:")
    print(public_book.print_information())

if __name__ == "__main__":
    main()



