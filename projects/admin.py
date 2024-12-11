from django.contrib import admin
from .models import Team, TeamMember, Project, Task, File, Notification, ProjectReport, User

admin.site.register(User)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(File)
admin.site.register(Notification)
admin.site.register(ProjectReport)