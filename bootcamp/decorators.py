#coding: utf-8
from django.http import HttpResponseBadRequest

# ajax: 将数据请求在后台执行，不干扰页面的展示与执行
def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()

        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
