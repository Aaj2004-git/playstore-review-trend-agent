from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class TopicCanonicalizer:
    def __init__(self):
        self.topics = []
        self.embeddings = {}

    def get_embedding(self, text):
        import openai
        emb = openai.Embedding.create(
            model="text-embedding-3-small",
            input=text
        )
        return np.array(emb['data'][0]['embedding'])

    def canonicalize(self, topic):
        if not self.topics:
            self.topics.append(topic)
            self.embeddings[topic] = self.get_embedding(topic)
            return topic

        topic_emb = self.get_embedding(topic)

        for existing in self.topics:
            sim = cosine_similarity(
                [topic_emb],
                [self.embeddings[existing]]
            )[0][0]

            if sim > 0.85:
                return existing

        self.topics.append(topic)
        self.embeddings[topic] = topic_emb
        return topic
