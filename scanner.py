import socket
import sys


if __name__ == '__main__':
    target = input('Enter the host >>\n')
    ip = socket.gethostbyname(target)
    start = int(input('Enter start of range >>\n'))
    end = int(input('Enter end of range >>\n'))

    if start > end or end > 65535:
        print('Bad range')
        sys.exit(0)
   
    for i in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
        conn = s.connect_ex((ip, i))
        if(conn == 0) :
            print ('{} - open'.format(i))
        s.close()