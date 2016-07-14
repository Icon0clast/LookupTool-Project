from os import *
import subprocess as sp
import time
from urllib import * 
from urllib.parse import *

def printMenu():
	print ("Lookup Tool v 1.1")
	print ("By - Joe Kulp 2016")
	print ()
	print ()
	print ("[1.]	Host Name a Lookup")
	print ("[2.]	Logged in User Lookup")
	print ("[3.]	User Name a Lookup")
	print ("[4.]	IP Address Lookup")
	print ("[5.]	Decode a Proofpoint URL")
	print ("[6.]	Exit Program")
	print 
	print ("Please make a selection: ",)
	return input()
 

def hostNameLookup(hostName): #Function invokes powershell script luHost.ps1 then parses the output
	psResult = sp.run([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe','-ExecutionPolicy','Unrestricted','.\luHost.ps1',hostName],
	stdout=sp.PIPE,
	stderr=sp.PIPE,
	universal_newlines=True)
	output = psResult.stdout
	error = psResult.stderr
	print ()
	print ()
	print (output)
	#print ("Return code given to Python script is: " + str(output)) ####ERRORCHECKING#####
	#print ("\n\nstderr: " + str(error)) ####ERRORCHECKING#####
	input("Press enter to return to main menu")
	time.sleep(1)
	return;

def loggedInUserLookup(loggedHost):
	psResult = sp.run([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe','-ExecutionPolicy','Unrestricted','.\luLoggedOnUser.ps1',loggedHost],
	stdout=sp.PIPE,
	stderr=sp.PIPE,
	universal_newlines=True)
	output = psResult.stdout
	error = psResult.stderr
	#print (output)
	loggedUser=(output)
	loggedUser=loggedUser.split('\n')[1] #Removes hostname from returned data
	userName=loggedUser
	userNameLookup(userName) #calls userNameLookup with loggedUser as arguments
	return;
	
def userNameLookup(userName): #Function invokes powershell script luUser.ps1 then parses the output
	psResult = sp.run([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe','-ExecutionPolicy','Unrestricted','.\luUser.ps1',userName],
	stdout=sp.PIPE,
	stderr=sp.PIPE,
	universal_newlines=True)
	output = psResult.stdout
	error = psResult.stderr
	print ()
	print ()
	print (output)
	#print ("Return code given to Python script is: " + str(output)) ####ERRORCHECKING#####
	#print ("\n\nstdout:\n\n" + str(output)) ####ERRORCHECKING#####
	#print ("\n\nstderr: " + str(error))
	input("Press enter to return to main menu")
	time.sleep(1)
	return;

def ipLookup(ipAddr):
	psResult = sp.run([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe','-ExecutionPolicy','Unrestricted','.\luIP.ps1',ipAddr],
	stdout=sp.PIPE,
	stderr=sp.PIPE,
	universal_newlines=True)
	output = psResult.stdout
	error = psResult.stderr
	print ()
	print ()
	print (output)
	#print ("Return code given to Python script is: " + str(output)) ####ERRORCHECKING#####
	#print ("\n\nstdout:\n\n" + str(output)) ####ERRORCHECKING#####
	#print ("\n\nstderr: " + str(error))
	input("Press enter to return to main menu")
	time.sleep(1)
	return;

	
def ppUrlDecode(ppUrl):
	url = urlparse(ppUrl)
	url = urllib.parse.parse_qs(url.query)['u'][0]
	url = url.replace('_', '/')
	url = url.replace('-', '%')
	url = urllib.parse.unquote(url)
	print (url)
	input("Press enter to return to main menu")
	return;


selection = printMenu()

while (selection != "6"):
	#os.system('cls')
	if selection == "1":
		print ("[+] You have selected Hostname lookup")
		print ("Please enter the Hostname or type BACK to return to main menu: ")
		hostName = input()
		if hostName != "BACK":
			print ("[+] Looking up " + hostName + " via Powershell")
			hostNameLookup(hostName) #print function hostNameLookup pass it hostName
	elif selection == "2":
		print ("[+] You have selected Logged in User Lookup")
		print ("Please enter the Hostname or type BACK to return to main menu: ")
		loggedHost = input()
		if loggedHost != "BACK":
			print ("[+] Looking up the user logged into " + loggedHost + " via Powershell")
			loggedInUserLookup(loggedHost) #print function loggedInUserLookup pass it userName)
	elif selection == "3":
		print ("[+] You have selected Username lookup")
		print ("Please enter the Username or type BACK to return to main menu: ")
		userName = input()
		if userName != "BACK":
			print ("[+] Looking up " + userName + " via Powershell")
			userNameLookup(userName) #print function userNameLookup pass it userName)
	elif selection == "4":
		print ("[+] You have selected IP Lookup")
		print ("Please enter the IP Address or type BACK to return to main menu: ")
		ipAddr = input()
		if ipAddr != "BACK":
			print ("[+] Looking up " + ipAddr + " via NSlookup")
			ipLookup(ipAddr)
	elif selection == "5":
		print ("[+] You have selected Proofpoint URL Decoding")
		print ("Please enter the URL to be decoded or type BACK to return to main menu: ")
		ppUrl = input()
		if ppUrl != "BACK":
			print ("[+] Decoding ProofPoint URL Please Wait...")
			time.sleep(.5)
			ppUrlDecode(ppUrl)
	print ("Returning to main menu")
	time.sleep(.5)
	os.system('cls')
	selection = printMenu()


	


