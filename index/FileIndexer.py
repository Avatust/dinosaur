
class FileIndexer():
  
  _indexPath = ""
  
  def __init__(self, path_to_index):
    self._index = {'counter' : 0}
    self.loadIndex(path_to_index)
  
  def getFilePath(self, fileID):
    return self._index[fileID]  # error otherwise
  
  def addFile(self, filePath):
    fileID = self._index['counter']
    self._index['counter']+=1
    self._index[fileID] = filePath
    return fileID
  
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
    
