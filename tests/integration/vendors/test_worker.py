import pytest
from celery import Celery
from pytest_lazyfixture import lazy_fixture

from pytest_celery import CELERY_SETUP_WORKER
from pytest_celery import CeleryTestWorker
from pytest_celery import CeleryWorkerContainer
from tests.defaults import ALL_WORKERS_FIXTURES


@pytest.mark.parametrize("container", lazy_fixture(ALL_WORKERS_FIXTURES))
class test_celery_worker_container:
    def test_client(self, container: CeleryWorkerContainer):
        assert container.client
        assert container.client == container, "Check tests/conftest.py/WorkerContainer.client"


@pytest.mark.parametrize("node", [lazy_fixture(CELERY_SETUP_WORKER)])
class test_base_test_worker:
    def test_ready(self, node: CeleryTestWorker):
        assert node.ready()

    def test_app(self, node: CeleryTestWorker, celery_setup_app: Celery):
        assert node.app is celery_setup_app