import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file{number}.txt' for number in range(1, 5)]
#Линейный вызов
    start = datetime.datetime.now()
    for file in filenames:
        read_info(file)
        end = datetime.datetime.now()
        print(f'{end - start} (линейный)')
#Многопроцессный
    start = datetime.datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессный)')