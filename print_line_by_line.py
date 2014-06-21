'''This module that contains various methods to process data files.
'''
import numpy as np

def readasnumpy( filename ) :
    ''' This function takes in a textfile, and return a numpy array that is the transpose of what is loaded '''
    arr1 = np.loadtxt(filename)
    return arr1.T

def readlinebyline( filename ) :
    '''This function takes in a textfile, and reads line by line
    and prints to stdout.'''
    f = open(filename,'r')
    for line in f :
        print 'line=',line
    f.close()

def printtonewtext( filename ) :
    '''
    This function takes in a textfile (i.e. data1.txt), and prints the square of the second column to a new textfile data3.txt
    '''
    f = open(filename,'r')
    fw = open('data3.txt','w')
    for line in f :
        print >> fw, int(line.split()[1])**2
    fw.close()
    f.close()
