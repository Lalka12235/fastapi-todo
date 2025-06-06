import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from tests.conftest import test_task_for_create,test_task_for_update


class TestApi:
    @pytest.mark.asyncio
    async def test_get_all_task():
        async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
            response = await ac.get('/tasks/{user_id}')
            data = response.json()
            print(data)
            assert data


    @pytest.mark.asyncio
    async def test_get_task():
        async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
            response = await ac.get('/tasks/{user_id}/{taskid}')
            data = response.json()
            print(data)
            assert data

    @pytest.mark.asyncio
    async def test_create_task(test_task_for_create):
        async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
            response = await ac.post('/tasks/{user_id}')
            data = {'Task': test_task_for_create}
            print(data)
            assert data


    @pytest.mark.asyncio
    async def test_update_task(test_task_for_update):
        async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
            response = await ac.put('/tasks/{user_id}/{task_id}')
            data = {'Task': test_task_for_update}
            print(data)
            assert data

    @pytest.mark.asyncio
    async def test_delete_task():
        async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
            response = await ac.delete('/tasks/{user_id}/{task_id}')
            data = response.json()
            print(data)
            assert data