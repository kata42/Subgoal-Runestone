import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys
from runestone.server import get_dburl
from sphinxcontrib import paverutils
import pkg_resources
from socket import gethostname

sys.path.append(os.getcwd())

home_dir = os.getcwd()
master_url = 'http://localhost'
master_app = 'runestone'
#serving_dir = "./build/SubGoals"
serving_dir = "./books/published/SubGoals"

#dest = "../../static"

from runestone import get_master_url

master_url = None
if master_url is None:
    master_url = get_master_url()

dynamic_pages = True

if dynamic_pages:
    dest = './published'
else:
    dest = '../../static'

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./books/published/SubGoals",
        sourcedir="_sources",
        outdir="./books/published/SubGoals",
        confdir=".",
        project_name = "SubGoals",
        template_args={'course_id': 'SubGoals',
                      'login_required':'true',
                       'appname':master_app,
                       'loglevel': 10,
                       'course_url':master_url,
                       'use_services': 'true',
                       'python3': 'true',
                       'dburl': 'postgresql://user:password@localhost/runestone',
                       'default_ac_lang': 'Java',
                       'basecourse': 'SubGoals',
                       'jobe_server': 'http://jobe2.cosc.canterbury.ac.nz',
                       'proxy_uri_runs': '/jobe/index.php/restapi/runs/',
                       'proxy_uri_files': '/jobe/index.php/restapi/files/',
                       'dynamic_pages': dynamic_pages,
                       'downloads_enabled': 'false',
                       'enable_chatcodes': 'False',
                       'allow_pairs': 'False'
                        }
    )
)

# if we are on runestone-deploy then use the proxy server not canterbury
if gethostname() == 'runestone-deploy':
    del options.build.template_args['jobe_server']
    del options.build.template_args['proxy_uri_runs']
    del options.build.template_args['proxy_uri_files']

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

# If DBURL is in the environment override dburl
options.build.template_args['dburl'] = get_dburl(outer=locals())

from runestone import build  # build is called implicitly by the paver driver.

