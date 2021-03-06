from rest_framework import serializers

from .models import Photo, Preview, PhotoEdit


class PreviewSerializer(serializers.ModelSerializer):
	"""Serialize the effects model.
	"""
	class Meta:
		model = Preview
		fields = ('preview_id', 'preview_name', 'path', 'photo')
		read_only_fields = ('preview_name', 'path')


class PhotoSerializer(serializers.ModelSerializer):
	"""Serialize the Photo model.

	Specify the Photo model fields to be returned to the user (or to be expected
	of the user).
	"""
	file_url = serializers.CharField(source='path.url', read_only=True)
	file_name = serializers.CharField(source='get_file_name', read_only=True)
	filter_effects = serializers.ChoiceField(
		['BLUR', 'EMBOSS', 'DETAIL', 'CONTOUR', 'SMOOTH', 'SHARPEN'],
		write_only=True,
		allow_null=True
	)

	class Meta:
		model = Photo
		fields = ('photo_id', 'path', 'filter_effects', 'file_url', 'file_name',)


class PhotoEditSerializer(serializers.ModelSerializer):
	"""Serialize the PhotoEdit model.
	"""

	file_name = serializers.CharField(source='get_file_name', read_only=True)

	class Meta:
		model = PhotoEdit
		fields = ('photo', 'upload', 'photo_edit_id', 'file_name', 'effect_name')
