from transformers import AutoTokenizer, AutoModel
from configuration import Configuration
import torch


class EmbeddingModel:
    def __init__(self, model_name):
        self._config = Configuration()
        self.model_name = self._config["embending_model"]
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(self.model_name)


    def _apply_mean_pooling(self, token_embeddings, attention_mask):
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        return (sum_embeddings / sum_mask).squeeze().numpy()

    def encode(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
             
        return self._apply_mean_pooling(outputs.last_hidden_state, inputs['attention_mask'])

