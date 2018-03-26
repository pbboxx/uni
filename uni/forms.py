# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from mptt.forms import TreeNodeChoiceField
from .fields import MultipleChoiceTreeField
from .models import Program, Category, Location
from django.utils.html import mark_safe






class CategoryForm(forms.Form):


	category = TreeNodeChoiceField(
	 label=("Category"),
	queryset=Category.objects.all(),
	required=True,
	level_indicator=mark_safe(
	 "&nbsp;&nbsp;&nbsp;&nbsp;"
	 ),
	 )
	location = TreeNodeChoiceField(
	 label=("Location"),
	queryset=Location.objects.all(),
	required=True,
	level_indicator=mark_safe(
	 "&nbsp;&nbsp;&nbsp;&nbsp;"
	 ),
	 )


