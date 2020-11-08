import sys, os

INTERP = "/home/thepantrylist/pantry_env/bin/python"

if sys.executable !=  INTERP: os.execl(INTERP, INTERP, *sys.argv)

from pantry import app as application