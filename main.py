from fastapi import FastAPI

tags_metadata = [
        {
            "name": "About",
            "description": "Who am I.",
        },
        {
            "name": "Locations",
            "description": "Locations where I am open to employment.",
        }
    ]

app = FastAPI(
    title="API Documentation",
    description="Sample API Documentation using FastAPI and Python",
    summary="Contains Dummy Data.",
    version="0.0.1",
    contact={
        "name": "David Romero",
        "url": "https://dromero.dev",
        "email": "dl_romero@outlook.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
    )

@app.get("/about/", tags=["About"])
async def about():
    return ({"About": "I am an experienced Data Center Engineer with strong skills in maintaining global data centers and servers with a passion for automation and team leadership."})

@app.get("/locations/", tags=["Locations"])
async def locations():
    return ({"Oregon": "All Locations", "California": "San Diego County"})

# Run - python -m uvicorn main:app --reload