#!/bin/bash -e

sleep 0.2s
exec ./ps_mem.py -t -p `ps -eaf|grep openssl-master.client|grep -v grep|awk '{a=(NR>2?a",":"")$2} END {print a}'` -w 0.1 | tee log
