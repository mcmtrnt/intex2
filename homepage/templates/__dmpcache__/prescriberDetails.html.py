# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554768684.3163018
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
        drugAvg = context.get('drugAvg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        mydrugs = context.get('mydrugs', UNDEFINED)
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
        drugAvg = context.get('drugAvg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        def content():
            return render_content(context)
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        mydrugs = context.get('mydrugs', UNDEFINED)
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
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( mydrugs[i].id ))
            __M_writer("/'>")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs[i].DrugName ))
            __M_writer('</a></td>                     \r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs[i].Qty ))
            __M_writer('</td>\r\n                        <td>(not accurate yet) ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugAvg[i].Qty ))
            __M_writer('</td>           \r\n                    </tr>          \r\n')
        __M_writer('                </tbody>\r\n    \r\n            </table>\r\n\r\n            \r\n    \r\n          </div>\r\n\r\n        </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/prescriberDetails.html", "uri": "prescriberDetails.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "53": 3, "66": 3, "67": 8, "68": 8, "69": 8, "70": 8, "71": 11, "72": 11, "73": 12, "74": 12, "75": 13, "76": 13, "77": 14, "78": 14, "79": 22, "80": 22, "81": 22, "82": 22, "83": 26, "84": 26, "85": 26, "86": 26, "87": 31, "88": 32, "89": 33, "90": 33, "91": 33, "92": 33, "93": 34, "94": 34, "95": 35, "96": 35, "97": 38, "103": 97}}
__M_END_METADATA
"""
