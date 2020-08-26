import gzip

from demo_reader.util import writer
#opener is Alias for gzip.open main difference is gzip.open decompresses
#the file while reading and open doesn't !!
opener = gzip.open 


if __name__ == '__main__':
   writer.main(opener)
