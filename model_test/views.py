# -*- coding: utf-8 -*-
"""
注意:
1. 自动生成的view代码做权限检验, 只有该App的User才能访问, 以防误上线后数据对其他人可见
   设置方法: 通过Django Admin中auth_user表配置, 添加用户并设置`is_staff=True`. 或者 `开发者中心-应用-数据库-正式环境/测试环境-应用用户信息管理-新增`
2. 不需要的代码可以去除
"""

from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

from common.mymako import render_mako_context

from common.log import logger
from .models import Author, Book
from .forms import AuthorForm, BookForm


@require_http_methods(["GET"])
@staff_member_required
def model_list(request):
    """
    首页，所有的 Model 列表
    """
    context = {}
    return render_mako_context(request, 'model_test/model_list.html', context)


#========================= Author's view method begin =========================
@require_http_methods(["GET", "POST"])
def author_create(request):
    # to form page
    if request.method == "GET":
        # auth check
        if not request.user.is_staff:
            return redirect('admin:index')

        context = {"obj": Author()}
        
        
        return render_mako_context(request, 'model_test/author_create.html', context)

    # auth check
    if not request.user.is_staff:
        return JsonResponse({"result": False, "message": u"非staff用户, 没有权限进行操作, 请找App管理员申请权限!", "data": []})

    # do create, put params into form
    form = AuthorForm(request.POST)

    if not form.is_valid():
        errors = form.errors.as_text()
        return JsonResponse({"result": False, "message": u"创建失败:\n%s" % errors, "data": []})

    try:
        form.save()
    except Exception as e:
        logger.error(u"创建失败: %s" % str(e))
        return JsonResponse({"result": False, "message": u"创建失败: %s" % str(e), "data": []})

    return JsonResponse({"result": True, "message": u"创建成功!", "data": []})


@require_http_methods(["GET", "POST"])
def author_update(request, id):
    # to form page
    try:
        author = Author.objects.get(id=id)
    except ObjectDoesNotExist as e:
        message = u"删除失败: 对象不存在! id=%s" % id
        logger.error(message)
        return JsonResponse({"result": False, "message": message, "data": []})

    if request.method == "GET":
        # auth check
        if not request.user.is_staff:
            return redirect('admin:index')

        context = {"obj": author}
        
        return render_mako_context(request, 'model_test/author_update.html', context)

    # auth check
    if not request.user.is_staff:
        return JsonResponse({"result": False, "message": u"非staff用户, 没有权限进行操作, 请找App管理员申请权限!", "data": []})

    # do update
    form = AuthorForm(request.POST, instance=author)

    if not form.is_valid():
        errors = form.errors.as_text()
        return JsonResponse({"result": False, "message": u"更新失败:\n%s" % errors, "data": []})

    try:
        author = form.save()
    except Exception as e:
        logger.error(u"更新失败: %s" % str(e))
        return JsonResponse({"result": False, "message": u"更新失败: %s" % str(e), "data": []})

    return JsonResponse({"result": True, "message": u"更新失败!", "data": []})


@require_http_methods(["POST"])
def author_delete(request, id):
    """
    do delete
    """
    # auth check
    if not request.user.is_staff:
        return JsonResponse({"result": False, "message": u"非staff用户, 没有权限进行操作, 请找App管理员申请权限!", "data": []})

    try:
        author = Author.objects.get(id=id)
        author.delete()
    except ObjectDoesNotExist as e:
        message = u"删除失败: 对象不存在! id=%s" % id
        logger.error(message)
        return JsonResponse({"result": False, "message": message, "data": []})
    except Exception as e:
        logger.exception(u"删除失败: %s" % str(e))
        return JsonResponse({"result": False, "message": u"删除失败: %s" % str(e), "data": []})

    return JsonResponse({"result": True, "message": u"删除成功!", "data": []})


@require_http_methods(["GET"])
@staff_member_required
def author_detail(request, id):
    """
    get the detail
    """
    try:
        author = Author.objects.get(id=id)
    except ObjectDoesNotExist as e:
        message = u"获取详情信息失败: 对象不存在! id=%s. %s" % (id, str(e))
        logger.error(message)
        raise Http404(message)

    context = {'obj': author}
    return render_mako_context(request, 'model_test/author_detail.html', context)


@require_http_methods(["GET"])
@staff_member_required
def author_list(request):
    """
    get the list
    """
    try:
        page = int(request.GET.get("page", 1))
        page_size = int(request.GET.get("page_size", 10))

        if page < 1:
            page = 1
        if page_size < 1:
            page_size = 10
    except:
        page = 1
        page_size = 10

    # use pagination
    all_query = Author.objects.all()
    paginator = Paginator(all_query, page_size)

    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    context = {'records': records}
    return render_mako_context(request, 'model_test/author_list.html', context)


#========================= Author's view method end =========================


#========================= Book's view method begin =========================
@require_http_methods(["GET", "POST"])
def book_create(request):
    # to form page
    if request.method == "GET":
        # auth check
        if not request.user.is_staff:
            return redirect('admin:index')

        context = {"obj": Book()}
        # 注意: `objects.all()` 当对应表数据较多的时候, 可能产生性能问题, 需要优化
        authors = Author.objects.all()
        context["authors"] = authors
        return render_mako_context(request, 'model_test/book_create.html', context)

    # auth check
    if not request.user.is_staff:
        return JsonResponse({"result": False, "message": u"非staff用户, 没有权限进行操作, 请找App管理员申请权限!", "data": []})

    # do create, put params into form
    form = BookForm(request.POST)

    if not form.is_valid():
        errors = form.errors.as_text()
        return JsonResponse({"result": False, "message": u"创建失败:\n%s" % errors, "data": []})

    try:
        form.save()
    except Exception as e:
        logger.error(u"创建失败: %s" % str(e))
        return JsonResponse({"result": False, "message": u"创建失败: %s" % str(e), "data": []})

    return JsonResponse({"result": True, "message": u"创建成功!", "data": []})


@require_http_methods(["GET", "POST"])
def book_update(request, id):
    # to form page
    try:
        book = Book.objects.get(id=id)
    except ObjectDoesNotExist as e:
        message = u"删除失败: 对象不存在! id=%s" % id
        logger.error(message)
        return JsonResponse({"result": False, "message": message, "data": []})

    if request.method == "GET":
        # auth check
        if not request.user.is_staff:
            return redirect('admin:index')

        context = {"obj": book}
        
        authors = Author.objects.all()
        context["authors"] = authors
        
        return render_mako_context(request, 'model_test/book_update.html', context)

    # auth check
    if not request.user.is_staff:
        return JsonResponse({"result": False, "message": u"非staff用户, 没有权限进行操作, 请找App管理员申请权限!", "data": []})

    # do update
    form = BookForm(request.POST, instance=book)

    if not form.is_valid():
        errors = form.errors.as_text()
        return JsonResponse({"result": False, "message": u"更新失败:\n%s" % errors, "data": []})

    try:
        book = form.save()
    except Exception as e:
        logger.error(u"更新失败: %s" % str(e))
        return JsonResponse({"result": False, "message": u"更新失败: %s" % str(e), "data": []})

    return JsonResponse({"result": True, "message": u"更新失败!", "data": []})


@require_http_methods(["POST"])
def book_delete(request, id):
    """
    do delete
    """
    # auth check
    if not request.user.is_staff:
        return JsonResponse({"result": False, "message": u"非staff用户, 没有权限进行操作, 请找App管理员申请权限!", "data": []})

    try:
        book = Book.objects.get(id=id)
        book.delete()
    except ObjectDoesNotExist as e:
        message = u"删除失败: 对象不存在! id=%s" % id
        logger.error(message)
        return JsonResponse({"result": False, "message": message, "data": []})
    except Exception as e:
        logger.exception(u"删除失败: %s" % str(e))
        return JsonResponse({"result": False, "message": u"删除失败: %s" % str(e), "data": []})

    return JsonResponse({"result": True, "message": u"删除成功!", "data": []})


@require_http_methods(["GET"])
@staff_member_required
def book_detail(request, id):
    """
    get the detail
    """
    try:
        book = Book.objects.get(id=id)
    except ObjectDoesNotExist as e:
        message = u"获取详情信息失败: 对象不存在! id=%s. %s" % (id, str(e))
        logger.error(message)
        raise Http404(message)

    context = {'obj': book}
    return render_mako_context(request, 'model_test/book_detail.html', context)


@require_http_methods(["GET"])
@staff_member_required
def book_list(request):
    """
    get the list
    """
    try:
        page = int(request.GET.get("page", 1))
        page_size = int(request.GET.get("page_size", 10))

        if page < 1:
            page = 1
        if page_size < 1:
            page_size = 10
    except:
        page = 1
        page_size = 10

    # use pagination
    all_query = Book.objects.all()
    paginator = Paginator(all_query, page_size)

    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    context = {'records': records}
    return render_mako_context(request, 'model_test/book_list.html', context)


#========================= Book's view method end =========================
