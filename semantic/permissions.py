DOCUMENTS = {
    "1": {"owner_id": 100, "title": "Alice's report", "shared_with": []},
    "2": {"owner_id": 200, "title": "Bob's report", "shared_with": []},
}

def can_read(user_id, document):
    return user_id == document["owner_id"] or user_id in document["shared_with"]

def can_share(user_id, document):
    return user_id == document["owner_id"]
