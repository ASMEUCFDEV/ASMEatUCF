from django.contrib import admin

from .models import PrinterFile, Colors, OfficerModel, OfficerTitleModel, AboutModel

admin.site.register(PrinterFile)
admin.site.register(Colors)
admin.site.register(OfficerModel)
admin.site.register(OfficerTitleModel)
admin.site.register(AboutModel)


from django.contrib import admin

from content_editor.admin import ContentEditor
from feincms3 import plugins
from feincms3.admin import TreeAdmin

from . import models




class PageAdmin(ContentEditor, TreeAdmin):
    list_display = ["indented_title", "move_column", "is_active"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["parent"]

    inlines = [
        plugins.richtext.RichTextInline.create(models.RichText),
        plugins.image.ImageInline.create(models.Image),
    ]

    # fieldsets = ... (Recommended! No example here though. Note
    # that the content editor not only allows collapsed, but also
    # tabbed fieldsets -- simply add 'tabbed' to the 'classes' key
    # the same way you'd add 'collapse'.

    # class Media: ... (Add font-awesome from a CDN and nicely
    # looking buttons for plugins as is described in
    # django-content-editor's documentation -- search for
    # "plugin_buttons.js")


admin.site.register(models.Page, PageAdmin)
