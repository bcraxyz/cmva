from flask import Flask, request, jsonify
from documents import get_document, share_document

app = Flask(__name__)

@app.get("/documents/<document_id>")
def download(document_id):
    user_id = int(request.headers["X-User-ID"])
    document = get_document(document_id, user_id)

    if not document:
        return "Forbidden", 403

    return jsonify(document)

@app.post("/documents/<document_id>/share")
def share(document_id):
    user_id = int(request.headers["X-User-ID"])
    target_user = int(request.json["user_id"])

    if share_document(document_id, user_id, target_user):
        return jsonify({"status": "shared"})

    return "Forbidden", 403

if __name__ == "__main__":
    app.run(debug=True)
