# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymssql


# class ComicPipeline(object):
#     def __init__(self):
#         self.f = open("comics_pipeline.json","w")
        
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + "\n"
#         self.f.write(line)
#         return item

#     def close_spider(self, spider):
#         self.f.close()

class ComicPipeline(object):
    def __init__(self):
        self.conn = pymssql.connect(host='localhost', user='sa', password='0000', database='practice2')
        self.cursor = self.conn.cursor()
        

    def process_item(self, item, spider):
        # self.cursor.execute("""
        # IF OBJECT_ID('persons2', 'U') IS NOT NULL
        #     DROP TABLE practice2;
        # CREATE TABLE practice2 (
        #     id INT NOT NULL,
        #     name VARCHAR(100),
        #     author VARCHAR(100),
        #     imgsrc VARCHAR(100),
        #     title VARCHAR(100),
        #     updatetime VARCHAR(100)             
        #     PRIMARY KEY(id)
        #     )
        #  """)
        self.cursor.execute("INSERT INTO practice2(author,imgsrc,title,updatetime,updateround,year,region,[index],category,updateto,idea) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['author'],item['imgsrc'],item['title'],item['updatetime'],item['updateround'],item['year'],item['region'],item['index'],item['category'],item['updateto'],item['idea']))
        
        self.conn.commit()
        # you must call commit() to persist your data if you don't set autocommit to True
        #region
        

#         self.cursor.execute("""CREATE TABLE practice2 (
#             id INT NOT NULL,
#             name VARCHAR(100),
#             author VARCHAR(100),
#             imgsrc VARCHAR(100),
#             title VARCHAR(100),
#             updatetime VARCHAR(100),
#             updateround VARCHAR(100),
#             year VARCHAR(100),
#             region VARCHAR(100),
#             index VARCHAR(100),
#             category VARCHAR(100),
#             updateto VARCHAR(100),
#             idea VARCHAR(100),
#             PRIMARY KEY(id)
#             )
#             """)
#         #self.cursor.execute("SELECT CAST(item['id'] AS int)")
        
        #try:
        #self.cursor.execute("INSERT INTO persons(id, name) VALUES (%d, %s)", item[id],item[author])
        #self.conn.commit()
       # except pymssql.Error,e:
           # print ("error")

        

# name = 'comics'
#     conn = pymssql.connect(host='localhost', user='sa', password='0000', database='1234')

#     cursor = conn.cursor()

#     # 新建、插入操作
#     cursor.execute("""
#     IF OBJECT_ID('persons', 'U') IS NOT NULL
#         DROP TABLE persons
#     CREATE TABLE persons (
#         id INT NOT NULL,
#         name VARCHAR(100),
#         salesrep VARCHAR(100),
#         PRIMARY KEY(id)
#     )
#     """)
#     cursor.executemany(
#         "INSERT INTO persons VALUES (%d, %s, %s)",
#         [(1, 'John Smith', 'John Doe'),
#         (2, 'Jane Doe', 'Joe Dog'),
#         (3, 'Mike T.', 'Sarah H.')])
#     # 如果没有指定autocommit属性为True的话就需要调用commit()方法
#     conn.commit()       