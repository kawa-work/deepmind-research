import re
import matplotlib.pyplot as plt

with open("/tmp/loss/sample.txt", mode="r") as f:
    s = f.read()

ext = re.findall('INFO:tensorflow:loss = ([0-9.]*), step = ([0-9]*)', s)

y, x = zip(*ext)
x = [float(s) for s in x]
y = [float(s) for s in y]
plt.plot(x, y)
plt.savefig('loss.png')

