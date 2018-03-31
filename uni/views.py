# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render ,  get_object_or_404

from .models import Program, Category, Location

from mptt.admin import MPTTModelAdmin
from .forms import CategoryForm
from mptt.forms import MoveNodeForm
from django.contrib.auth.decorators import login_required



# Error Pages
def server_error(request):
    return render(request, "500.html",)

def not_found(request):
    return render(request, "404.html",)


def permission_denied(request):
    return render(request, "403.html",)


def bad_request(request):
    return render(request, "400.html",)




@login_required
def home_dash(request,filter=None):
    """
    :param request: mandatory
    :param slug:
    :return: home page
    """


    return render(request, "home.html",)




@login_required
def profile_dash(request,filter=None):
    """
    :param request:
    :param slug:
    :return:  Profile account
    """
    return render(request, "profile.html",)



@login_required
def career(request,filter=None):
    """
    :param request:
    :param filter:
    :return:  Career
    """
    return render(request, "career.html",)



@login_required
def job(request,filter=None):
    """
    :param request:
    :param filter:
    :return: Jobs
    """

    return render(request, "job.html",)

@login_required
def degree(request,filter=None):

    categories = Category.objects.all()
    locations =Location.objects.all()
    programs = Program.objects.all()[:1000]
    form= CategoryForm(request.GET)

    if form.is_valid():
        query_loc = request.GET.get('location')

        if form.cleaned_data["location"] and form.cleaned_data["category"]:
            filter_loc = locations.filter(id=query_loc)
            filter_node_loc = filter_loc.get_descendants(include_self=True)
            filter_cat = categories.filter(name=form.cleaned_data["category"])
            filter_node_cat = filter_cat.get_descendants(include_self=True)
            for e in filter_node_cat:
                vals = str(e)
                programs = Program.objects.filter(location_id__in=filter_node_loc, name__icontains=vals)

        elif form.cleaned_data["location"]:
            query_loc = request.GET.get('location')
            filter = locations.filter(id = query_loc)
            filter_node = filter.get_descendants(include_self=True)
            programs = Program.objects.filter(location_id__in=filter_node)

        elif form.cleaned_data["category"]:
            filter = categories.filter(name=form.cleaned_data["category"])
            filter_node = filter.get_descendants(include_self=True)
            for e in filter_node:
                vals = str(e)
                programs = Program.objects.filter(name__icontains=vals)


    return render(request, "degree.html", { 'programs':programs, 'categories':categories, 'locations': locations,'form':form,})





# def program_list(request,filter=None):
#     """
#
#     :param request: mandatory
#     :param slug:
#     :return: all the programs
#     """
#     categories = Category.objects.all()
#     locations =Location.objects.all()
#     programs = Program.objects.all()[:1000]
#     form= CategoryForm(request.GET)
#
#     if form.is_valid():
#         query_loc = request.GET.get('location')
#
#         if form.cleaned_data["location"] and form.cleaned_data["category"]:
#             filter_loc = locations.filter(id=query_loc)
#             filter_node_loc = filter_loc.get_descendants(include_self=True)
#             filter_cat = categories.filter(name=form.cleaned_data["category"])
#             filter_node_cat = filter_cat.get_descendants(include_self=True)
#             for e in filter_node_cat:
#                 vals = str(e)
#                 programs = Program.objects.filter(location_id__in=filter_node_loc, name__icontains=vals)
#
#         elif form.cleaned_data["location"]:
#             query_loc = request.GET.get('location')
#             filter = locations.filter(id = query_loc)
#             filter_node = filter.get_descendants(include_self=True)
#             programs = Program.objects.filter(location_id__in=filter_node)
#
#         elif form.cleaned_data["category"]:
#             filter = categories.filter(name=form.cleaned_data["category"])
#             filter_node = filter.get_descendants(include_self=True)
#             for e in filter_node:
#                 vals = str(e)
#                 programs = Program.objects.filter(name__icontains=vals)
#
#
#     return render(request,"program_list.html",{ 'programs':programs, 'categories':categories, 'locations': locations,'form':form,})