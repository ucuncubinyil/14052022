import time
import random

baslangic = time.time( )
dd1 = random.sample( range( 0, 5000000 ), 5000000 )
cifts = list()

for item in dd1:
	if item %2 ==0:
		cifts.append(item)

bitis =  time.time()
print(f"For : {bitis-baslangic}")
####################################


baslangic = time.time( )
cifts = (list(filter(lambda  x:x%2==0, dd1)))

bitis =  time.time()
print(f"Filter : {bitis-baslangic}")

#######################################

baslangic = time.time( )

cifts = [item for item in dd1 if item%2==0] # best metod
bitis =  time.time()

print(f"For-OneLine : {bitis-baslangic}")