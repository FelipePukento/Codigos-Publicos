
import os

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#
def jumpingOnClouds(c):
    count = 0
    x = 0
    while count < n-1:
        if count+2 < n and c[count+2] == 0:
            x += 1
            count+=2
        elif c[count+1] == 0 or count == n+1:
            x += 1
            count+=1
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))
  

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
