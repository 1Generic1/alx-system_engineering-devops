# 0x06-regular_expressions

Resources
Read or watch:

Regular expressions - basics https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518 <br>
Regular expressions - advanced https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518 <br>
Rubular is your best friend https://rubular.com/ <br>
Use a regular expression against a problem: now you have 2 problems https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/<br>
Learn Regular Expressions with simple, interactive exercises https://regexone.com/ <br>

## Requirements

## General
	Allowed editors: vi, vim, emacs
	All your files will be interpreted on Ubuntu 20.04 LTS
	All your files should end with a new line
	A README.md file, at the root of the folder of the project, is mandatory
	All your Bash script files must be executable
	The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
	All your regex must be built for the Oniguruma library

# TASKS

## 0-simply_match_school.rb

## Requirements:
	
	The regular expression must match School
	Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:
	
	sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
	School$
	sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
	School$
	sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
	SchoolSchool$
	sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
	$

## 1-repetition_token_0.rb


Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 2-repetition_token_1.rb

Requirements:

	Find the regular expression that will match the above cases
	Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 3-repetition_token_2.rb

Requirements:

	Find the regular expression that will match the above cases
	Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

## 4-repetition_token_3.rb

Requirements:

	Find the regular expression that will match the above cases
	Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
	Your regex should not contain square brackets

## 5-beginning_and_end.rb

Requirements:

	The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between
	Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

Example:

	sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
	$
	sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
	hbn$
	sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
	$
	sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
	h8n$
	sylvain@ubuntu

## 6-phone_number.rb

This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.

Requirement:

	The regular expression must match a 10 digit phone number
Example:

## 7-OMG_WHY_ARE_YOU_SHOUTING.rb

Requirement:

	The regular expression must be only matching: capital letters
Example:

## 100-textme.rb

This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter.

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

Requirements:

Your script should output: [SENDER],[RECEIVER],[FLAGS]
The sender phone number or name (including country code if present)
The receiver phone number or name (including country code if present)
The flags that were used
You can find a [log file here].

Example:

	$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
	Google,+16474951758,-1:0:-1:0:-1
	$
	$
	$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
	+17272713208,+19172319348,-1:0:-1:0:-1
	$
	$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
	18572406905,14022180266,-1:0:-1:-1:-1
	$
	$
	$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
	12392190384,19148265919,-1:0:-1:-1:-1
	$

