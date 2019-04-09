# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554833281.038983
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/main.drugs.html'
_template_uri = 'main.drugs.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        opioids = context.get('opioids', UNDEFINED)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        __M_writer('\r\n\r\n    ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n    \r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        opioids = context.get('opioids', UNDEFINED)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n        \r\n    <table class="table table-striped table-bordered table-hover">\r\n            <caption style="caption-side: top">&nbsp;</caption>\r\n            <thead class="thead-dark">\r\n                <tr>\r\n                    <th>Name</th>\r\n                    <th>Is Opioid</th>                  \r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n')
        for i in range (len(opioids)):  
            __M_writer("                <tr> \r\n                    <td><a href='/homepage/drugDetails/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( opioids[i].id ))
            __M_writer("/'>")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( opioids[i].DrugName ))
            __M_writer('</a></td>                     \r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( opioids[i].IsOpioid ))
            __M_writer('</td>           \r\n                </tr>          \r\n')
        __M_writer('            </tbody>\r\n    \r\n        </table>\r\n       \r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/main.drugs.html", "uri": "main.drugs.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "41": 2, "42": 4, "43": 4, "53": 6, "63": 6, "64": 17, "65": 18, "66": 19, "67": 19, "68": 19, "69": 19, "70": 20, "71": 20, "72": 23, "78": 72}}
__M_END_METADATA
"""
