# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554938723.6115932
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
        prescriber = context.get('prescriber', UNDEFINED)
        self = context.get('self', UNDEFINED)
        drugAvg = context.get('drugAvg', UNDEFINED)
        mydrugs = context.get('mydrugs', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        extra = context.get('extra', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
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
        prescriber = context.get('prescriber', UNDEFINED)
        self = context.get('self', UNDEFINED)
        drugAvg = context.get('drugAvg', UNDEFINED)
        mydrugs = context.get('mydrugs', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        extra = context.get('extra', UNDEFINED)
        drugs = context.get('drugs', UNDEFINED)
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
        __M_writer('</strong></li>\r\n                <br>\r\n                <li>Total Prescriptions: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.TotalPrescriptions ))
        __M_writer('</strong></li>\r\n                <li>Number of Opioids Prescribed: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( extra.NumOpioids ))
        __M_writer('</strong></li>\r\n')
        if extra.AtRisk  == '1':
            __M_writer('                    <li>At Risk: <strong>Yes</strong></li>\r\n')
        else:
            __M_writer('                <li>At Risk: <strong>No</strong></li>\r\n')
        __M_writer('                <li>Prescriber Score: <strong>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( extra.PrescriberScore ))
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
            __M_writer('\r\n')
            if request.user.has_perm('auth.change_user'):
                __M_writer('                                <div style="float:right;"><a href=\'/homepage/editDrug/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.DoctorID ))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugs[i].DrugName ))
                __M_writer('/\'><button class="btn btn-primary" id="editBtn">Edit</button></a></div>    \r\n')
            __M_writer('                        </td>\r\n                        <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( drugAvg[i] ))
            __M_writer('</td>          \r\n                    </tr>          \r\n')
        __M_writer('                </tbody>\r\n    \r\n            </table>\r\n')
        if request.user.has_perm('auth.change_user'):
            __M_writer("                <a href='/homepage/addDrug/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( prescriber.DoctorID ))
            __M_writer('/\'><button class="btn btn-primary" id="addBtn">Add New Prescription</button></a>        \r\n')
        __M_writer('          </div>\r\n\r\n        </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/prescriberDetails.html", "uri": "prescriberDetails.html", "source_encoding": "utf-8", "line_map": {"29": 0, "45": 1, "55": 3, "70": 3, "71": 8, "72": 9, "73": 9, "74": 9, "75": 9, "76": 9, "77": 10, "78": 11, "79": 11, "80": 11, "81": 13, "82": 15, "83": 15, "84": 16, "85": 16, "86": 17, "87": 17, "88": 18, "89": 18, "90": 20, "91": 20, "92": 21, "93": 21, "94": 22, "95": 23, "96": 24, "97": 25, "98": 27, "99": 27, "100": 27, "101": 30, "102": 31, "103": 32, "104": 32, "105": 32, "106": 36, "107": 46, "108": 47, "109": 47, "110": 47, "111": 47, "112": 47, "113": 48, "114": 49, "115": 49, "116": 49, "117": 51, "118": 54, "119": 55, "120": 55, "121": 55, "122": 55, "123": 55, "124": 56, "125": 57, "126": 57, "127": 57, "128": 59, "129": 63, "130": 64, "131": 65, "132": 65, "133": 65, "134": 65, "135": 68, "136": 68, "137": 69, "138": 70, "139": 70, "140": 70, "141": 70, "142": 70, "143": 72, "144": 73, "145": 73, "146": 76, "147": 79, "148": 80, "149": 80, "150": 80, "151": 82, "157": 151}}
__M_END_METADATA
"""
