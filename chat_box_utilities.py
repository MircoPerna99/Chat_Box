from RAG_custom.repository import RepositoryManager
from RAG_custom.embedder import Embedder

class ChatBoxUtilities():
    def __init__(self):
        self._repository = RepositoryManager()
        self._embedder = Embedder()
    
    def find_context(self, text):
        text_embedded , amount_token = self._embedder.encode(text=text)
        results_research = self._repository.find_chunks(text_embedded)
        if(results_research == None or len(results_research) == 0):
            return None
        context = "\n\n".join([f"---\n{chunk}" for chunk in results_research])
        return context
    