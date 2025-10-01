import psutil
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


times = []
cpu_vals = []
mem_vals = []
temp_vals = []
hum_vals = []

start_time = time.time()

def update(frame):
    t = int(time.time() - start_time)
    
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    temp = random.uniform(20, 40)  
    hum = random.uniform(30, 90)   
    

    times.append(t)
    cpu_vals.append(cpu)
    mem_vals.append(mem)
    temp_vals.append(temp)
    hum_vals.append(hum)

   
    plt.cla()
    plt.plot(times, cpu_vals, label="CPU %")
    plt.plot(times, mem_vals, label="Memory %")
    plt.plot(times, temp_vals, label="Temperature")
    plt.plot(times, hum_vals, label="Humidity")

    plt.ylim(0, 100)
    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.legend(loc="upper left")
    
    if t > 60:
        plt.xlim(t - 60, t)
    else:
        plt.xlim(0, 60)

ani = animation.FuncAnimation(plt.gcf(), update, interval=1000)
plt.show()
