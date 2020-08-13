import threading
from threading import Thread


class PrintThread(Thread):
    def run(self):
        for i in range(1, 11):
            print("Child ", i)


t = threading.current_thread()
print(t)
pt = PrintThread()
pt.start()
# Display all running threads
for t in threading.enumerate():
    print(t)
    t.join()

for i in range(1, 11):
    print("Main", i)