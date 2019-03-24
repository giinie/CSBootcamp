import tracemalloc
tracemalloc.start(10)  # 스택 프레임을 최대 10개까지 저장.

time1 = tracemalloc.take_snapshot()
import waste_memory
x = waste_memory.run()
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'lineno')
for stat in stats[:3]:
    print(stat)
