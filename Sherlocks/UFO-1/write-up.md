# Hack The Box Sherlocks - UFO-1

![alt text](img/logo.png)

## Scenario :

Being in the ICS Industry, your security team always needs to be up to date and should be aware of the threats targeting organizations in your industry. You just started as a Threat intelligence intern, with a bit of SOC experience. Your manager has given you a task to test your skills in research and how well can you utilize Mitre Att&ck to your advantage. Do your research on Sandworm Team, also known as BlackEnergy Group and APT44. Utilize Mitre ATT&CK to understand how to map adversary behavior and tactics in actionable form. Smash the assessment and impress your manager as Threat intelligence is your passion.

### According to the sources cited by Mitre, in what year did the Sandworm Team begin operations?

According to [Mitre](https://attack.mitre.org/groups/G0034/). 

![alt text](img/Q1.png)
"This group has been active since at least 2009."

> Answer: 2009 

### Mitre notes two credential access techniques used by the BlackEnergy group to access several hosts in the compromised network during a 2016 campaign against the Ukrainian electric power grid. One is LSASS Memory access (T1003.001). What is the Attack ID for the other?

After analysed the [ATT&CK](https://mitre-attack.github.io/attack-navigator//#layerURL=https%3A%2F%2Fattack.mitre.org%2Fcampaigns%2FC0025%2FC0025-enterprise-layer.json) panel.
We can see in highlight that the BlackEnergy group used Bruteforce to access to several hosts. 

![alt text](img/Q2.png)

> Answer: T1110

### During the 2016 campaign, the adversary was observed using a VBS script during their operations. What is the name of the VBS file?

On the techniques table used by the APT44 group.
If we search for the VBS query we find that : 

![alt text](img/Q3.png)

> Answer: ufn.vbs

### The APT conducted a major campaign in 2022. The server application was abused to maintain persistence. What is the Mitre Att&ck ID for the persistence technique was used by the group to allow them remote access?

After going through the 2022 Campaign Attack navigator, we have identified three techniques used to maintain persistence. However, the only one that allows remote access is [webshell](https://attack.mitre.org/techniques/T1505/003/).

> Answer: T1505.003 

### What is the name of the malware/tool used in question 4?

Take a closer look at the webshell used while reviewing the techniques employed in the 2022 campaign.

![alt text](img/Q5.png)

### Which SCADA application binary was abused by the group to achieve code execution on SCADA Systems in the same campaign in 2022?

![alt text](img/Q6.png)

> Answer: scilc.exe

### Identify the full command line associated with the execution of the tool from question 6 to perform actions against substations in the SCADA environment.

On the same text :

> Answer: C:\sc\prog\exec\scilc.exe -do pack\scil\s1.txt

### What malware/tool was used to carry out data destruction in a compromised environment during the same campaign?

![alt text](img/Q8.png)

> Answer: CaddyWiper

### The malware/tool identified in question 8 also had additional capabilities. What is the Mitre Att&ck ID of the specific technique it could perform in Execution tactic?

Into the execution section of [CaddyWiper](https://mitre-attack.github.io/attack-navigator//#layerURL=https%3A%2F%2Fattack.mitre.org%2Fsoftware%2FS0693%2FS0693-enterprise-layer.json) Attack navigator

![alt text](img/Q9.png)

> Answer: T1106

### The Sandworm Team is known to use different tools in their campaigns. They are associated with an auto-spreading malware that acted as a ransomware while having worm-like features .What is the name of this malware?

[NotPetya](https://attack.mitre.org/software/S0368/) malware "appears as a form of ransomware"

> Answer: NotPetya

### What was the Microsoft security bulletin ID for the vulnerability that the malware from question 10 used to spread around the world?

![alt text](img/Q11.png)

> Answer: MS17-010

### What is the name of the malware/tool used by the group to target modems?

The reference to APT44 mentions targeting modems. Referring back to the pinned text, it discusses the [AcidRain](https://attack.mitre.org/software/S1125/) malware.

> Answer: AcidRain 

### Threat Actors also use non-standard ports across their infrastructure for Operational-Security purposes. On which port did the Sandworm team reportedly establish their SSH server for listening?


According to a [reference](https://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/) : 

![alt text](img/Q13.png)

> Answer: 6789

### The Sandworm Team has been assisted by another APT group on various operations. Which specific group is known to have collaborated with them?

![alt text](img/Q14.png)

> Answer: APT28