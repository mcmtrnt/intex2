# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554837534.7540874
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/editExistingPrescriber.html'
_template_uri = 'editExistingPrescriber.html'
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
        len = context.get('len', UNDEFINED)
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        self = context.get('self', UNDEFINED)
        range = context.get('range', UNDEFINED)
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
        doctor = context.get('doctor', UNDEFINED)
        len = context.get('len', UNDEFINED)
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        prescribers = context.get('prescribers', UNDEFINED)
        self = context.get('self', UNDEFINED)
        range = context.get('range', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('auth.change_user'):
            __M_writer('    <div class="container-fluid">\r\n        <div class="row content">\r\n            <div class="col-sm-3">\r\n                <h4>Prescribers you may edit:</h4> \r\n\r\n')
            if request.user.has_perm('auth.can_search'):
                __M_writer('                    <div class="input-group">\r\n                        <input type="text" class="form-control" id="prescriberInput" placeholder="Search..">\r\n                        <span class="input-group-btn">\r\n                            <button class="btn btn-primary" id="prescriberBtn">Search</button>\r\n                        </span>\r\n                    </div>\r\n')
            __M_writer("\r\n\r\n        \r\n                <ul id='prescriberList'>\r\n")
            for i in range (len(prescribers)):    
                __M_writer("                    <li><a href='/homepage/editExistingPrescriber/")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].DoctorID ))
                __M_writer("/'> ")
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Fname ))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescribers[i].Lname ))
                __M_writer('</a></li>                     \r\n')
            __M_writer('                </ul>\r\n        \r\n            </div>\r\n            <div class="col-sm-9">\r\n                <div class="content">\r\n                    <div class="wrapper">\r\n                        <div id="formContent"> \r\n                            <div>\r\n                                <p>Edit ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.Lname ))
            __M_writer('</p>\r\n                            </div>\r\n                            <form method="POST">\r\n                                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form.as_table()))
            __M_writer('\r\n                                <input type="submit" value="Edit">\r\n                                <div>\r\n                                    <button class="btn btn-danger"><a href=\'/homepage/delete/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( doctor.DoctorID ))
            __M_writer("/'>Delete</a></button>\r\n                                </div>\r\n                                <div><p></p></div>\r\n                                \r\n                            </form>                   \r\n                                                                \r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n\r\n        </div>\r\n    </div>\r\n")
        else:
            __M_writer('    <div>\r\n        <p>\r\n            You are not authorized to edit prescribers\r\n        </p>\r\n    </div>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/editExistingPrescriber.html", "uri": "editExistingPrescriber.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "53": 3, "66": 3, "67": 4, "68": 5, "69": 10, "70": 11, "71": 18, "72": 22, "73": 23, "74": 23, "75": 23, "76": 23, "77": 23, "78": 23, "79": 23, "80": 25, "81": 33, "82": 33, "83": 33, "84": 33, "85": 36, "86": 36, "87": 39, "88": 39, "89": 52, "90": 53, "91": 59, "97": 91}}
__M_END_METADATA
"""
