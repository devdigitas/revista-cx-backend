from rest_framework import serializers

from apps.core.models import *


class SettingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Setting
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'id': { 'read_only': True }
        }


class PageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Page
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'id': { 'read_only': True }
        }

    def update(self, instance, validated_data):
        is_active = validated_data.get('isActive')

        if not is_active:
            validated_data['page'] = 0

        if is_active != instance.isActive:
            updated_page = super().update(instance, validated_data)
            pages = Page.objects.filter(isActive=True).order_by('page')
            counter = 1
            for page in pages:
                if page.page == 0:
                    page.page = pages.count()
                else:
                    page.page = counter
                    counter += 1
                page.save()
        else:
            updated_page = super().update(instance, validated_data)

        return updated_page