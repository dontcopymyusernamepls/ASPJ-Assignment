from flask_limiter import Limiter 
from flask_limiter.util import get_remote_address

limiter = Limiter(default_limits=["200 per day", "1 per hour"], key_func=get_remote_address)