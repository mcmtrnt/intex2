# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554765884.5221996
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/drugDetails.html'
_template_uri = 'drugDetails.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


from homepage import models as hmod 

from homepage import models as hmod 

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
        self = context.get('self', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        drugs = context.get('drugs', UNDEFINED)
        range = context.get('range', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        drugs = context.get('drugs', UNDEFINED)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n        <div class="row content">\r\n          <div class="col-sm-3">\r\n            <h4>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs.DrugName ))
        __M_writer('</h4>\r\n            <ul>\r\n                ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs.IsOpioid ))
        __M_writer('\r\n')
        if drugs.IsOpioid == '0':
            __M_writer('              <li>Is Opioid: No</li>\r\n')
        else:
            __M_writer('              <li>Is Opioid: Yes</li>\r\n')
        __M_writer('            </ul>\r\n    \r\n          </div>\r\n      \r\n          <div class="col-sm-9">\r\n\r\n            <table class="table table-striped table-bordered table-hover">\r\n                <caption style="caption-side: top">Top 10 prescribers of ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs.DrugName ))
        __M_writer(':</caption>\r\n                <thead class="thead-dark">\r\n                    <tr>\r\n                        <th>Name</th>\r\n                        <th>Specialty</th> \r\n                        <th>Qty</th>                  \r\n                    </tr>\r\n                </thead>\r\n                <tbody>\r\n')
        for i in range (len(prescribers)):
            __M_writer('                    ')
            __M_writer("  \r\n                    <tr> \r\n                        <td><a href='/homepage/prescriberDetails/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].id ))
            __M_writer("/'>")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].DoctorID ))
            __M_writer('</a></td>\r\n                        <td></td>                     \r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Qty ))
            __M_writer('</td>\r\n        \r\n                    </tr>          \r\n')
        __M_writer('                </tbody>\r\n    \r\n            </table>\r\n\r\n    \r\n          </div>\r\n\r\n        </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/drugDetails.html", "uri": "drugDetails.html", "source_encoding": "utf-8", "line_map": {"18": 33, "20": 33, "33": 0, "45": 1, "55": 3, "66": 3, "67": 8, "68": 8, "69": 10, "70": 10, "71": 11, "72": 12, "73": 13, "74": 14, "75": 16, "76": 23, "77": 23, "78": 32, "79": 33, "80": 33, "81": 35, "82": 35, "83": 35, "84": 35, "85": 37, "86": 37, "87": 41, "93": 87}}
__M_END_METADATA
"""
