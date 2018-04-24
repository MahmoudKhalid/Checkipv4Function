#Created by Mahmoud Khalid
#My Profile : FB/mahmoud.banzema.1
#Checking IPv4 Function instead of inet_aton

def checkipv4(ipv4address):
	splitip = ipv4address.rsplit('.')
	resultcheckip = []
	if ipv4address.count('.') == 3 and len(splitip) == 4:
		for check in splitip:
			if check.isdigit() == True and int(check) < 255:
				resultcheckip.append("True")
			else:
				resultcheckip.append("False")
		isfalse = "False" in resultcheckip
		if isfalse == True:
			return "False"
		else:
			return "True"
	else:
		return "False"
