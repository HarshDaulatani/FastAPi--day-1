from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()


posts : list[dict] = [
    {
        "id" : 1,
        "author" : "Harsh",
        "title" : "FastAPI",
        "content" : "This Framework is super fast",
        "date_posted" : "Jan 15 2026",
    },
    {
        "id" : 2,
        "author" : "Apple",
        "title" : "Python",
        "content" : "Python is super easy",
        "date_posted" : "Jan 17 2026",
    },
]


@app.get("/",response_class=HTMLResponse,include_in_schema=False)
@app.get("/posts",response_class=HTMLResponse,include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"
 
  
 
@app.get("/api/posts")
def get_posts():
    return posts