import sys

if int(sys.version[0]) < 3:
  sys.exit("[+] versi python tidak didukung.. gunakan 'python mbf.py'")

import core

if __name__ == "__main__":
  core.man-mbf()