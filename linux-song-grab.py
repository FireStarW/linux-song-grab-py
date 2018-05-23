#linux grab-song python by uh me
#import obspython as obs
import dbus
import re
import os
import sys
from shutil import copyfile

bus = dbus.SessionBus()
serviceList = []
for service in bus.list_names():
	if re.match('org.mpris.MediaPlayer2.', service):
              serviceList.append(service)            

if not serviceList:
  print("No media players open")
  sys.exit()

#assume first loaded media player is one in use
player = dbus.SessionBus().get_object(serviceList[0], '/org/mpris/MediaPlayer2')

metadata = None
#check if current data us different
try:
	while (True):
	#	try:
			while ( (player.Get('org.mpris.MediaPlayer2.Player', 'Metadata', dbus_interface='org.freedesktop.DBus.Properties') != metadata)): 
				metadata = player.Get('org.mpris.MediaPlayer2.Player', 'Metadata', dbus_interface='org.freedesktop.DBus.Properties')

				#raw metadata output
				#for attr, value in metadata.items():
				#	print(attr, '\t', value)

				#create tag strings
				stringTitle = metadata['xesam:title'] if 'xesam:title' in metadata else ''
				print(stringTitle)

				stringArtist = metadata['xesam:artist'] if 'xesam:artist' in metadata else ''
				stringArtist = stringArtist[0]
				print(stringArtist)

				stringAlbum = metadata['xesam:album'] if 'xesam:album' in metadata else ''
				print(stringAlbum)

				stringArt = metadata['mpris:artUrl'] if 'mpris:artUrl' in metadata else ''
				print(stringArt)

				stringDate = metadata['year'] if 'year' in metadata else ''
				stringDate = str(stringDate)
				print(stringDate)

				#write text files and make album art copy
				oneLinerText = open('oneLiner.txt','w')
				oneLinerString = ''
				if stringTitle:
					oneLinerString += stringTitle
				if stringArtist:
					oneLinerString += " - " + stringArtist	
				if stringAlbum:
					oneLinerString += " - " + stringAlbum	
				if stringDate:
					oneLinerString += " - " + stringDate										
				oneLinerText.write(oneLinerString)

				artistText = open('artist.txt','w')
				artistText.write(stringArtist)
				titleText = open('title.txt','w')
				titleText.write(stringTitle)
				albumText = open('album.txt','w')
				albumText.write(stringAlbum)
				yearText = open('year.txt','w')
				yearText.write(stringDate)

				#close files
				artistText.close()
				titleText.close()
				albumText.close()
				yearText.close()
				oneLinerText.close()
				
				if stringArt:
					sourceArt = "/" + stringArt[8:]
				else: 
					sourceArt = "default.gif" 
					
				copyfile(sourceArt, "albumArt")

except KeyboardInterrupt:
    pass

except dbus.DBusException:
	#media player is closed
	print("Media players closed")
	sys.exit()
