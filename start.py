import getpass
import os

startupPath = r"C:/Users/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup".format(
    getpass.getuser())

currentDirectory = os.getcwd()
fileContent = r'''cd {} & env\Scripts\activate & py auto_joiner.py'''.format(currentDirectory)
print(fileContent)
with open((startupPath+'/teams_join.bat'), 'w+') as f:
    f.write(fileContent)
with open(('teams_join.bat'), 'w+') as f:
    f.write(fileContent)
