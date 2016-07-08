from article.models import Article
from comment.models import Comment
from utils.responses import json_response


def create_comment(request):
    if not request.user.is_authenticated():
        return json_response({"status": "error",
                "msg": "您没有登录，不能发表评论哦～"})
    article_id = int(request.POST["article_id"])
    to_comment_id = int(request.POST.get("to_comment_id", 0))
    content = request.POST["content"].strip()

    if not content:
        return json_response({"status": "error",
                "msg": "评论内容不能为空."})
    article = Article.objects.get(id=article_id)
    if to_comment_id != 0:
        to_comment = Comment.objects.get(id=to_comment_id)
    else:
        to_comment = None
    comment = Comment(article=article, owner=request.user,
            content=content, to_comment=to_comment)
    comment.save()
    return json_response({"status": "ok", "msg": ""})
