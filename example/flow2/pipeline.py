from prefect import flow

from task import get_string, process_string, print_string

@flow(name='string pipeline', log_prints=True)
def string_pipeline(length: int = 10):
    generated_string = get_string(length=length)
    processed_string = process_string(result_string=generated_string)
    print_string(result_string=processed_string)


if __name__ == '__main__':
    string_pipeline()