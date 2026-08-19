from permissions import DOCUMENTS, can_read, can_share

def get_document(document_id, user_id):
    document = DOCUMENTS.get(document_id)
    if document and can_read(user_id, document):
        return document
    return None

def share_document(document_id, user_id, target_user):
    document = DOCUMENTS.get(document_id)
    if not document:
        return False
    if can_read(user_id, document):
        document["shared_with"].append(target_user)
        print(f"Shared {document_id} with user {target_user}")
        return True
    return False
