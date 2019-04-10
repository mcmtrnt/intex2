# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554938882.813487
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/highestOpioidPrescribers.html'
_template_uri = 'highestOpioidPrescribers.html'
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
        request = context.get('request', UNDEFINED)
        highest = context.get('highest', UNDEFINED)
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
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
        request = context.get('request', UNDEFINED)
        highest = context.get('highest', UNDEFINED)
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n    <div class="row content">\r\n        <div class="col-sm-3">\r\n            <h4>Available Analysis:</h4>\r\n            <ul>\r\n                <li><a href=\'/homepage/highestOpioidPrescribers/\'>Highest Opioid Prescribers</a></li>\r\n                <li><a href=\'/homepage/amIHighRisk/\'>Am I High Risk</a></li>\r\n')
        if request.user.has_perm('homepage.view_doctor'):
            __M_writer("                    <li><a href='/homepage/similarPrescribers/'>Find Similar Prescribers</a></li>\r\n                    <li><a href='/homepage/visualizations/'>Individual Visualizations</a></li>\r\n")
        __M_writer('                <li><a href=\'/homepage/maps/\'>Map of Overall Prescriptions/Opiods</a></li>\r\n                <li><a href=\'/homepage/mapDeaths/\'>Map of Opioid Related Deaths</a></li>\r\n                <li><a href=\'/homepage/specialtyComparator/\'>Specialty Comparator</a></li>\r\n                <li><a href=\'/homepage/specialtyVisualization/\'>Specialty Visualization</a></li>\r\n                <li><a href=\'/homepage/prescribersVisualization/\'>Prescribers Visualization</a></li>\r\n            </ul>\r\n    \r\n        </div>\r\n      \r\n        <div class="col-sm-9">\r\n\r\n            <table class="table table-striped table-bordered table-hover">\r\n\r\n                    <thead class="thead-dark">\r\n                        <tr>\r\n                            <th>DoctorID</th>\r\n                            <th>Number of Opioids Prescribed</th>\r\n                        </tr>\r\n                    </thead>\r\n                    <tbody>\r\n')
        for i in range(len(highest)):
            __M_writer("                        <tr> \r\n                            <td><a href='/homepage/prescriberDetails/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( highest[i].DoctorID ))
            __M_writer("/'>")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( highest[i].DoctorID ))
            __M_writer('</a></td>\r\n                            <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( highest[i].NumOpioids ))
            __M_writer('</td>\r\n                        </tr>          \r\n')
        __M_writer('                    </tbody>\r\n        \r\n                </table>\r\n\r\n\r\n        </div>\r\n\r\n    </div>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/highestOpioidPrescribers.html", "uri": "highestOpioidPrescribers.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "51": 3, "62": 3, "63": 12, "64": 13, "65": 16, "66": 36, "67": 37, "68": 38, "69": 38, "70": 38, "71": 38, "72": 39, "73": 39, "74": 42, "80": 74}}
__M_END_METADATA
"""
