# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555030563.9002798
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div class="jumbotron jumbotron-fluid">\r\n        <div class="container">\r\n          <h1 class="display-4">Gain insight into the Opioid Crisis</h1>\r\n          <p class="lead">Use this site to view data and analytics about prescribers and opiods</p>\r\n')
        if request.user.is_authenticated:
            __M_writer('            <div>\r\n                <a class="btn btn-primary" href="/homepage/main/" role="button">Get Started</a>\r\n            </div>\r\n')
        else:          
            __M_writer('            <div>\r\n                <a class="btn btn-primary" href="/homepage/login/" role="button">Login</a>\r\n            </div>\r\n')
        __M_writer('        </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 21, "48": 3, "55": 3, "56": 9, "57": 10, "58": 13, "59": 14, "60": 18, "66": 60}}
__M_END_METADATA
"""
