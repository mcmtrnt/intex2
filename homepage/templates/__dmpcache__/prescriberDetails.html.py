# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554920863.3301194
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/prescriberDetails.html'
_template_uri = 'prescriberDetails.html'
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
        mydrugs = context.get('mydrugs', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        drugs = context.get('drugs', UNDEFINED)
        range = context.get('range', UNDEFINED)
        drugAvg = context.get('drugAvg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        len = context.get('len', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
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
        mydrugs = context.get('mydrugs', UNDEFINED)
        def content():
            return render_content(context)
        drugs = context.get('drugs', UNDEFINED)
        range = context.get('range', UNDEFINED)
        drugAvg = context.get('drugAvg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        len = context.get('len', UNDEFINED)
        prescriber = context.get('prescriber', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container-fluid">\r\n        <div class="row content">\r\n          <div class="col-sm-3">\r\n')
        if request.user.has_perm('homepage.view_doctor'):
            __M_writer('                <h4><b>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Lname ))
            __M_writer('</b></h4>\r\n')
        else:
            __M_writer('                <h4><b>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.DoctorID ))
            __M_writer('</b></h4>\r\n')
        __M_writer('\r\n            <ul>\r\n                <li>Gender: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Gender ))
        __M_writer('</strong></li>\r\n                <li>Credentials: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Credentials ))
        __M_writer('</strong></li>\r\n                <li>Location: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.State ))
        __M_writer('</strong></li>\r\n                <li>Specialty: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Specialty ))
        __M_writer('</strong></li>\r\n            </ul>\r\n\r\n')
        if request.user.has_perm('auth.view_analytics'):
            if request.user.has_perm('homepage.view_doctor'):
                __M_writer('                    <input type="text" class="form-control" style="display: none" id="prescriberInput" value="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescriber.DoctorID))
                __M_writer('">\r\n                    <input type="submit" value="See Related Doctors" id="seeRelated">\r\n')
        __M_writer('   \r\n            <ul id=\'relatedDoctors\'>\r\n                <li></li>\r\n            </ul>\r\n    \r\n          </div>\r\n      \r\n          <div class="col-sm-9">\r\n\r\n            <table class="table table-striped table-bordered table-hover">\r\n')
        if request.user.has_perm('homepage.view_doctor'):
            __M_writer('                    <caption style="caption-side: top">Drugs prescribed by ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Lname ))
            __M_writer(':</caption>\r\n')
        else:
            __M_writer('                    <caption style="caption-side: top">Drugs prescribed by ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.DoctorID ))
            __M_writer(':</caption>\r\n')
        __M_writer('                <thead class="thead-dark">\r\n                    <tr>\r\n                        <th>Name</th>\r\n')
        if request.user.has_perm('homepage.view_doctor'):
            __M_writer('                            <th>Qty prescribed by ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Fname ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.Lname ))
            __M_writer('</th>\r\n')
        else:
            __M_writer('                            <th>Qty prescribed by ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.DoctorID ))
            __M_writer('</th>\r\n')
        __M_writer('                        <th>Avg Qty prescribed by all doctors</th>                 \r\n                    </tr>\r\n                </thead>\r\n                <tbody>\r\n')
        for i in range (len(drugs)):  
            __M_writer("                    <tr> \r\n                        <td><a href='/homepage/drugDetails/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( mydrugs[i].id ))
            __M_writer("/'>")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs[i].DrugName ))
            __M_writer('</a></td>  \r\n\r\n                        <td>\r\n                            ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs[i].Qty ))
            __M_writer('\r\n                            <div style="float:right;"><a href=\'/homepage/editDrug/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.DoctorID ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs[i].DrugName ))
            __M_writer('/\'><button class="btn btn-primary" id="editBtn">Edit</button></a></div>    \r\n                            </td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugAvg[i].Qty ))
            __M_writer('</td>          \r\n                    </tr>          \r\n')
        __M_writer("                </tbody>\r\n    \r\n            </table>\r\n\r\n            <a href='/homepage/addDrug/")
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.DoctorID ))
        __M_writer('/\'><button class="btn btn-primary" id="addBtn">Add New Prescription</button></a>\r\n\r\n            \r\n    \r\n          </div>\r\n\r\n        </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/prescriberDetails.html", "uri": "prescriberDetails.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "54": 3, "68": 3, "69": 8, "70": 9, "71": 9, "72": 9, "73": 9, "74": 9, "75": 10, "76": 11, "77": 11, "78": 11, "79": 13, "80": 15, "81": 15, "82": 16, "83": 16, "84": 17, "85": 17, "86": 18, "87": 18, "88": 21, "89": 22, "90": 23, "91": 23, "92": 23, "93": 27, "94": 37, "95": 38, "96": 38, "97": 38, "98": 38, "99": 38, "100": 39, "101": 40, "102": 40, "103": 40, "104": 42, "105": 45, "106": 46, "107": 46, "108": 46, "109": 46, "110": 46, "111": 47, "112": 48, "113": 48, "114": 48, "115": 50, "116": 54, "117": 55, "118": 56, "119": 56, "120": 56, "121": 56, "122": 59, "123": 59, "124": 60, "125": 60, "126": 60, "127": 60, "128": 62, "129": 62, "130": 65, "131": 69, "132": 69, "138": 132}}
__M_END_METADATA
"""
