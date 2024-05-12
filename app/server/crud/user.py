from ..database import database

collection = database.get_collection('users')

async def retrieve(userid):
    item = await collection.find_one({'userid': userid})
    return item

async def add(data: dict) -> dict:
    item = await collection.insert_one(data)
    new_item = await collection.find_one({"_id": item.inserted_id})    
    new_item['_id'] = str(new_item['_id'])
    return new_item