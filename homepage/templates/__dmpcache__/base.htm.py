# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555005576.9637246
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>OpioInfo</title>\r\n        <link rel="icon" href="/static/homepage/media/3b375d48-0186-450c-aa3c-e7bbf013b0de.png/">\r\n\r\n')
        __M_writer('        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">\r\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>\r\n\r\n\r\n        \r\n        <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n\r\n        <header>\r\n            <div class="nav navbar-default custom-nav justify-content-between">\r\n                <div>            \r\n                    <img style="width: 4rem; height: 4rem;" src="/static/homepage/media/3b375d48-0186-450c-aa3c-e7bbf013b0de.png/"/>\r\n                </div>   \r\n                    <li class="nav-item active">\r\n                        <a class="btn btn-outline-primary" href="/homepage/index/">Home <span class="sr-only">(current)</span></a>\r\n                    </li>\r\n')
        if request.user.is_authenticated:
            __M_writer('                        <li class="nav-item">\r\n                            <a class="btn btn-outline-primary" href="/homepage/main/">Main Page</a>\r\n                        </li>\r\n')
            if request.user.has_perm('auth.change_user'):
                __M_writer('                            <li class="nav-item">\r\n                                <a class="btn btn-outline-primary" href="/homepage/editPrescribers/">Edit Prescribers</a>\r\n                            </li>\r\n')
            if request.user.has_perm('auth.view_analytics'):
                __M_writer('                            <li class="nav-item">\r\n                                <a class="btn btn-outline-primary" href="/homepage/analytics/">Analytics</a>\r\n                            </li>\r\n')
        else:
            __M_writer('                        <li class="nav-item">\r\n                            <a class="nav-link" href=""></a>\r\n                        </li>\r\n                        <li class="nav-item">\r\n                            <a class="nav-link" href=""></a>\r\n                        </li>\r\n')
        __M_writer('\r\n')
        if request.user.is_authenticated:
            __M_writer('                        <div>\r\n                            <a class="btn btn-primary" href="/homepage/logout/" role="button">Logout</a>\r\n                        </div>\r\n')
        else:          
            __M_writer('                        <div>\r\n                            <a class="btn btn-primary" href="/homepage/login/" role="button">Login</a>\r\n                        </div>\r\n')
        __M_writer('            </div> \r\n        </header>\r\n\r\n        <main>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n        <footer>\r\n                <div>\r\n                    <a class="btn btn-primary" style="opacity: 0;" href="/homepage/easterEgg/" role="button">EasterEgg</a>\r\n                </div>\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                Site content goes here in sub-templates.\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "27": 2, "28": 11, "29": 21, "30": 22, "31": 22, "32": 35, "33": 36, "34": 39, "35": 40, "36": 44, "37": 45, "38": 49, "39": 50, "40": 57, "41": 58, "42": 59, "43": 62, "44": 63, "45": 67, "50": 73, "56": 71, "62": 71, "68": 62}}
__M_END_METADATA
"""
