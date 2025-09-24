
from huggingface_hub import InferenceClient
from decouple import config

client = InferenceClient(
    provider="nebius",
    api_key=config('HUGGIN_FACE_API'),
)

result = client.feature_extraction(
    "Today is a sunny day and I will get some ice cream.",
    model="Qwen/Qwen3-Embedding-8B",
)
print(result[0])