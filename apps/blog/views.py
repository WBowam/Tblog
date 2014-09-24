from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# import ugettext_lazy for location
from django.utils.translation import ugettext_lazy as _

from models import Article
from base_views import Index, Detail, List


def home(request):
    """
    View for index page.
    """
    context = (Index()).get_context()
    context["message"] = _("Recent Articles")
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    context['ip'] = 'begin' + ip + 'end'
    return render(request, 'index.html', context)


def detail(request, id):
    """
    View for detail page.
    """
    context = (Detail()).get_context(id)
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    ip = 'begin' + ip + 'end'
    context["ip"] = ip
    return render(request, 'detail.html', context)


def like(request, id):
    """
    View for detail page.
    """
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    ip = 'begin' + ip + 'end'
    article = Article.objects.get(id=id)
    if ip in article.liked_ip:
        pass
    else:
        article.like_times += 1
        article.liked_ip += ip
        article.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def dislike(request, id):
    """
    View for detail page.
    """
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    ip = 'begin' + ip + 'end'
    article = Article.objects.get(id=id)
    if ip in article.disliked_ip:
        pass
    else:
        if ip in article.liked_ip:
            article.like_times -= 2
        else:
            article.like_times -= 1
        article.disliked_ip += ip
        article.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def category_articles(request, category_name):
    context = (List()).get_context(CATEGORY=category_name)
    context["message"] = _("There are %r articles in the category %s") %\
        (len(context["articles_list"]), category_name)
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    context['ip'] = 'begin' + ip + 'end'
    return render(request, 'index.html', context)


def tag_articles(request, tag_name):
    context = (List()).get_context(TAG=tag_name)
    context["message"] = _("There are %r articles in the tag %s") %\
        (len(context["articles_list"]), tag_name)
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    context['ip'] = 'begin' + ip + 'end'
    return render(request, 'index.html', context)
