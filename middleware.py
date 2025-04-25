from fastapi import Request
import time

async def log_middleware(request: Request, call_next):
    # Log request details
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    
    print(f"Request: {request.method} {request.url} - Process Time: {process_time}")
    
    return response