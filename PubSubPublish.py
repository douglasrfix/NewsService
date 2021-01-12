import datetime
import ipfshttpclient
message_data = 'hello'
network = ipfshttpclient.connect(timeout=(20.0, 86400.0))
print(datetime.datetime.now())
for x in range(1):
    network.pubsub.publish('IntraGalacticMediaService', message_data)

print(datetime.datetime.now())
network.close()
