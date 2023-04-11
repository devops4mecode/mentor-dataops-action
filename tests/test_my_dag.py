from airflow.models import DagBag

def test_dag_load():
    dagbag = DagBag(dag_folder='dags/', include_examples=False)
    assert len(dagbag.dags) == 1
    assert 'my_dag' in dagbag.dags

def test_task_count():
    dag = DagBag(dag_folder='dags/', include_examples=False).dags['my_dag']
    assert len(dag.tasks) == 3
