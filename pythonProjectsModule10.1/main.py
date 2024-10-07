import threading
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f"Работа потоков {time_res}")
threads = []
file_args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

time_start_threads = datetime.now()
for arg in file_args:
    thr = threading.Thread(target=write_words, args=arg)
    threads.append(thr)
    thr.start()

for thr in threads:
    thr.join()

time_end_threads = datetime.now()
time_res_threads = time_end_threads - time_start_threads
print(f"Работа потоков {time_res_threads}")