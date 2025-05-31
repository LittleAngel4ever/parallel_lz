import threading
import time

# Using semaphore for create simulation of the task execution
def semp(task_id, semaphore):
    with semaphore:
        print(f"Task {task_id} is starting.")
        tm = 2
        time.sleep(tm)
        print(f"Task {task_id} is finished.")
          
def main():
    semaphore = threading.Semaphore(5)
    threads = []
    print("Start executing all tasks in five threads")
    start = time.time()

    # Start all tasks 
    for i in range (100):
        t = threading.Thread(target = semp, args = (i, semaphore))
        threads.append(t)
        t.start()

    # Ending all tasks
    for t in threads:
        t.join()
    print("\nAll tasks completed in ", time.time() - start, "seconds.")

if __name__ == "__main__":
    main()