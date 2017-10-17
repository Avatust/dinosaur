# Puts together rest of the module and carries out indexing


### TODO:
    # index filenames too, maybe directories
    # MIME type of files or general reading of non-binary
    # make it error-proof


from .fileindexer import FileIndexer
from .keyindexer import KeyIndexer
from .tokenizer import tokenize
from .normalizer import normalize

import os
import glob

def index(root_directory, fileIndex, keyIndex, **kwargs):
    if ('extensions' in kwargs.keys()):
        for dirpath, dirs, filenames in os.walk(root_directory, topdown= True):
                for filename in filenames:
                    if (any(map(filename.endswith, kwargs['extensions']))):
                        fullName = os.path.join(dirpath, filename)
                        with open(fullName) as file:
                            fileID = fileIndex.addFile(fullName)
                            for word in normalize(tokenize(file.read())):
                                keyIndex.addEntry(word, fileID)
