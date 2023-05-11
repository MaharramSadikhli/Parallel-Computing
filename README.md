# Parallel Computing
 Parallel Computing via GPU and CPU
 Developed and Written by Maharram Sadikhli
 
INFORMATION REQUIRED FOR PARALLELIZATION ON CPU
The performance gain with parallelization depends on the number of processors/cores,
matrix size and parallelization algorithm. More processors/cores, larger matrix sizes,
and the appropriate parallelization algorithm result in greater acceleration and efficiency
gains.
However, in some cases parallelization can be slower or less efficient than serial
processing. These situations can be caused by device resources that do not meet the
requirements of the parallelization process, not enough hardware.

MATRIX SIZE SELECTION
The larger the matrix sizes we are going to parallelize, the more intensive the matrix
aggregation becomes and the greater the processing time. Therefore, the parallelization
process becomes even more important as the matrix sizes increase. I chose the matrix
sizes as 100, 500, 1000, 5000 and 10000.

1). 100 dimensional matrices are suitable for parallelization.
is size. Although the processing time is quite short,
A significant acceleration can be achieved with the parallelization process.
2). 500-dimensional matrices are more suitable for parallelization.
is size. Because the processing time is longer, parallelization
Greater acceleration can be achieved with the process.
3). 1000 dimensional matrices are too dense for parallelization
It can be a transaction. However, adequate hardware and proper parallelization
If I use the algorithm, I can achieve significant speedup.
4). 5000 dimensional matrices is a very challenging dimension for parallelization.
However, I can achieve acceleration by using multiple processors or cores and using a
good parallelization algorithm.
5). 10000 dimensional matrices are the most challenging dimension for parallelization.

Even if sufficient hardware and appropriate algorithm are provided, lower efficiency may
occur compared to serial processing.


RESULT FROM THE STUDY
I've found that parallel computing costs pretty fast because GPUs have a high number
of processing units. Especially in operations on big data discovery, the performance of
GPUs was much higher compared to CPUs. I've also had ones that are pretty fast at
these types of operations as GPUs have hardware that's particularly aggressive in
terms of graphics processing.

Click on the link below for a more detailed explanation of the results: https://silent-rose-d11.notion.site/README-732512e96fc74555954951bbe316041a



