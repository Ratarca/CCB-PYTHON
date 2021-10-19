"""
    Tips to consumption
"""
import logging

# Flatten info
def flatten_info(info):
    try:
        otp = {}
        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a , name + str(i) + "_")
                    i += 1
            else:
                otp[name[:-1]] = x
            
            flatten(info)

            return otp
    except Exception as err:
        logging.error(f"Error is : {} \n erro into files/consumption")

# Batch file
def batch(data, chunk_size=10000):
    _batch = []
    try:
        while True:
            for _ in range(chunk_size):
                _batch.append(next(data))
            yield _batch
            _batch = []
    except StopIteration:
        if len(_batch):
            yield _batch
