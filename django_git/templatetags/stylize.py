from django.template import Library, Node, resolve_variable
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = Library()

# usage: {% stylize "language" %}...language text...{% endstylize %}
class StylizeNode(Node):
	def __init__(self, nodelist, *varlist):
		self.nodelist, self.vlist = (nodelist, varlist)

	def render(self, context):
		style = 'text'
		if len(self.vlist) > 0:
			style = resolve_variable(self.vlist[0], context)
		return highlight(self.nodelist.render(context),
				get_lexer_by_name(style, encoding='UTF-8'), HtmlFormatter(cssclass="pygment_highlight"))

def stylize(parser, token):
	nodelist = parser.parse(('endstylize',))
	parser.delete_first_token()
	return StylizeNode(nodelist, *token.contents.split()[1:])

stylize = register.tag(stylize)
