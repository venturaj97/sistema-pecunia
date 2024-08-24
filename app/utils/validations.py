from fastapi import HTTPException, status


def check_balance(user_balance: float, transfer_value: float):
    if user_balance < transfer_value:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Saldo insuficiente para realizar a transferência."
        )