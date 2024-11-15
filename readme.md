# How to run this project

In case you want to have a pre-populated database, just make sure you run the seed with the command before starting the server

 `py prisma/seed.py`

To start the server run the below command

`uvicorn main:app`

## API Routes

To easily see every available route, access `http://localhost:8000/docs`

There are 5 routes:

- GET /tasks - get all tasks
- GET /tasks/{task_id} - get one task
- POST /tasks - create a task
- PATCH /tasks/{task_id} - update a task
- DELETE /tasks/{task_id} - delete a task
