'''
Look at this https://en.m.wikipedia.org/wiki/Chord_(peer-to-peer) for more intformation about chords(a DHT protocol)
'''

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

#From Slide 14 in Naming Slides for Class CECS 327
class ChordNode:
  def finger(self, i):
    succ = (self.nodeID + pow(2, i-1)) % self.MAXPROC # succ(p+2ˆ(i-1))
    lwbi = self.nodeSet.index(self.nodeID) # self in nodeset
    upbi = (lwbi + 1) % len(self.nodeSet) # next neighbor
    for k in range(len(self.nodeSet)): # process segments
      if self.inbetween(succ, self.nodeSet[lwbi]+1, self.nodeSet[upbi]+1):
        return self.nodeSet[upbi] # found successor
      (lwbi,upbi) = (upbi, (upbi+1) % len(self.nodeSet)) # next segment

  def recomputeFingerTable(self):
    self.FT[0] = self.nodeSet[self.nodeSet.index(self.nodeID)-1] # Pred.
    self.FT[1:] = [self.finger(i) for i in range(1,self.nBits+1)] # Succ.

  def localSuccNode(self, key):
    if self.inbetween(key, self.FT[0]+1, self.nodeID+1): # in (FT[0],self]
      return self.nodeID # responsible node
    elif self.inbetween(key, self.nodeID+1, self.FT[1]): # in (self,FT[1]]
      return self.FT[1] # succ. responsible
    for i in range(1, self.nBits+1): # rest of FT
      if self.inbetween(key, self.FT[i], self.FT[(i+1) % self.nBits]):
        return self.FT[i]