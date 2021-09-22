from fastapi import FastAPI
from adaptnlp import EasySummarizer
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    txt: str
    maxsize: Optional[int] = 5
    minsize: Optional[int] = 2


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    summarizer = EasySummarizer()
    s = summarizer.summarize(text = item.txt, model_name_or_path="t5-small", mini_batch_size=1, num_beams = 4, min_length=item.minsize, max_length=item.minsize, early_stopping=True)
    print(summarizer.summarize(text = item, model_name_or_path="t5-small", mini_batch_size=1, num_beams = 4, min_length=2, max_length=5, early_stopping=True))
    return s
