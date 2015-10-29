def lookandsay(n):
    integer = 1
    numInt = 1
    stringInt = str(integer)
    read = ""

    print integer

    for i in range(n-1):
        while len(stringInt) != 0:
            if len(stringInt) == 1:
                read += "1" + stringInt[0]
            else:
                print "executed else case"
                while stringInt[0] == stringInt[1]:
                    numInt += 1
                read += str(numInt) + stringInt[0]
                print "read is ", read
            stringInt = stringInt[numInt:]
        print int(read)
        stringInt = read
        print "stringInt is ", stringInt

def rotate(image):
    """
    Given an array that represents an image, rotates the image 90 degree clockwise.
    """
    # Debugging needed
    n = len(image)
    newImage = [[None]*n]*n
    for i in range(n):
        for j in range(n):
            newImage[n-1-j][i] = image[i][j]
            print i, " ", j
    return newImage

def nextLargest(n):
    """
    Takes in an integer n, and returns the next largest integer that can be created
    with the digits of n.
    """
    return

def num2s(N):
    """
    Returns the number of 2s that appear between 0 and N, inclusive.
    """
    return

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a%b)

if __name__ == "__main__":
    print gcd(0, 15)
