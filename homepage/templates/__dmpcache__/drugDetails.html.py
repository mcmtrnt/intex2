# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554768165.4188406
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
        prescribers = context.get('prescribers', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        range = context.get('range', UNDEFINED)
        myPrescribers = context.get('myPrescribers', UNDEFINED)
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
        prescribers = context.get('prescribers', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        range = context.get('range', UNDEFINED)
        myPrescribers = context.get('myPrescribers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n        <div class="row content">\r\n          <div class="col-sm-3">\r\n            <h4><b>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs.DrugName ))
        __M_writer('</b></h4>\r\n            <ul>\r\n')
        if drugs.IsOpioid == '0':
            __M_writer('              <li>Is Opioid: <strong>No</strong></li>\r\n')
        else:
            __M_writer('              <li>Is Opioid: <strong>Yes</strong></li>\r\n')
        __M_writer('            </ul>\r\n    \r\n          </div>\r\n      \r\n          <div class="col-sm-9">\r\n\r\n            <table class="table table-striped table-bordered table-hover">\r\n                <caption style="caption-side: top">Top 10 prescribers of ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs.DrugName ))
        __M_writer(':</caption>\r\n                <thead class="thead-dark">\r\n                    <tr>\r\n                        <th>Name</th>\r\n                        <th>Specialty</th> \r\n                        <th>Qty</th>                  \r\n                    </tr>\r\n                </thead>\r\n                <tbody>\r\n')
        for i in range (len(prescribers)):
            __M_writer('                    ')
            __M_writer("  \r\n                    <tr> \r\n                        <td><a href='/homepage/prescriberDetails/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( myPrescribers[i].DoctorID ))
            __M_writer("/'>")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( myPrescribers[i].Fname ))
            __M_writer('</a></td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( myPrescribers[i].Specialty ))
            __M_writer('</td>                     \r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Qty ))
            __M_writer('</td>\r\n        \r\n                    </tr>          \r\n')
        __M_writer('                </tbody>\r\n    \r\n            </table>\r\n\r\n    \r\n          </div>\r\n\r\n        </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/drugDetails.html", "uri": "drugDetails.html", "source_encoding": "utf-8", "line_map": {"18": 32, "20": 32, "33": 0, "46": 1, "56": 3, "68": 3, "69": 8, "70": 8, "71": 10, "72": 11, "73": 12, "74": 13, "75": 15, "76": 22, "77": 22, "78": 31, "79": 32, "80": 32, "81": 34, "82": 34, "83": 34, "84": 34, "85": 35, "86": 35, "87": 36, "88": 36, "89": 40, "95": 89}}
__M_END_METADATA
"""
