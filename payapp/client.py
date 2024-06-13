from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift_timestamp import TimestampService

def get_timestamp():
    transport = TSocket.TSocket('localhost', 10000)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = TimestampService.Client(protocol)

    transport.open()
    timestamp = client.getCurrentTimestamp()
    transport.close()
    
    return timestamp
