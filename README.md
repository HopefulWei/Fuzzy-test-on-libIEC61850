# negative-size-param in server_example_complex_array
## ASAN negative-size-param in server_example_61400_25.c, server_example_basic_io.c, server_example_config_file.c, server_example_control.c, server_example_dynamic.c, server_example_files.c, server_example_goose.c, server_example_logging.c, etc. 
Their are negative-size-param in server_example_61400_25.c, server_example_basic_io.c, server_example_config_file.c, server_example_control.c, server_example_dynamic.c,server_example_files.c, server_example_goose.c, server_example_logging.c, etc.
libIEC61850 1.3.0 1.3.1 1.3.2 version has this problem.

ASAN’s error is

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
==2662==ERROR: AddressSanitizer: negative-size-param: (size=-1)
    #0 0x4582ab  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x4582ab)
    #1 0x52ce31  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x52ce31)
    #2 0x52cf65  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x52cf65)
    #3 0x52cfb3  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x52cfb3)
    #4 0x5121bb  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x5121bb)
    #5 0x512ab7  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x512ab7)
    #6 0x4f1bbf  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x4f1bbf)
    #7 0x7f92126f06b9  (/lib/x86_64-linux-gnu/libpthread.so.0+0x76b9)
    #8 0x7f9211afb41c  (/lib/x86_64-linux-gnu/libc.so.6+0x10741c)

0x625000007907 is located 7 bytes inside of 8196-byte region [0x625000007900,0x625000009904)
allocated by thread T1 here:
    #0 0x4b90d8  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x4b90d8)
    #1 0x4f1d80  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x4f1d80)
    #2 0x512bbb  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x512bbb)
    #3 0x511805  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x511805)
    #4 0x511960  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x511960)
    #5 0x7f92126f06b9  (/lib/x86_64-linux-gnu/libpthread.so.0+0x76b9)

Thread T4 created by T1 here:
    #0 0x42b4e9  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x42b4e9)
    #1 0x4f1c0b  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x4f1c0b)
    #2 0x512d61  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x512d61)
    #3 0x511805  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x511805)
    #4 0x511960  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x511960)
    #5 0x7f92126f06b9  (/lib/x86_64-linux-gnu/libpthread.so.0+0x76b9)

Thread T1 created by T0 here:
    #0 0x42b4e9  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x42b4e9)
    #1 0x4f1c44  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x4f1c44)
    #2 0x511b61  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x511b61)
    #3 0x4f5280  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x4f5280)
    #4 0x4f0553  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x4f0553)
    #5 0x4ea89b  (/home/gw/share/libiec61850-1.3.1/examples/server_example_basic_io/server_example_basic_io+0x4ea89b)
    #6 0x7f9211a1482f  (/lib/x86_64-linux-gnu/libc.so.6+0x2082f)

The problematic code is on lines

 while (running) {
                Thread_sleep(xxx);
The reason for the error is that the Thread_sleep function is called. The specific reason is still not determined.

CVE-2016-4073 has the same problem.
We can reproduce it by continuously sending MMS packets to the server. In fact, it is fuzzing.
The fuzzing code is MMS.py in the repository, We can use it by "python mms.py -ip 127.0.0.1", which can result segmentation fault.
