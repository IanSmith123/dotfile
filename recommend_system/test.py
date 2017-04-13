

dic = [
    {
        'les1ie': [
            {'book_name': 'harry', 'book_rating': 3, 'book_author': 'tom'},
            {'book_name': 'asdf', 'book_rating': 33, 'book_author': 'stven'},
        ],
    },
]
print(dic[0]['les1ie'][0])
dic[0]['les1ie'][0]['book_name'] = 'test'
print dic[0]['les1ie'][0]['book_name']

t = 1
t+=2
print t