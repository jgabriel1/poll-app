import uvicorn

if __name__ == "__main__":
    uvicorn.run('app:app', use_colors=False, port=8000)
