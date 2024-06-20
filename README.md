


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
### 🧪 4. Test the endpoint:

Send a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.

Example request:

```json
{
    "text": "recipe apple pie "
}
```
Excepted response:

```json
{
    "summary": "A recipe for apple pie is one of the most popular pies in the U.S. This recipe can be adapted to make any type of pie. For more information, go to www.allrecipes.com. For a recipe for apple pie, visit CNN.com/Cooking."
}
```

