import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('newton-forward-interpolation-formula.webp')
imgplot = plt.imshow(img)
plt.show()

def main():
    n = int(input("Enter the number of values of x and y: "))
    x = []
    y = []
    i = n
    for i in range(n):
        x.append(float(input("Enter the value of x: ")))
        y.append(float(input("Enter the value of y: ")))

    print(x, y)

    h = x[1] - x[0]

    x0 = float(input("Enter the value of x for which you want to find the value of y: "))
    u = (x0 - x[0])/h
    temp = y
    yDiff = []
    diff(temp, yDiff, n)
    print(yDiff)
    print(newton_forward_interpolation(x, y, yDiff, u, h, n))


# For calculating delta ys
def diff(y, yDiff, n):
    if len(y) != n:
        yDiff.append(y[0])
    if (len(y) == 1):
        return
    yNew = []
    for i in range(len(y)):
        if i+1 == len(y):
            break
        yNew.append(y[i+1]-y[i])
    diff(yNew, yDiff, n)
# _________________________________________________________


# For calculating the value of y
def newton_forward_interpolation(x, y, yDiff, u, h, n):
    ans = y[0] + u*yDiff[0]
    for i in range(1, n-1):
        temp = u
        for j in range(1, i):
            temp *= u - j
        temp *= yDiff[i]
        temp /= fact(i + 1)
        ans += temp
    return ans
# _________________________________________________________

# For calculating the factorial
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
# _________________________________________________________

main()
