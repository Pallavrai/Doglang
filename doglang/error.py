class Error:
    def __init__(self,stage,error):
        raise Exception(f'{stage} Error: {error}')