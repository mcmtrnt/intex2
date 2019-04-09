# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554852220.0681832
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/similarPrescribers.html'
_template_uri = 'similarPrescribers.html'
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
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        doctors = context.get('doctors', UNDEFINED)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        def content():
            return render_content(context)
        doctors = context.get('doctors', UNDEFINED)
        len = context.get('len', UNDEFINED)
        range = context.get('range', UNDEFINED)
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('auth.view_analytics'):
            __M_writer('    <div class="container-fluid">\r\n        <div class="row content">\r\n            <div class="col-sm-3">\r\n                <h4>Available Analysis:</h4>\r\n                <ul>\r\n                    <li><a href=\'/homepage/highRiskPrescribers/\'>High Risk Prescribers</a></li>\r\n                    <li><a href=\'/homepage/amIHighRisk/\'>Am I High Risk</a></li>\r\n                    <li><a href=\'/homepage/similarPrescribers/\'>Find Similar Prescribers</a></li>\r\n                </ul>\r\n        \r\n            </div>\r\n        \r\n            <div class="col-sm-6">\r\n                    <caption style="caption-side: top">Enter a Prescriber\'s ID to see similar Prescribers</caption>\r\n                <div class="content">\r\n                    <div class="wrapper">\r\n                        <div id="formContent">    \r\n                                \r\n                            <form method="POST">\r\n                                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
            __M_writer('\r\n                                    <input type="submit" value="Predict">\r\n                                </form>   \r\n                                            \r\n                        </div>\r\n                    </div>\r\n                </div>\r\n\r\n            </div>\r\n\r\n            <div class="col-sm-3">\r\n                <h4>Similar Prescribers:</h4>\r\n\r\n                <ul>\r\n')
            for i in range (len(doctors)):                
                __M_writer("                    <li><a href='/homepage/prescriberDetails/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctors[i].DoctorID ))
                __M_writer("/'>")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctors[i].Fname ))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctors[i].Lname ))
                __M_writer('</a></li>                                                     \r\n')
            __M_writer('                </ul>\r\n                \r\n\r\n            </div>\r\n\r\n        </div>\r\n    </div>\r\n')
        else:
            __M_writer('    <h4>You are not authorized to view Analytics</h4>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/similarPrescribers.html", "uri": "similarPrescribers.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "52": 3, "64": 3, "65": 4, "66": 5, "67": 24, "68": 24, "69": 38, "70": 39, "71": 39, "72": 39, "73": 39, "74": 39, "75": 39, "76": 39, "77": 41, "78": 48, "79": 49, "80": 51, "86": 80}}
__M_END_METADATA
"""
