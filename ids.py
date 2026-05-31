# # Libraries
# import time
# #from collections import defaultdict
# from message import create_popup
# from collections import defaultdict
# # Define Class call MiniIdps
# class MiniIdps:
#     # class attributes
#     consider_bruteforce = 10
#     consider_dos = 300
#     consider_nmap = 10
#     # Contructor
#     def __init__(self):
#         # Instance attributes
#         self.log_fail = defaultdict(int)
#         self.request_num = defaultdict(int)
#         self.port_scan = defaultdict(set)
#         self.blocked_ip = set()  

    
#     # Method alert : Use to send the alert message and save alert to log
#     def alert(self, title, msg):
#         cur_time = time.ctime()  
#         message = f"{title}\n{msg}\nTime: {cur_time}"
#         print(f"[Alert]: {message}")

#         # Save alerts to log file 
#         try:
#             with open("Alerts.log", 'a') as file:
#                 file.write(message + "\n\n")
#         except IOError:
#             print("Can't write log to the file, there are some errors accour!.")
            
#         # call the message 
#         create_popup(message)
    
#     # Method block_ips : Use to add the ip into the file
#     def block_ips(self, ip):
#         # Check is the IPs in the file is Exist
#         if ip in self.blocked_ip:
#             return
        
#         # add the new ip into the blocked_ip 
#         self.blocked_ip.add(ip)
#         # write the ip into the file 
#         try:
#             with open("block_ip.txt", 'a') as file:
#                 file.write(ip + "\n")
#         except IOError:
#             print("Can't write IPs into the file errors found.!!")
        
#         # alert the the blocked ip 
#         self.alert("IP Block", f"Block IP: {ip}")


#     # Method bruteforce_detection
#     def bruteforce_detection(self, ip):
#         # increase brute force num
#         self.log_fail[ip] += 1

#         # Checking if the IP reach the limit and not in the blocked_ip
#         if (self.log_fail[ip] >= self.consider_bruteforce) and (ip not in self.blocked_ip):
#             self.alert("Brute Force", f"From IP: {ip}")
#             self.block_ips(ip)
    

#     # Method dos_detection
#     def dos_detection(self, ip):
#         # increase dos num
#         self.request_num[ip] += 1

#         # Checking if the IP reach the limit and not in the blocked_ip
#         if (self.request_num[ip] >= self.consider_dos) and (ip not in self.blocked_ip):
#             self.alert("DOS Attack", f"From IP: {ip}")
#             self.block_ips(ip)

    
#     # Method nmap_detection
#     def nmap_detection(self, ip, port):
#         self.port_scan[ip].add(port)

#         if len(self.port_scan[ip]) >= self.consider_nmap:
#             self.alert("Nmap Detected", f"IP from: {ip}")
#             self.block_ips(ip)

    
#     # Method maanage_event: Use to Analyze the event for malicious behavior
#     def manage_event(self, event):
#         ip = event.get("ip")
#         action = event.get("action")

#         # checking id thge ips is/isn't in the blocked_ip jusr return
#         if not ip or ip in self.blocked_ip:
#             return
#         # 
#         if action == "login_fail":
#             self.bruteforce_detection(ip)
#         elif action == "request":
#             self.dos_detection(ip)
#         elif action == "scan":
#             port = event.get("port")
#             if port:
#                 self.nmap_detection(ip, port)




import time
from message import create_popup
from collections import defaultdict


class MiniIdps:
    # thresholds
    consider_bruteforce = 10
    consider_dos = 300
    consider_nmap = 10   # you can change if you want

    def __init__(self):
        self.log_fail = defaultdict(int)
        self.request_num = defaultdict(int)
        self.port_scan = defaultdict(set)
        self.blocked_ip = set()

    def alert(self, title, msg):
        cur_time = time.ctime()
        message = f"{title}\n{msg}\nTime: {cur_time}"
        print(f"[Alert]: {message}")

        try:
            with open("Alerts.log", "a") as file:
                file.write(message + "\n\n")
        except IOError:
            print("Can't write log file.")

        create_popup(message)

    def block_ips(self, ip):
        if ip in self.blocked_ip:
            return

        self.blocked_ip.add(ip)

        try:
            with open("block_ip.txt", "a") as file:
                file.write(ip + "\n")
        except IOError:
            print("Can't write IP file.")

    def bruteforce_detection(self, ip):
        self.log_fail[ip] += 1

        if self.log_fail[ip] >= self.consider_bruteforce and ip not in self.blocked_ip:
            self.alert("Brute Force", f"From IP: {ip}")
            self.block_ips(ip)


    def dos_detection(self, ip):
        self.request_num[ip] += 1

        if self.request_num[ip] >= self.consider_dos and ip not in self.blocked_ip:
            self.alert("DOS Attack", f"From IP: {ip}")
            self.block_ips(ip)

    def nmap_detection(self, ip, port):
        # Track unique ports hit by this IP
        self.port_scan[ip].add(port)

        # Detection threshold (you can adjust)
        if len(self.port_scan[ip]) >= self.consider_nmap:
            self.alert("Nmap Detected", f"From IP: {ip}")
            self.block_ips(ip)


    def manage_event(self, event):
        ip = event.get("ip")
        action = event.get("action")

        if not ip or ip in self.blocked_ip:
            return


        if action == "login_fail":
            self.bruteforce_detection(ip)

        elif action == "scan":
            port = event.get("port")
            if port:
                self.nmap_detection(ip, port)
            return 


        elif action == "request":
            self.dos_detection(ip)
