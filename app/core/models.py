from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sentences(models.Model):
    SENTIMENT = (
        ("Positive", "Positive"),
        ("Neutral", "Neutral"),
        ("Negative", "Negative"),
    )

    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name="category_sentence",
        null=True,
        blank=True,
    )

    text = models.TextField(max_length=255, null=True, blank=True)
    sentiment = models.CharField(
        choices=SENTIMENT, max_length=255, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def colour_class(self):
        COLOUR_CLASSES = {
            "Positive": "bg-success",
            "Neutral": "bg-secondary",
            "Negative": "bg-danger",
        }
        colour_class = COLOUR_CLASSES[self.sentiment] if self.sentiment else " "
        return colour_class
