import os
import ipfshttpclient
import datetime
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

entrycwd = os.getcwd()
os.chdir('/home/douglasrfix/')
#print(datetime.datetime.now())
ipfsserver = ipfshttpclient.connect()
returned_dictionary = ipfsserver.add('Test.json',pin=True)
#print(returns)
ipfspath = '/ipfs/'+ returned_dictionary['Hash']
ipnsname = ipfsserver.name.publish(ipfspath)
#print(ipnsname)
ipfsserver.pubsub.publish('IntraGalacticMediaService', str(ipnsname))
ipfsserver.close()
os.chdir(entrycwd)
#print(datetime.datetime.now())



#ipfs_server.pubsub.publish('PrairieObserver', message_data)