
import numpy as np
import time
import matplotlib.pyplot as plt
import pyopencl as cl

# Matris boyutları
n_vals = [100, 500, 1000, 5000, 10000]

# İşlemci sayıları
n_procs = [1, 2, 3, 4]

# GPU kullanarak paralel hesaplamaların sonuçlarını saklayacak matrisler
parallel_times = np.zeros((len(n_procs), len(n_vals)))
speedup = np.zeros((len(n_procs), len(n_vals)))
efficiency = np.zeros((len(n_procs), len(n_vals)))

# Seri hesaplama süresini tutacak matris
serial_times = np.zeros(len(n_vals))

# Matrisleri oluştur ve seri hesaplama süresini ölç
for i, n in enumerate(n_vals):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    
    start_time = time.time()
    C = A + B
    end_time = time.time()
    
    serial_times[i] = end_time - start_time

# Paralel hesaplama sürelerini ölç
for i, n in enumerate(n_vals):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    C = np.zeros((n, n))
    
    for j, p in enumerate(n_procs):
        # GPU ile paralel hesaplama

        ctx = cl.create_some_context()
        queue = cl.CommandQueue(ctx)
        
        A_buf = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=A)
        B_buf = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=B)
        C_buf = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, C.nbytes)
        
        kernel_code = """
            __kernel void add_matrices(__global const float *A,
                                       __global const float *B,
                                       __global float *C)
            {
                int i = get_global_id(0);
                int j = get_global_id(1);
                
                int n = get_global_size(0);
                int m = get_global_size(1);
                
                C[i * n + j] = A[i * n + j] + B[i * n + j];
            }
        """
        
        prg = cl.Program(ctx, kernel_code).build()
        start_time = time.time()
        
        # Paralel hesaplama
        global_size = (n, n)
        local_size = None
        prg.add_matrices(queue, global_size, local_size, A_buf, B_buf, C_buf)
        cl.enqueue_copy(queue, C, C_buf)
        
        end_time = time.time()
        
        parallel_times[j,i] = end_time - start_time
        speedup[j,i] = serial_times[i] / parallel_times[j,i]
        efficiency[j,i] = speedup[j,i] / p

# Grafikleri çizdir

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


# for i, p in enumerate(n_procs):
#     plt.plot(n_vals, speedup[i,:], label=f'{p} Processors')

# plt.title('Speedup vs Matrix Size')
# plt.xlabel('Matrix Size')
# plt.ylabel('Speedup')
# plt.legend()
# plt.show()