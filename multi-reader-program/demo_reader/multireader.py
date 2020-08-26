# demo_reader/multireader

import os

from demo_reader.compressed import bzipped, gzipped

extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}
class MultiReader:
   #init method is for intialization
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1] 
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')   
    #close method to close the opened file
    def close(self):
        self.f.close()
    #read method to read the file which is opened 
    def read(self):
        return self.f.read()
    