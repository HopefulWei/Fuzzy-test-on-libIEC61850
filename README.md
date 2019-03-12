# Fuzzy-test-on-libIEC61850
## What is the MMS.py and MMS_update.py?
MMS.py is used to fuzz on libIEC61850 by sending MMS packets, which contains the initate-packet to establish connection and fuzzing packets. 
MMS_update.py is used to fuzz on libIEC61850 by sending MMS packets. It is an improved version of MMS.py, which can input fuzzing byte number to choose which byte you want to fuzz.
## How to use it?
### MMS.py
```
# sudo python MMS.py -ip 127.0.0.1
```
### MMS_update.py
```
# sudo python MMS_update.py -ip 127.0.0.1
Please input byte number:
byte_number(1,2,3....)
```
## Fuzzy test results
### 1. ASAN negative-size-param in server_example_61400_25.c, server_example_basic_io.c, server_example_config_file.c, server_example_control.c, server_example_dynamic.c, server_example_files.c, server_example_goose.c, server_example_logging.c, etc.
ASAN’s error is
```
=================================================================
==2624==ERROR: AddressSanitizer: negative-size-param: (size=-1)
    #0 0x45825b  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x45825b)
    #1 0x518913  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x518913)
    #2 0x518a47  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x518a47)
    #3 0x518a95  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x518a95)
    #4 0x50becf  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x50becf)
    #5 0x50c7cb  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x50c7cb)
    #6 0x510af6  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x510af6)
    #7 0x7f5adb12b6b9  (/lib/x86_64-linux-gnu/libpthread.so.0+0x76b9)
    #8 0x7f5ada53641c  (/lib/x86_64-linux-gnu/libc.so.6+0x10741c)

0x625000007907 is located 7 bytes inside of 8196-byte region [0x625000007900,0x625000009904)
allocated by thread T1 here:
    #0 0x4b9088  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x4b9088)
    #1 0x510f82  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x510f82)
    #2 0x50c8cf  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x50c8cf)
    #3 0x50b519  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x50b519)
    #4 0x50b674  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x50b674)
    #5 0x7f5adb12b6b9  (/lib/x86_64-linux-gnu/libpthread.so.0+0x76b9)

Thread T4 created by T1 here:
    #0 0x42b499  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x42b499)
    #1 0x510b42  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x510b42)
    #2 0x50ca75  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x50ca75)
    #3 0x50b519  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x50b519)
    #4 0x50b674  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x50b674)
    #5 0x7f5adb12b6b9  (/lib/x86_64-linux-gnu/libpthread.so.0+0x76b9)

Thread T1 created by T0 here:
    #0 0x42b499  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x42b499)
    #1 0x510b7b  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x510b7b)
    #2 0x50b875  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x50b875)
    #3 0x4eb43e  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x4eb43e)
    #4 0x50e702  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x50e702)
    #5 0x4ea680  (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x4ea680)
    #6 0x7f5ada44f82f  (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)

SUMMARY: AddressSanitizer: negative-size-param (/home/gw/share/libiec61850-1.3.2/examples/server_example_files/server_example_files+0x45825b) 
==2624==ABORTING
```

gdb's error:
```
Thread 3 received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0xb07 of process 883]
0x0006e8fc in private_ClientConnection_getTasksCount (self=0x0)
    at src/iec61850/server/impl/client_connection.c:76
76	    Semaphore_wait(self->tasksCountMutex);
```
