from  datetime import datetime
class ChunkModel():
    def __init__(self):
        self.id : str 
        self.chunk_index : int
        self.text: str
        self.token_count : int
        self.embedding : list[float]
        self.created_at : datetime
    
    def init(self, id  = "", chunk_index = 0, text = "", token_count  = 0, embedding = [] ,created_at = None):
        self.id = id
        self.chunk_index = chunk_index
        self.text = text
        self.token_count = token_count
        self.embedding = embedding
        self.created_at  = created_at