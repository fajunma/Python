from numpy import matrix
from numpy import linalg
A = matrix([[1, 2], [3, 4]])
B = linalg.inv(A)


def numSquares( n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0]
    while len(dp) <= n:
        dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
        print(dp)
    return dp[n]

def travn(node):
    if node==None:
        return
    n = 2
    print(node)
    if node[1]+1 <= n:
        travn([node[0], node[1]+1])
    if node[0]+1 <= n:
        travn([node[0]+1, node[1]])


if __name__ == '__main__':
    print(B)
    print(numSquares(8))
    travn([0, 0])
