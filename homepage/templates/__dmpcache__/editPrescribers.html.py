# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554747794.2162151
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/editPrescribers.html'
_template_uri = 'editPrescribers.html'
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container-fluid">\r\n    <div class="row content">\r\n        <div class="col-sm-3">\r\n            <h4>List all prescibers here they could edit</h4>           \r\n    \r\n            <ul>\r\n                <li>presciber</li>\r\n                <li>presciber</li>\r\n                <li>presciber</li>\r\n                <li>presciber</li>\r\n            </ul>\r\n    \r\n        </div>\r\n        <div class="col-sm-9">\r\n            <div class="content">\r\n                <div class="wrapper">\r\n                    <div id="formContent"> \r\n                        <div>\r\n                            <p></p>\r\n                        </div>\r\n                        <form method="POST">\r\n                            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
        __M_writer('\r\n                            <input type="submit" value="Submit">\r\n                        </form>                   \r\n                                                            \r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n\r\n    </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/editPrescribers.html", "uri": "editPrescribers.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "48": 3, "56": 3, "57": 25, "58": 25, "64": 58}}
__M_END_METADATA
"""
