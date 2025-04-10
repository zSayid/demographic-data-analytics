import numpy as np 
import matplotlib.pyplot as plt 
from fastapi import APIRouter, HTTPException
from io import BytesIO
import base64
import random

router = APIRouter(prefix="/api", tags=["visualization"])

@router.get("/population_graph/{country}")
def get_population_graph(country: str):
    
    """
    Berilgan mamlakatning so‘nggi 50 yildagi aholi o‘sish grafikini qaytaradi.
    Grafik PNG formatida qaytariladi.
    """
    
    years = np.arange(1970, 2021, 1) # 1970-yildan 2020-yilgacha
    population = np.cumsum(np.random.randint(50000, 200000, size=len(years))) + random.randint(5_000_000, 
    
    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    
    # PNG rasmni base64 ga o'tkazamiz
    img_str = base64.b64encode(buf.getvalue()).decode("utf-8")
    
    return {"country": country, "years": years.tolist(), "population": population.tolist(), "image": img_str}