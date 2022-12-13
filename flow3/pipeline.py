from prefect import flow
import torch.cuda as cuda

from check_torch_cuda import check_cuda
    

@flow(name='pollinator', log_prints=True)
def pollinator_pipeline(input = None):
    check_cuda()


if __name__ == '__main__':
    pollinator_pipeline()