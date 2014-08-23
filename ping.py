import multiprocessing
import subprocess
import time


running = True

def pinger(host, sleep=1):

    while running:

        cmd = 'ping -c 1 {}'.format(host)
        status, output= subprocess.getstatusoutput(cmd)
        print(output)
        time.sleep(sleep)



def main():
#    for site in ('www.heise.de', 'www.spiegel.de', '8.8.8.8'):
    for site in ('www.heise.de', ):
        p = multiprocessing.Process(target=pinger, args=(site,))
        p.start()
    while 1:
        time.sleep(1)

if __name__ == '__main__':
    main()

