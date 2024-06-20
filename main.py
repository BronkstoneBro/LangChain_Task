from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import uvicorn
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

app = FastAPI()

# Creating a pipeline for summarization
summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")


class TextToSummarize(BaseModel):
    text: str


def llm_summarizer(chat_input: str) -> str:
    """

    Implementation of summarization task with langchain and HuggingFace

    """
    summarizer = HuggingFacePipeline(pipeline=summarization_pipeline)
    return summarizer(chat_input)


@app.post("/summarize", status_code=status.HTTP_200_OK)
async def summarize(body: TextToSummarize):
    if not body.text.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Text cannot be empty")

    summary = llm_summarizer(body.text.strip().lower())
    return {"summary": summary}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
