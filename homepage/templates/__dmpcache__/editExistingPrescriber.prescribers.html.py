# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554837538.6147847
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/editExistingPrescriber.prescribers.html'
_template_uri = 'editExistingPrescriber.prescribers.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        len = context.get('len', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        self = context.get('self', UNDEFINED)
        range = context.get('range', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
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
        prescribers = context.get('prescribers', UNDEFINED)
        self = context.get('self', UNDEFINED)
        range = context.get('range', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    \r\n    <ul>\r\n')
        for i in range (len(prescribers)):    
            __M_writer("            <li><a href='/homepage/editExistingPrescriber/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].DoctorID ))
            __M_writer("/'> ")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Lname ))
            __M_writer('</a></li>                     \r\n')
        __M_writer('    </ul>\r\n   \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/editExistingPrescriber.prescribers.html", "uri": "editExistingPrescriber.prescribers.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "41": 3, "42": 3, "52": 5, "62": 5, "63": 8, "64": 9, "65": 9, "66": 9, "67": 9, "68": 9, "69": 9, "70": 9, "71": 11, "77": 71}}
__M_END_METADATA
"""
