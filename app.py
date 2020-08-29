import qrcode
import random
import os

f= open("data.txt","w+")


def key_gen():
	sub_key="abcdefghijklmnopqrstuvwxyz0234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	key_len=23
	op =  "".join(random.sample(sub_key,key_len ))

	with open("1.txt", "a") as myfile:
		myfile.write(op+'\n')
	print(op)
	return op


def code_gen():
	ip=key_gen()
	img=qrcode.make(ip)

	img.save(ip+'.png')
	#return img.show('save.png')


for i in range(0,1000):
	code_gen()
	i-=1