import time

def time_it(func):
    def wrapper(task):
        start_time = time.time()
        result = func(task)
        end_time = time.time()
        duration = end_time - start_time
        print(f"{task[0]} took {round(duration, 2)} seconds")
        return result
    return wrapper

@time_it
def do_task(task):
    task_name, task_duration = task
    time.sleep(task_duration)

if __name__ == "__main__":
    task_name, duration = list(map(lambda x: x.strip(), input().strip().split(',')))
    task = [task_name, int(duration)]
    do_task(task)
