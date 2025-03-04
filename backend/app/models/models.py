from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    user_type = Column(String)  # 'student' or 'lecturer'
    device_id = Column(String, unique=True)  # For device binding
    is_active = Column(Boolean, default=True)

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True)
    name = Column(String)
    lecturer_id = Column(Integer, ForeignKey("users.id"))
    
    lecturer = relationship("User")
    sessions = relationship("ClassSession", back_populates="course")

class ClassSession(Base):
    __tablename__ = "class_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    qr_code_data = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    location_lat = Column(Float)
    location_lng = Column(Float)
    radius = Column(Float)  # Geofence radius in meters
    
    course = relationship("Course", back_populates="sessions")
    attendances = relationship("Attendance", back_populates="session")

class Attendance(Base):
    __tablename__ = "attendances"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    session_id = Column(Integer, ForeignKey("class_sessions.id"))
    timestamp = Column(DateTime)
    location_lat = Column(Float)
    location_lng = Column(Float)
    wifi_ssid = Column(String)
    device_id = Column(String)
    
    student = relationship("User")
    session = relationship("ClassSession", back_populates="attendances") 