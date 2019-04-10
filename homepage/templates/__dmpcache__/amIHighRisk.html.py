# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554856717.5203025
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/amIHighRisk.html'
_template_uri = 'amIHighRisk.html'
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
        form = context.get('form', UNDEFINED)
        atRisk = context.get('atRisk', UNDEFINED)
        chance = context.get('chance', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        atRisk = context.get('atRisk', UNDEFINED)
        chance = context.get('chance', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('auth.view_analytics'):
            __M_writer('    <div class="container-fluid">\r\n        <div class="row content">\r\n            <div class="col-sm-3">\r\n                <h4>Available Analysis:</h4>\r\n                <ul>\r\n                        <li><a href=\'/homepage/amIHighRisk/\'>Am I High Risk</a></li>\r\n')
            if request.user.has_perm('homepage.view_doctor'):
                __M_writer("                            <li><a href='/homepage/similarPrescribers/'>Find Similar Prescribers</a></li>\r\n")
            __M_writer('                        <li><a href=\'/homepage/visualizations/\'>Visualizations</a></li>\r\n                        <li><a href=\'/homepage/maps/\'>Map of Overall Prescriptions/Opiods</a></li>\r\n                        <li><a href=\'/homepage/mapDeaths/\'>Map of Opioid Related Deaths</a></li>\r\n                        <li><a href=\'/homepage/specialtyComparator/\'>Specialty Comparator</a></li>\r\n                </ul>\r\n        \r\n            </div>\r\n        \r\n            <div class="col-sm-6">\r\n                <div class="content">\r\n                    <div class="wrapper">\r\n                        <div id="formContent">\r\n                            <form method="POST">\r\n                                <div><p>Enter Prescriber Information</p></div>\r\n                                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
            __M_writer('\r\n                                <input type="submit" value="Predict">\r\n                                \r\n                                <div><p></p></div>\r\n                                \r\n                            </form> \r\n                        </div>\r\n                    </div>\r\n                </div>\r\n\r\n            </div>\r\n\r\n            <div class="col-sm-3">\r\n                <h4>Prediction:</h4>\r\n                <p>At risk: <strong>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( atRisk ))
            __M_writer('</strong></p>\r\n                <p>There is a <strong>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( chance ))
            __M_writer('%</strong> chance you will be at risk of prescribing opioids</p>\r\n                \r\n\r\n            </div>\r\n\r\n        </div>\r\n    </div>\r\n')
        else:
            __M_writer('    <h4>You are not authorized to view Analytics</h4>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/amIHighRisk.html", "uri": "amIHighRisk.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "51": 3, "62": 3, "63": 4, "64": 5, "65": 11, "66": 12, "67": 14, "68": 28, "69": 28, "70": 42, "71": 42, "72": 43, "73": 43, "74": 50, "75": 51, "76": 53, "82": 76}}
__M_END_METADATA
"""
