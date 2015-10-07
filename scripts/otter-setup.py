import os
import random
import re
import shutil
import string
import sys

def generate_secret_key():
    return "".join(
        [random.SystemRandom().choice(
                string.digits + string.ascii_letters + string.punctuation
            ) for i in range(100)])

TEMP_PROJECT_NAME_DIR = 'ot_myprojectdir'

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
update_dict = {}
update_dict['ot_myproject'] = input("Project Name (e.g,. My Project): ")
update_dict['ot_myprojectdir'] = input("Project Dir (e.g., myproject): ")
update_dict['ot_adminname'] = input("Admin Name: ")
update_dict['ot_adminemail'] = input("Admin Email: ")
default_url_template = '%%s.%s.com' % update_dict['ot_myprojectdir']
dev_url = default_url_template % 'dev'
stage_url = default_url_template % 'stage'
prod_url = default_url_template % 'prod'
update_dict['ot_dev_url'] = input("Dev URL [%s]: " % dev_url) or dev_url
update_dict['ot_stage_url'] = input("Stage URL [%s]: " % stage_url) or stage_url
update_dict['ot_production_url'] = \
    input("Production URL [%s]: " % prod_url) or prod_url

v = sys.version_info
update_dict['ot_python_version'] = '%d.%d.%d' % (v.major, v.minor, v.micro)

# Update files with values
project_dir = os.path.join(root_dir, TEMP_PROJECT_NAME_DIR)
for fn in (os.path.join(project_dir, 'settings.py'),
           os.path.join(project_dir, 'wsgi.py'),
           os.path.join(project_dir, 'urls.py'),
           os.path.join(root_dir, 'package.json'),
           os.path.join(root_dir, 'runtime.txt'),
           os.path.join(root_dir, 'Procfile'),
           os.path.join(root_dir, 'manage.py')):
    print("Updating %s" % fn)
    with open(fn, 'r') as f:
        contents = f.read()
    for key, val in update_dict.items():
        contents = re.sub(r'\b%s\b' % key, val, contents)
    with open(fn, 'w') as f:
        f.write(contents)

dotenv_fn = os.path.join(root_dir, '.env')
project_sub_dir = update_dict['ot_myprojectdir']
with open(dotenv_fn, 'w') as f:
    f.write("SECRET_KEY=%s\n" % generate_secret_key())
    f.write("DATABASE_URL=postgres://%s:%s@localhost/%s\n" %
                tuple([project_sub_dir]*3))
print("Initialized .env file with DATABASE_URL and SECRET_KEY. Database "
      "settings assume that database name is '%s'." % project_sub_dir)

# Update project dir name
project_sub_dir = os.path.join(root_dir, project_sub_dir)
print("Moving project directory to %s" % project_sub_dir)
os.rename(project_dir, project_sub_dir)
