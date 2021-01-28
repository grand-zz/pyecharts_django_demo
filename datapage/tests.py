
# Create your views here.
import json
import MySQLdb
from random import randrange

from django.http import HttpResponse

from django.shortcuts import render



from pyecharts.charts import Bar,Page
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table





def table_base() -> Table:
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
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="Table")
    )
    return table

def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)
    page.add(
        table_base(),
    )
    page.render("datapage/page_simple_layout.html")

if __name__ == "__main__":
    page_simple_layout()