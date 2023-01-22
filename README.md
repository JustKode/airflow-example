## Airflow Example
Airflow Example

## Quick Start

### Installation

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export AIRFLOW_HOME=~/airflow

# change load_examples = False
$ airflow db init
$ vim $AIRFLOW_HOME/airflow.cfg
$ airflow users create \
    --username admin \
    --firstname Park \
    --lastname Minjae \
    --role Admin \
    --email sobu0715@gmail.com
$ airflow webserver --port 8080

# In another terminal
$ airflow scheduler
```