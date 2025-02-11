# Hack The Box - Sherlocks : Crown jewel 2

![logo](img/logo.png)

## Introduction

In this challenge, we are provided with three event log files: `APPLICATION.evtx`, `SECURITY.evtx`, and `SYSTEM.evtx`. Our goal is to analyze these logs to uncover any suspicious activities or security incidents.

## Analysis

### APPLICATION.evtx

The `APPLICATION.evtx` log file contains events related to application-level activities. We will look for any unusual or error events that might indicate issues or malicious activities.

### SECURITY.evtx

The `SECURITY.evtx` log file contains security-related events, such as login attempts, account management, and policy changes. This log is crucial for identifying potential security breaches or unauthorized access.

### SYSTEM.evtx

The `SYSTEM.evtx` log file contains system-level events, including hardware changes, driver updates, and system errors. Analyzing this log can help us identify any system stability issues or hardware-related problems.

## Write-up : 

After converted .evtx files into json with [evtx](https://github.com/omerbenamram/evtx) project we can analyse it.

**Task 1: When utilizing ntdsutil.exe to dump NTDS on disk, it simultaneously employs the Microsoft Shadow Copy Service. What is the most recent timestamp at which this service entered the running state, signifying the possible initiation of the NTDS dumping process?**

Let's find `ntdsutil.exe` into the SECURITY file, then we find that in the `Record 95`.

```json 
      },
      "EventID": 4799,
      "Version": 0,
      "Level": 0,
      "Task": 13826,
      "Opcode": 0,
      "Keywords": "0x8020000000000000",
      "TimeCreated": {
        "#attributes": {
          "SystemTime": "2024-05-15T05:39:55.636252Z"
        }
      }
```

> Answer: 2024-05-15 05:39:55

**Task 2: Identify the full path of the dumped NTDS file.**

As we can see in the Record 648 :
```json
    },
    "EventData": {
      "Data": {
        "#text": [
          "NTDS",
          "3940,D,100",
          "",
          "2",
          "C:\\Windows\\Temp\\dump_tmp\\Active Directory\\ntds.dit",
          "0",
          "\n[1] 0.000003 +J(0)\n[2] 0.0 +J(0)\n[3] 0.000007 +J(0) +M(C:0K, Fs:1, WS:4K # 0K, PF:0K # 0K, P:0K)\n[4] 0.0 +J(0)\n[5] 0.0 +J(0)\n[6] 0.023198 -0.019281 (2) WT +J(0) +M(C:-424K, Fs:26, WS:-464K # 76K, PF:-356K # 0K, P:-356K)\n[7] 0.000279 +J(0)\n[8] 0.000029 +J(0) +M(C:0K, Fs:1, WS:4K # 0K, PF:0K # 0K, P:0K)\n[9] 0.001762 -0.000919 (6) WT +J(0) +M(C:0K, Fs:4, WS:-20K # 0K, PF:-20K # 0K, P:-20K)\n[10] 0.000140 +J(0)\n[11] 0.000060 +J(0) +M(C:0K, Fs:1, WS:-4K # 0K, PF:-8K # 0K, P:-8K).",
          "0 0",
          ""
        ]
      },
      "Binary": null
    }
  }
}
```
> Answer:  C:\Windows\Temp\dump_tmp\Active Directory\ntds.dit

**Task 3: When was the database dump created on the disk?**

we search about the `dump` database. The APPLICATION.evtx file into the record 645, indicate when that the database has been created : 
```json 
     "Version": 0,
      "Level": 4,
      "Task": 1,
      "Opcode": 0,
      "Keywords": "0x80000000000000",
      "TimeCreated": {
        "#attributes": {
          "SystemTime": "2024-05-15T05:39:56.486774Z"
        }
      },
```

>Answer: 2024-05-15 05:39:56

**Task 4: When was the newly dumped database considered complete and ready for use?** 

as the hint told us : 'In Application Event Log, filter for Event ID 327. This Event ID is recorded whenever a newly created database (new copy of NTDS.dit database) is detached by the database engine and marked ready to use.'

Let's find about our 327 event id : 

```json 
"EventID": {
        "#attributes": {
          "Qualifiers": 0
        },
        "#text": 327
      },
      "Version": 0,
      "Level": 4,
      "Task": 1,
      "Opcode": 0,
      "Keywords": "0x80000000000000",
      "TimeCreated": {
        "#attributes": {
          "SystemTime": "2024-05-15T05:39:58.549018Z"
        }
      },
```

> Answer: 2024-05-15 05:39:58

**Task 5: Event logs use event sources to track events coming from different sources. Which event source provides database status data like creation and detachment?**

The provider name given when we have created our database is `ESENT`

> Answer: ESENT

**Task 6: When ntdsutil.exe is used to dump the database, it enumerates certain user groups to validate the privileges of the account being used. Which two groups are enumerated by the ntdsutil.exe process? Give the groups in alphabetical order joined by comma space.**

We search about the use of `ntdsutil.exe` in SECURITY.evtx file.
We found two `TargetUserName` wich are used :

> Answer: Administrators, Backup Operators

**Task 7: Now you are tasked to find the Login Time for the malicious Session. Using the Logon ID, find the Time when the user logon session started.**

The account logon id is `4768` according to this [site](https://www.manageengine.com/products/active-directory-audit/account-logon-events/event-id-4768.html)

Let's find about this id in the `SECURITY.evtx` file.
We find about the administrator login event. 

```json

 },
      "EventID": 4799,
      "Version": 0,
      "Level": 0,
      "Task": 13826,
      "Opcode": 0,
      "Keywords": "0x8020000000000000",
      "TimeCreated": {
        "#attributes": {
          "SystemTime": "2024-05-15T05:36:31.356481Z"
        }
      },
      "EventRecordID": 5939,
      "Correlation": null,
      "Execution": {
        "#attributes": {
          "ProcessID": 764,
          "ThreadID": 812
        }
      },
      "Channel": "Security",
      "Computer": "DC01.forela.local",
      "Security": null
    },
    "EventData": {
      "TargetUserName": "Administrators",
```

> Answer: 2024-05-15 05:36:31