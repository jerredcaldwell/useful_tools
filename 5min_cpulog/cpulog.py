import psutil
from datetime import datetime
import time

end = time.time() + 60 * 5
with open('log.txt', 'w') as f:

    while time.time() < end:
        # time.sleep(1)
        usage = psutil.cpu_percent(2)
        usage = str(usage)
        a = str(datetime.now())
        f.write(a + '    CPU: ' + usage)
        f.write('\n')
        print(usage)
