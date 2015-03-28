#!/usr/bin/python
import ctypes
import os,random,subprocess
from urlparse import parse_qs

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
PORT_NUMBER = 8081
vlc_pid = None

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):	
	#Handler for the GET requests
	def do_GET(self):
		global vlc_pid
		path = self.path
		parse = parse_qs(path[2:])
		print parse['function']
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		if((parse['function'][0])=="lock"):
			ctypes.windll.user32.LockWorkStation()
			# Send the html message
			self.wfile.write("PC Will be Locked")
			return
		if((parse['function'][0])=="friends"):
			if(vlc_pid):
				vlc_pid.kill()
			season = ("0"+str(random.randint(1,10)))[-2:]
			season_path = "H:\TV Series\Friends\Friends Season "+str(season)+" [720p]"
			random_file_path = random.choice(os.listdir(season_path))
			while(random_file_path[-4:]==".srt"):
				random_file_path = random.choice(os.listdir(season_path))
			print "Playing FRIENDS Episode"+random_file_path 
			vlc_pid = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe",season_path+"\\"+random_file_path])
			self.wfile.write("Random FRIENDS Episode Playing")
			return
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()