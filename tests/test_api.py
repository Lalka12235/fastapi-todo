import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_get_all_task():
    async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
        response = await ac.get('/tasks/{user_id}')
        data = response.json()
        print(response)