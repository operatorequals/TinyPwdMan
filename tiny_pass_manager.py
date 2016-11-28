#!/usr/bin/env python
import sys, getpass, hashlib, clipboard, pprint
ArgumentLetters='ACVEL'
def usage ():	print "Usage:\n\t%s key_db_file %s [service] [username]" % (sys.argv[0], '|'.join(ArgumentLetters))
def xor(s1, s2): s2=s2*((len(s1) / 512) + 1) ; return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
def get_inputs( messages ): return [raw_input(messages[i]) for i in range(len(messages))]
if len(sys.argv) < 3 : usage(); sys.exit(-1);
def open_key_db() : 
	try :
		encr_key_db = open( sys.argv[1], 'r' ).read().decode('base64')
		passwd = hashlib.sha512( getpass.getpass("*** Master Password*** :") ).hexdigest()
	except : return dict(); 
	return dict([( line.split(':',2)[0], (line.split(':',2)[1], line.split(':',2)[2])) for line in xor( encr_key_db, passwd ).splitlines() ])
KeyDB = open_key_db()
def save_key_db() :
	passwd = hashlib.sha512( getpass.getpass("*** Master Password*** :") ).hexdigest()
	key_db_file = open( sys.argv[1], 'w' )
	key_db_file.write( xor( '\n'.join(["%s:%s:%s"%(k,v[0],v[1]) for k,v in KeyDB.iteritems()]), passwd ).encode('base64') )
def addKey() :
	inputs = get_inputs( ["Service: ", "Username: ", "Password: ", "Retype Password: "] )
	if inputs[2] == inputs[3] : KeyDB[inputs[0]] = (inputs[1], inputs[2])
def getKey() :
	if (len(sys.argv) == 5) and (KeyDB[sys.argv[3]][0] == sys.argv[4]) :
		clipboard.copy( (KeyDB[ sys.argv[3]]) [1] )
def listKeyDB() : pprint.pprint(KeyDB)
def editKey() :
	if (len(sys.argv) == 5) and (KeyDB[sys.argv[3]][0] == sys.argv[4]) :
		new_passwd = get_inputs( ["Password: ", "Retype Password: "] )
		if len(set(new_passwd)) == 1 : KeyDB[sys.argv[3]][0] = new_passwd[0]
funcDict = {'A' : [addKey, save_key_db],
			'C' : [getKey],
			'L' : [listKeyDB],
			'E' : [editKey, save_key_db]} 
for func in funcDict[sys.argv[2]] : func();