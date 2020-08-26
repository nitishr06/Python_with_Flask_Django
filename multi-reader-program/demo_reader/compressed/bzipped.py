import bz2

from demo_reader.util import writer
#opener is Alias for bzip.open main difference is gzip.open decompresses
#the file while reading and open doesn't !!
opener = bz2.open 


if __name__ == '__main__':
    writer.main(opener)   
