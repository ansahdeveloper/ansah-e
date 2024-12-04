from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")

def generate_response(query, business):
    # Construct a prompt that includes business-specific information
    prompt = f"""
    Business Name: {business.name}
    Business Type: {business.type}
    Query: {query}
    
    Please provide a friendly and professional response:
    """
    
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=150)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response.strip()

