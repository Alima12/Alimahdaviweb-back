from django.contrib import admin
from .models import Titles, Message, ContactMe, AboutMe, SocialMedia

admin.site.register(Titles)
admin.site.register(Message)
admin.site.register(ContactMe)
admin.site.register(AboutMe)
admin.site.register(SocialMedia)
