#! coding:utf-8
import review
import copy



# 读取文件内容，存放在字典，
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

        # 将书籍列表转换成每个reader名字对应的字典

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
    # 移除刚刚手动添加的那个键值
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



    print(reader_to_book)
    print(len(reader_to_book), len(reader_list))



    # reader_list 返回时读取文本生成的字典， reader_to_book返回每个读者对应的书本的目录
    return reader_list, reader_to_book





# 添加额外数据到字典中
def add_data(info):
    user = input("user?")
    title = input("title?")
    author = input("author?")
    rating = input("rating?")

    dic = {"book_rating": rating, "book_name": title, "book_author": author, "reader_name": user}
    info.append(dic)
    return info




# 遍历字典，获取最高分的作品
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

            if book_name[book_dic_order]['book_name'] == con['book_name']:
                # print book_dic
                # print type(book_name[book_dic_order]['book_rating'])

                book_name[book_dic_order]['book_rating'] = int(con['book_rating']) + int(book_name[book_dic_order]['book_rating'])
                book_name[book_dic_order]['book_amount'] = int(book_name[book_dic_order]['book_amount']) + 1
                # print 'change to ', book_name
                # print book_dic
                # input()
                flag = True

            elif book_name[book_dic_order]['book_name'] != con['book_name'] and book_dic_order == len(book_name) -1 and not flag:
                dic = {'book_name': con['book_name'], 'book_rating': con['book_rating'], 'book_amount': 1}
                book_name.append(dic)
                # print 'append to', book_name

                # input()

        # print book_name
    # 计算每本书的平均得分
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

    return best_rating, best_rating_book_name,book_avg_rating_list




# 获取最距离最近的两个users, 计算每个user与其他user的距离
def get_closest_user(username, reader_to_muti_book):
    if username in reader_to_muti_book:
        sum = 0
        for book in reader_to_muti_book[username]:
            # TODO: 遍历每一个名字，找他们相似程度最大的一个
            reader_relation_rating = 0
            # TODO:尝试使用  set 来求两个读者之间的交叉部分
            for reader in reader_to_muti_book:
                for book_info in reader_to_muti_book[reader]:
                    if book['book_name'] == book_info['book_name']:
                        sum += int(book['book_rating']) * int(book_info['book_rating'])
                        print sum
                        # input()



    else:
        # TODO: 返回平均得分最高的那一个，直接调用前面写的函数
        pass



# 循环输出提示以及选项
def main():
    pass

info = read_file('ratings.txt')
get_top_rating(info[0])
get_closest_user('Cust10', info[1])