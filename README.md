# Fuzzy-test-on-libIEC61850
## What is the MMS.py and MMS_update.py?
MMS.py is used to fuzz on libIEC61850 by sending MMS packets, which contains the initate-packet to establish connection and fuzzing packets. 
MMS_update.py is used to fuzz on libIEC61850 by sending MMS packets. It is an improved version of MMS.py, which can input fuzzing byte number to choose which byte you want to fuzz. The bytes include TPKT_version, TPKT_reserved, TPKT_length, COTP_len, COTP_PDU_type, IEC_Presentation_1, IEC_Presentation_2, SPDU_CPC, SPDU_length_1, SPDU_PDV, SPDU_length_2,
SPDU_context_1, SPDU_context_2, SPDU_ASN, SPDU_length_3, MMS_ITAG, MMS_ITAG_length, invoke_ID_1, invoke_ID_2, MMS_LTAG, MMS_LTAG_length and etc.
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
### 2. SEGV in server_example_61400_25.c, server_example_basic_io.c etc after fuzzing on the updated IEC61850 
the gdb's error
```
Thread 3 received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0xc07 of process 1158]
0x0007190c in private_ClientConnection_getTasksCount (self=0x0)
    at src/iec61850/server/impl/client_connection.c:76
76	src/iec61850/server/impl/client_connection.c: No such file or directory.
```
The ASAN's error:
```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==1312==ERROR: AddressSanitizer: SEGV on unknown address 0x00000000 (pc 0x001634cc bp 0xb04a0df8 sp 0xb04a0de0 T1277)
==1312==The signal is caused by a READ memory access.
==1312==Hint: address points to the zero page.
    #0 0x1634cb in private_ClientConnection_getTasksCount client_connection.c:76
    #1 0x153f7d in mmsConnectionHandler mms_mapping.c:2409
    #2 0x10c0b4 in isoConnectionIndicationHandler mms_server.c:420
    #3 0x1459de in IsoServer_closeConnection iso_server.c:768
    #4 0x144cd0 in finalizeIsoConnection iso_connection.c:98
    #5 0x144c89 in handleTcpConnection iso_connection.c:436
    #6 0x167bd0 in destroyAutomaticThread thread_bsd.c:89
    #7 0x33ac4a in __asan::AsanThread::ThreadStart(unsigned long long, __sanitizer::atomic_uintptr_t*) (libclang_rt.asan_osx_dynamic.dylib:i386+0x5dc4a)
    #8 0x327827 in asan_thread_start(void*) (libclang_rt.asan_osx_dynamic.dylib:i386+0x4a827)
    #9 0xa75a34d4 in _pthread_body (libsystem_pthread.dylib:i386+0x34d4)
    #10 0xa75a3379 in _pthread_start (libsystem_pthread.dylib:i386+0x3379)
    #11 0xa75a2a55 in thread_start (libsystem_pthread.dylib:i386+0x2a55)

==1312==Register values:
eax = 0x00000000  ebx = 0x004f0f10  ecx = 0x00000000  edx = 0x02561c70  
edi = 0x00000000  esi = 0x00000000  ebp = 0xb04a0df8  esp = 0xb04a0de0  
AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV client_connection.c:76 in private_ClientConnection_getTasksCount
Thread T1277 created by T1 here:
    #0 0x3276d3 in wrap_pthread_create (libclang_rt.asan_osx_dynamic.dylib:i386+0x4a6d3)
    #1 0x167b4b in Thread_start thread_bsd.c:100
    #2 0x144c3a in IsoConnection_create iso_connection.c:513
    #3 0x145cc5 in handleIsoConnections iso_server.c:404
    #4 0x145355 in isoServerThread iso_server.c:491
    #5 0x33ac4a in __asan::AsanThread::ThreadStart(unsigned long long, __sanitizer::atomic_uintptr_t*) (libclang_rt.asan_osx_dynamic.dylib:i386+0x5dc4a)
    #6 0x327827 in asan_thread_start(void*) (libclang_rt.asan_osx_dynamic.dylib:i386+0x4a827)
    #7 0xa75a34d4 in _pthread_body (libsystem_pthread.dylib:i386+0x34d4)
    #8 0xa75a3379 in _pthread_start (libsystem_pthread.dylib:i386+0x3379)
    #9 0xa75a2a55 in thread_start (libsystem_pthread.dylib:i386+0x2a55)

Thread T1 created by T0 here:
    #0 0x3276d3 in wrap_pthread_create (libclang_rt.asan_osx_dynamic.dylib:i386+0x4a6d3)
    #1 0x167b92 in Thread_start thread_bsd.c:104
    #2 0x1452d8 in IsoServer_startListening iso_server.c:609
    #3 0x10bfa2 in MmsServer_startListening mms_server.c:437
    #4 0x16410c in IedServer_start ied_server.c:598
    #5 0xf38ac in main server_example_basic_io.c:137
    #6 0xa7292610 in start (libdyld.dylib:i386+0x1610)

==1312==ABORTING
Abort trap: 6
The problematic code:
```
#### How to trigger it ？
```
# sudo python MMS_update.py -ip 127.0.0.1
Please input byte number:
5
```
