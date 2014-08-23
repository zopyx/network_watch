import multiprocessing
import subprocess
import time


running = True

def pinger(host, sleep=1):

    while running:

        cmd = 'ping -c 1 -q {}'.format(host)
        status, output= subprocess.getstatusoutput(cmd)
        print(output)
        last_line = output.split('\n')[-1]
        print(last_line)
        time_field = last_line.split('=')
        ms = time_field[1].split('/')[0].strip()
        time.sleep(sleep)
        status_line = '{} ; {} ; {}'.format(host, time.time(), ms)
        fn = '{}.csv'.format(host)
        with open(fn, 'a') as fp:
            fp.write(status_line + '\n')



def main():
    for site in ('www.heise.de', 'www.spiegel.de', '8.8.8.8'):
        p = multiprocessing.Process(target=pinger, args=(site,))
        p.start()
    while 1:
        time.sleep(1)

if __name__ == '__main__':
    main()

