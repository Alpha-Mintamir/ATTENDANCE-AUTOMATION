from math import radians, sin, cos, sqrt, atan2

class GeofenceService:
    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2):
        # Haversine formula to calculate distance between two points
        R = 6371000  # Earth's radius in meters

        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c

        return distance

    @staticmethod
    def is_within_geofence(point_lat, point_lng, center_lat, center_lng, radius):
        distance = GeofenceService.calculate_distance(
            point_lat, point_lng, center_lat, center_lng
        )
        return distance <= radius 