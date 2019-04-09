# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554830392.4007602
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
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        request = context.get('request', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        drugAvg = context.get('drugAvg', UNDEFINED)
        mydrugs = context.get('mydrugs', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        request = context.get('request', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
        def content():
            return render_content(context)
        drugAvg = context.get('drugAvg', UNDEFINED)
        mydrugs = context.get('mydrugs', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n        <div class="row content">\r\n          <div class="col-sm-3">\r\n')
        if request.user.has_perm('homepage.view_doctor'):
            __M_writer('                <h4><b>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Lname ))
            __M_writer('</b></h4>\r\n')
        else:
            __M_writer('                <h4><b>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.DoctorID ))
            __M_writer('</b></h4>\r\n')
        __M_writer('\r\n            <ul>\r\n                <li>Gender: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Gender ))
        __M_writer('</strong></li>\r\n                <li>Credentials: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Credentials ))
        __M_writer('</strong></li>\r\n                <li>Location: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.State ))
        __M_writer('</strong></li>\r\n                <li>Specialty: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Specialty ))
        __M_writer('</strong></li>\r\n            </ul>\r\n    \r\n          </div>\r\n      \r\n          <div class="col-sm-9">\r\n\r\n            <table class="table table-striped table-bordered table-hover">\r\n')
        if request.user.has_perm('homepage.view_doctor'):
            __M_writer('                    <caption style="caption-side: top">Drugs prescribed by ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Lname ))
            __M_writer(':</caption>\r\n')
        else:
            __M_writer('                    <caption style="caption-side: top">Drugs prescribed by ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.DoctorID ))
            __M_writer(':</caption>\r\n')
        __M_writer('                <thead class="thead-dark">\r\n                    <tr>\r\n                        <th>Name</th>\r\n')
        if request.user.has_perm('homepage.view_doctor'):
            __M_writer('                            <th>Qty prescribed by ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Lname ))
            __M_writer('</th>\r\n')
        else:
            __M_writer('                            <th>Qty prescribed by ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.DoctorID ))
            __M_writer('</th>\r\n')
        __M_writer('                        <th>Avg Qty prescribed by all doctors</th>                  \r\n                    </tr>\r\n                </thead>\r\n                <tbody>\r\n')
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
{"filename": "C:/Users/Trent/intex/homepage/templates/prescriberDetails.html", "uri": "prescriberDetails.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "54": 3, "68": 3, "69": 8, "70": 9, "71": 9, "72": 9, "73": 9, "74": 9, "75": 10, "76": 11, "77": 11, "78": 11, "79": 13, "80": 15, "81": 15, "82": 16, "83": 16, "84": 17, "85": 17, "86": 18, "87": 18, "88": 26, "89": 27, "90": 27, "91": 27, "92": 27, "93": 27, "94": 28, "95": 29, "96": 29, "97": 29, "98": 31, "99": 34, "100": 35, "101": 35, "102": 35, "103": 35, "104": 35, "105": 36, "106": 37, "107": 37, "108": 37, "109": 39, "110": 43, "111": 44, "112": 45, "113": 45, "114": 45, "115": 45, "116": 46, "117": 46, "118": 47, "119": 47, "120": 50, "126": 120}}
__M_END_METADATA
"""
