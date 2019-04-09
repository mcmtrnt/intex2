# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554852253.1489162
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/analytics.html'
_template_uri = 'analytics.html'
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
        def content():
            return render_content(context._locals(__M_locals))
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
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('auth.view_analytics'):
            __M_writer('    <div class="container-fluid">\r\n        <div class="row content">\r\n            <div class="col-sm-3">\r\n                <h4>Available Analysis:</h4>\r\n                <ul>\r\n                    <li><a href=\'/homepage/highRiskPrescribers/\'>High Risk Prescribers</a></li>\r\n                    <li><a href=\'/homepage/amIHighRisk/\'>Am I High Risk</a></li>\r\n                    <li><a href=\'/homepage/similarPrescribers/\'>Find Similar Prescribers</a></li>\r\n                    <li><a href=\'/homepage/visualizations/\'>visualizations</a></li>\r\n                </ul>\r\n        \r\n            </div>\r\n        \r\n            <div class="col-sm-9">\r\n\r\n                <h4>Use the options on the left to view analytics and visualizations regarding opioid prescriptions</h4>\r\n\r\n            </div>\r\n\r\n        </div>\r\n    </div>\r\n')
        else:
            __M_writer('    <h4>You are not authorized to view Analytics</h4>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/analytics.html", "uri": "analytics.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "47": 3, "54": 3, "55": 4, "56": 5, "57": 26, "58": 27, "59": 29, "65": 59}}
__M_END_METADATA
"""