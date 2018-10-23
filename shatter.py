#hello
from datetime import datetime
from prettytable import PrettyTable
import glob
import re
s1 = " WELCOME TO SHATTER "
s2 = """
	Download the emailed chat to same folder
	as the script and run the script. PRESS 1
	to calculate normally or PRESS 2 to account
	for spams!!
"""
s3 = " RESULTS "
print "\n\n%s" %(s1.center(80,'*'))
print "\n\n%s" %(s2.center(60,' '))
choice = int(raw_input("\n\nENTER CHOICE (1 or 2) AS STATED ABOVE "))
regex = re.compile(r'''(
        	(\d{1,2}/\d{1,2}/\d\d,\s\d{1,2}:\d\d\s\w\w)
        	\s\-\s
        	(.*?):
        	.*
        )''',re.VERBOSE)

files = glob.glob('WhatsApp Chat with *')
print "\n\n%s" %(s3.center(80,'*'))
for name in files:
	file = open(name, 'r')
	participants_message_count = {}
	participants_last_message_time = {}
	last_sender = ""
	permit_increment = True
	for line in file:
		for mo in regex.findall(line):
			if(choice == 2):
				datetime_object = datetime.strptime(mo[1], '%m/%d/%y, %I:%M %p')
				if(last_sender == mo[2] and (participants_last_message_time[mo[2]] == datetime_object)):
					permit_increment = False
				participants_last_message_time[mo[2]] = datetime_object

			if(permit_increment == True):
				if mo[2] in participants_message_count:
					participants_message_count[mo[2]] += 1
				else:
					participants_message_count[mo[2]] = 1

			last_sender = mo[2]
			permit_increment = True

	# print "\n\n%s" %(name.center(80,' '))
	print "\n\n%s" %(re.sub("\.txt","",name).center(80,' '))
	table = PrettyTable(['Name', 'Message Count'])
	for key in participants_message_count:
		table.add_row([key,participants_message_count[key]])
	print table.get_string(sortby="Message Count", reversesort=True)
