from datetime import datetime
from sqlalchemy.orm import Session
from .geofence_service import GeofenceService
from ..models import models

class AttendanceService:
    def __init__(self, db: Session):
        self.db = db
        self.geofence_service = GeofenceService()

    async def verify_and_record_attendance(self, attendance_data: dict):
        # Get the class session
        session = self.db.query(models.ClassSession).filter(
            models.ClassSession.qr_code_data == attendance_data["qr_data"]
        ).first()

        if not session:
            raise ValueError("Invalid or expired QR code")

        # Verify student is within geofence
        is_within_fence = self.geofence_service.is_within_geofence(
            attendance_data["location"]["latitude"],
            attendance_data["location"]["longitude"],
            session.location_lat,
            session.location_lng,
            session.radius
        )

        if not is_within_fence:
            raise ValueError("Student is not within the classroom area")

        # Verify WiFi network
        if attendance_data["wifi_ssid"] != "UNIVERSITY_WIFI":  # Configure as needed
            raise ValueError("Not connected to university WiFi")

        # Record attendance
        new_attendance = models.Attendance(
            student_id=attendance_data["student_id"],
            session_id=session.id,
            timestamp=datetime.now(),
            location_lat=attendance_data["location"]["latitude"],
            location_lng=attendance_data["location"]["longitude"],
            wifi_ssid=attendance_data["wifi_ssid"],
            device_id=attendance_data["device_id"]
        )

        self.db.add(new_attendance)
        self.db.commit()
        return new_attendance 