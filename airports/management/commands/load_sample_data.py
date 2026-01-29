from django.core.management.base import BaseCommand
from airports.models import AirportRoute


class Command(BaseCommand):
    help = "Load sample airport route data into the database"

    def handle(self, *args, **options):
        self.stdout.write("Clearing existing airport data...")
        AirportRoute.objects.all().delete()

        self.stdout.write("Creating sample airport route network...")

        # Terminal airports (leaf nodes)
        self.stdout.write("Creating terminal airports...")

        sfo = AirportRoute.objects.create(
            airport_code="SFO",
            position="West Coast Terminal",
            duration=25,
        )

        sea = AirportRoute.objects.create(
            airport_code="SEA",
            position="Pacific Northwest Hub",
            duration=35,
        )

        mia = AirportRoute.objects.create(
            airport_code="MIA",
            position="Southeast Gateway",
            duration=40,
        )

        atl = AirportRoute.objects.create(
            airport_code="ATL",
            position="Southern Hub",
            duration=55,
        )

        # Regional hubs
        self.stdout.write("Creating regional hubs...")

        lax = AirportRoute.objects.create(
            airport_code="LAX",
            position="West Coast Hub",
            duration=45,
            left=sfo,
            right=sea,
        )

        ord = AirportRoute.objects.create(
            airport_code="ORD",
            position="Central Hub",
            duration=65,
            left=mia,
            right=atl,
        )
        # Major connecting airports
        self.stdout.write("Creating major connecting airports...")

        jfk = AirportRoute.objects.create(
            airport_code="JFK",
            position="East Coast Gateway",
            duration=75,
            left=lax,
        )

        dfw = AirportRoute.objects.create(
            airport_code="DFW",
            position="National Hub",
            duration=85,
            right=ord,
        )

        # Main hub
        self.stdout.write("Creating main hub...")

        den = AirportRoute.objects.create(
            airport_code="DEN",
            position="Main Hub",
            duration=95,
            left=jfk,
            right=dfw,
        )

        self.stdout.write(self.style.SUCCESS("✅ Sample data loaded successfully!"))

        self.stdout.write("\nAirport Route Network Structure:")
        self.stdout.write(
            """
                    DEN (Main Hub, 95 min)
                   /                        \\
        JFK (East Coast Gateway, 75)    DFW (National Hub, 85)
               /                                    \\
        LAX (West Coast Hub, 45)            ORD (Central Hub, 65)
           /              \\                    /              \\
    SFO (25)          SEA (35)           MIA (40)          ATL (55)
            """
        )

        self.stdout.write("\nStatistics:")
        self.stdout.write(f"Total airports created: {AirportRoute.objects.count()}")
        self.stdout.write(
            f"Shortest duration: {AirportRoute.get_airport_with_shortest_duration()}"
        )
        self.stdout.write(
            f"Longest duration: {AirportRoute.get_airport_with_longest_duration()}"
        )

        self.stdout.write("\nTest Queries:")
        self.stdout.write("1. DEN → Left → SFO (25 min)")
        self.stdout.write("2. DEN → Right → ATL (55 min)")
        self.stdout.write("3. JFK → Left → SFO (25 min)")
        self.stdout.write("4. DFW → Right → ATL (55 min)")
