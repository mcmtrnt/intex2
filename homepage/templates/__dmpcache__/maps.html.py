# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554913969.071718
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/maps.html'
_template_uri = 'maps.html'
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
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n    <div class="row content">\r\n        <div class="col-sm-3">\r\n            <h4>Available Analysis:</h4>\r\n            <ul>\r\n                <li><a href=\'/homepage/amIHighRisk/\'>Am I High Risk</a></li>\r\n')
        if request.user.has_perm('homepage.view_doctor'):
            __M_writer("                    <li><a href='/homepage/similarPrescribers/'>Find Similar Prescribers</a></li>\r\n")
        __M_writer('                <li><a href=\'/homepage/visualizations/\'>Visualizations</a></li>\r\n                <li><a href=\'/homepage/maps/\'>Map of Overall Prescriptions/Opiods</a></li>\r\n                <li><a href=\'/homepage/mapDeaths/\'>Map of Opioid Related Deaths</a></li>\r\n                <li><a href=\'/homepage/specialtyComparator/\'>Specialty Comparator</a></li>\r\n                <li><a href=\'/homepage/specialtyVisualization/\'>Specialty Visualization</a></li>\r\n            </ul>\r\n    \r\n        </div>\r\n      \r\n        <div class="col-sm-9">\r\n\r\n                <div class=\'tableauPlaceholder\' id=\'viz1554854662881\' style=\'position: relative\'><noscript><a href=\'#\'><img alt=\' \' src=\'https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;In&#47;IntexII&#47;StatesAverageOverallPrescriptionsandAverageOpioidsPresicriptions&#47;1_rss.png\' style=\'border: none\' /></a></noscript><object class=\'tableauViz\'  style=\'display:none;\'><param name=\'host_url\' value=\'https%3A%2F%2Fpublic.tableau.com%2F\' /> <param name=\'embed_code_version\' value=\'3\' /> <param name=\'path\' value=\'views&#47;IntexII&#47;StatesAverageOverallPrescriptionsandAverageOpioidsPresicriptions?:embed=y&amp;:display_count=y&amp;publish=yes\' /> <param name=\'toolbar\' value=\'yes\' /><param name=\'static_image\' value=\'https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;In&#47;IntexII&#47;StatesAverageOverallPrescriptionsandAverageOpioidsPresicriptions&#47;1.png\' /> <param name=\'animate_transition\' value=\'yes\' /><param name=\'display_static_image\' value=\'yes\' /><param name=\'display_spinner\' value=\'yes\' /><param name=\'display_overlay\' value=\'yes\' /><param name=\'display_count\' value=\'yes\' /><param name=\'filter\' value=\'publish=yes\' /></object></div>                <script type=\'text/javascript\'>                    var divElement = document.getElementById(\'viz1554854662881\');                    var vizElement = divElement.getElementsByTagName(\'object\')[0];                    vizElement.style.width=\'100%\';vizElement.style.height=(divElement.offsetWidth*0.75)+\'px\';                    var scriptElement = document.createElement(\'script\');                    scriptElement.src = \'https://public.tableau.com/javascripts/api/viz_v1.js\';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>\r\n\r\n        </div>\r\n\r\n    </div>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/maps.html", "uri": "maps.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "47": 3, "54": 3, "55": 11, "56": 12, "57": 14, "63": 57}}
__M_END_METADATA
"""
