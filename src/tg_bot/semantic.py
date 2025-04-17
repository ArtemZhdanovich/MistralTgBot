
def semantic_analyze(model, sentences, question):

    # 2. Calculate embeddings by calling model.encode()
    embeddings = model.encode(sentences)
    emb_q = model.encode(question)
    print(embeddings.shape)
    # [3, 384]

    # 3. Calculate the embedding similarities
    similarities = model.similarity(emb_q, embeddings)
    index = similarities.argmax()

    return sentences[index]
