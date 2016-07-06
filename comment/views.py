from article.models import Article
from comment.models import Comment
from utils.responses import json_response


def create_comment(request):
    if not request.user.is_authenticated():
        return json_response({"status": "error",
                "msg": "您没有登录，不能发表评论哦～"})
    article_id = int(request.POST["article_id"])
    content = request.POST["content"].strip()

    article = Article.objects.get(id=article_id)
    comment = Comment(article=article, owner=request.user,
            content=content)
    comment.save()
    return json_response({"status": "ok", "msg": ""})
