class Review:
    def __init__(self, title, author, rating):
        self.__title = title
        self.__author = author
        self.__rating = int(rating)

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_rating(self):
        return self.__rating

    def __str__(self):
        return ("Title: " + self.__title + " by " + self.__author +
                ", rating = " + str(self.__rating))
