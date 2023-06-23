from jinja2 import Template, FileSystemLoader, Environment


def render(template, folder='templates', **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template)
    return template.render(**kwargs)

# from os.path import join
# def render(template_name, folder='templates', **kwargs):
#     file_path = join(folder, template_name)
#     with open(file_path, encoding='utf-8') as f:
#         template = Template(f.read())
#     return template.render(**kwargs)
