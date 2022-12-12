from prefect import flow

from src.pipeline1.task import get_random_integer, process_integer, load_integer
from src.pipeline2.task import get_string, process_string, print_string


@flow(
    name='string pipeline',
    log_prints=True
)
def string_pipeline(
    length: int = 10
):
    generated_string = get_string(length=length)
    processed_string = process_string(result_string=generated_string)
    print_string(result_string=processed_string)


@flow(
    name='integer pipeline',
    log_prints=True
)
def integer_pipeline(
    low: int = 0,
    high: int = 10
):
    random_integer = get_random_integer(low=low, high=high)
    second_random_integer = get_random_integer(low=low, high=high)
    result = process_integer(random_integer=random_integer, multiply_with=second_random_integer)
    load_integer(random_integer=result)
    


if __name__ == '__main__':
    string_pipeline()
    integer_pipeline()