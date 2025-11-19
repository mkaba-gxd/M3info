import os
import sys
import pymysql
import warnings
import pandas as pd
from pathlib import Path

def getinfo(comm):

    try :
        connection = pymysql.connect(host="192.168.9.100", user="gxd_pipeline", password="gw!2341234", database="gxd")
    except Exception as e:
        sys.exit({e})

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        db_tbl = pd.read_sql(comm, connection)

    return db_tbl

def Search_fcDir(fc_id, directory: Path):

    fcDirs = [fcDir for fcDir in directory.iterdir() if fcDir.name.endswith(fc_id)]
    if len(fcDirs) != 1: return None
    fcDirs.sort()

    return os.path.basename(fcDirs[-1])

def init(msg="No matching data found.", parser=None):
    print(msg)
    if parser :
        parser.print_help()
    sys.exit(1)


