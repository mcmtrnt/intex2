# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554919546.9432492
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/addDrug.html'
_template_uri = 'addDrug.html'
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        doctor = context.get('doctor', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        doctor = context.get('doctor', UNDEFINED)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('auth.change_user'):
            __M_writer('    <div class="container-fluid">\r\n        <div class="row content">\r\n\r\n            <div class="col-sm-12">\r\n                <div class="content">\r\n                    <div class="wrapper">\r\n                        <div id="formContent"> \r\n                            <div>\r\n                                <p>Add a new Drug for ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.Lname ))
            __M_writer('</p>\r\n                            </div>\r\n                            <form method="POST">\r\n                                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
            __M_writer('\r\n                                <input type="submit" value="Add">\r\n                            </form>                   \r\n                                                                \r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n\r\n\r\n        </div>\r\n    </div>\r\n')
        else:
            __M_writer('    <div>\r\n        <p>\r\n            You are not authorized to edit prescribers\r\n        </p>\r\n    </div>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/addDrug.html", "uri": "addDrug.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "50": 3, "60": 3, "61": 4, "62": 5, "63": 13, "64": 13, "65": 13, "66": 13, "67": 16, "68": 16, "69": 28, "70": 29, "71": 35, "77": 71}}
__M_END_METADATA
"""
