from datetime import datetime
import pytz
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

selected_timezone = "us"  # Default to UTC

country_timezones = {
    "US": "America/New_York",
    "IN": "Asia/Kolkata",
    "JP": "Asia/Tokyo",
    # Add more countries and their timezones
}

def set_country_timezone(country_code: str):
    global selected_timezone
    if country_code in country_timezones:
        selected_timezone = pytz.timezone(country_timezones[country_code])
    else:
        raise ValueError("Timezone not found for country code")

def get_current_time():
    return datetime.now(selected_timezone)

class TimezoneMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Example: Get timezone from headers
        country_code = request.headers.get('X-Country-Code')
        if country_code:
            try:
                set_country_timezone(country_code)
            except ValueError as e:
                return Response(f"Error: {str(e)}", status_code=400)
        response = await call_next(request)
        return response
