# import parallel as par

# def main():
#    par.main()

# if __name__ == "__main__":
#    main()



import parallel as par

def main():
    par.main()

if __name__ == "__main__":
    main()
"""
if __name__ == "__main__":
    tasks = Parallel(
        num_tasks = 100,       # количество заданий в Task1
        max_threads = 5,       # максимальное число одновременных потоков
        num_files = 6,         # число «больших» файлов в Task2
        max_processes = 4      # лимит процессов в Task2
    )

    print("=== Задание 1: Ограничение потоков (Semaphore) ===")
    tasks.task1()

    print("\n=== Задание 2: Параллельная vs последовательная обработка файлов ===")
    tasks.task2()

    print("\n=== Задание 3: Синхронизация с Lock в asyncio ===")
    asyncio.run(tasks.task3())
"""