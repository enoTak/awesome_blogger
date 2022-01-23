from flask import (
    render_template,
    request,
    redirect,
    url_for,
    render_template,
    flash,
    session
)
from flask_blog import app
from datetime import datetime


@app.route("/")
def show_entries():
    # TODO: show all entries
    entries = [
        {
            "id": 1,
            "title": "初めての投稿",
            "text": "testtesttest",
            "create_at": datetime.now(),
        },
        {
            "id": 2,
            "title": "2つ目の投稿",
            "text": "testtesttest for 2",
            "create_at": datetime.now(),
        }
    ]
    return render_template("entries/index.html", entries=entries)


@app.route("/entries", methods=["POST"])
def add_entry():
    # TODO: 記事の作成処理を実装
    return "新しく記事が作成されました"


@app.route("/entries/new", methods=["GET"])
def new_entry():
    return render_template("entries/new.html")


@app.route("/entries/<int:id>", methods=["GET"])
def show_entry(id):
    # TODO: 記事を取得(まだテストデータ)
    entry = {
        "id": 1,
        "title": "初めての投稿",
        "text": "testtesttest",
        "create_at": datetime.now(),
    }
    return render_template("entries/show.html", entry=entry)


@app.route("/entries/<int:id>/edit", methods=["GET"])
def edit_entry(id):
    # TODO: 記事の編集フォームを表示
    return f"記事{id}の編集フォームを表示"


@app.route("/entries/<int:id>/update", methods=["POST"])
def update_entry(id):
    # TODO: 記事の更新処理を実装
    return f"記事{id}が更新されました"


@app.route("/entries/<int:id>/delete", methods=["POST"])
def delete_entry(id):
    # TODO: 記事の削除処理を実装
    return f"記事{id}が削除されました"