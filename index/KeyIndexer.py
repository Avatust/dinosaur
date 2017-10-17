# an interface to the index

### TODO:
  # error-proofness
  # indent

import pickle
from os.path import isfile

class KeyIndexer():
  
  _indexPath = ""
  
  def __init__(self, path_to_index):
    self._index = dict()
    self.loadIndex(path_to_index)
  
  def lookUp(self, word):
    return self._index.get(word, set())   # returns the set of fileIDs or an empty set
  
  def addEntry(self, word, fileID):
    if word in self._index.keys():
      self._index[word].add(fileID)
     else:
      self._index[word] = {fileID,}
  
  def loadIndex(self, path_to_index):
    #load index to memory
    self._indexPath = path_to_index
    if isfile(path_to_index):
      with open(path_to_index) as file:
        self._index = pickle.load(file)
  
  def saveIndex(self, path_to_index = None):
    if (path_to_index == None):
      path_to_index = _indexPath
    with open(path_to_index, 'wb') as file:
      pickle.dump(self._index, file)
    

  
