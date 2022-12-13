from prefect import flow

from task import get_random_integer, process_integer, load_integer


@flow(name='integer pipeline', log_prints=True)
def integer_pipeline(low: int = 0, high: int = 10):
    random_integer = get_random_integer(low=low, high=high)
    second_random_integer = get_random_integer(low=low, high=high)
    result = process_integer(random_integer=random_integer, multiply_with=second_random_integer)
    load_integer(random_integer=result)
    

if __name__ == '__main__':
    integer_pipeline()