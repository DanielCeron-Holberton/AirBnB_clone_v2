#!/usr/bin/python3
"""
Module that contains script for make a package of the app and deploy it fully
"""
from fabric.api import *
from datetime import datetime

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """Function to deploy the app"""
    return do_deploy(do_pack())
