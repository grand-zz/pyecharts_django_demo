
# Create your views here.
import json
import MySQLdb
from random import randrange

from django.http import HttpResponse
from pyecharts.commons.utils import JsCode
from django.shortcuts import render, redirect

from pyecharts.charts import Bar,Page
from pyecharts import options as opts

from pyecharts.components import Table


def table_base(rq) -> Table:
    table = Table()
    print ('111111111',rq)
    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [
        ["mc", 5905, 1857594, 1146.4],
        ["mc", 1295, 1158259, 600.5],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="Table")
    )
    return table

def page_default_layout(rq):
    page = Page(layout=Page.SimplePageLayout)
    print ('aa')
    page.add(
        table_base(rq),
    )
    page.render('templates/datapage/page_simple_layout.html')


def chart(request):
    request.encoding = 'utf-8'
    if 'rq1' in request.GET and request.GET['rq1']:
        message = '你搜索的内容为: ' + request.GET['rq1']
        rq1 = request.GET['rq1']
    print ('bb',rq1)
    page_default_layout(rq1)
    print ('cc')
    return render(request, 'datapage/page_simple_layout.html')

def index(request):
    return render(request, 'datapage/index.html')

