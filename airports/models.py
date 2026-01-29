from django.db import models
from django.core.validators import MinValueValidator


class AirportRoute(models.Model):
    """
    Represents an airport node in the flight route system.

    The airport routes form a binary tree structure where each airport can have:
    - A left child airport (left route)
    - A right child airport (right route)

    """

    airport_code = models.CharField(
        max_length=10,
        unique=True,
        help_text="Unique airport code (e.g., JFK, LAX, DEL)",
    )

    position = models.CharField(
        max_length=50, help_text="Position identifier in the route network"
    )

    duration = models.IntegerField(
        validators=[MinValueValidator(0)], help_text="Flight duration in minutes"
    )

    left = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="parent_left",
        help_text="Left child airport in the route",
    )

    right = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="parent_right",
        help_text="Right child airport in the route",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["airport_code"]
        verbose_name = "Airport Route"
        verbose_name_plural = "Airport Routes"

    def __str__(self):
        return f"{self.airport_code} (Position: {self.position}, Duration: {self.duration}min)"

    def get_last_reachable_node(self, direction):
        """
        Traverse the route tree in the specified direction until the last node is reached.

        Args:
            direction (str): Either 'left' or 'right'

        Returns:
            AirportRoute: The last reachable airport node in the specified direction
        """
        current = self

        if direction.lower() == "left":
            while current.left is not None:
                current = current.left
        elif direction.lower() == "right":
            while current.right is not None:
                current = current.right

        return current

    @classmethod
    def get_airport_with_longest_duration(cls):
        """
        Returns:
            AirportRoute: Airport with the longest duration, or None if no airports exist
        """
        return cls.objects.order_by("-duration").first()

    @classmethod
    def get_airport_with_shortest_duration(cls):
        """
        Returns:
            AirportRoute: Airport with the shortest duration, or None if no airports exist
        """
        return cls.objects.order_by("duration").first()
