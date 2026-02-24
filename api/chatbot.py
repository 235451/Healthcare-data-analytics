"""
Doctor AI Chatbot API
--------------------
Secure endpoint for doctors to query the AI clinical assistant.
Used for decision support in government hospitals.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from api.schemas import ChatbotInput
from api.auth import get_current_user
from src.doctor_chatbot import doctor_chatbot

router = APIRouter(
    prefix="/doctor",
    tags=["Doctor AI Assistant"]
)


@router.post("/chatbot", status_code=status.HTTP_200_OK)
def doctor_chatbot_endpoint(
    payload: ChatbotInput,
    current_user: dict = Depends(get_current_user)
):
    """
    Handle doctor queries to AI chatbot.

    Args:
        payload (ChatbotInput): Doctor question + patient context
        current_user (dict): Authenticated doctor/admin user

    Returns:
        dict: AI-generated medical response
    """

    if not payload.query.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Query cannot be empty"
        )

    try:
        ai_response = doctor_chatbot(
            query=payload.query,
            patient=payload.patient # type: ignore
        )

        return {
            "success": True,
            "doctor_id": current_user.get("user_id"),
            "answer": ai_response
        }

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Chatbot processing failed: {str(exc)}"
        )
