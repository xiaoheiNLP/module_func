# -*-coding:utf-8-*-
import pickle

class data_readOrwrite():
    def data_read(self, filename):
        fopen = open(filename, 'rb')
        mydata = pickle.load(fopen)
        return mydata

    def data_write(self, filename, mydata):
        fopen = open(filename, 'wb')
        pickle.dump(mydata, fopen)
        fopen.close()


if __name__ == '__main__':
    print()

