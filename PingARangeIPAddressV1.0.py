#!/usr/bin/env python

#This is small auto Python script file to ping a range of IP address.
#To ping a range of IP addresses in Python and print either: "The IP is reachable with a X% percent package loss" or "The IP isn't reachable with a X% package loss".
#The range to try is 192.168.0.X with X being the range of 0-255.
#Created by Tommas Huang 
#Created date: 2019-07-31

import shlex
#The shlex class makes it easy to write lexical analyzers for simple syntaxes resembling that of the Unix shell.
from subprocess import PIPE, Popen
#Special value that can be used as the stdin, stdout or stderr argument to Popen and indicates that a pipe to the standard stream should be opened.
   
cmd1 = shlex.split("grep -oP '\d+(?=% packet loss)'")
#Used shlex.split() recently to split a command as argument to subprocess.
##Just want to see the packet loss.
for x in range(1, 256):
#The range() function generates the integer numbers between the given start integer to the stop integer.
#X being the range of 0-255.
    cmd = "ping  -c 4  192.168.43.{}".format(x).split()
    #cmd: Command that was used to spawn the child process. The command is ping in both Windows and Unix-like systems.
    #The option -n (Windows) or -c (Unix) controls the number of packets which in this example was set to 1.
    #The built-in string class provides the ability to do complex variable substitutions and value formatting via the format()
    #The split() method splits a string into a list.
    p1 = Popen(cmd, stdout=PIPE, stderr=PIPE)
    p2 = Popen(cmd1, stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()
    #The parameters stdin, stdout, and stderr represent the standard input, output, and error handles of the program, respectively. They can be PIPE, file descriptors or file objects, or they can be set to None, indicating inheritance from the parent process.
    #Subprocess.PIPE can initialize stdin, stdout or stderr parameters when creating a Popen object. Indicates the standard of communication with the child process.
    #When creating a Popen object, it is used to initialize the stderr parameter, indicating that the error is output through the standard output stream.
    output = p2.communicate()[0].rstrip()
    #The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
    if output == "100%":
        print("{}% percent packet loss from unreachable ip {}".format(output, cmd[-1]))
    else:
        print("{}% percent packet loss from reachable ip {}".format(output, cmd[-1]))
       #format(value[, format_spec]): Convert a value to a “formatted” representation, as controlled by format_spec. The interpretation of format_spec will depend on the type of the value argument.
       #Will print the command failed unreachable ip or passed reachable ip with its exit status.
   