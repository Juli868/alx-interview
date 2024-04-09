#!/usr/bin/python3
import re
import sys
import signal
reg = '^\d{1,3}\.^\d{1,3}\.^\d{1,3}\.^\d{1,3} - [date.!?] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
def print_results():
    pass
def main(signum, frame):
    for i in range(10):
        total = 0
        given = sys.stdin
        '''
        if re.search(reg, given):
            """split the string and find the total."""
            total += number
        '''
        print('Hey')

if (__name__ == '__main__'):
    signal.signal(signal.SIGINT, main)
    main()
