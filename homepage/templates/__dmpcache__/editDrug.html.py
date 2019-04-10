# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554920882.2661228
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/editDrug.html'
_template_uri = 'editDrug.html'
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
        doctor = context.get('doctor', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        DrugName = context.get('DrugName', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        doctor = context.get('doctor', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        DrugName = context.get('DrugName', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('auth.change_user'):
            __M_writer('    <div class="container-fluid">\r\n        <div class="row content">\r\n\r\n            <div class="col-sm-12">\r\n                <div class="content">\r\n                    <div class="wrapper">\r\n                        <div id="formContent"> \r\n                            <div>\r\n                                <p>Edit the quantity of ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( DrugName ))
            __M_writer(' for ')
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
{"filename": "C:/Users/Trent/intex/homepage/templates/editDrug.html", "uri": "editDrug.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "51": 3, "62": 3, "63": 4, "64": 5, "65": 13, "66": 13, "67": 13, "68": 13, "69": 13, "70": 13, "71": 16, "72": 16, "73": 28, "74": 29, "75": 35, "81": 75}}
__M_END_METADATA
"""
