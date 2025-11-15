from fastapi import APIRouter
from services.forecasting_service import forecast_demand
from services.reorder_service import calculate_reorder_levels
from services.supplier_service import compute_supplier_rating
from openai import OpenAI

router = APIRouter(prefix="/agent", tags=["AI Agent"])
client = OpenAI()

SYSTEM_PROMPT = """
You are an Inventory AI Agent. Your tasks:
- Forecast demand
- Calculate reorder levels
- Analyze supplier quality
- Detect anomalies
- Recommend purchase orders
- Provide inventory insights
"""

@router.post("/")
def ai_agent(prompt: dict):
    user_input = prompt["query"]

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    return {"response": response.choices[0].message["content"]}
