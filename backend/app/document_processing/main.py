from openai import OpenAI

# Read the file and store its contents
with open("backend/app/document_processing/tardigrades.txt", "r") as file:
    file_content = file.read()

# Initialize the OpenAI client
client = OpenAI()

# Create a prompt using the file content
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that knows a lot about tardigrades and only responds with JSON"},
        {"role": "user", "content": file_content + "make a table of important points about this topic with a column for questions about the topic and another column for the answers to the topic and a column for the points themselves"},
    ]
)

# Print the response
print(response)
