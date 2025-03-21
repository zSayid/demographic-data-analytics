# app/routes/population.py

from fastapi import APIRouter, HTTPException
import requests

router = APIRouter(prefix="/api", tags=["Population"])

# Aholi ma'lumotlarini olish uchun tashqi API manzili (misol uchun)
EXTERNAL_API_URL = "https://restcountries.com/v3.1/name"

@router.get("/population/{country}")
def get_population(country: str):
    """
    Berilgan mamlakatning aholi sonini qaytaradi.
    """

    # Tashqi API'ga so‘rov yuboramiz
    response = requests.get(f"{EXTERNAL_API_URL}/{country}")

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Mamlakat topilmadi")

    data = response.json()

    # Ma'lumotlarni o‘qib olish
    try:
        population = data[0]["population"]
        return {"country": country, "population": population}
    except (IndexError, KeyError):
        raise HTTPException(status_code=500, detail="Aholi ma'lumotlari topilmadi")
