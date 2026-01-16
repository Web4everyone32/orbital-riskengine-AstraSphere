from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/map", response_class=HTMLResponse)
def space_map():
    with open("ui/space-map.html", encoding="utf-8") as f:
        return f.read()
