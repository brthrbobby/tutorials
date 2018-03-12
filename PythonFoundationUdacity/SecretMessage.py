
import os

#TODO get file names
content = os.listdir(r"C:\Users\Bobby Musser\python prank tutorial")
#print(content)

#Change working directory to where the files are located
currentDir = os.getcwd()
os.chdir(r"C:\Users\Bobby Musser\python prank tutorial")
#create translation table (imput, output, things to be deleted)
dictTrans = str.maketrans('', '', '0123456789')
#print(dictTrans)

#TODO for each file rename files by removing numbers
for fileName in content:
    os.rename(fileName, fileName.translate(dictTrans))

#Go back to original working directory
os.chdir(currentDir)



