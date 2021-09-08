from fastapi import APIRouter

from .cloud_flare import router as cf_router

router = APIRouter()
router.include_router(cf_router)
