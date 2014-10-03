#! /usr/bin/python

from jinja2 import Template
from os import listdir

bpath = "./examples/"
xs = listdir(bpath)
xs = [x for x in xs if x.endswith(".hs")]
xs = [(x[3:-3], open(bpath + x).read().strip()) for x in xs]
tpl = Template(open("./index.html.jinja").read())

open("./index.html", "w").write(tpl.render(**dict(xs)))