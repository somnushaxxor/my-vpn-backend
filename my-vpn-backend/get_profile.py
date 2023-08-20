from fastapi import APIRouter
from fastapi.responses import FileResponse
from ovpn_profile_service import OvpnProfileService

get_profile_router = APIRouter()

@get_profile_router.get("/profile")
async def get_profile():
    return FileResponse(OvpnProfileService.create_profile())
