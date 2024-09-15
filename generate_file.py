import os
import time

CURRENT_EPOCH = int(time.time())
WEEK_AWAY = CURRENT_EPOCH + 604800

def generate_file(satellite):
    os.system("wget http://www.amsat.org/amsat/ftp/keps/current/nasabare.txt -O nasabare.txt")
    os.system(f"predict -q station.qth -t nasabare.txt -f {satellite} {CURRENT_EPOCH} {WEEK_AWAY} > tmp.txt")

