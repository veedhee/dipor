import jinja2
from jinja2 import nodes
from jinja2.ext import Extension

class RoutesExtension(Extension):
    tags = {"route"}

    def __init__(self, environment):
        super(RoutesExtension, self).__init__(environment)

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [parser.parse_expression()]

        while True:
            if parser.stream.skip_if("comma"):
                args.append(parser.parse_expression())
            else:
                break

        node = self.call_method('_generate_routes', args, lineno=lineno)
        return nodes.CallBlock(node, [], [], [], lineno=lineno)

    def _generate_routes(self, routes, parent_ul_class, ul_class, li_class, dropdown_li_class, dropdown_ul_class, a_class, caller):
        routes2html = self.__generate_routes(routes, ul_class, li_class, dropdown_li_class, dropdown_ul_class, a_class, html=f"<ul class='{parent_ul_class}'>")
        return jinja2.Markup(routes2html)

    
    def __generate_routes(self, routes, ul_class, li_class, dropdown_li_class, dropdown_ul_class, a_class, html, is_subpath=False):
        for k, v in routes.items():
            if not v[1]:
                html += f"<li class='{li_class}'><a class='{a_class}' href='{k}'>"+str(v[0])+"</a></li>"
            else:
                html += f"<li class='{li_class} {dropdown_li_class}'><a class='{a_class}' href='{k}'>"+str(v[0])+f"<ul class='{ul_class} {dropdown_ul_class}'>"
                html = self.__generate_routes(v[1], ul_class, li_class, dropdown_li_class, dropdown_ul_class, a_class, html, is_subpath=True)
        if is_subpath:
            html += "</ul></li>"
            return html

        return html+"</ul>"