import json
import MySQLdb
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Bar
from pyecharts import options as opts


# def index(request):
#     conn = MySQLdb.connect(host="10.101.192.43", user="root", passwd="root", db="mysql", charset='utf8')
#     with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#         cursor.execute("SELECT id,clr,pwh,pp,gzlx,rq,sj,ms,clcs,wczt,syyqm,bz FROM b_epos ORDER BY rq,sj")
#         students = cursor.fetchall()
#     # print (students)
#     # print (type(students))
#     # aa=students
#     # request, 'student/index.html', {'students': students}
#     return render()


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def bar_base() -> Bar:
    conn = MySQLdb.connect(host="10.101.192.43", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("select gzlx,count(1) as cnt from b_epos group by gzlx")
        students = cursor.fetchall()
        aa = []
        bb = []
        # print (type(students))
        # print (students[0])
        for student in students:
            # print (student)
            # print (student.get('gzlx'))
            # print (student.get('cnt'))
            aa.append(student.get('gzlx'))
            bb.append(student.get('cnt'))
        # print (aa,bb)
        c = (
            Bar()
            .add_xaxis(aa)
            .add_yaxis("商家A", bb)
            # .add_yaxis("商家B", bb)
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
            .dump_options_with_quotes()
        )
    return c


class ChartView(APIView):
    def get(self, request, *args, **kwargs) :
        return JsonResponse(json.loads(bar_base()))


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/index.html").read())