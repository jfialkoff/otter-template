import os
import re
import shutil

TEMP_PROJECT_NAME_DIR = 'project_name'

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
update_dict = {}
update_dict['project_name'] = input("Project Name (e.g,. My Project): ")
update_dict['project_sub_dir'] = input("Project Dir (e.g., myproject): ")
update_dict['admin_name'] = input("Admin Name: ")
update_dict['admin_email'] = input("Admin Email: ")
default_url_template = '%%s.%s.com' % update_dict['project_sub_dir']
dev_url = default_url_template % 'dev'
stage_url = default_url_template % 'stage'
prod_url = default_url_template % 'prod'
update_dict['dev_url'] = input("Dev URL [%s]: " % dev_url) or dev_url
update_dict['stage_url'] = input("Stage URL [%s]: " % stage_url) or stage_url
update_dict['production_url'] = \
    input("Production URL [%s]: " % prod_url) or prod_url

# Update files with values
project_dir = os.path.join(root_dir, TEMP_PROJECT_NAME_DIR)
for fn in (os.path.join(project_dir, 'settings.py'),
           os.path.join(project_dir, 'wsgi.py'),
           os.path.join(project_dir, 'urls.py'),
           os.path.join(root_dir, 'manage.py')):
    print("Updating %s" % fn)
    with open(fn, 'r') as f:
        contents = f.read()
    for key, val in update_dict.items():
        re.sub(r'{{\s*%s\s*}}' % key, val, contents)
    """
    with open(fn, 'w') as f:
        f.write(contents)
    """

# Update project dir name
project_sub_dir = os.path.join(root_dir, update_dict['project_sub_dir'])
print("Moving project directory to %s" % project_sub_dir)
#shutil.move(project_dir, os.path.join(root_dir, project_sub_dir))
