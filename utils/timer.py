import time
import sys

def run_with_timer(task_func, *args, **kwargs):
    """
    Wrapper function to run tasks with a timer feedback.
    """
    print(f"[*] Starting task: {task_func.__name__}...", end="", flush=True)
    
    start_time = time.time()
    result = task_func(*args, **kwargs)
    end_time = time.time()
    
    elapsed = end_time - start_time
    print(f" done in {elapsed:.2f} seconds.")
    return result
