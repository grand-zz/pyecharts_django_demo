import json
import MySQLdb
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Bar,Grid
from pyecharts import options as opts

from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts


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


def grid_vertical() -> Grid:    # 垂直网格

    conn = MySQLdb.connect(host="10.101.192.43", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("select gzlx,count(1) as cnt from b_epos  where rq BETWEEN '2021.01.18' and '2021.01.24' group by gzlx")
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

        )

    conn = MySQLdb.connect(host="10.101.192.43", user="root", passwd="root", db="mysql", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("select gzlx,count(1) as cnt from b_epos  where rq BETWEEN '2021.01.11' and '2021.01.17' group by gzlx")
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
        d = (
            Bar()
            .add_xaxis(aa)
            .add_yaxis("商家A", bb)
            # .add_yaxis("商家B", bb)
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))

        )
    # table = Table()
    #
    # headers = ["City name", "Area", "Population", "Annual Rainfall"]
    # rows = [
    #     ["Brisbane", 5905, 1857594, 1146.4],
    #     ["Adelaide", 1295, 1158259, 600.5],
    #     ["Darwin", 112, 120900, 1714.7],
    #     ["Hobart", 1357, 205556, 619.5],
    #     ["Sydney", 2058, 4336374, 1214.8],
    #     ["Melbourne", 1566, 3806092, 646.9],
    #     ["Perth", 5386, 1554769, 869.4],
    # ]
    # table.add(headers, rows)
    # table.set_global_opts(
    #     title_opts=ComponentTitleOpts(title="Table-基本示例", subtitle="我是副标题支持换行哦")
    # )

    grid = (
        Grid()  # 上下图和左右图
            .add(chart=c, grid_opts=opts.GridOpts(pos_bottom="60%", width="38%"))
            .add(chart=d, grid_opts=opts.GridOpts(pos_top="60%", width="38%"))

            # 获取全局 options，JSON 格式（JsCode 生成的函数带引号，在前后端分离传输数据时使用）
            .dump_options_with_quotes()  # 官方解释：保留 JS 方法引号
    )
    return grid



class ChartView(APIView):
    def get(self, request, *args, **kwargs) :
        return JsonResponse(json.loads(grid_vertical()))


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/index.html").read())