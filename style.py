import os
import sys
import matplotlib
import json
from IPython.core.display import HTML

def apply_style():
    sys.path.append(os.getcwd())
    s = json.load(open(os.getcwd()+"/"+os.path.dirname(__file__)+"/assets/bmh_matplotlibrc.json"))
    matplotlib.rcParams.update(s)
    styles = open(os.getcwd()+"/"+os.path.dirname(__file__)+"/assets/custom.css").read()
    HTML(styles)

apply_style()
