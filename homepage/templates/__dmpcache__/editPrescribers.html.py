# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554820666.518587
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
        len = context.get('len', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        range = context.get('range', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
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
        len = context.get('len', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        range = context.get('range', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="container-fluid">\r\n    <div class="row content">\r\n        <div class="col-sm-3">\r\n            <h4>Prescribers you may edit:</h4> \r\n\r\n            \r\n            <div class="input-group">\r\n                <input type="text" class="form-control" id="prescriberInput" placeholder="Search..">\r\n                <span class="input-group-btn">\r\n                    <button class="btn btn-primary" id="prescriberBtn">Search</button>\r\n                </span>\r\n            </div>\r\n\r\n\r\n    \r\n            <ul>\r\n')
        for i in range (len(prescribers)):    
            __M_writer("                <li><a href='/homepage/editExistingPrescriber/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].DoctorID ))
            __M_writer("/'> ")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Lname ))
            __M_writer('</a></li>                     \r\n')
        __M_writer('            </ul>\r\n    \r\n        </div>\r\n        <div class="col-sm-9">\r\n            <div class="content">\r\n                <div class="wrapper">\r\n                    <div id="formContent"> \r\n                        <div>\r\n                            <p>Add a new Prescriber</p>\r\n                        </div>\r\n                        <form method="POST">\r\n                            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
        __M_writer('\r\n                            <input type="submit" value="Add">\r\n                        </form>                   \r\n                                                            \r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n\r\n    </div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/editPrescribers.html", "uri": "editPrescribers.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "51": 3, "62": 3, "63": 20, "64": 21, "65": 21, "66": 21, "67": 21, "68": 21, "69": 21, "70": 21, "71": 23, "72": 34, "73": 34, "79": 73}}
__M_END_METADATA
"""
