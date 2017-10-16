# an interface to the index

class KeyIndexer():
  
  _indexPath = ""
  
  def __init__(self, path_to_index):
    self.loadIndex(path_to_index)
  
  def lookUp(self, word):
    return {"set of indexed files IDs"}
  
  def addEntry(self, word, fileID):
    pass
  
  def loadIndex(self, path_to_index):
    #load index to memory
    self._indexPath = path_to_index
    pass
  
  def saveIndex(self, path_to_index = None):
    if (path_to_index == None):
      path_to_index = _indexPath

  
