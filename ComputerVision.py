from openai import OpenAI

endpoint = "Your endpoint"
deployment_name = "gpt-5.4-mini"
api_key = "Your Api"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "what's in this image?"},
            {"type": "input_image", "image_url": "https://image.tmdb.org/t/p/w235_and_h235_face/u6RVP8ukgLaymeoi5VmX0JRAcCn.jpg"}
        ]
    }]
)

print(f"answer: {response.output_text}")