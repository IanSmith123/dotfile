#! coding:utf-8
import review



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

    return reader_list





# 添加额外数据到字典中
def add_data():
    pass


# 遍历字典，获取最高分的作品
def get_top_rating(info):
    book_name = [{'book_name': info[0]['book_name'], 'book_rating':int(info[0]['book_rating'])}, ]
    print book_name,type(book_name[0]['book_rating'])

    info.pop(0)

    for con in info:
        for book_dic_order in xrange(len(book_name)):
            # print 123
            if book_name[book_dic_order]['book_name'] == con['book_name']:
                # print book_dic
                # print type(book_name[book_dic_order]['book_rating'])
                book_name[book_dic_order]['book_rating'] = int(con['book_rating']) + int(book_name[book_dic_order]['book_rating'])

                # print book_dic
            else:
                dic = {'book_name': con['book_name'], 'book_rating': con['book_rating']}
                book_name.append(dic)
    print book_name





    pass


# 获取最距离最近的两个users
def get_closest_user(username):
    pass

# 循环输出提示以及选项
def main():
    pass

info = read_file('ratings-small.txt')
get_top_rating(info)