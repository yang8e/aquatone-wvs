import os
import sys

def aquatone_scan(target):
    os.system('aquatone-discover -d '+target)
    os.system('aquatone-scan -p huge -d '+target)

input_url = sys.argv[1]
aquatone_scan(input_url)
