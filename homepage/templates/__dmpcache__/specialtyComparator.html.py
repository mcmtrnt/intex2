# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554916505.3679764
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/specialtyComparator.html'
_template_uri = 'specialtyComparator.html'
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        valueList = context.get('valueList', UNDEFINED)
        len = context.get('len', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        valueList = context.get('valueList', UNDEFINED)
        len = context.get('len', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('auth.view_analytics'):
            __M_writer('    <div class="container-fluid">\r\n        <div class="row content">\r\n            <div class="col-sm-3">\r\n                <h4>Available Analysis:</h4>\r\n                <ul>\r\n                    <li><a href=\'/homepage/amIHighRisk/\'>Am I High Risk</a></li>\r\n')
            if request.user.has_perm('homepage.view_doctor'):
                __M_writer("                        <li><a href='/homepage/similarPrescribers/'>Find Similar Prescribers</a></li>\r\n")
            __M_writer('                    <li><a href=\'/homepage/visualizations/\'>Individual Visualizations</a></li>\r\n                    <li><a href=\'/homepage/maps/\'>Map of Overall Prescriptions/Opiods</a></li>\r\n                    <li><a href=\'/homepage/mapDeaths/\'>Map of Opioid Related Deaths</a></li>\r\n                    <li><a href=\'/homepage/specialtyComparator/\'>Specialty Comparator</a></li>\r\n                    <li><a href=\'/homepage/specialtyVisualization/\'>Specialty Visualization</a></li>\r\n                    <li><a href=\'/homepage/prescribersVisualization/\'>Prescribers Visualization</a></li>\r\n                </ul>\r\n        \r\n            </div>\r\n        \r\n            <div class="col-sm-6">\r\n                    <caption style="caption-side: top">Enter a Prescriber\'s ID which specialty they relate to most</caption>\r\n                <div class="content">\r\n                    <div class="wrapper">\r\n                        <div id="formContent">    \r\n                                \r\n                            <form method="POST">\r\n                                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
            __M_writer('\r\n                                    <input type="submit" value="Predict">\r\n                                </form>   \r\n                                            \r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n\r\n            <div class="col-sm-3">\r\n                <h4>Most Similar Specialty:</h4>\r\n\r\n                <ul>\r\n')
            for i in range (3, len(valueList)):                
                __M_writer('                    <li>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( valueList[i] ))
                __M_writer('</li>                                                     \r\n')
            __M_writer('                </ul>                \r\n\r\n            </div>\r\n\r\n        </div>\r\n    </div>\r\n')
        else:
            __M_writer('    <h4>You are not authorized to view Analytics</h4>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/specialtyComparator.html", "uri": "specialtyComparator.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "52": 3, "64": 3, "65": 4, "66": 5, "67": 11, "68": 12, "69": 14, "70": 31, "71": 31, "72": 44, "73": 45, "74": 45, "75": 45, "76": 47, "77": 53, "78": 54, "79": 56, "85": 79}}
__M_END_METADATA
"""