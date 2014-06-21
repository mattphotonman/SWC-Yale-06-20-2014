'''
This contains simple plotting tools 
'''
import pylab as plb
import numpy as np

def plot_in_line( myarray, figname='fig1' ) :
    '''Expects a 2xN numpy array, and saves our figure'''

    plb.plot(myarray[0],myarray[1],c='r',ls=':')
    plb.savefig(figname) 

if __name__ == "__main__":
    '''Checks if we're just running plot_my_data.'''
    myarray = np.array([range(10),[i**2 for i in range(10)]])
    plot_in_line(myarray)
