import ipfshttpclient
import base64
import base58
import requests
import sqlite3
sqlpart1 = 'insert into pubsubmessage (author_peerID, IPNS_name, message_seqno, topicIDs_list, dts, raw_message) '
sqlpart2 = 'values(?, ?, ?, ?, strftime("%Y-%m-%d %H:%M:%f","now"), ?)'
sql_statement = sqlpart1 + sqlpart2

#database = sqlite3.connect('/home/douglasrfix/IntraGalacticMediaService.db', isolation_level=None)
database = sqlite3.connect('/home/douglasrfix/IntraGalacticMediaService.db')
cursor = database.cursor()
ipfs_server = ipfshttpclient.connect(timeout=(20.0, 400))
#uncommitedInserts = 1

#while True:

try:
    with ipfs_server.pubsub.subscribe('IntraGalacticMediaService') as subscription:
        for message in subscription:

            decoded_message_from = base64.standard_b64decode(message['from'])
            base58_encoded_author_peerID = base58.b58encode(decoded_message_from) #BITCOIN_ALPHABET
            decoded_IPNS_name = base64.standard_b64decode(message['data'])
            decoded_seqno = int.from_bytes(base64.standard_b64decode(message['seqno']), byteorder='big', signed=False)
            string_topicIDs_list = str(message['topicIDs'])
            string_message = str(message)
            cursor.execute(sql_statement, [base58_encoded_author_peerID, decoded_IPNS_name, decoded_seqno, string_topicIDs_list, string_message])
            database.commit()

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
    ipfs_server.close()

#database.commit()
#database.close()
#ipfs_serve.close()

