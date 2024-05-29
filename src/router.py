from fastapi import APIRouter, Response, status, HTTPException
from pydantic import BaseModel, Field
from .models import Event
from .manager import AccountManager


router = APIRouter()

accounts_manager = AccountManager()


@router.post("/reset")
def reset():
    accounts_manager.reset()
    return Response("OK", status_code=status.HTTP_200_OK)


@router.get("/balance")
def get_balance(account_id: str):
    return accounts_manager.get_balance(account_id)
    

@router.post(
    "/event",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "content": {
                "application/json": {
                    "example": {"destination": {"id": "account_id", "balance": 100}}
                }
            },
            "description": "Deposit event successfully processed",
        },
        status.HTTP_200_OK: {
            "content": {
                "application/json": {
                    "example": {"origin": {"id": "account_id", "balance": 50}}
                }
            },
            "description": "Withdraw event successfully processed",
        },
        status.HTTP_200_OK: {
            "content": {
                "application/json": {
                    "example": {
                        "origin": {"id": "account_id", "balance": 50},
                        "destination": {"id": "another_account_id", "balance": 150},
                    }
                }
            },
            "description": "Transfer event successfully processed",
        },
    },
)
def create_event_or_account(event: Event):
    match event.type:
        case "deposit":
            accounts_manager.deposit(event.destination, event.amount)
            return {
                "destination": {
                    "id": event.destination,
                    "balance": accounts_manager.accounts[event.destination],
                }
            }
        case "withdraw":
            accounts_manager.withdraw(event.origin, event.amount)
            return {
                "origin": {
                    "id": event.origin,
                    "balance": accounts_manager.accounts[event.origin],
                }
            }
        case "transfer":
            accounts_manager.transfer(event.origin, event.destination, event.amount)
            return {
                "origin": {
                    "id": event.origin,
                    "balance": accounts_manager.accounts[event.origin],
                },
                "destination": {
                    "id": event.destination,
                    "balance": accounts_manager.accounts[event.destination],
                },
            }
        case _:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid event type"
            )
