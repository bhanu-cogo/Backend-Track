from fastapi import FastAPI, File, Form, UploadFile
from pathlib import Path
from fastapi.responses import HTMLResponse

app=FastAPI()

@app.post('/upload/files')
async def upload_files(files: UploadFile):
    return {"filename":files.filename}  


@app.get('/')
async def upload_form_file():
    return HTMLResponse(content="""
        <form method="post" action="/upload/files" enctype="multipart/form-data">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>""")
