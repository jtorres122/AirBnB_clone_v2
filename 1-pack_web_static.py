#!/usr/bin/python3
# fabric file to create tgz file
from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """function that creates targz file out of web_static directory"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    tgzname = "versions/web_static_{}.tgz".format(time)
    if os.path.isdir("versions") is False:
        local("mkdir versions")
    try:
        local("tar -cvzf {} web_static".format(tgzname))
        return tgzname
    except:
        return None
