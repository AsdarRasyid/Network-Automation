import telnetlib

host = input("masukkan ip address remote: ") 
user = input("masukkan nama user: ")
passwd = input("masukkan password: ")

eksekusi = telnetlib.Telnet(host)

eksekusi.read_until(b"Username: ") 
eksekusi.write(user.encode('ascii') + b"\n")

eksekusi.read_until(b"Password: ") 
eksekusi.write(passwd.encode('ascii') + b"\n")

eksekusi.write(b"conf t\n")
eksekusi.write(b"hostname asdar-router\n")
eksekusi.write(b"int lo20\n") 
eksekusi.write(b"ip address 11.11.11.1 255.255.255.255\n") 
eksekusi.write(b"end\n") 
eksekusi.write(b"exit\n")

print(eksekusi.read_all().decode('ascii'))