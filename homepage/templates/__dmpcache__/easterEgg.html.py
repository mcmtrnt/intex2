# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554859509.8429277
_enable_loop = True
_template_filename = 'C:/Users/Trent/intex/homepage/templates/easterEgg.html'
_template_uri = 'easterEgg.html'
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
        __M_writer('\r\n    <h4>Drug Jokes just for fun!</h4>\r\n\r\n    <table class="table table-striped table-bordered table-hover" id=\'drugTable\'>\r\n        <caption style="caption-side: top">&nbsp;</caption>\r\n        <thead class="thead-dark">\r\n            <tr>\r\n                <th>Jokes</th>                 \r\n            </tr>\r\n        </thead>\r\n        <tbody>\r\n            <tr>\r\n                <td>I bought some shoes from a drug dealer. I don\'t know what he laced them with, but I\'ve been tripping all day.</td>\r\n            </tr>\r\n            <tr>\r\n                <td>I know I know, smoking\'s bad for me and all. But, my mama told me never to be a quitter.</td>\r\n            </tr>\r\n            <tr>\r\n                <td>What do crabs smoke? Seaweed.</td>\r\n            </tr>\r\n            <tr>\r\n                <td>What\'s the difference between a sidewalk, a drug dealer, and a prostitute? Sidewalks crack doesn\'t leave an odor!</td>\r\n            </tr>\r\n            <tr>\r\n                <td>I swear to drunk I\'m not God, but seriously, stay in drugs, eat school, and don\'t do vegetables.</td>\r\n            </tr>\r\n            <tr>\r\n                <td>What does a wizard say when doing drugs? Injecto Patronum!</td>\r\n            </tr>\r\n        </tbody>\r\n\r\n    </table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/intex/homepage/templates/easterEgg.html", "uri": "easterEgg.html", "source_encoding": "utf-8", "line_map": {"29": 0, "36": 1, "46": 3, "52": 3, "58": 52}}
__M_END_METADATA
"""
