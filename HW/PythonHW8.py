import sys


class Book:
    def __init__(self, title, author, pub_year, edition):
        self.title = title
        self.authors = []  # 初始化為 list

        authors_list = author.split(", ")  # 處理複數作者

        for author in authors_list:  # 處理單一作者
            name_parts = author.split()

            if len(name_parts) > 1:
                self.FirstName = name_parts[0]
                self.LastName = name_parts[-1]

            else:
                self.FirstName = name_parts[0]
                self.LastName = None

            self.authors.append(author)

        self.pub_year = pub_year
        self.edition = edition

    def __str__(self):
        """Format: `"Title: {title}; Authors: {authors};
        Year: {pub_year}; Edition: {edition}"`"""
        if (
            self.authors is not None
            and self.edition is not None
            and self.pub_year is not None
            and self.title is not None
        ):
            self.authors.sort()
            author_str = ", ".join(self.authors)
            return f"Title: {self.title}; Authors: {author_str}; Year: {self.pub_year}; Edition: {self.edition}"
        else:
            return "wrong input"

    def __lt__(self, other):
        if self.FirstName == other.FirstName:
            return self.LastName < other.LastName  # 小到大就是 <
        else:
            return self.FirstName < other.FirstName

    def add_author(self, author):
        """The {authors} section should be seperated by a comma and a space.
        The {authors} section should be sorted in alphabetical order."""

        author = author.strip()
        if author not in self.authors:
            self.authors.append(author)
        return self.authors

    def rm_author(self, author):
        if author in self.authors:
            self.authors.remove(author)

        else:
            pass

    def update_edition(self, edition):
        self.edition = edition.strip()

    def update_pubyear(self, year):
        self.pub_year = int(year)

    def update_title(self, title):
        self.title = title.strip()

    def print(self):
        print(self)


def main():
    books = []
    num_books = int(input())
    if input() == "---":
        for i in range(num_books):
            title = input()
            authors = input()
            publication_year = int(input())
            edition = input()
            book = Book(title, authors, publication_year, edition)
            books.append(book)
            if input() == "-":
                while True:
                    command = input()
                    if command == "---":
                        break
                    else:
                        command_parts = command.split()
                        action = command_parts[0]
                        argument = " ".join(command_parts[1:])

                        if action == "update_edition":
                            book.update_edition(argument)
                        elif action == "add_author":
                            book.add_author(argument)
                        elif action == "rm_author":
                            book.rm_author(argument)
                        elif action == "update_title":
                            book.update_title(argument)
                        elif action == "update_pubyear":
                            book.update_pubyear(argument)
                        elif action == "print":
                            book.print()


if __name__ == "__main__":
    main()

    # input = sys.stdin.read
    # data = input().split("___\n") # 返回的是一本書的基本資料，以及指令

    # books = []
    # for book_data in data[1:]:
    #     if not book_data.strip():
    #         continue

    #     sections = book_data.strip().split("\n_\n")
    #     book_info = sections[0]
    #     commands = sections[1]

    #     # First section
    #     title = book_info[0]
    #     authors = book_info[1]
    #     pub_year = int(book_info[2])
    #     edition = book_info[3]
    #     book = Book(title, authors, pub_year, edition)
    #     books.append(book)  # 對應上方空 list

    #     # Second section
    #     for command in commands:
    #         command_parts = command.split()
    #         action = command_parts[0]
    #         argument = command_parts[1:] if len(command_parts) > 1 else None

    #         if action == "update_edition":
    #             book.update_edition(argument)

    #         elif action == "add_author":
    #             book.add_author(argument)

    #         elif action == "rm_author":
    #             book.rm_author(argument)

    #         elif action == "update_title":
    #             book.update_title(argument)

    #         elif action == "update_pubyear":
    #             book.update_pubyear(int(argument))

    #         elif action == "print":
    #             print(book, flush=True)

    #         else:
    #             print("Invalid command")
