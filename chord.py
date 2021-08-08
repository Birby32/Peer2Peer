class ChordNode:

  # constructor
  def __init__(self):
    # each node has a key table
    self.key_table = {}
    # each node has an ID
    # needs to be intialized to a random value
    self.nodeID = None
    # this nodeset should come from server right?
    self.nodeSet = []
    # finger table
    self.FT = {}

  # from slides
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

  def ping():
    """
    Returns when the server is ready.
    """
    return ''

  def keys(self):
    """
    Returns all keys stored on THIS node in plain text
    """
    print("Key Table:")
    for key in self.key_table:
      print(key, ":", self.key_table[key][0], self.key_table[key][1])
      print()

  def get(self, key):
    """
    Returns the value for the key stored in this DHT or an empty response
    if it doesn't exist.
    """
    if key in self.key_table:
      return self.key_table[key]
    return ()

  def put(key):
    """
    Upserts the key into the DHT. The value is equal to the body of the HTTP
    request.
    """
    raise NotImplemented

  def delete(self, key):
    """
    Deletes the key from the DHT if it exists, noop otherwise.
    """
    if key in self.key_table:
      del self.key_table[key]
      return 1
    return 0

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