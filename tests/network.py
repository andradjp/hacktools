import socket

target_host = 'jpandrade.info'

print('[+] Creating socket...')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('[!] Socket created!')
print('[+] Connecting with remote host...')
client.connect((target_host, 80))
print('[+] Connection ok')
request = 'GET / HTTP/1.1\r\nHost:%s\r\n\r\n' % target_host
client.send(request.encode())
while True:
    data = client.recv(128)
    print(data.decode())
    if data == '':
        break
print('[-] Closing the socket')
client.close()