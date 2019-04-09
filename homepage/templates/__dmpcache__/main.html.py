# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554830388.025133
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/main.html'
_template_uri = 'main.html'
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
        prescribers = context.get('prescribers', UNDEFINED)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        opioids = context.get('opioids', UNDEFINED)
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
        prescribers = context.get('prescribers', UNDEFINED)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        opioids = context.get('opioids', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n    <div class="row content">\r\n      <div class="col-sm-6">\r\n        <h4>Prescribers</h4>\r\n        \r\n')
        if request.user.has_perm('auth.can_search'):
            __M_writer('            <div class="input-group">\r\n                <input type="text" class="form-control" id="prescriberInput" placeholder="Search Prescribers..">\r\n                <span class="input-group-btn">\r\n                    <button class="btn btn-primary" id="prescriberBtn">Search</button>\r\n                </span>\r\n            </div>\r\n')
        __M_writer('        \r\n\r\n        <table class="table table-striped table-bordered table-hover">\r\n                <caption style="caption-side: top">*Only the top 100 Prescribers are shown</caption>\r\n                <thead class="thead-dark">\r\n                    <tr>\r\n                        <th>Name</th>\r\n                        <th>Specialty</th>\r\n                        <th>Total Prescriptions</th>                       \r\n                    </tr>\r\n                </thead>\r\n                <tbody>\r\n')
        for i in range (len(prescribers)):
            __M_writer('                    \r\n                        <tr> \r\n')
            if request.user.has_perm('homepage.view_doctor'):
                __M_writer("                                <td><a href='/homepage/prescriberDetails/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].DoctorID ))
                __M_writer("/'> ")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Fname ))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Lname ))
                __M_writer('</a>  </td>                     \r\n')
            else:
                __M_writer("                                <td><a href='/homepage/prescriberDetails/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].DoctorID ))
                __M_writer("/'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].DoctorID ))
                __M_writer('</a></td>\r\n')
            __M_writer('                            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Specialty ))
            __M_writer('</td>\r\n                            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].TotalPrescriptions ))
            __M_writer('</td>    \r\n                                    \r\n                        </tr>   \r\n                        \r\n')
        __M_writer('                </tbody>\r\n    \r\n            </table>\r\n\r\n\r\n      </div>\r\n  \r\n      <div class="col-sm-6">\r\n            <h4>Drugs</h4>\r\n\r\n')
        if request.user.has_perm('auth.can_search'):
            __M_writer('                <div class="input-group">\r\n                    <input type="text" class="form-control" id="drugInput" placeholder="Search Drugs..">\r\n                    <span class="input-group-btn">\r\n                        <button class="btn btn-primary" id="drugBtn">Search</button>\r\n                    </span>\r\n                </div>\r\n')
        __M_writer('\r\n            <table class="table table-striped table-bordered table-hover">\r\n                    <caption style="caption-side: top">&nbsp;</caption>\r\n                    <thead class="thead-dark">\r\n                        <tr>\r\n                            <th>Name</th>\r\n                            <th>Is Opioid</th>                  \r\n                        </tr>\r\n                    </thead>\r\n                    <tbody>\r\n')
        for i in range (len(opioids)):  
            __M_writer("                        <tr> \r\n                            <td><a href='/homepage/drugDetails/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( opioids[i].id ))
            __M_writer("/'>")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( opioids[i].DrugName ))
            __M_writer('</a></td>                     \r\n                            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( opioids[i].IsOpioid ))
            __M_writer('</td>           \r\n                        </tr>          \r\n')
        __M_writer('                    </tbody>\r\n        \r\n                </table>\r\n\r\n      </div>\r\n    </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/main.html", "uri": "main.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "52": 3, "64": 3, "65": 10, "66": 11, "67": 18, "68": 30, "69": 31, "70": 33, "71": 34, "72": 34, "73": 34, "74": 34, "75": 34, "76": 34, "77": 34, "78": 35, "79": 36, "80": 36, "81": 36, "82": 36, "83": 36, "84": 38, "85": 38, "86": 38, "87": 39, "88": 39, "89": 44, "90": 54, "91": 55, "92": 62, "93": 72, "94": 73, "95": 74, "96": 74, "97": 74, "98": 74, "99": 75, "100": 75, "101": 78, "107": 101}}
__M_END_METADATA
"""
