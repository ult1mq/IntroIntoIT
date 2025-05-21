from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import wikipedia

app = FastAPI(
    title="Wiki-Service",
    description="Простейший сервис на FastAPI + wikipedia",
    version="1.0.0"
)

class PageSummary(BaseModel):
    title: str
    summary: str

class SearchResult(BaseModel):
    query: str
    results: list[str]

class PageRequest(BaseModel):
    title: str

@app.get("/page/{title}", response_model=PageSummary, tags=["path"])
def get_page_summary(title: str):
    """
    Получить заголовок и первый абзац страницы Wikipedia
    """
    try:
        summary = wikipedia.summary(title, sentences=2, auto_suggest=False)
    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail="Страница не найдена")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return PageSummary(title=title, summary=summary)

@app.get("/search", response_model=SearchResult, tags=["query"])
def search_wikipedia(query: str, limit: int = 5):
    """
    Поисковый запрос по Wikipedia, возвращает до `limit` заголовков
    """
    try:
        results = wikipedia.search(query, results=limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return SearchResult(query=query, results=results)

@app.post("/page/summary", response_model=PageSummary, tags=["body"])
def post_page_summary(req: PageRequest):
    """
    Через POST возвращает анонс страницы Wikipedia по названию в теле запроса
    """
    try:
        summary = wikipedia.summary(req.title, sentences=2, auto_suggest=False)
    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail="Страница не найдена")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return PageSummary(title=req.title, summary=summary)
