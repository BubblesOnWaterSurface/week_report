import time_related as tr
import os_related as ord

path = r'F:\工作文件夹\文字报告类\周例会'
file_name = ('蒋家升-技术部周工作计划%s年%s月第%s周.xls' % (tr.y, tr.m, tr.w))
ord.recombination(path, file_name)