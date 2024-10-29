from openpyxl.styles.builtins import title


class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        type = f"Book List: \n{"-" * 40}\n"
        title = f"{'Book Name': <11} | {'Author': <11} | {'Pages': <11}\n"
        infor = f"{self.name: >10} | {self.author: >10} | {self.page_count}\n"
        return type+title+infor

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        type = f"Magazine List: \n{"-" * 40}\n"
        title = f"{'Name': <11} | {'Chief Editor'} \n"
        infor = f"{self.name: >10} | {self.chief_editor: >10}\n"
        return type+title+infor

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



