# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554860678.0087776
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/main.prescribers.html'
_template_uri = 'main.prescribers.html'
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
        len = context.get('len', UNDEFINED)
        request = context.get('request', UNDEFINED)
        range = context.get('range', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
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
        len = context.get('len', UNDEFINED)
        request = context.get('request', UNDEFINED)
        range = context.get('range', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    \r\n<table class="table table-striped table-bordered table-hover">\r\n        <caption style="caption-side: top">*Only the top 100 Prescribers are shown</caption>\r\n        <thead class="thead-dark">\r\n            <tr>\r\n                <th>Name</th>\r\n                <th>Specialty</th>\r\n                <th>Total Prescriptions</th>                       \r\n            </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        for i in range (len(prescribers)):
            __M_writer('                    \r\n                <tr> \r\n')
            if request.user.has_perm('homepage.view_doctor'):
                __M_writer("                        <td><a href='/homepage/prescriberDetails/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].DoctorID ))
                __M_writer("/'> ")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Fname ))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Lname ))
                __M_writer('</a>  </td>                     \r\n')
            else:
                __M_writer("                        <td><a href='/homepage/prescriberDetails/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].DoctorID ))
                __M_writer("/'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].DoctorID ))
                __M_writer('</a></td>\r\n')
            __M_writer('                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Specialty ))
            __M_writer('</td>\r\n                    <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].TotalPrescriptions ))
            __M_writer('</td>    \r\n                            \r\n                </tr>   \r\n                \r\n')
        __M_writer('        </tbody>\r\n\r\n    </table>\r\n   \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/main.prescribers.html", "uri": "main.prescribers.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "42": 3, "43": 3, "53": 5, "64": 5, "65": 17, "66": 18, "67": 20, "68": 21, "69": 21, "70": 21, "71": 21, "72": 21, "73": 21, "74": 21, "75": 22, "76": 23, "77": 23, "78": 23, "79": 23, "80": 23, "81": 25, "82": 25, "83": 25, "84": 26, "85": 26, "86": 31, "92": 86}}
__M_END_METADATA
"""
