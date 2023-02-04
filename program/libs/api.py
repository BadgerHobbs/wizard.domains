
import openai
import socket
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="program/libs/templates")

def is_domain_available(domain_name):
    try:
        socket.gethostbyname(domain_name)
        return False
    except socket.gaierror:
        return True


@router.get("/api/domains", response_class=HTMLResponse)
async def domains(request: Request, prompt: str, ) -> dict:

    prompt = prompt.strip()

    if not prompt or len(prompt) > 120:
        return {
            "error": "Prompt too long. Must be less than 120 characters in length."
        }

    prompt_template = "Generate 5 concise, funny domain names (no TLD) based on the this prompt: "
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_template + prompt,
        max_tokens=50,
        n=1,
        stop=None,
        top_p=0.8,
        frequency_penalty=1.0,
        presence_penalty=1.0,
    )
    
    generated_domains = set([line.strip().split(" ")[-1].strip() for line in response["choices"][0]["text"].split("\n")])

    return templates.TemplateResponse(
        "domain_result.html",
        {
            "request": request,
            "generated_domains": [domain  for domain in generated_domains if domain], 
        }
    )


@router.get("/api/availability", response_class=HTMLResponse)
async def availability(request: Request, domain: str) -> dict:

    domain = domain.split(".")[0]
    
    domain_extensions = [
        ".com",
        ".org",
        ".net",
        ".io",
        ".ai",
        ".app",
        ".dev",
    ]

    return templates.TemplateResponse(
        "domain_availability.html",
        {
            "request": request,
            "domain": domain, 
            "domain_extensions": domain_extensions, 
            "is_domain_available": is_domain_available,
        }
    )