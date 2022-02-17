from fastapi import FastAPI

@app.post("/send_mail")
async def send_mail(email: EmailSchema):
    template = """
        <html>
        <body>


<p>Hi !!!
        <br>Thanks for using fastapi mail, keep using it..!!!</p>


        </body>
        </html>
        """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass
        body=template,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    print(message)


return JSONResponse(status_code=200, content={"message": "email has been sent"})