import requests

def get_order_status(business, order_id):
    # This is a placeholder function. In a real-world scenario, you would
    # use the business's integration details to make an API call to their
    # e-commerce platform or custom API.
    
    if business.custom_api_details:
        # Use custom API
        api_url = business.custom_api_details.get('order_status_endpoint')
        api_key = business.custom_api_details.get('api_key')
        
        response = requests.get(
            f"{api_url}/{order_id}",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        
        if response.status_code == 200:
            return response.json().get('status')
    
    # If no custom API or if the request failed, return a default status
    return "Status unavailable"

