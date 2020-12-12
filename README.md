# python_celery

In a `.venv`:

```text
$ pip install -r requirements.txt
$ sqlite3 db.sqlite3
$ docker run -p 5672:5672 rabbitmq
$ celery -A tasks worker --loglevel=info
$ python
```

Python:

```python
from tasks import send_thing
result = send_thing.delay("hello world")
result.status
result.status
result.get()
```

SQL:

```sql
-- a history of the tasks run
SELECT * FROM celery_taskmeta;
```

[video](https://www.youtube.com/watch?v=THxCy-6EnQM)
