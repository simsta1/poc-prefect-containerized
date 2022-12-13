import numpy as np

from prefect import task


@task(
    log_prints=True
)
def get_random_integer(low: int, high: int):
    random_integer = np.random.randint(low=low, high=high)
    print('Starting with Random Integer:', random_integer)
    return random_integer

@task
def process_integer(random_integer: int, multiply_with: int):
    random_integer = random_integer * multiply_with

    return random_integer

@task(
    log_prints=True
)
def load_integer(random_integer):
    print('End with Random Integer:', random_integer)
    
    return 0