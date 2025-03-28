import ollama

def llm(prompt: str, model: str = "deepseek-r1:1.5b"):
    response = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}]
    )    
    return response['message']['content']


# Call the function and print the response
def main():
    query = input('Enter a question: ')
    response = llm(query)
    print(response)

if __name__ == "__main__":
    main()