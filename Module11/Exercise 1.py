class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        type = f"{"-" * 41}\n|{'Book List': ^40}|\n{"-" * 41}\n"
        title = f"|{'Book Name': ^14}|{'Author': ^14}|{'Pages': ^10}|\n"
        infor = f"|{self.name: ^14}|{self.author: ^14}|{self.page_count: ^10}|\n"
        close_line = f"{'-'*42}\n"
        return type+title+infor+close_line

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        type = f"{"-" * 41}\n|{'Magazine List': ^40}|\n{"-" * 41}\n"
        title = f"|{'Name': ^19}|{'Chief Editor': ^20}|\n"
        infor = f"|{self.name: ^19}|{self.chief_editor: ^20}|\n"
        close_line = f"{'-' * 42}\n"
        return type+title+infor+close_line

def main():
    publication_name = "Donald Duck"
    publication_chief_editor = "Aki Hyyppä"
    public_maga = Magazine(publication_name,publication_chief_editor)
    print(public_maga.print_information())

    publication_name = "Donald Duck"
    publication_author = "Rosa Liksom"
    publication_pages = 192
    public_book = Book(publication_name,publication_author, publication_pages)
    print(public_book.print_information())

if __name__ == "__main__":
    main()



