from sense_hat import SenseHat
from time import sleep
import pygame
import os

#Created by Marco G @Dragonspeed3000
#GNU General Public License

os.chdir("InstruSon")
sense = SenseHat()

X = [255, 255, 255]
O = [0, 0, 0]
S = [0, 0, 255]
A = [255, 0, 0]

Logo = [
  O, S, S, S, O, O, O, O,
  S, O, O, O, O, O, O, O,
  O, S, S, O, O, O, O, O,
  O, O, O, S, O, A, A, O,
  S, S, S, O, X, O, O, A,
  O, X, O, X, O, A, A, A,
  X, O, X, O, A, O, O, A,
  O, X, O, O, O, A, A, A]

Ab = [
  O, O, O, O, O, O, O, O,
  O, X, X, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, X, O, O,
  X, O, O, X, O, X, O, O,
  X, X, X, X, O, X, X, X,
  X, O, O, X, O, X, O, X,
  X, O, O, X, O, X, X, X]

A = [
  O, O, O, O, O, O, O, O,
  O, X, X, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, X, X, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, O, O, O]

Bb = [
  O, O, O, O, O, O, O, O,
  X, X, X, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, X, O, O,
  X, X, X, O, O, X, O, O,
  X, O, O, X, O, X, X, X,
  X, O, O, X, O, X, O, X,
  X, X, X, O, O, X, X, X]
  
B = [
  O, O, O, O, O, O, O, O,
  X, X, X, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, X, X, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, X, X, O, O, O, O, O]
 
C = [
  O, O, O, O, O, O, O, O,
  O, X, X, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  O, X, X, O, O, O, O, O]

Db = [
  O, O, O, O, O, O, O, O,
  X, X, X, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, X, O, O,
  X, O, O, X, O, X, O, O,
  X, O, O, X, O, X, X, X,
  X, O, O, X, O, X, O, X,
  X, X, X, O, O, X, X, X]

D = [
  O, O, O, O, O, O, O, O,
  X, X, X, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, X, X, O, O, O, O, O]

Eb = [
  O, O, O, O, O, O, O, O,
  X, X, X, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, X, O, O,
  X, X, X, O, O, X, O, O,
  X, O, O, O, O, X, X, X,
  X, O, O, O, O, X, O, X,
  X, X, X, O, O, X, X, X]

E = [
  O, O, O, O, O, O, O, O,
  X, X, X, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, X, X, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, X, X, O, O, O, O, O]

F = [
  O, O, O, O, O, O, O, O,
  X, X, X, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, X, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, O, O, O, O, O, O]

Gb = [
  O, O, O, O, O, O, O, O,
  O, X, X, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, O, O, X, O, O,
  X, O, X, X, O, X, O, O,
  X, O, O, X, O, X, X, X,
  X, O, O, X, O, X, O, X,
  O, X, X, O, O, X, X, X]

G = [
  O, O, O, O, O, O, O, O,
  O, X, X, O, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, O, O, O, O, O,
  X, O, X, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  X, O, O, X, O, O, O, O,
  O, X, X, O, O, O, O, O]

listeImg = [Ab, A, Bb, B, C, Db, D, Eb, E, F, Gb, G]
sense.clear()
modifInstru = False
selNote = 0
nbInstru = 4
selInstru = 0
listeSelec = []
listeInstru = ["Cla", "Trb", "Gtr", "Vl"]
listeSound = []

pygame.mixer.init()
sense.set_pixels(Logo)
sleep(5)
sense.show_message("H/B : INSTRU", text_colour=[255, 100, 100])
sense.show_message("D/G : NOTE", text_colour=[100, 100, 255])
sense.set_pixels(listeImg[selNote])

while (True):
	event = sense.stick.wait_for_event(emptybuffer=True)
	sleep(0.1)
	event = sense.stick.wait_for_event()
	
	if (event.direction == "up"):
		selInstru += 1
		
		modifInstru = True
	if (event.direction == "down"):
		selInstru -= 1
		
		modifInstru = True
	if (event.direction == "right"):
		selNote += 1
		
	if (event.direction == "left"):
		selNote -= 1
		
	if ((event.direction == "middle") and (event.action == "released")):
		# On valide un choix
		if ([selInstru, selNote] in listeSelec):
			# Deselection
			listeSelec.remove([selInstru, selNote])
		else:
			# Selection
			listeSelec.append([selInstru, selNote])

	if ((event.direction == "middle") and (event.action == "held")):
		# On joue les sons
		for choix in listeSelec:
			nom = str(choix[0]+1)+"_"+str(choix[1]+1)+".ogg"
			listeSound.append(pygame.mixer.Sound(nom))
		for objSound in listeSound:
			objSound.play()
		sleep(2)
		listeSound = []
		listeSelec = []
	selNote = selNote % 12
	selInstru = selInstru % nbInstru
	if (modifInstru): # Message nouvel Instru
		sense.show_message(listeInstru[selInstru], 0.055)
		modifInstru = False
	sense.set_pixels(listeImg[selNote])
	
	if ([selInstru, selNote] in listeSelec): # Utilisation du selec pour afficher un feedback visuel
		sense.set_pixel(7, 0, 255, 255, 255)
	else:
		sense.set_pixel(7, 0, 0, 0, 0)
