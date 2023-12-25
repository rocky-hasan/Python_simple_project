def main():
    try:
        BookList = []
        with open('booklist.txt', 'r') as f:
            line = f.readline()
            while line:
                BookList.append(line.rstrip("\n").split(','))
                line = f.readline()
    except FileNotFoundError:
        print("File not Found")
        print("Start a new existing file")
        BookList = []

    choice = 0
    while choice != 4:
        print('*** Book Manager****')
        print("1) Add a Book")
        print("2) Search Book")
        print("3) Display Book")
        print("4) Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Add Book..")
            nBook = input("Enter the name of Book :")
            nAuthor = input("Enter the name of Author :")
            nPages = input("Enter the name of Pages :")
            BookList.append([nBook, nAuthor, nPages])
        if choice == 2:
            print('Looking for a Book: ')
            keyword = input("Enter the book name:")
            for book in BookList:
                if keyword in book:
                    print(book)
        if choice == 3:
            print("Display All Book")
            for i in range(len(BookList)):
                print(BookList[i])
        if choice == 4:
            print("Quit Program")
    print("Program Terminated")

    with open('booklist.txt', mode='w') as f:
        for book in BookList:
            f.write(','.join(book) + '\n')


if __name__ == '__main__':
    main()
