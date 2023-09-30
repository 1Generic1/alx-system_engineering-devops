# 0x05-processes_and_signals

## Resources

	https://www.linfo.org/pid.html <br>
	https://www.thegeekstuff.com/2012/03/linux-processes-environment/ <br>
	https://www.educative.io/answers/what-are-linux-signals <br>
	https://www.digitalocean.com/community/tutorials/process-management-in-linux <br>

## Requirements

## General
	
	Allowed editors: vi, vim, emacs
	All your files will be interpreted on Ubuntu 20.04 LTS
	All your files should end with a new line
	A README.md file, at the root of the folder of the project, is mandatory
	All your Bash script files must be executable
	Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any error
	The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
	The second line of all your Bash scripts should be a comment explaining what is the script doing

# TASKS

## 0-what-is-my-pid

Write a Bash script that displays its own PID.

	sylvain@ubuntu$ ./0-what-is-my-pid
	4120
	sylvain@ubuntu$

## 1-list_your_processes

Write a Bash script that displays a list of currently running processes.

Requirements:

	Must show all processes, for all users, including those which might not have a TTY
	Display in a user-oriented format
	Show process hierarchy

## 2-show_your_bash_pid

Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

	You cannot use pgrep
	The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)
