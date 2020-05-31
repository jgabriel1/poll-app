import sys

import uvicorn
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    uvicorn.run(
        'app:app',
        port=8000,
        reload=True if sys.argv[1] != 'noreload' else False,
        use_colors=False
    )
