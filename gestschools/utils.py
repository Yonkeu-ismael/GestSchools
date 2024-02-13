from django import VERSION

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa




def django_major_version():
    return VERSION[:2]


def value_by_version(args):
    """
    Return value by version
    Return latest value if version not found
    """
    version_map = args_to_dict(args)
    major_version = '.'.join(str(v) for v in django_major_version())
    return version_map.get(major_version,
                           list(version_map.values())[-1])


def args_to_dict(args):
    """
    Convert template tag args to dict
    Format {% suit_bc 1.5 'x' 1.6 'y' %} to { '1.5': 'x', '1.6': 'y' }
    """
    return dict(zip(args[0::2], args[1::2]))

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None