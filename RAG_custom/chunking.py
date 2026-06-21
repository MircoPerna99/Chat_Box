
#TODO: Improving the function for semantic
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    index = 0
    while index < len(text):
        chunk = text[index:index + chunk_size]
        chunks.append(chunk)
        index += chunk_size - overlap
    return chunks