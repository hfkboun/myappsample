text = open("/home/hfkboun/Desktop/midterm_results.txt").read().splitlines()

#print(text)
print("---------------------------------------------------------")
nlist=[]
for word in text:
	nlist += word.split(" ")

print(nlist)	

j=0
i=0
toplam=0.0
#print(len(nlist))
for i in range(int(len(nlist)/2)):
	if i==len(nlist) or i == (len(nlist)+1):
		break
	toplam = toplam+float(nlist[j+1])
	#print(nlist[j+1]+"   "+str(toplam))
	j=j+2
	

print("Average is: ",toplam/(len(nlist)/2)) 	
