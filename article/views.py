from django.shortcuts import render, redirect

from block.models import Block
from .models import Article


def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")
    return render(request, "article_list.html", {"articles": articles_objs, "b": block})


def article_create(request, block_id):
    if request.method == "GET":
        block_id = int(block_id)
        block = Block.objects.get(id=block_id)
        return render(request, "article_create.html", {"b": block})
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        block_id = int(block_id)
        block = Block.objects.get(id=block_id)
        article = Article(block=block, title=title, content=content, status=0)
        article.save()
        return redirect("/article/list/%s" % block_id)
