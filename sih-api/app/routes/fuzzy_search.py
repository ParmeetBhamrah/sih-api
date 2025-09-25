from fastapi import APIRouter, Query
import pandas as pd
from fuzzywuzzy import process, fuzz
from app.models import CodeSystemConcept

router = APIRouter()

namaste_df = pd.read_csv("app/data/namaste_mock_data.csv")

@router.get("/namaste/search")
def search_namaste(query: str = Query(..., min_length=1), limit: int = 5, threshold: int = 70):
    search_keys = namaste_df['display'].tolist() + namaste_df['code'].tolist()
    
    matches = process.extract(query, search_keys, limit=limit)
    
    matched_rows = []
    for match_text, score in matches:
        if score < threshold:
            continue
        row = namaste_df[(namaste_df['display'] == match_text) | (namaste_df['code'] == match_text)]
        if not row.empty:
            r = row.iloc[0]
            matched_rows.append({
                "code": r['code'],
                "display": r['display'],
                "definition": r.get('definition', None),
                "score": score
            })

    return {"resourceType": "CodeSystem", "concepts": matched_rows}
