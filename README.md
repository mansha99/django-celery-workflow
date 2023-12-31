## What this Repo is for ?

It contains source code for tutorial published at

https://medium.com/@mansha99/workflow-using-django-celery-cf65092c5add

### What it demonstrates?

Creating Workflow using Django and Celery

##### Please refer to

###### tasks/celery_tasks.py for all Celery tasks

###### tasks/management/commands folder for all commands

## Dependencies

```console
pip install django
pip install django-redis
pip install requests
```

## Commands

#### Launching workflow

```console
python3 manage.py workflow
```

#### Clear cache (deleting all .pyc file)

```console
python3 manage.py clearcache
```

#### Celery chain example

```console
python3 manage.py chain_cmd
```

#### Celery group example

```console
python3 manage.py group_cmd
```

#### Task with output (Calculating factorial)

```console
python3 manage.py factorial 3
```
