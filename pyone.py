#encoding:utf-8
import os
import sys
import re
import json
import base64
import zlib
import requests
import flask

if len(sys.argv)==1:
    print("usage: %s run.py"%sys.argv[0])
    file = "run.py"
else:
    file = sys.argv[1]
    
exec(open(file, encoding="utf-8").read())
