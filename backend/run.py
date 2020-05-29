import uvicorn
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    uvicorn.run(
        'app:app',
        port=8000,
        reload=True,
        use_colors=False
    )
