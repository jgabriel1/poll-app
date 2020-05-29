from fastapi import APIRouter

router = APIRouter()


@router.post('/vote', status_code=204)
def compute_votes():
    pass
