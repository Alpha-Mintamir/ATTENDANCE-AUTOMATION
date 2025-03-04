from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .database import get_db
from .services.attendance_service import AttendanceService
from .services.qr_service import QRCodeService
from .services.report_service import ReportService

app = FastAPI(title="University Attendance System")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Basic models
class AttendanceRecord(BaseModel):
    student_id: str
    class_id: str
    timestamp: datetime
    location: dict
    wifi_ssid: str
    device_id: str

@app.get("/")
async def root():
    return {"message": "University Attendance System API"}

@app.post("/api/attendance/verify")
async def verify_attendance(
    attendance_data: dict,
    db: Session = Depends(get_db)
):
    try:
        attendance_service = AttendanceService(db)
        result = await attendance_service.verify_and_record_attendance(attendance_data)
        return {"status": "success", "message": "Attendance recorded successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/class/generate-qr")
async def generate_class_qr(
    class_data: dict,
    db: Session = Depends(get_db)
):
    qr_service = QRCodeService()
    qr_image = qr_service.generate_class_qr(
        class_data["class_id"],
        class_data["lecturer_id"],
        class_data.get("duration_minutes", 10)
    )
    # Save QR data to database and return image
    return {"status": "success", "qr_image": qr_image}

@app.get("/api/reports/attendance")
async def get_attendance_report(
    course_id: int,
    start_date: datetime,
    end_date: datetime,
    db: Session = Depends(get_db)
):
    report_service = ReportService(db)
    report_df = report_service.generate_attendance_report(course_id, start_date, end_date)
    
    # Generate Excel file
    filename = f"attendance_report_{course_id}_{datetime.now().strftime('%Y%m%d')}.xlsx"
    report_service.export_to_excel(report_df, filename)
    
    return {"status": "success", "report_url": f"/downloads/{filename}"}
