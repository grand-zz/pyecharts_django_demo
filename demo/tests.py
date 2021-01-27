# from django.test import TestCase
# import MySQLdb
# from random import randrange
# # Create your tests here.
# conn = MySQLdb.connect(host="10.101.192.43", user="root", passwd="root", db="mysql", charset='utf8')
# with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#     cursor.execute("select gzlx,count(1) as cnt from b_epos group by gzlx")
#     students = cursor.fetchall()
#     aa=[]
#     bb=[]
#     # print (students)
#     # # print (type(students))
#     # # print (students[0])
#     # print(list(students))
#     for student in students:
#         # print (student)
#         # print (student.get('gzlx'))
#         # print (student.get('cnt'))
#         # print (list(student))
#         aa.append(student.get('gzlx'))
#         bb.append(student.get('cnt'))
#     print (aa)
#     print (type(bb))
#     print (bb)
# print (type([randrange(0, 100) for _ in range(6)]))


from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts


table = Table()

headers = ["City name", "Area", "Population", "Annual Rainfall"]
rows = [
    ["Brisbane", 5905, 1857594, 1146.4],
    ["Adelaide", 1295, 1158259, 600.5],
    ["Darwin", 112, 120900, 1714.7],
    ["Hobart", 1357, 205556, 619.5],
    ["Sydney", 2058, 4336374, 1214.8],
    ["Melbourne", 1566, 3806092, 646.9],
    ["Perth", 5386, 1554769, 869.4],
]
table.add(headers, rows)
table.set_global_opts(
    title_opts=ComponentTitleOpts(title="Table-基本示例", subtitle="我是副标题支持换行哦")
)
table.render("table_base.html")
