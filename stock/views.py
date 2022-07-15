import datetime
import json
import requests
from IPython.core.display import HTML
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .angel_api import *

class StockView(APIView):
    def get(self, request):
        data = request.data
        stock_check = {}
        stock_check["start_date"] = data.get('start_date', datetime.datetime.now().date())
        stock_check['end_date'] = data.get('start_date', datetime.datetime.now().date())
        stock_check['stock_code'] = data.get('stock_code')
        stock_check['exch_type'] = data.get('exch_type')
        stock_check['exch'] = data.get('exch')
        stock_check['interval'] = data.get('interval')
        graph_data = get_data_static()
        # graph_data = get_data(stock_check)
        # print(json.dumps(graph_data.to_dict()))
        # plot_graph(graph_data)
        # return HttpResponse( {"data": json.dumps(graph_data.to_dict())})
        #return render(request, "home/base.html", {"data": json.dumps(graph_data.to_dict())})
        return render(request, "home/index.html", {"plot_div": graph_data})