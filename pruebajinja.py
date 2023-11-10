import os
from jinja2 import Environment, FileSystemLoader, Template
 
template_path = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
 
def render_template(template_name: str, **context) -> dict[Template, str]:
    """Retorna un template jinja renderizado.
 
    Args:
        template_name (str): Nombre y path de template dentro de app/templates
        context (kwargs): Valores que el template pueda requerir para su renderización.
    Returns:
        dict: retorna un diccionario con el template como 'response' y mimetype de text/html
    """
 
    template = jinja_env.get_template(template_name)
    return {"response": template.render(context), "mimetype": "text/html"}