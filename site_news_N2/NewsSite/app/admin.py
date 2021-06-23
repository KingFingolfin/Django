from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html_join
from .models import OneTopic, Ad, Contact, Gmails, Comment


class ContactAdmin(admin.ModelAdmin):
    list_display = ("Name", "Email")
    list_display_links = ("Email", "Name")
    readonly_fields = ("Name", "Email")


class OneTopicAdmin(admin.ModelAdmin):
    list_display = ("title", "nameAuthor","get_picture")
    list_filter = ("news_type", "nameAuthor")
    search_fields = ("title",)
    save_on_top = True
    fieldsets = (
        ("Article", {"fields": (("title", "picture"),)}),
        (None, {"fields": (("text", "news_type"),)}),
        ("Author", {"classes": ("collapse",), "fields": (("nameAuthor", "imageAuthor"), "aboutAuthor")}),
    )

    def get_picture(self,obj):
        return mark_safe(f'<img src={obj.picture.url} width="50" >')
    get_picture.short_description = "Picture"


# Register your models here.
admin.site.register(OneTopic, OneTopicAdmin)
admin.site.register(Ad)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Gmails)
admin.site.register(Comment)

admin.site.site_title = "News For You(admin)"
admin.site.site_header = "News For You(admin)"