#!/usr/bin/python
# coding:utf-8

##############################################
# program for recommend book
# notice: write for python 2
#
###############################################


import copy
import random


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







# To get info in document and save to dict,
# input: filename
# return: tuple of all book list and user map books
def read_file(filename):
    f = open(filename, 'r')
    old_con = f.readlines()
    f.close()
    con = []
    for i in old_con:
        con.append(i.replace('\n', ''))
    reader_list = []

    for i in xrange(len(con)):
        if i % 4 == 0:
            reader_name = con[i]
        elif i % 4 == 1:
            book_name = con[i]
        elif i % 4 == 2:
            book_author = con[i]
        elif i % 4 == 3:
            book_rating = con[i]

        if not i % 4 and i > 1:
            dic = {
                'reader_name': reader_name,
                'book_name': book_name,
                'book_author': book_author,
                'book_rating': book_rating,
            }
            reader_list.append(dic)

        # convert book list to map of reader to books

    convert_list = copy.deepcopy(reader_list)
    # print convert_list
    reader_name = convert_list[0]['reader_name']
    reader_to_book = {
        convert_list[0]['reader_name']:
            [
                {
                    'book_name': convert_list[0]['book_name'],
                    'book_author': convert_list[0]['book_author'],
                    'book_rating': convert_list[0]['book_rating'],
                },
            ]
    }
    # print reader_to_book
    # remove the key which used just now
    convert_list.pop(0)

    for book in convert_list:
        flag = 0
        dic = {
            book['reader_name']:[
                {
                    'book_name':book['book_name'],
                    'book_author':book['book_author'],
                    'book_rating': book['book_rating']

                },
            ]
        }

        if book['reader_name'] in reader_to_book:
            reader_to_book[book['reader_name']].append(dic[book['reader_name']][0])

        else:
            reader_to_book.update(dic)



    # print(reader_to_book)
    # print(len(reader_to_book), len(reader_list))




    # reader_list is a dict of all book, reader_to_book is a map of reader to books
    return reader_list, reader_to_book


# 添加额外数据到字典中
def add_data(info):
    user = raw_input("user?")
    title = raw_input("title?")
    author = raw_input("author?")
    rating = raw_input("rating?")

    dic = {"book_rating": rating, "book_name": title, "book_author": author, "reader_name": user}
    info.append(dic)
    return info



# 遍历字典，获取最高分的作品
# loop all the dict to get the top rating book
# input: list of all books
# return: best_rating and rest_rating_book_name and all the rating of books
def get_top_rating(info):
    book_name = [{'book_name': info[0]['book_name'], 'book_rating':int(info[0]['book_rating']), 'book_amount': 1}, ]
    # print book_name
    # input()
    info.pop(0)

    for con in info:
        # print con, book_name
        flag = False
        for book_dic_order in range(len(book_name)):
            # print 123
            # input()

            # print book_dic_order, 'in book', book_name[book_dic_order]['book_name'],', in con ', con['book_name']

            # if it exists already, update its weight and amount
            if book_name[book_dic_order]['book_name'] == con['book_name']:
                # print book_dic
                # print type(book_name[book_dic_order]['book_rating'])

                book_name[book_dic_order]['book_rating'] = int(con['book_rating']) + int(book_name[book_dic_order]['book_rating'])
                book_name[book_dic_order]['book_amount'] = int(book_name[book_dic_order]['book_amount']) + 1
                # print 'change to ', book_name
                # print book_dic
                # input()
                flag = True


            # if this book doesn't exist, add a new record
            elif book_name[book_dic_order]['book_name'] != con['book_name'] and book_dic_order == len(book_name) -1 and not flag:
                dic = {'book_name': con['book_name'], 'book_rating': con['book_rating'], 'book_amount': 1}
                book_name.append(dic)
                # print 'append to', book_name

                # input()

        # print book_name

    # to get avg_rating of each books
    # print book_name
    best_rating = 0
    best_rating_book_name = ''
    book_avg_rating_list = {}
    for book in book_name:
        # print float(book['book_rating'])
        book_avg_rating = float(book['book_rating']) / book['book_amount']
        dic = {book['book_name']: book_avg_rating}
        book_avg_rating_list.update(dic)

        if book_avg_rating > best_rating:
            best_rating = book_avg_rating
            best_rating_book_name = book['book_name']
            # print best_rating

    # print best_rating, best_rating_book_name
    # print book_avg_rating_list

    return best_rating, best_rating_book_name, book_avg_rating_list



# To get closest users, calculator their distense
# input: customer, map of reader to books
# return: list of all recommend books
def get_closest_user(customer, reader_to_muti_book):
    if customer in reader_to_muti_book:
        sum = 0
        max_sum = 0
        best_close_dic = {}
        for reader in reader_to_muti_book:
            if reader == customer:
                break

            # convert customer,reader to list, then use "set" to get common book
            customer_book = {item['book_name'] for item in reader_to_muti_book[customer]}

            reader_book = {item['book_name'] for item in reader_to_muti_book[reader]}
            # print reader_book
            # print customer_book

            # use set to get
            common_book = reader_book & customer_book
            # print common_book


            # calc the distance of customer to each reader
            for common in common_book:
                # print common
                for each_reader_book in reader_to_muti_book[reader]:
                    if each_reader_book['book_name'] == common:
                        reader_rating = each_reader_book['book_rating']
                        for each_customer_book in reader_to_muti_book[customer]:
                            if each_customer_book['book_name'] == common:
                                customer_rating = each_customer_book['book_rating']

                                sum += int(reader_rating) * int(customer_rating)
                                # print 'sum: ', sum

                                break

            # dic = {reader: sum}
            # print dic
            if sum > max_sum:
                max_sum = sum
                best_close_dic = {reader: sum}
                # print dic
            sum = 0
            # input()




        # if did not get close reader
        if len(best_close_dic) == 0:
            return 0


        # get all positive rating book of closest reader
        best_close_reader = best_close_dic.keys()[0]
        # print best_close_reader
        best_close_common_book = {item['book_name'] for item in reader_to_muti_book[best_close_reader]}
        customer_book = {item['book_name'] for item in reader_to_muti_book[customer]}
        common_book = customer_book & best_close_common_book

        recommend_list = []
        for each_book in reader_to_muti_book[best_close_reader]:
            # print each_book['book_name'], each_book['book_rating']
            if each_book['book_name'] not in common_book and int(each_book['book_rating']) > 0:
                recommend_book = each_book['book_name'], each_book['book_author'], each_book['book_rating']
                recommend_list.append(recommend_book)
                # customer_book = { item['book_name'] for item in reader_to_muti_book[customer]}

        return recommend_list

    # 如果customer 不在列表里面，则随机返回rating 比较高的几本书
    # if customer not in that list, the return several high raiting book
    if customer not in reader_to_muti_book:
        # top_rating_list = get_top_rating(read_file('ratings.txt')[0])[2]
        # print top_rating_list
        reader_name = reader_to_muti_book.keys()
        book_list = []
        while len(book_list) < 11:
            random_num = random.randint(0, len(reader_name)-2)
            print random_num
            random_name = reader_name[random_num]
            print
            for book in reader_to_muti_book[random_name]:

                # input()
                if int(book['book_rating']) >= 3 and len(book_list) < 11:
                    book_info = book['book_name'], book['book_author'], book['book_rating']
                    book_list.append(book_info)

            return book_list








# loop for out put promote
def main():
    output = '''
Welcome to the CSC110 Book Recommender. Type the word in the
left column to do the action on the right.
recommend : recommend books for a particular user
best      : the book with the highest rating among all users
add       : add a new book
quit      : exit the program'''
    print (output)

    cmd = raw_input("next task? ")
    while cmd != 'quit':
        if cmd == 'recommend':
        # if cmd == 'r':
            user = raw_input('user?')
            info = read_file('ratings.txt')
            recommand_list = get_closest_user(user, info[1])
            print recommand_list
            input()
            for book in recommand_list:
                book_info = Review(book[0], book[1], book[2])

                print book_info.__str__()
            # for book_info in recommand_list:
            #     print 'Title: %s, rating = %s' % book_info

        if cmd == 'best':
            info = read_file('ratings.txt')
            best_book = get_top_rating(info[0])
            print "The highest rated book is:"
            print best_book[1]
            print 'with an overall score of %s' % best_book[0]

        if cmd == 'add':
            info = read_file('ratings.txt')
            add_data(info[0])

        cmd = raw_input("next task? ")

if __name__ == '__main__':
    main()




# info = read_file('ratings.txt')
# get_top_rating(info[0])
# get_closest_user('NauNu', info[1])