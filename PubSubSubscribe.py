import ipfshttpclient
import base64
import base58
import requests
import sqlite3
#database = sqlite3.connect('/home/douglasrfix/NewsService.db', isolation_level=None)
#database = sqlite3.connect('/home/douglasrfix/NewsService.db')
#cursor = database.cursor()
ipfs_server = ipfshttpclient.connect(timeout=(20.0, 20))
#uncommitedInserts = 1

#while True:

try:
    with ipfs_server.pubsub.subscribe('FreeSpeechNewsService') as subscription:
        for message in subscription:
            print(message)
            #print(message['data'])
            data = base64.standard_b64decode(message['seqno'])
            print(data)
            bdata = bytes(data)
            print(bdata)
            #string = base58.b58encode(data)
            #print(string)


                #cursor.execute('insert into PubSubMessage (Message, DTS) values(?, strftime("%Y-%m-%d %H:%M:%f","now"))', [str(message)])
                #if uncommitedInserts > 50:
                    #database.commit()
                    #uncommitedInserts = 0
                #else:
                    #uncommitedInserts +=1

except requests.exceptions.ConnectionError as e:
    print(e)
        #if uncommitedInserts > 0:
            #database.commit()
            #uncommitedInserts = 0

    #except KeyboardInterrupt:
        #database.commit()
        #database.close()
        #ipfs_serve.close()
        #break
finally:
    ipfs_serve.close()

#database.commit()
#database.close()
#ipfs_serve.close()

