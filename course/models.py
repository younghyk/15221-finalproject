from django.db import models


class Department(models.Model):
    id = models.SmallIntegerField(
        unique=True,
        primary_key=True,
        null=False,
        blank=False
    )
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False
    )

    def __unicode__(self):
        return str(self.id) + ": " + self.title


class Course(models.Model):
    id = models.SmallIntegerField(
        unique=True,
        primary_key=True,
        null=False,
        blank=False
    )
    department = models.ForeignKey(
        'Department',
        null=False,
        blank=False
    )
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    description = models.CharField(
        max_length=1000,
        null=False,
        blank=False
    )
    units = models.SmallIntegerField(
        null=False,
        blank=False
    )
    corequirements = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    prerequirements = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    fallsemester = models.BooleanField(
        default=False
    )
    springsemester = models.BooleanField(
        default=False
    )
    summersemester = models.BooleanField(
        default=False
    )
    availablenextsemester = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False
    )

    @property
    def full_id_str(self):
        return str(self.department_id) + "-" + str(self.id)

    def __unicode__(self):
        return self.full_id_str + ": " + self.title
