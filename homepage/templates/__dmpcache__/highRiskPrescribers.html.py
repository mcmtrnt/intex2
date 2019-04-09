# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554839878.6259995
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/highRiskPrescribers.html'
_template_uri = 'highRiskPrescribers.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n    <div class="row content">\r\n        <div class="col-sm-3">\r\n            <h4>Available Analysis:</h4>\r\n            <ul>\r\n                <li><a href=\'/homepage/highRiskPrescribers/\'>High Risk Prescribers</a></li>\r\n                <li><a href=\'/homepage/amIHighRisk/\'>Am I High Risk</a></li>\r\n                <li><a href=\'/homepage/similarPrescribers/\'>Find Similar Prescribers</a></li>\r\n            </ul>\r\n    \r\n        </div>\r\n      \r\n        <div class="col-sm-9">\r\n\r\n            <table class="table table-striped table-bordered table-hover">\r\n\r\n                <caption style="caption-side: top"></caption>\r\n\r\n                <thead class="thead-dark">\r\n                    <tr>\r\n                        <th></th>\r\n                    </tr>\r\n                </thead>\r\n\r\n                <tbody>\r\n                    <tr>\r\n                        <td></td>\r\n                    </tr>\r\n                </tbody>\r\n    \r\n            </table>\r\n\r\n        </div>\r\n\r\n    </div>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/highRiskPrescribers.html", "uri": "highRiskPrescribers.html", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "46": 3, "52": 3, "58": 52}}
__M_END_METADATA
"""
