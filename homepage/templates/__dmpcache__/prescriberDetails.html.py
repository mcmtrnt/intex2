# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554762626.5431097
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/prescriberDetails.html'
_template_uri = 'prescriberDetails.html'
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
        prescriber = context.get('prescriber', UNDEFINED)
        self = context.get('self', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        prescriber = context.get('prescriber', UNDEFINED)
        self = context.get('self', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        range = context.get('range', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n        <div class="row content">\r\n          <div class="col-sm-3">\r\n            <h4><b>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Fname ))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Lname ))
        __M_writer('</b></h4>           \r\n\r\n            <ul>\r\n                <li>Gender: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Gender ))
        __M_writer('</strong></li>\r\n                <li>Credentials: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Credentials ))
        __M_writer('</strong></li>\r\n                <li>Location: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.State ))
        __M_writer('</strong></li>\r\n                <li>Specialty: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Specialty ))
        __M_writer('</strong></li>\r\n            </ul>\r\n    \r\n          </div>\r\n      \r\n          <div class="col-sm-9">\r\n\r\n            <table class="table table-striped table-bordered table-hover">\r\n                <caption style="caption-side: top">Drugs prescribed by ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Fname ))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Lname ))
        __M_writer(':</caption>\r\n                <thead class="thead-dark">\r\n                    <tr>\r\n                        <th>Name</th>\r\n                        <th>Qty prescribed by ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Fname ))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Lname ))
        __M_writer('</th>  \r\n                        <th>Avg Qty prescribed by all doctors</th>                  \r\n                    </tr>\r\n                </thead>\r\n                <tbody>\r\n')
        for i in range (len(drugs)):  
            __M_writer("                    <tr> \r\n                        <td><a href='/homepage/drugDetails/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs[i].DrugName ))
            __M_writer("/'>")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs[i].DrugName ))
            __M_writer('</a></td>                     \r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs[i].Qty ))
            __M_writer('</td>\r\n                        <td>(not accurate yet) ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs[i].Qty ))
            __M_writer('</td>           \r\n                    </tr>          \r\n')
        __M_writer('                </tbody>\r\n    \r\n            </table>\r\n\r\n            \r\n    \r\n          </div>\r\n\r\n        </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/prescriberDetails.html", "uri": "prescriberDetails.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "51": 3, "62": 3, "63": 8, "64": 8, "65": 8, "66": 8, "67": 11, "68": 11, "69": 12, "70": 12, "71": 13, "72": 13, "73": 14, "74": 14, "75": 22, "76": 22, "77": 22, "78": 22, "79": 26, "80": 26, "81": 26, "82": 26, "83": 31, "84": 32, "85": 33, "86": 33, "87": 33, "88": 33, "89": 34, "90": 34, "91": 35, "92": 35, "93": 38, "99": 93}}
__M_END_METADATA
"""
