from django.shortcuts import render


def article_list(request, block_id):
    block_id = int(block_id)
    return render(request, "article_list.html")
