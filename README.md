


### ▶️ 1. Create a virtual environment

```bash
python -m venv env
source env/bin/activate 

```

## 🛠️ 2. Install dependencies:

```bash

pip install fastapi uvicorn langchain_huggingface transformers torch torchvision torchaudio 

```

### ▶️ 3. Run the application:

```bash
uvicorn main:app --reload

```

###  4.Test the endpoint:

Send a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.