#!/usr/bin/python3
"""
Module that contains script for make a package of the app
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Function that make the folder and package of the app
    """
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        path_name = "versions/web_static_{}.tgz".format(date)
        _gzip = local("tar -cvzf {} web_static".format(rout))
        return path_name
    except Exception:
        return None
