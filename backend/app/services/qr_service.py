import qrcode
import json
from datetime import datetime, timedelta
import uuid

class QRCodeService:
    def generate_class_qr(self, class_id: str, lecturer_id: str, duration_minutes: int = 10):
        # Generate unique session ID
        session_id = str(uuid.uuid4())
        
        # Create QR data
        qr_data = {
            "class_id": class_id,
            "lecturer_id": lecturer_id,
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            "valid_until": (datetime.now() + timedelta(minutes=duration_minutes)).isoformat()
        }
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(json.dumps(qr_data))
        qr.make(fit=True)
        
        return qr.make_image(fill_color="black", back_color="white")