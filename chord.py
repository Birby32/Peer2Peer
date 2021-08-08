def ping():
  """
  Returns when the server is ready.
  """
  return ''

def keys():
  """
  Returns all keys stored on THIS node in plain text separated by a carriage
  return and a new line:
    <key1>\r\n<key2>\r\n...
  """
  raise NotImplemented

def get(key):
  """
  Returns the value for the key stored in this DHT or an empty response
  if it doesn't exist.
  """
  return key

def put(key):
  """
  Upserts the key into the DHT. The value is equal to the body of the HTTP
  request.
  """
  raise NotImplemented

def delete(key):
  """
  Deletes the key from the DHT if it exists, noop otherwise.
  """
  raise NotImplemented

def peers():
  """
  Returns the names of all peers that form this DHT in plain text separated by
  a carriage return and a new line:
    <peer1>\r\n<peer2>\r\n
  """
  raise NotImplemented

def join():
  """
  Join a new DHT. If this node is already a member of a DHT, leave that
  DHT cooperatively. At least one node of the DHT that we are joining will
  be present in the request body.
  HTTP request body will look like:
    <name1>:<host1>:<port1>\r\n<name2>:<host2>:<port2>...
  """
  raise NotImplemented

def leave():
  """
  Leave the current DHT. This request should only retrn the DHT this node
  is leaving has stabilized and this node is a standalone node now; noop is
  not part of any DHT.
  """
  raise NotImplemented