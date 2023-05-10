import numpy as np
import time
import matplotlib.pyplot as plt
import os
import errno

#Matris Boyutlari
n_vals = [100,500,1000,5000,10000]
# n_vals = [10,50,100,500,1000]

#Islemci sayilari
n_procs = [1,2,3,4] #[1,2,3,4]
pid_list = []

#Paralel hesaplamalarin sonuclarini saklayacak matrisler
parallel_times = np.zeros((len(n_procs), len(n_vals)))
speedup = np.zeros((len(n_procs), len(n_vals)))
efficiency = np.zeros((len(n_procs), len(n_vals)))

#Seri hesaplama suresini tutacak matris
serial_times = np.zeros(len(n_vals))

#Matrisleri olusturup seri hesaplama suresinin olcumu
for i, n in enumerate(n_vals):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    start_time = time.time()
    C = A + B
    end_time = time.time()

    serial_times[i] = end_time - start_time

#Paralel hesaplama surelerinin olcumu
for i, n in enumerate(n_vals):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    for j, p in enumerate(n_procs):
        start_time = time.time()

        #Child islem olusumu
        pid = []
        
        for k in range(p):
            pid.append(os.fork())
            #pid = os.fork()

        if pid[j] == 0:
        #if pid == 0:
            print("Child process started with PID: ",os.getpid())
            #Child islem, matris toplaminin hesabi
            C_chunk = A[k::p,:] + B[k::p,:]

            #Hesaplnan matrisi ana surec ile paylasimi
            os._exit(0)
        else:
            print("Parent process.Created child process with PID: ",pid)
            

        while len(pid_list) > 0:
            pid = pid_list.pop(0)
            os.waitpid(pid, 0)

        #Ana surec, tum child islemlerinin bitmesini bekler
        for k in range(p):
            while True:
                try:
                    os.waitpid(pid[k],0)
                    break
                except ChildProcessError as e:
                    if e.errno != errno.EINTR:
                        raise
            # os.waitpid(pid[k],0)

            

        end_time = time.time()

        parallel_times[j,i] = end_time - start_time
        speedup[j,i] = serial_times[i] / parallel_times[j,i]
        efficiency[j,i] = speedup[j,i] / p


#Grafiklerin cizdirilmesi

for i, p in enumerate(n_procs):
    plt.plot(n_vals, parallel_times[i,:], label=f'`{p} Processors')

plt.title('Time vs Matrix Size')
plt.xlabel('Matrix Size')
plt.ylabel('Time')
plt.legend()
plt.show()




for i, p in enumerate(n_procs):
    plt.plot(n_vals, speedup[i,:], label=f'`{p} Processors')

plt.title('Speedup vs Matrix Size')
plt.xlabel('Matrix Size')
plt.ylabel('Speedup')
plt.legend()
plt.show()

for i, p in enumerate(n_procs):
    plt.plot(n_vals, efficiency[i,:], label=f'{p} Processors')

plt.title('Efficiency and Matrix Size')
plt.xlabel('Matrix Size')
plt.ylabel('Efficiency')
plt.legend()
plt.show()            



for i, p in enumerate(n_procs):
    plt.plot(n_vals, serial_times[i,:], label=f'`{p} Processors')

plt.title('Time vs Matrix Size')
plt.xlabel('Matrix Size')
plt.ylabel('Time')
plt.legend()
plt.show()
