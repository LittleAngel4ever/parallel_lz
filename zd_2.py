import time
import multiprocessing

# Create simulation of the task execution
def times(file_id):
    print(f"[File {file_id}] Processing has begun")
    tm = 10  
    time.sleep(tm)
    print(f"[File {file_id}] Processing complete")
    return file_id, tm

# Parallel processing
def par(list_of_files, max_operations = 10):
    print("\n=== Parallel processing of large files ===")
    start = time.time()

    with multiprocessing.Pool(processes = max_operations) as pool:
        pool.map(times, list_of_files)
    print("\nParallel processing completed in ", time.time() - start , "seconds.")

# Sequential processing
def seq(list_of_files):
    print("\n=== Sequential processing of large files ===")
    start = time.time()

    for f_id in list_of_files:
        times(f_id)
    print("\nSequential processing completed in ", time.time() - start , "seconds.")

def main():
    print("==== Processing Large Files: Parallel vs. Sequential ====")
    list_of_files = [1, 2, 3, 4, 5]
    max_processes = min(10, len(list_of_files))

    par(list_of_files, max_processes)
    
    seq(list_of_files)

if __name__ == '__main__':
    main()