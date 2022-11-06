class Manga:
    def __init__(self, manga_title, manga_author, price, copies):
        self.manga_title = manga_title
        self.manga_author = manga_author
        self.price = price
        self.copies = copies
class AnimeHub(Manga):
    def __init__(self, manga_title, manga_author, price, copies):
        Manga.__init__(self, manga_title, manga_author, price, copies)
    def gettitle(self):
        return self.manga_title
    def getauthor(self):
        return self.manga_author
    def getprice(self):
        return self.price
    def getcopies(self):
        return self.copies
    def borrow(self, copy):
        self.copies -= copy
    def returnmanga(self, copy):
        self.copies += copy
    def mangaborrow(self, copy):
        return self.borrow(copy)
    def mangareturn(self, copy):
        return self.returnmanga(copy)
    def __str__(self):
        return "manganame:{},mangaauthor:{},price:{},copies:{}".format(self.manga_title, self.manga_author, self.price, self.copies)

status = 1
mangalist = []
while status == 1:
    print("-"*60)
    print("Welcome to Manga Management System")
    print("-"*60)
    print("1. Add mangas\n2. Borrow mangas\n3. Display mangas\n4. Return books")
    c = int(input("Enter the choice: "))
    if c == 1:
        n = int(input("Enter the No. of Mangas: "))
        for i in range(n):
            manga_title = input("Enter the Manga name: ")
            manga_author = input("Enter the Author of the Manga: ")
            price = input("Enter the Manga price: ")
            copies = input("Enter the No. of copies: ")
            mangalist.append(AnimeHub(manga_title, manga_author, price, copies))
        print("Mangas are added")
    elif c == 2:
        manganame = input("Enter the Manga to be searched: ")
        flag = True
        if len(mangalist) != 0:
            for manga in mangalist:
                if manganame ==  manga.gettitle():
                    copy = int(input("Enter the number of copies to be borrowed: "))
                    print(manga.gettitle(), "is present")
                    manga.mangaborrow()
                break
            else:
                flag = False
        if flag == False:
            print(manga, "doesnt exist")
    elif c == 3:
        if len(mangalist) != 0:
            for manga in mangalist:
                print(manga)
        else:
            print("Manga not present")
    elif c == 4:
        manganame = input("Enter the Manga to be returned: ")
        flag = True
        if len(mangalist) != 0:
            for manga in mangalist:
                copy = int(input("Enter the number of copies to be returned: "))
                print(manga.gettitle(), "is returned")
                manga.mangareturn()
                break
            else:
                flag = False
        if flag == False:
            print(manga, "not exist")
    else:
        print("No Mangas present")
    print("Do you want to continue(1 = Yes and 2= No)")

