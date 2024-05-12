from ..database import database

collection = database.get_collection('goals')

async def retrieve_for_user(userid):
    items = []
    async for item in collection.find({'userid': userid}):
        item['_id'] = str(item['_id'])
        items.append(item)
    return items

async def add(data: dict) -> dict:
    item = await collection.insert_one(data)
    new_item = await collection.find_one({"_id": item.inserted_id})    
    new_item['_id'] = str(new_item['_id'])
    return new_item