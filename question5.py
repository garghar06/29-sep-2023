import matplotlib.pyplot as plt

with open("test.txt") as f:
    data = f.read()

data = data.split('\n')
print("data",data)
x = [int(row.split(' ')[0]) for row in data]
print("x",x)

y = [int(row.split(' ')[1]) for row in data]
print("y",y)
plt.plot(x, y)

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('SAMPLE GRAPH!')

plt.show()
