"""
Сегодня хотел бы по практиковаться в отслеживании того, сколько памяти тратит тот или иной скрипт.
Не давно я начал измерять время, теперь пора бы начать замерять память.
"""
from tqdm import tqdm
import time
import psutil
from  functools import partial, reduce
from memory_profiler import profile
# Интерестное решение со StackOwerflow
# with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
#     while True:
#         rambar.n=psutil.virtual_memory().percent
#         cpubar.n=psutil.cpu_percent()
#         rambar.refresh()
#         cpubar.refresh()
#         time.sleep(0.5)

test_data = [1, 2, 3, 4, 5]
a = lambda x: x*2

implosive_attractor = profile(lambda *funcs: partial(lambda *args: reduce(lambda x, f: f(x), funcs[1:], funcs[0](*args))))

@profile
def func_for(data):
    x = []
    for i in data:
        x.append(i*2)
    a = sum(x)
    return a

if __name__ == '__main__':
    implosive_attractor(map, list, sum)(a, test_data)
    func_for(test_data)
    pass