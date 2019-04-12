# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555040878.344026
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
        doctors = context.get('doctors', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        form = context.get('form', UNDEFINED)
        range = context.get('range', UNDEFINED)
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
        doctors = context.get('doctors', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        len = context.get('len', UNDEFINED)
        form = context.get('form', UNDEFINED)
        range = context.get('range', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('auth.view_analytics'):
            __M_writer('    <div class="container-fluid">\r\n        <div class="row content">\r\n            <div class="col-sm-3">\r\n                <h4>Available Analysis:</h4>\r\n                <ul>\r\n                    <li><a href=\'/homepage/highestOpioidPrescribers/\'>Highest Opioid Prescribers</a></li>\r\n                    <li><a href=\'/homepage/opioidVisualization/\'>Opioid/Prescriptions Visualization</a></li>\r\n                    <li><a href=\'/homepage/amIHighRisk/\'>Am I High Risk</a></li>\r\n')
            if request.user.has_perm('homepage.view_doctor'):
                __M_writer("                        <li><a href='/homepage/similarPrescribers/'>Find Similar Prescribers</a></li>\r\n                        <li><a href='/homepage/visualizations/'>Individual Visualizations</a></li>\r\n")
            __M_writer('                    <li><a href=\'/homepage/maps/\'>Map of Overall Prescriptions/Opiods</a></li>\r\n                    <li><a href=\'/homepage/mapDeaths/\'>Map of Opioid Related Deaths</a></li>\r\n                    <li><a href=\'/homepage/specialtyComparator/\'>Specialty Comparator</a></li>\r\n                    <li><a href=\'/homepage/specialtyVisualization/\'>Specialty Visualization</a></li>\r\n                    <li><a href=\'/homepage/prescribersVisualization/\'>Prescribers Visualization</a></li>\r\n                </ul>\r\n        \r\n            </div>\r\n        \r\n            <div class="col-sm-6">\r\n                    <caption style="caption-side: top">Enter a Prescriber\'s ID to see similar Prescribers</caption>\r\n                <div class="content">\r\n                    <div class="wrapper">\r\n                        <div id="formContent">    \r\n                                \r\n                            <form method="POST">\r\n                                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
            __M_writer('\r\n                                    <input type="submit" value="Predict">\r\n                                </form>   \r\n                                            \r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n\r\n            <div class="col-sm-3">\r\n                <h4>Similar Prescribers:</h4>\r\n\r\n                <ul>\r\n')
            for i in range (len(doctors)):     
                if i == 0:
                    __M_writer("                        <li><a href='/homepage/prescriberDetails/")
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctors[i].DoctorID ))
                    __M_writer("/'>Current Prescriber : <strong>")
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctors[i].Fname ))
                    __M_writer(' ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctors[i].Lname ))
                    __M_writer('</strong></a></li> \r\n')
                else:
                    __M_writer("                        <li><a href='/homepage/prescriberDetails/")
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctors[i].DoctorID ))
                    __M_writer("/'><strong>")
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctors[i].Fname ))
                    __M_writer(' ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctors[i].Lname ))
                    __M_writer('</strong></a></li> \r\n')
            __M_writer('                </ul>\r\n                \r\n\r\n            </div>\r\n\r\n        </div>\r\n    </div>\r\n')
        else:
            __M_writer('    <h4>You are not authorized to view Analytics</h4>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/similarPrescribers.html", "uri": "similarPrescribers.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "52": 3, "64": 3, "65": 4, "66": 5, "67": 13, "68": 14, "69": 17, "70": 33, "71": 33, "72": 46, "73": 47, "74": 48, "75": 48, "76": 48, "77": 48, "78": 48, "79": 48, "80": 48, "81": 49, "82": 50, "83": 50, "84": 50, "85": 50, "86": 50, "87": 50, "88": 50, "89": 53, "90": 60, "91": 61, "92": 63, "98": 92}}
__M_END_METADATA
"""
