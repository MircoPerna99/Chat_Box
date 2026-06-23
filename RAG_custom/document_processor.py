from .chunking import Chunker
from .embedder import Embedder
from .repository import RepositoryManager
from .Model.chunk_model import ChunkModel

class DocumentProcessor():
    def __init__(self):
        self.chunker = Chunker()
        self.embedder = Embedder()
        self.repository = RepositoryManager()
    
    
    def save_file(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
        chunks = self.chunker.chunk_text(text)
        chunks_to_save = []
        for i in range(len(chunks)):
            embedding, amount_token = self.embedder.encode(chunks[i]) 
            new_chunk = ChunkModel()
            new_chunk.init(chunk_index=i,text=chunks[i],token_count=amount_token, embedding=embedding)
            chunks_to_save.append(new_chunk)
        
        self.repository.add_chunks(chunks_to_save) 
            