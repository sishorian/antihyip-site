import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Question(models.Model):
    """
    A single question.
    """

    text = models.CharField(max_length=100, help_text=_("The question itself"))
    description = models.CharField(
        max_length=200,
        blank=True,  # null=True not needed because we have empty string
        help_text=_("Clarify the question"),
    )

    def __str__(self):
        return str(self.text)


class Answer(models.Model):
    """
    An answer to a specific question.
    """

    text = models.CharField(max_length=100, help_text=_("The answer itself"))
    description = models.CharField(
        max_length=200,
        blank=True,
        help_text=_("Clarify the meaning in context of the question"),
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        help_text=_("The question you are answering"),
    )

    """
    # Replaced by bad_score.
    bad_absolute = models.BooleanField(
        # Fail by default to reduce the theoretical damage
        # of "forgot to set the flag".
        default=True,  # pyright: ignore[reportArgumentType]
        help_text=_(  # pyright: ignore[reportArgumentType]
            "If chosen by user, flags the site as fraud"
        ),
    )
    """
    bad_score = models.PositiveSmallIntegerField(
        default=100,  # pyright: ignore[reportArgumentType]
        help_text=_(  # pyright: ignore[reportArgumentType]
            "Likeliness of the site being a fraud, 100 = fraud"
        ),
    )

    def __str__(self):
        return str(self.text)


class QGroup(models.Model):
    """
    A group of questions.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text=_("Label for the group"),
    )
    description = models.CharField(
        max_length=200, blank=True, help_text=_("Meaning of the group's name")
    )
    questions = models.ManyToManyField(
        Question, help_text=_("That are part of this group")
    )

    def __str__(self):
        return str(self.name)


class BadSite(models.Model):
    """
    Model representing a site known to be fraud.
    """

    id = models.UUIDField(
        "ID",
        primary_key=True,
        default=uuid.uuid4,
        help_text=_("Unique ID for a particular site"),
    )
    # If there are multiple domains, just create entrires with duplicate name.
    name = models.CharField(
        max_length=50,
        # unique=True,
        help_text=_("Name of the site or the company behind it"),
    )
    # domains = models.JSONField(
    #     help_text=_("JSON list of strings of different domains of the same site")
    # )
    domain = models.CharField(
        max_length=100,
        unique=True,
        help_text=_("Domain of the site, e.g. pyramid.com"),
    )
    bad_type = models.CharField(
        max_length=100,
        help_text=_("What type of fraud it is, e.g. pyramid, scam, etc."),
    )

    def __str__(self):
        return str(self.name)
