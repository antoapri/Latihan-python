print("\n",10*"=","soal ke1",10*"=","\n")
#----0++++5----8++++11----
inputuser = float(input('masukan angka lebih dari 0 kurang dari 5 \ndan lebih dari 8 kurang dari 11 ='))

isLebihdari0 = (inputuser > 0)
isLebihdari8 = (inputuser > 8)
isKurangdari5 = (inputuser <5)
isKurangdari11 = (inputuser <11)

print("lebih dari 0=",isLebihdari0)
print("kurang dari 5=",isKurangdari5)
print("lebih dari 8=",isLebihdari8)
print("kurang dari 11=",isKurangdari11)

banding = isLebihdari0 and isKurangdari5 or isLebihdari8 and isKurangdari11 
print ("angka yang anda masukan =", banding)

print("\n",10*"=","soal ke2",10*"=","\n")
#++++0----5++++8----11++++
inputuser = float(input('masukan angka kurang dari 0 atau lebih dari 5 \ndan kurang dari 8 atau lebih dari 11 ='))

isLebihdari5 = (inputuser > 5)
isLebihdari11 = (inputuser > 11)
isKurangdari0 = (inputuser <0)
isKurangdari8 = (inputuser <8)

print("kurang dari 0=",isKurangdari0)
print("lebih dari 5=",isLebihdari5)
print("kurang dari 8=",isKurangdari8)
print("leboih dari 11=",isLebihdari11)

banding = isKurangdari0 or isLebihdari5 and isKurangdari8 or isLebihdari11
print ("angka yang anda masukan =", banding)
