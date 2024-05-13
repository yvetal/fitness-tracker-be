from ..database import database

collection = database.get_collection('workout_plans')

async def retrieve_by_difficulty(difficulty):
    items = []
    async for item in collection.find({'difficulty': difficulty}):
        item['_id'] = str(item['_id'])
        items.append(item)
    return items

async def add(data: dict) -> dict:
    item = await collection.insert_one(data)
    new_item = await collection.find_one({"_id": item.inserted_id})    
    new_item['_id'] = str(new_item['_id'])
    return new_item

async def add_dummies():
    dummies = [
        {
            "name": "Bronze boy",
            "difficulty": "Beginner",
            "elements": [
                {
                    'type': 'Cycling',
                    'distance': 5
                },
                {
                    'type': 'Running',
                    'distance': 2
                }               
            ]
        },
        {
            "name": "Iron boy",
            "difficulty": "Beginner",
            "elements": [
                {
                    'type': 'Cycling',
                    'distance': 5
                },
                {
                    'type': 'Running',
                    'distance': 2
                },
                {
                    'type': 'Swimming',
                    'distance': 1
                }
            ]
        },
        {
            "name": "Bronze dude",
            "difficulty": "Intermediate",
            "elements": [
                {
                    'type': 'Cycling',
                    'distance': 10
                },
                {
                    'type': 'Running',
                    'distance': 5
                }               
            ]
        },
        {
            "name": "Iron dude",
            "difficulty": "Intermediate",
            "elements": [
                {
                    'type': 'Cycling',
                    'distance': 10
                },
                {
                    'type': 'Running',
                    'distance': 5
                },
                {
                    'type': 'Swimming',
                    'distance': 2
                }
            ]
        },
        
        {
            "name": "Bronze man",
            "difficulty": "Advanced",
            "elements": [
                {
                    'type': 'Cycling',
                    'distance': 50
                },
                {
                    'type': 'Running',
                    'distance': 20
                }               
            ]
        },
        {
            "name": "Iron man",
            "difficulty": "Advanced",
            "elements": [
                {
                    'type': 'Cycling',
                    'distance': 50
                },
                {
                    'type': 'Running',
                    'distance': 20
                },
                {
                    'type': 'Swimming',
                    'distance': 10
                }
            ]
        }
    ]

    await collection.delete_many({})
    for dummy in dummies:
        await add(dummy)