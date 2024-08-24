# app/services/notifications.py
import random

def send_notification(user_id: int, message: str):
    # Simula a falha do serviço de notificação 50% das vezes
    if random.choice([True, False]):
        return {"status": "fail", "data": {"message": "Route 'GET:/api/v1/notify' not found"}}
    else:
        return {"status": "success", "data": {"message": f"Notification sent to user {user_id}"}}
