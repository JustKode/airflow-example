## Airflow Example
Airflow 2.3.0 Example

## Quick Start

### Prerequisite
- Docker Compose
- Python 3.6~

### Installation

```bash
$ mkdir -p ./dags ./logs ./plugins
$ echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
$ docker-compose up -d
```

### Login
- Go to http://localhost:8080
- Login (id: airflow, password: airflow)