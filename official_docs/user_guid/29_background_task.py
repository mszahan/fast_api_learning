from fastapi import BackgroundTasks, FastAPI


app = FastAPI()


def write_notification(email: str, message=''):
    with open('log.txt', mode='w') as email_file:
        content = f'notification for {email}: {message}'
        email_file.write(content)


@app.post('/send-notification/{email}')
async def send_notification(email: str, background_task: BackgroundTasks):
    background_task.add_task(write_notification, email, message='Some message')
    return {'message': 'set task to background'}
