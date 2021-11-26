import numpy as np

def StupidFunction(a,b):
    """
    Say something dumb about the inputs

    Parameters
    ----------
    a : string, one stupid thing
    b : string, other stupid thing

    Returns
    -------
    stupid : string,
        The truth about the two strings
    """
    
    plural=np.array([False,False])
    if a[len(a)-1]=='s':
        plural[0]=True
    if b[len(b)-1]=='s':
        plural[1]=True
    tobe={
        True: 'are',
        False: 'is'
        }
    stupid = a + " " + tobe[plural[0]] +" stupid and so " +tobe[plural[1]] + " " + b
    return stupid
    
if __name__ == '__main__':
    a, b = 'beans', 'your hat'
    truth = StupidFunction(a, b)
    print(truth)
