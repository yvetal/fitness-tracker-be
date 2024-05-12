from ..database import database

collection = database.get_collection('devices')

async def retrieve_for_user(userid):
    item = await collection.find_one({'userid': userid})
    item['_id'] = str(item['_id'])

    item['deviceId'] = str(item['_id'])
    return item

async def add(data: dict) -> dict:
    if not await collection.find_one({'userid': data['userid']}):
        item = await collection.insert_one(data)
        new_item = await collection.find_one({"_id": item.inserted_id})    
        new_item['_id'] = str(new_item['_id'])
        return new_item
    else:
        raise Exception('Device already added!')

async def delete_for_user(userid: str) -> dict:
    if await collection.delete_one({'userid': userid}):
        return 
    else:
        raise Exception('Device not deleted!')