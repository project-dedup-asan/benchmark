import numpy as np
from matplotlib import pyplot as plt


def RANGE(start, end, step):
	r = start
	while(r<end):
		yield r
		r += step

plt.grid(b=True,which='both',axis='both')
plt.title('Memory Consumption per Target Instance',loc='center')
plt.xlabel('Time(s)')
plt.ylabel('Memory (MB)')

with open("w_asan1") as f:
	lines = f.readlines()
	y1 = [float(line.split()[0])/(1024*1024) for line in lines]
	x1 = list(RANGE(0, len(y1)/10-0.1, 0.1))

with open("w_asan3") as f:
	lines = f.readlines()
	y3 = [float(line.split()[0])/(1024*1024) for line in lines]
	x3 = list(RANGE(0, len(y3)/10-0.1, 0.1))

with open("w_asan6") as f:
	lines = f.readlines()
	y6 = [float(line.split()[0])/(1024*1024) for line in lines]
	x6 = list(RANGE(0, len(y6)/10-0.1, 0.1))

with open("w_asan12") as f:
	lines = f.readlines()
	y12 = [float(line.split()[0])/(1024*1024) for line in lines]
	x12 = list(RANGE(0, len(y12)/10-0.1, 0.1))

with open("wo_asan1") as f:
	lines = f.readlines()
	wy1 = [float(line.split()[0])/(1024*1024) for line in lines]
	wx1 = list(RANGE(0, len(wy1)/10-0.1, 0.1))

with open("wo_asan3") as f:
	lines = f.readlines()
	wy3 = [float(line.split()[0])/(1024*1024) for line in lines]
	wx3 = list(RANGE(0, len(wy3)/10-0.1, 0.1))

with open("wo_asan6") as f:
	lines = f.readlines()
	wy6 = [float(line.split()[0])/(1024*1024) for line in lines]
	wx6 = list(RANGE(0, len(wy6)/10-0.1, 0.1))

with open("wo_asan12") as f:
	lines = f.readlines()
	wy12 = [float(line.split()[0])/(1024*1024) for line in lines]
	wx12 = list(RANGE(0, len(wy12)/10-0.1, 0.1))

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

#leg = ax1.legend()
topics = ['1', '3', '6', '12']
y = [y1[len(y1)-1], y3[len(y3)-1], y6[len(y6)-1], y12[len(y12)-1]]
wy = [wy1[len(wy1)-1], wy3[len(wy3)-1], wy6[len(wy6)-1], wy12[len(wy12)-1]]



value_a_x = create_x(2, 0.8, 1, 4)
value_b_x = create_x(2, 0.8, 2, 4)
ax = plt.subplot()
ax.bar(value_a_x, wy, color='blue', label = 'w/o ASan')
ax.bar(value_b_x, y, color='red', label = 'w/ ASan')
middle_x = [(a+b)/2 for (a,b) in zip(value_a_x, value_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(topics)
plt.legend()

plt.savefig('fig2.png', dpi=300)

