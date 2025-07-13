from fastapi.routing import APIRouter

router = APIRouter()


@router.post("/register")
async def register_user():
    pass


@router.post("/login")
async def login_user():
    pass


@router.get("/")
async def get_user_profile():
    pass


@router.put("/")
async def update_user_profile():
    pass
