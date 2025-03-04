from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models import models
from datetime import datetime, timedelta
import pandas as pd

class ReportService:
    def __init__(self, db: Session):
        self.db = db

    def generate_attendance_report(self, course_id: int, start_date: datetime, end_date: datetime):
        # Query all sessions and attendances for the course
        sessions = self.db.query(models.ClassSession).filter(
            models.ClassSession.course_id == course_id,
            models.ClassSession.start_time.between(start_date, end_date)
        ).all()

        report_data = []
        for session in sessions:
            attendances = self.db.query(models.Attendance).filter(
                models.Attendance.session_id == session.id
            ).all()

            for attendance in attendances:
                report_data.append({
                    'date': session.start_time.date(),
                    'student_name': attendance.student.full_name,
                    'student_id': attendance.student.id,
                    'check_in_time': attendance.timestamp,
                    'status': self._get_attendance_status(attendance, session)
                })

        # Convert to DataFrame for easy export
        df = pd.DataFrame(report_data)
        return df

    def _get_attendance_status(self, attendance, session):
        if attendance.timestamp <= session.start_time:
            return "On Time"
        elif attendance.timestamp <= session.start_time + timedelta(minutes=15):
            return "Late"
        else:
            return "Very Late"

    def export_to_excel(self, df, filename):
        df.to_excel(filename, index=False)
        return filename 