"""
Input Formats: 

    The first line contains a number representing the testcase count.

    The folllowing 4 lines contain the book's information.

    After that, the command lines will be given after a line of dash ("-"), 
    and end with a line of three dashes ("---").

Commands are as follows:

    `add_author {author}`

    `rm_author {author}`

    `update_edition {edition}`

    `update_pubyear {year}`

    `update_title {title}`

    `print`

Output Formats:

    Whenever the `print` command is given, the book's information should be printed.

# test case e.g.
      3
      ---
      Linear Algebra
      David Cherney, Tom Denton, Rohit Thomas, Hello World
      2013
      First
      -
      update_edtion Second
      add_author Andrew Waldron
      rm_author Hello World
      print
      ---
      Calculus
      Gilbert Strang, Hello World
      2004
      10th
      -
      print
      rm_author Hello World
      update_title Calculus 2
      update_pubyear 2012
      print
      ---
      Introduction to Probability
      Tim Cheney, David Kincaid, Hello World
      1993
      4th
      -
      add_author Andrew Waldron
      update_title Introduction to Probability and Statistics
      update_pubyear 2013
      update_edition 5th
      print
      ---
    
"""

class Book:
    def __init__(self, title, authors, pub_year, edition):
        self.title = title
        self.authors = [ ]  # 把 authors 處理成 list 
        authors_list = authors.split(", ") 
        for author in authors_list:
            name_parts = author.split(" ") # 單獨名字處理
            if len(name_parts) > 1:
                self.FirstName = name_parts[0]
                self.LastName = name_parts[-1]
            else:
                self.FirstName = name_parts[0]
                self.LastName = None
            self.authors.append(author)
        self.pub_year = pub_year
        self.edition = edition
    
    
    def add_author(self, author):
        if author not in self.authors:
            self.authors.append(author)
        return self.authors
    
    def rm_author(self, author):
        if author in self.authors:
            self.authors.remove(author)
        else:
            pass
        return self.authors
    
    def update_edition(self, edition):
        if edition != self.edition:
            self.edition = edition
        else:
            pass
    
    def update_pubyear(self, year):
        if year != self.pub_year:
            self.pub_year = year
        else:
            pass
    
    def update_title(self, title):
        if title != self.title:
            self.title = title
        else:
            pass
    
    def __str__(self):
        """Format: `"Title: {title}; Authors: {authors};
        Year: {pub_year}; Edition: {edition}"`"""
        
        if self.authors is not None and self.edition is not None and self.pub_year is not None and self.title is not None:
            self.authors.sort() # 先排序
            all_authors = ", ".join(self.authors) # turn a list into a single string --> for output format 
            return f"Title: {self.title}; Authors: {all_authors}; Year: {self.pub_year}; Edition: {self.edition}"

    
    def __lt__(self, other): # sort 中：名字要照字母排序( 小到大 )
        if self.FirstName == other.FirstName:
            return self.LastName < other.LastName
        else:
            return self.FirstName < other.FirstName
            
        
def main():
   
    num_books = int(input().strip())
    books = [] # 最後要來收集答案的 list 
    if input().strip() == "---": 
        for _ in range (num_books): # 總共做幾本書
            title = input()
            authors = input()
            pub_year = int(input())
            edtion = input()
            book = Book(title, authors, pub_year, edtion)
            books.append(book)
                
        if input().strip() == "-":
            while True:  # 如果還沒碰到下一個限制，就不斷執行這件事
                command = input().split(" ", 1)   ## 1 指定了分割次数为1，也就是说只会分割一次，即第一个空格之前的部分是命令，之后的部分是参数
            
                cmd = command[0]
                arg = command[1:] if len(command) > 1 else ""
                
                if cmd == "add_author":
                    book.add_author(arg)
                elif cmd == "rm_author":
                    book.rm_author(arg)
                elif cmd == "update_edition":
                    book.update_edition(arg)
                elif cmd == "update_pubyear":
                    book.update_pubyear(arg)
                elif cmd == "update_title":
                    book.update_title(arg)
                elif cmd == "print":
                    print(book)
                elif cmd == "---":
                    break           
                    
    
if __name__ == "__main__":
    main()
    # x = Book("Linear Algebra", "David Cherney, Tom Denton, Rohit Thomas, Hello World", 2013, "First")
    # x.add_author("Andrew Waldron")
    # x.rm_author("Hello World")
    # x.update_title("Calculus")
    # x.update_edition("2nd")
    # x.update_pubyear(2012)
    # print(x)
    