# Hack The Box Challenges - SpookyPass

## Description
All the coolest ghosts in town are going to a Haunted Houseparty - can you prove you deserve to get in?

## Write-up: 

After openned the file we can underline the presence of "ELF" string wich caracterize a executable file.
So let's run it : 

```bash
✗ ./pass      
Welcome to the SPOOKIEST party of the year.
Before we let you in, you'll need to give us the password:
```

To get the flag, we need to find the password.
The file is compilated, but it's interesting to see the strings of the file :
```bash 
✗ strings pass

[...]

Welcome to the 
[1;3mSPOOKIEST
[0m party of the year.
Before we let you in, you'll need to give us the password: 
s3cr3t_p455_f0r_gh05t5_4nd_gh0ul5
Welcome inside!
You're not a real ghost; clear off!
;*3$"
GCC: (GNU) 14.2.1 20240805
GCC: (GNU) 14.2.1 20240910
main.c
_DYNAMIC

[...]

```

Then, in the command output, we notice the presence of an unobfuscated string containing "secret". This could be our famous password. Answer the password prompt with this string `s3cr3t_p455_f0r_gh05t5_4nd_gh0ul5`:

```bash
✗ ./pass      
Welcome to the SPOOKIEST party of the year.
Before we let you in, you'll need to give us the password: s3cr3t_p455_f0r_gh05t5_4nd_gh0ul5
Welcome inside!
HTB{un0bfu5c4t3d_5tr1ng5}
```

> Flag : HTB{un0bfu5c4t3d_5tr1ng5}