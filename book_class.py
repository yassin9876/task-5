class Book:
    def __init__(self,title , author ,isbn ):
        self.title =title
        self.author =author
        self.__isbn =isbn
        self.available= True
    def display_info(self):
            print(f"{self.title},{self.author},{self.__isbn},| Available:{self.available}")
            
