from django.shortcuts import render, redirect
from django.views.generic import View, DetailView

from block.models import Block
from comment.models import Comment
from .models import Article
from .forms import ArticleForm
from utils.paginator import paginate_queryset


def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    page_no = int(request.GET.get("page_no", "1"))
    all_articles = Article.objects.filter(block=block,
        status=0).order_by("-id")
    page_articles, pagination_data = paginate_queryset(all_articles, page_no)
    return render(request, "article_list.html", {"articles": page_articles,
            "b": block, "pagination_data": pagination_data})


class ArticleCreateView(View):

    template_name = "article_create.html"

    def init_data(self, block_id):
        self.block_id = block_id
        self.block = Block.objects.get(id=block_id)

    def get(self, request, block_id):
        self.init_data(block_id)
        return render(request, self.template_name, {"b": self.block})

    def post(self, request, block_id):
        self.init_data(block_id)
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
            article.block = self.block
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % self.block_id)
        else:
            return render(request, self.template_name, {"b": self.block, "form": form})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_no = int(self.request.GET.get("page_no", "1"))
        all_comments = Comment.objects.filter(article=context["article"],
                                              status=0)
        comments, pagination_data = paginate_queryset(all_comments,
                page_no, cnt_per_page=3)
        context['comments'] = comments
        context['pagination_data'] = pagination_data
        return context
