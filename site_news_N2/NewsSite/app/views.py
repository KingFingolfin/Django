from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import OneTopic, Ad, Comment
from .forms import ContactForm, GmailsForm, CommentForm


def homepage(request):
    topics = OneTopic.objects.all()

    ad = Ad.objects.all()[:1].get()

    topics_paginator = Paginator(topics, 10)

    page_num = request.GET.get('page')

    page = topics_paginator.get_page(page_num)

    form_gmail = GmailsForm()

    if request.method == "POST":
        form_gmail = GmailsForm(request.POST)
    if form_gmail.is_valid():
        data = form_gmail.save(commit=False)
        data.Email = form_gmail.cleaned_data.get('Email')
        data.save()

        return redirect('App:HomePage')

    context = {
        'topics': topics,
        'page': page,
        'count': topics_paginator.count,
        'ad': ad,
        'form_gmail': form_gmail,
    }

    return render(request, 'app/tech-index.html', context)


def search(request):
    topic_name = request.GET.get('input_name')

    topics = OneTopic.objects.all()

    not_found = 0

    if topic_name != '' and topic_name is not None:
        topics = topics.filter(title__contains=topic_name)
    if not topics:
        not_found = 1



    ad = Ad.objects.all()[:1].get()

    topics_paginator = Paginator(topics, 10)

    page_num = request.GET.get('page')

    page = topics_paginator.get_page(page_num)

    form_gmail = GmailsForm()

    if request.method == "POST":
        form_gmail = GmailsForm(request.POST)
    if form_gmail.is_valid():
        data = form_gmail.save(commit=False)
        data.Email = form_gmail.cleaned_data.get('Email')
        data.save()

        return redirect('App:Search')
    context = {
        'not_found': not_found,
        'topics': topics,
        'page': page,
        'count': topics_paginator.count,
        'ad': ad,
        'form_gmail': form_gmail,
    }

    return render(request, 'app/search.html', context)


def single_test(request, id):
    one_topic = OneTopic.objects.get(id=id)
    ad = Ad.objects.all()

    also_like_topics = OneTopic.objects.filter(news_type=one_topic.news_type)

    also_like_topics = also_like_topics.exclude(title=one_topic.title)

    comment = Comment.objects.filter(article=id)

    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        data = comment_form.save(commit=False)
        data.article = one_topic
        data.username = comment_form.cleaned_data.get('username')
        data.text = comment_form.cleaned_data.get('text')
        data.save()

        return redirect('App:Single_Test', id)

    form_gmail = GmailsForm()

    if request.method == "POST":
        form_gmail = GmailsForm(request.POST)
    if form_gmail.is_valid():
        data = form_gmail.save(commit=False)
        data.Email = form_gmail.cleaned_data.get('Email')
        data.save()

        return redirect('App:Single_Test', id)

    context = {
        'also_like_topics': also_like_topics,
        'one_topic': one_topic,
        'ad': ad,
        'comment': comment,
        'comment_form': comment_form,
        'form_gmail': form_gmail,
    }

    return render(request, 'app/tech-single.html', context)


def ContactUs(request):
    form = ContactForm(use_required_attribute=False)

    if request.method == "POST":
        form = ContactForm(request.POST)
    if form.is_valid():
        data = form.save(commit=False)
        data.Name = form.cleaned_data.get('Name')
        data.Email = form.cleaned_data.get('Email')
        data.Phone = form.cleaned_data.get('Phone')
        data.Subject = form.cleaned_data.get('Subject')
        data.Message = form.cleaned_data.get('Message')
        data.save()

        return redirect('App:Contact_Us')

    form_gmail = GmailsForm()

    if request.method == "POST":
        form_gmail = GmailsForm(request.POST)
    if form_gmail.is_valid():
        data = form_gmail.save(commit=False)
        data.Email = form_gmail.cleaned_data.get('Email')
        data.save()

        return redirect('App:Contact_Us')

    context = {
        'form_gmail': form_gmail,
        'form': form,
    }

    return render(request, 'app/tech-contact.html', context)


def Politic(request):
    topics = OneTopic.objects.filter(news_type=3)
    ad = Ad.objects.all()[:1].get()
    topics_paginator = Paginator(topics, 10)

    page_num = request.GET.get('page')

    page = topics_paginator.get_page(page_num)

    form_gmail = GmailsForm()

    if request.method == "POST":
        form_gmail = GmailsForm(request.POST)
    if form_gmail.is_valid():
        data = form_gmail.save(commit=False)
        data.Email = form_gmail.cleaned_data.get('Email')
        data.save()

        return redirect('App:Politic')
    context = {
        'topics': topics,
        'page': page,
        'count': topics_paginator.count,
        'ad': ad,
        'form_gmail': form_gmail,
    }

    return render(request, 'app/politic.html', context)


def Science(request):
    topics = OneTopic.objects.filter(news_type=2)
    ad = Ad.objects.all()[:1].get()
    topics_paginator = Paginator(topics, 10)

    page_num = request.GET.get('page')

    page = topics_paginator.get_page(page_num)

    form_gmail = GmailsForm()

    if request.method == "POST":
        form_gmail = GmailsForm(request.POST)
    if form_gmail.is_valid():
        data = form_gmail.save(commit=False)
        data.Email = form_gmail.cleaned_data.get('Email')
        data.save()

        return redirect('App:Science')
    context = {
        'topics': topics,
        'page': page,
        'count': topics_paginator.count,
        'ad': ad,
        'form_gmail': form_gmail,
    }

    return render(request, 'app/politic.html', context)


def Art(request):
    topics = OneTopic.objects.filter(news_type=4)

    ad = Ad.objects.all()[:1].get()
    topics_paginator = Paginator(topics, 10)

    page_num = request.GET.get('page')

    page = topics_paginator.get_page(page_num)

    form_gmail = GmailsForm()

    if request.method == "POST":
        form_gmail = GmailsForm(request.POST)
    if form_gmail.is_valid():
        data = form_gmail.save(commit=False)
        data.Email = form_gmail.cleaned_data.get('Email')
        data.save()

        return redirect('App:Art')
    context = {
        'topics': topics,
        'page': page,
        'count': topics_paginator.count,
        'ad': ad,
        'form_gmail': form_gmail,
    }

    return render(request, 'app/politic.html', context)


def History(request):
    topics = OneTopic.objects.filter(news_type=5)
    ad = Ad.objects.all()[:1].get()
    topics_paginator = Paginator(topics, 10)

    page_num = request.GET.get('page')

    page = topics_paginator.get_page(page_num)

    form_gmail = GmailsForm()

    if request.method == "POST":
        form_gmail = GmailsForm(request.POST)
    if form_gmail.is_valid():
        data = form_gmail.save(commit=False)
        data.Email = form_gmail.cleaned_data.get('Email')
        data.save()

        return redirect('App:History')
    context = {
        'topics': topics,
        'page': page,
        'count': topics_paginator.count,
        'ad': ad,
        'form_gmail': form_gmail,
    }

    return render(request, 'app/politic.html', context)


def Other(request):
    topics = OneTopic.objects.filter(news_type=1)
    ad = Ad.objects.all()[:1].get()
    topics_paginator = Paginator(topics, 10)

    page_num = request.GET.get('page')

    page = topics_paginator.get_page(page_num)

    form_gmail = GmailsForm()

    if request.method == "POST":
        form_gmail = GmailsForm(request.POST)
    if form_gmail.is_valid():
        data = form_gmail.save(commit=False)
        data.Email = form_gmail.cleaned_data.get('Email')
        data.save()

        return redirect('App:Other')
    context = {
        'topics': topics,
        'page': page,
        'count': topics_paginator.count,
        'ad': ad,
        'form_gmail': form_gmail,
    }

    return render(request, 'app/politic.html', context)


def Gmails(request):
    form_gmail = GmailsForm()

    if request.method == "POST":
        form_gmail = GmailsForm(request.POST)
    if form_gmail.is_valid():
        data = form_gmail.save(commit=False)
        data.Email = form_gmail.cleaned_data.get('Email')
        data.save()

        return redirect('App:HomePage')

    context = {
        'form_gmail': form_gmail,
    }

    return render(request, 'app/base.html', context)
