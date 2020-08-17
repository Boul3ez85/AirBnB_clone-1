#!/ysr/bin/python3
"""a script to generate a .tgz files from the contents of the
web_static folder of the AirBnB repo"""

import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """Represent a function to generate .tgz files"""

    if not os.path.exists("versions/"):
        os.mkdir("versions")

    date = datetime.now()
    pth = "versions/web_static_{}.tgz".format(date.strftime("%Y%m%d%H%M%S"))
    local("tar -cvzf {} web_static".format(pth))
    if not os.path.exists("{}".format(pth)):
        return None
    else:
        return pth
