from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.compat import make_admonition
from sphinx.locale import _

def setup(app):
    app.add_config_value('rfc2119_include_mandatory', True, True)
    app.add_node(mandatorylist)
    app.add_node(
        mandatory,
        html=(visit_mandatory_node, depart_mandatory_node),
        latex=(visit_mandatory_node, depart_mandatory_node),
        text=(visit_mandatory_node, depart_mandatory_node))

    app.add_directive('must', MandatoryDirective)
    app.add_directive('shall', MandatoryDirective)
    app.add_directive('mandatorylist', MandatoryListDirective)
    app.connect('doctree-resolved', process_mandatory_nodes)
    app.connect('env-purge-doc', purge_mandatory)
    """
    app.add_node(mandatorynotlist)
    app.add_node(recommendedlist)
    app.add_node(recommendednotlist)
    app.add_node(optionallist)
    app.add_node(mandatorynot)
    app.add_node(recommended)
    app.add_node(recommendednot)
    app.add_node(optional)
    """
    return {"version": "0.1"}


class mandatory(nodes.Admonition, nodes.Element):
    pass


class mandatorylist(nodes.General, nodes.Element):
    pass

def visit_mandatory_node(self, node):
    self.visit_admonition(node)

def depart_mandatory_node(self, node):
    self.depart_admonition(node)


class MandatoryListDirective(Directive):
    
    has_content = True

    def run(self):
        return [mandatorylist('')]


class MandatoryDirective(Directive):
    has_content = True
    def run(self):
        env = self.state.document.settings.env
        env.app.warn('DEBUG')
        targetid = "mandatory-%d" % env.new_serialno('mandatory')
        targetnode = nodes.target('', '', ids=[targetid])

        ad = make_admonition(
            mandatory, self.name, [_('Mandatory')], self.options,
            self.content, self.lineno, self.content_offset,
            self.block_text, self.state, self.state_machine)

        if not hasattr(env, 'mandatory_all_mandatory'):
            env.mandatory_all_mandatory = []
        env.mandatory_all_mandatory.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'mandatory': ad[0].deepcopy(),
            'target': targetnode})

        return [targetnode] + ad

def purge_mandatory(app, env, docname):
    if not hasattr(env, 'mandatory_all_mandatorys'):
        return
    env.mandatory_all_mandatory = [mandatory for mandatory in env.mandatory_all_mandatory if mandatory['docname'] != docname]


def process_mandatory_nodes(app, doctree, fromdocname):
    if not app.config.rfc2119_include_mandatory:
        for node in doctree.traverse(mandatory):
            node.parent.remove(node)

    env = app.builder.env

    for node in doctree.traverse(mandatorylist):
        if not app.config.rfc2119_include_mandatory:
            node.replace_self([])
            continue

        content = []

        for mandatory_info in env.mandatory_all_mandatory:
            para = nodes.paragraph()
            filename = env.doc2path(mandatory_info['docname'], base=None)
            description = (
                _('(The original entry is located in %s, line %d and can be found ') %
                (filename, mandatory_info['lineno']))
            para += nodes.Text(description, description)

            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(_('here'), _('here'))
            newnode['refdocname'] = mandatory_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, mandatory_info['docname'])
            newnode['refuri'] += '#' + mandatory_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para+= nodes.Text('.)', '.)')

            content.append(mandatory_info['mandatory'])
            content.append(para)

        node.replace_self(content)
