import telnetlib
import time

router1 = {'host': '192.168.6.70', 'user': 'cisco', 'password': 'cisco'}
router2 = {'host': '192.168.6.71', 'user': 'cisco', 'password': 'cisco'}
router3 = {'host': '192.168.6.72', 'user': 'cisco', 'password': 'cisco'}

routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router["host"]}')

    tn = telnetlib.Telnet(host=router['host'])

    tn.read_until(b'Username: ')
    tn.write(router['user'].encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(router['password'].encode() + b'\n')

    tn.write(b'terminal length 0\n')
    tn.write(b'enable\n')
    tn.write(b'cisco\n')  # password enable cisco

    tn.write(b'conf t\n')
    tn.write(b'hostname network\n')
    tn.write(b'interface loopback 0\n')
    tn.write(b'ip address 1.1.1.1 255.255.255.255\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 f0/0 192.168.6.1\n')
    tn.write(b'end\n')
    tn.write(b'show ip route\n')
    tn.write(b'exit\n')
    time.sleep(1)

    output = tn.read_all()
    output = output.decode()
    print(output)
    print('#' * 50)


