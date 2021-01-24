from django.test import TestCase
import MySQLdb
from random import randrange
# Create your tests here.
conn = MySQLdb.connect(host="10.101.192.43", user="root", passwd="root", db="mysql", charset='utf8')
with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
    cursor.execute("select gzlx,count(1) as cnt from b_epos group by gzlx")
    students = cursor.fetchall()
    aa=[]
    bb=[]
    # print (students)
    # # print (type(students))
    # # print (students[0])
    # print(list(students))
    for student in students:
        # print (student)
        # print (student.get('gzlx'))
        # print (student.get('cnt'))
        # print (list(student))
        aa.append(student.get('gzlx'))
        bb.append(student.get('cnt'))
    print (aa)
    print (type(bb))
    print (bb)
print (type([randrange(0, 100) for _ in range(6)]))

