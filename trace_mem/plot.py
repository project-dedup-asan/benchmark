import numpy as np
from matplotlib import pyplot as plt

def RANGE(start, end, step):
	r = start
	while(r<end):
		yield r
		r += step

with open("w_asan12") as f:
	lines = f.readlines()
	y12 = [float(line.split()[0])/(1024*1024) for line in lines]
	x12 = list(RANGE(0, len(y12)/10, 0.1))

with open("wo_asan12") as f:
	lines = f.readlines()
	wy12 = [float(line.split()[0])/(1024*1024) for line in lines]
	wx12 = list(RANGE(0, len(wy12)/10, 0.1))

with open("wo_asan11") as f:
	lines = f.readlines()
	wy11 = [float(line.split()[0])/(1024*1024) for line in lines]
	wx11 = list(RANGE(0, len(wy11)/10, 0.1))

with open("w_asan1") as f:
	lines = f.readlines()
	y1 = [float(line.split()[0])/(1024*1024) for line in lines]
	x1 = list(RANGE(0, len(y1)/10-0.1, 0.1))


#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#ax1 = set_title("Memory Consumption")
#ax1 = set_xlabel('Time (s)')
#ax1 = set_ylabel('Memory (MB)')
#plt.plot(x3[:len(wy12)],y3[:len(wy12)], 'b')

y_asan_1_wo_asan11 = [y1[i]+wy11[i] for i in range(len(wy12))]

plt.plot(x12[:len(wy12)],y12[:len(wy12)], 'r', label= 'w/ ASan')
plt.plot(x1[:len(wy12)],y_asan_1_wo_asan11 , 'g', label='ideal')
plt.plot(wx12[:len(wy12)],wy12[:len(wy12)], 'b', label= 'w/o ASan')
plt.grid(b=True,which='both',axis='both')
plt.title('Memory Consumption',loc='center')
plt.xlabel('Time(s)')
plt.ylabel('Memory (MB)')
plt.xlim(-50, 630)
plt.legend()

#leg = ax1.legend()
plt.savefig('fig1.png', dpi=300)

