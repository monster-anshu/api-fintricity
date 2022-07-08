from fastapi import APIRouter
from .countries import router as countries
router = APIRouter(
    prefix="/onboarding"
)

router.include_router(countries)
@router.get('/')
def get():
    return "Onboarding"
