from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

app = FastAPI()

# validation error handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = error['loc'][-1]  # error['loc'] is a tuple so error['loc'][-1] is the field name
        if error['type'] == 'missing':
            errors.append(f"Field '{field}' is required")
        else:
            errors.append(f"Field '{field}' is invalid")
    
    return JSONResponse(
        status_code=422,
        content={"detail": errors}
    )

# models
class Numbers(BaseModel):
    a: StrictFloat | StrictInt
    b: StrictFloat | StrictInt

class Strings(BaseModel):
    s1: StrictStr 
    s2: StrictStr 

class RemoveSubstring(BaseModel):
    s: StrictStr
    substr: StrictStr

# Endpoints
@app.post("/add_numbers")
async def add_numbers(payload: Numbers):
    try:
        result = payload.a + payload.b
        return {
            "result": result
        }
    except Exception as error:
        print(f"Error in add_numbers: {str(error)}")
        raise error

@app.post("/subtract_numbers")
async def subtract_numbers(payload: Numbers):
    try:
        result = payload.a - payload.b
        return {
            "result": result
        }
    except Exception as error:
        print(f"Error in subtract_numbers: {str(error)}")
        raise error

@app.post("/concat_strings")
async def concat_strings(payload: Strings):
    try:
        result = payload.s1 + payload.s2
        return {
            "result": result
        }
    except Exception as error:
        print(f"Error in concat_strings: {str(error)}")
        raise error

@app.post("/remove_substring")
async def remove_substring(payload: RemoveSubstring):
    try:
        result = payload.s.replace(payload.substr, "")
        return {
            "result": result
        }
    except Exception as error:
        print(f"Error in remove_substring: {str(error)}")
        raise error

# Main block
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)