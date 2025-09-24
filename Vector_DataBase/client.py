from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams
from decouple import config
from huggingface_hub import InferenceClient

#  Connect to Qdrant Cloud
client = QdrantClient(
    url=config("QDRANT_URL"),
    api_key=config("QDRANT_API_KEY"),
)

# Check if collection exists, create if not
if not client.collection_exists("ai_memory"):
    client.create_collection(
        collection_name="ai_memory",
        vectors_config=VectorParams(
            size=4096,        # Qwen3-8B embedding size
            distance="Cosine" # distance metric
        )
    )

#  Get embedding from Qwen
hf_client = InferenceClient(
    provider="nebius",
    api_key=config('HUGGING_FACE_API'),
)

text = "Today is a sunny day and I will get some ice cream."
result = hf_client.feature_extraction(text, model="Qwen/Qwen3-Embedding-8B")

# result[0] is the full embedding (4096-dim)
embedding_vector = result[0].tolist()  # convert to Python list if it is a NumPy array

#  Insert embedding into Qdrant
client.upsert(
    collection_name="ai_memory",
    points=[PointStruct(
        id=1,
        vector=embedding_vector,
        payload={
            "text": text,
            "user_id": 123,
            "type": "user"
        }
    )]
)

print("Embedding successfully upserted into Qdrant!")


 
