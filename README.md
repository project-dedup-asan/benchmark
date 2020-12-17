# Benchmark
---
## Description
To figure out the memory usage while fuzzing, we make a benchmark.

## How to
To trace the memory usage with respect to fuzzing instances enabled ASan, please follow the command line as shown below.

```bash
# example
$ ./honggfuzz/hongfuzz -t 60 -n ${num_instance} -S --input ${input} -- ${program} & ./benchmark.py

```

## BPF
To trace the madivse(..., MADV_MERGEABLE), we design BPF program that probes `ksm_madvise()`. To run this program, please follow the command line as shown below. It should be run before running a fuzzer.

```bash
# example
$ sudo ./bpf_ksm/trace_ksm_madvise.py

# Trace Logg
# ./honggfuzz/honggfuzz -t 60 -n 3 -S --input honggfuzz/examples/openssl/corpus_client -- openssl-master.client
# TIME     PID    COMM             COUNT
# 16:07:29 8049   7                1
# 17:07:29 8049   7                2
# 17:07:29 8049   7                3
# 17:07:29 8049   7                4
# 17:07:29 8047   7                5
# 17:07:29 8047   7                6
# 17:07:29 8047   7                7
# 17:07:29 8048   7                8
# 17:07:29 8048   7                9
# 17:07:29 8048   7                10
# 17:07:29 8048   7                11
# 17:07:29 8047   7                12
# 17:07:29 8049   7                13
# 17:07:29 8048   7                14
# 17:07:29 8047   7                15
# 17:07:29 8049   7                16
# 17:07:29 8048   7                17
# 17:07:29 8047   7                18
# 17:07:29 8049   7                19
# 17:07:29 8049   7                20
# 17:07:29 8049   7                21
# 17:07:29 8048   7                22
# 17:07:29 8048   7                23
# 17:07:29 8049   7                24
# 17:07:29 8048   7                25
# 17:07:29 8047   7                26
# 17:07:29 8047   7                27
# 17:07:29 8048   7                28
# 17:07:29 8047   7                29
# 17:07:29 8049   7                30
# 17:07:29 8047   7                31
# 17:07:29 8048   7                32
# 17:07:29 8047   7                33
# 17:07:29 8049   7                34
# 17:07:29 8047   7                35
# 17:07:29 8048   7                36

```
