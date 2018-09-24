import json
from operator import itemgetter

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def start():

    # Open the list as json to identify it as dictionary
    with open("bookdb", "r") as bookDB:
        bookList = json.load(bookDB)

    print("What would you like to do?\n\n\t[A] List books by author\n\t[B] List "
        "books by title\n\t[C] Add a new book\n\t[Q] Quit")

    action = input(">")

    if action.lower() == "a":
        sortedBookList = sorted(bookList, key=itemgetter("author"))
        print("\n***************************\n")
        for i in range(len(bookList)):
            print((bcolors.OKGREEN + sortedBookList[i].get("author")+" - "
                +sortedBookList[i].get("title") + bcolors.ENDC))
        print(bcolors.OKBLUE + "\nYou have read %s books in total" 
            % len(bookList) + bcolors.ENDC)
        print("\n***************************\n")
        start()

    elif action.lower() == "b":
        sortedBookList = sorted(bookList, key=itemgetter("title"))
        print("\n***************************\n")
        for i in range(len(bookList)):
            print(bcolors.OKGREEN + sortedBookList[i].get("title")+" - "
                +sortedBookList[i].get("author") + bcolors.ENDC)
        print(bcolors.OKBLUE + "\nYou have read %s books in total" 
            % len(bookList) + bcolors.ENDC)
        print("\n***************************\n")
        start()

    elif action.lower() == "c":
        print("Who is the author?")
        author = input(">")
        print("What is the title?")
        title = input(">")
        with open("bookdb", "w") as bookDB:
            bookList.append({"author": author, "title": title})
            bookDB.write(json.dumps(bookList))
        print("All done! What do you want to do next?")
        start()

    elif action.lower() == "q":
        quit()

    else:
        print("Not an option -> quit()")
        quit()

start()