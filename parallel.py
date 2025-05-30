import threading
import multiprocessing
import asyncio
import time
import random
  
""" 
class Parallel:
    def writing_file(name, data):
        with open(f"{name}.txt", "w") as file:
            file.write(data)
            time.sleep(1)

    # Последовательное выполнение
    start = time.time()
    for i in range (10):
        writing_file(f"File_0{i}", "data")
    print(time.time() - start)

    # Параллельное выполнение

    start = time.time()
    threads = []
    for i in range (10):
        thread = threading.Thread(target = writing_file(f"File_0{i}", "data"))

    for t in threads:
       t.join()
    print("Время", time.time() - start)


    data = list(range(0, 1000000))
    def quad(data):
        for i in range(len(data)):
            data[i] = data[i]**2
        return(sum(data))


    # Последовательное выполнение
    start = time.time()
    with multiprocessing.Pool(processes = 2) as pool:
        results = pool.map(quad, data)
    print("Время", time.time() - start)
"""


class Parallel:
    def __init__(self, num_tasks: int = 100, max_threads: int = 5, num_files: int = 5, max_processes: int = 10):
        # Параметры для задач
        self.num_tasks = num_tasks
        self.max_threads = max_threads

        # Имена «больших» файлов для обработки (симуляция)
        self.files = [f"file_{i}.txt" for i in range(1, num_files + 1)]
        self.max_processes = max_processes

        # Для задания 3
        self.shared_counter = 0
        self.async_lock = asyncio.Lock()

    def task1(self):
        """
        Задание 1. Ограничение числа одновременных потоков (Semaphore).
        Выполнить num_tasks «тяжёлых» задач с ограничением max_threads.
        """
        semaphore = threading.Semaphore(self.max_threads)
        durations = []
        threads = []

        def worker(task_id: int):
            with semaphore:
                print(f"[Task1] Задача #{task_id} запущена")
                start = time.perf_counter()
                time.sleep(random.uniform(1, 2))  # имитируем работу
                dt = time.perf_counter() - start
                print(f"[Task1] Задача #{task_id} завершена за {dt:.2f}s")
                durations.append(dt)

        start_all = time.perf_counter()
        for i in range(1, self.num_tasks + 1):
            t = threading.Thread(target=worker, args=(i,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        total_time = time.perf_counter() - start_all
        avg_time = sum(durations) / len(durations) if durations else 0
        print(f"\n[Task1] Все {self.num_tasks} задач завершены")
        print(f"[Task1] Общая длительность: {total_time:.2f}s")
        print(f"[Task1] Среднее время одной задачи: {avg_time:.2f}s")

    def task2(self):
        """
        Задание 2. Обработка «больших» файлов.
        Сначала параллельно (multiprocessing.Pool), потом последовательно.
        """
        def process_file(fname: str):
            print(f"[Task2] Начинаем обработку {fname}")
            dt = random.uniform(5, 10)
            time.sleep(dt)  # имитируем тяжёлую операцию
            print(f"[Task2] {fname} обработан за {dt:.2f}s")
            return dt

        # --- параллельно ---
        start_par = time.perf_counter()
        pool_size = min(len(self.files), self.max_processes)
        with multiprocessing.Pool(processes=pool_size) as pool:
            pool.map(process_file, self.files)
        par_time = time.perf_counter() - start_par
        print(f"\n[Task2] Параллельная обработка заняла {par_time:.2f}s")

        # --- последовательно ---
        start_seq = time.perf_counter()
        for f in self.files:
            process_file(f)
        seq_time = time.perf_counter() - start_seq
        print(f"[Task2] Последовательная обработка заняла {seq_time:.2f}s")

    async def task3(self):
        """
        Задание 3. Синхронизация с помощью asyncio.Lock.
        Несколько корутин безопасно увеличивают общую переменную.
        """
        async def coro_inc(coro_id: int):
            for _ in range(20):
                await asyncio.sleep(random.uniform(0.1, 0.5))
                # Критическая секция
                async with self.async_lock:
                    self.shared_counter += 1
                    print(f"[Task3] Coroutine {coro_id} -> counter = {self.shared_counter}")

        print("\n[Task3] Запускаем корутины...")
        coros = [coro_inc(i) for i in range(1, 11)]
        await asyncio.gather(*coros)
        print(f"[Task3] Финальное значение счётчика: {self.shared_counter}")
