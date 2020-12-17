#!/usr/bin/python
#

from __future__ import print_function
from bcc import BPF
from time import strftime

bpf_text = """
#include <uapi/linux/ptrace.h>
#include <linux/mm.h>
#include <linux/sched.h>

struct data_t {
  u32 pid;
  u32 count;
  char comm[TASK_COMM_LEN];
};

BPF_PERF_OUTPUT(events);

int trace_ksm_madvise(struct pt_regs *ctx)
{
  struct data_t data = {};

  u32 pid = bpf_get_current_pid_tgid() >> 32;
  data.pid = pid;
  bpf_get_current_comm(&data.comm, sizeof(data.comm));
  data.count = 1;

  events.perf_submit(ctx, &data, sizeof(data));

  return 0;
}
"""

b = BPF(text=bpf_text)
b.attach_kprobe(event="ksm_madvise", fn_name="trace_ksm_madvise")

#header
print("%-8s %-6s %-16s %-8s" % ("TIME", "PID", "COMM", "COUNT"))

count = 0

#process event
def print_event(cpu, data, size):
    global count
    event = b["events"].event(data)
    count += 1
    print("%-8s %-6d %-16s %-8d" % (strftime("%H:%M:%S"), event.pid,
                                    event.comm.decode('utf-8', 'replace'), count))


b["events"].open_perf_buffer(print_event)
while 1:
    try:
        b.perf_buffer_poll()
    except KeyboardInterrupt:
        exit()
