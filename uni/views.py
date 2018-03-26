# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render ,  get_object_or_404

from .models import Program, Category, Location

from mptt.admin import MPTTModelAdmin
from .forms import CategoryForm
from mptt.forms import MoveNodeForm



def show_category(request,hierarchy= None):
    """

    :param request:  mandatory
    :param hierarchy:  hierarcy category
    :return:  the  categories associate with  a program
    """
    category_slug = hierarchy.split('/')
    parent = None
    root = Category.objects.all()

    for slug in category_slug[:-1]:
        parent = root.get(parent=parent, slug = slug)

    try:
        instance = Category.objects.get(parent=parent,slug=category_slug[-1])
    except:
        instance = get_object_or_404(Program, slug = category_slug[-1])
        return render(request, "programDetail.html", {'instance':instance})
    else:
        return render(request, 'categories.html', {'instance':instance})



def program_detail(request,slug=None):
    """
    :param request:  mandatory
    :param slug: slug program
    :return: the program detail
    """
    instance = get_object_or_404(Program,slug=slug)
    return render(request,"program_detail.html",{ 'instance':instance})




def program_list(request,filter=None):
    """

    :param request: mandatory
    :param slug:
    :return: all the programs
    """
    categories = Category.objects.all()
    locations =Location.objects.all()
    programs = Program.objects.all()
    form= CategoryForm()

    query_cat = request.GET.get('category')
    query_loc = request.GET.get('location')

    if query_cat and query_loc :
        filter = categories.filter(id = query_cat)
        filter_node = filter.get_descendants(include_self=True)
        programs = Program.objects.filter(category_id__in=filter_node)


    return render(request,"program_list.html",{ 'programs':programs, 'categories':categories, 'locations': locations,'form':form,})