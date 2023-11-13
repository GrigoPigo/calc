from fastapi import FastAPI
app = FastAPI()
@app.get("/")
@app.get("/add/{num1}/{num2}")

def pluson(num1: float, num2: float):
    result = num1 + num2
    return {"result": result}

@app.get("/substract/{num1}/{num2}")

def minuson(num1: float, num2: float):
    result = num1 - num2
    return {"result": result}

@app.get("/multiply/{num1}/{num2}")

def umnajon(num1: float, num2: float):
    result - num1 * numm2
    return {"result" : result}
    
@app.get("/divide/{num1}/{num2}")

def delison(num1: float, num2 : float):
    if num2 == 0:
        return {"error": "на ноль делить нельзя" }
    result = num1 / num2
    return {"result": result}
    
