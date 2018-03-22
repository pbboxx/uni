# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from mptt.forms import TreeNodeChoiceField
from .fields import MultipleChoiceTreeField
from .models import Program, Category, Location
from django.utils.html import mark_safe

# class MultipleChoiceTreeField(forms.ModelMultipleChoiceField):

#  	widget = forms.CheckboxSelectMultiple
#  	def label_from_instance(self, obj):

#  		return obj




# class ProgramForm(forms.ModelForm):

#  	categories = MultipleChoiceTreeField(
# 	label=("Categories"),
#  	required=False,
#  	queryset=Category.objects.all(), )


# 	class Meta:
#  		model = Program
#  		fields = ['name']


# 	def __init__(self, *args, **kwargs):
#  		super(ProgramForm, self).__init__(*args, **kwargs)
#  		self.helper = FormHelper()
#  		self.helper.form_action = ""
#  		self.helper.form_method = "POST"
#  		self.helper.layout = layout.Layout(
#  			layout.Field("name"),
#  			layout.Field("categories"),
#  			layout.Field("categories",
#  					template="utils/"\
#  					"checkbox_select_multiple_tree.html"
#  						),
#  			bootstrap.FormActions(
#  				layout.Submit("submit", ("Save")),
#  				)
#  			)


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


