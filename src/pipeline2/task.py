import random
import string

import pandas as pd

from prefect import task



@task
def get_string(length: int):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str

@task
def process_string(result_string):
    return result_string.upper()
    
@task(log_prints=True)
def print_string(result_string):
    print('The generated password is:', result_string)
