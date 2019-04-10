# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554914282.6563933
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
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        myPrescribers = context.get('myPrescribers', UNDEFINED)
        len = context.get('len', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
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
        def content():
            return render_content(context)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        myPrescribers = context.get('myPrescribers', UNDEFINED)
        len = context.get('len', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n        <div class="row content">\r\n          <div class="col-sm-3">\r\n            <h4><b>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs.DrugName ))
        __M_writer('</b></h4>\r\n            <ul>\r\n')
        if drugs.IsOpioid == '0':
            __M_writer('              <li>Is Opioid: <strong>No</strong></li>\r\n')
        else:
            __M_writer('              <li>Is Opioid: <strong>Yes</strong></li>\r\n')
        __M_writer('            </ul>\r\n\r\n')
        if request.user.has_perm('auth.view_analytics'):
            __M_writer('              <input type="text" class="form-control" style="display: none" id="drugInput" value="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(drugs.DrugName))
            __M_writer('">\r\n              <input type="submit" value="See Related Drugs" id="seeRelated">\r\n')
        __M_writer('   \r\n            <ul id=\'relatedDrugs\'>\r\n                <li></li>\r\n            </ul>\r\n    \r\n          </div>\r\n      \r\n          <div class="col-sm-9">\r\n\r\n            <table class="table table-striped table-bordered table-hover">\r\n                <caption style="caption-side: top">Top 10 prescribers of ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs.DrugName ))
        __M_writer(':</caption>\r\n                <thead class="thead-dark">\r\n                    <tr>\r\n                        <th>Name</th>\r\n                        <th>Specialty</th> \r\n                        <th>Qty</th>                  \r\n                    </tr>\r\n                </thead>\r\n                <tbody>\r\n')
        for i in range (len(prescribers)):
            __M_writer('                    ')
            __M_writer('  \r\n                    <tr> \r\n')
            if request.user.has_perm('homepage.view_doctor'):
                __M_writer("                          <td><a href='/homepage/prescriberDetails/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( myPrescribers[i].DoctorID ))
                __M_writer("/'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( myPrescribers[i].Fname ))
                __M_writer('</a></td>\r\n')
            else:
                __M_writer("                          <td><a href='/homepage/prescriberDetails/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( myPrescribers[i].DoctorID ))
                __M_writer("/'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( myPrescribers[i].DoctorID ))
                __M_writer('</a></td>\r\n')
            __M_writer('                        <td>')
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
{"filename": "C:/Users/Trent/intex/homepage/templates/drugDetails.html", "uri": "drugDetails.html", "source_encoding": "utf-8", "line_map": {"18": 41, "20": 41, "33": 0, "47": 1, "57": 3, "70": 3, "71": 8, "72": 8, "73": 10, "74": 11, "75": 12, "76": 13, "77": 15, "78": 17, "79": 18, "80": 18, "81": 18, "82": 21, "83": 31, "84": 31, "85": 40, "86": 41, "87": 41, "88": 43, "89": 44, "90": 44, "91": 44, "92": 44, "93": 44, "94": 45, "95": 46, "96": 46, "97": 46, "98": 46, "99": 46, "100": 48, "101": 48, "102": 48, "103": 49, "104": 49, "105": 53, "111": 105}}
__M_END_METADATA
"""
