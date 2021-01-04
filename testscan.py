import os
#try:
#    from os import scandir, walk
#except ImportError:
#    from scandir import scandir, walk
entrycwd = os.getcwd()
os.chdir('/home/douglasrfix/')
for entry in os.scandir(os.getcwd()):
   if not entry.name.startswith('.') and entry.is_file():
       #print(entry.name)
       if(entry.name.rfind(".json")) == 4:
           os.rename(entry.name,str(entry.name))
           print(entry.name)

os.chdir(entrycwd)