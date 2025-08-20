from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse


app = FastAPI()


@app.get('/html', response_class=HTMLResponse)
async def get_html():
    return """
            <html> 
            <head> 
            <title>Hello world!</title> 
            </head> 
            <body> 
            <h1>Hello world!</h1> 
            </body> 
            </html>
        """


@app.get('/text', response_class=PlainTextResponse)
async def text():
    return 'Hello world'


# default status code is 307 temporary redirect
@app.get('/redirect')
async def redirect():
    return RedirectResponse('new-url')


@app.get('/custom-redirect')
async def custom_redirect():
    return RedirectResponse('new-url', status_code=status.HTTP_301_MOVED_PERMANENTLY)
