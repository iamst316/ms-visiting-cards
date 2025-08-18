import base64
from openai import OpenAI
# from dotenv import load_dotenv
import os

# load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

def parse_card():
    # Path to your cropped PNG
    image_path = os.path.join(os.path.dirname(__file__), "test-1.png")

    # Encode image as base64
    with open(image_path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an OCR and data extraction assistant. Extract business card details into clean JSON."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Extract the following fields from the image that contains multiple business cards: Name, Job Title, Company, Address, Phone, Fax, Email. Return JSON with an array of objects containing these fields."
                        
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content

    '''
        ```json
        {
        "Name": "Jayanta Roy Chowdhury",
        "Job Title": "Senior Editor (Business)",
        "Company": "ABP Pvt. Limited",
        "Address": "9-10, Bahadur Shah Zafar Marg, New Delhi-110 002",
        "Phone": "2370 2170-79, 2370 2059",
        "Fax": "011-2370 2065",
        "Email": "jayantaroy@abpmail.com"
        }
        ```
    '''
