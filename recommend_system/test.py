import copy

dic = [
    {
        'les1ie': [
            {'book_name': 'harry', 'book_rating': 3, 'book_author': 'tom'},
            {'book_name': 'asdf', 'book_rating': 33, 'book_author': 'stven'},
        ],
    },
]
dic2 = {'book_name': 'aa', 'book_rating': 233, 'book_author': 'fven'}
# print(dic[0]['les1ie'][0])
# dic[0]['les1ie'][0]['book_name'] = 'test'
dic[0]['les1ie'].append(dic2)
# print dic
# print dic2.viewkeys()
# dic = {'a':'ba'}
# print dic.keys()
# li = [3,32]
# print len(li)
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


