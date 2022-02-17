from random import randint


def generate_send_verification_code(client,number_to: str):
    code = (randint(100000, 999999))
    message = client.messages.create(
        to=number_to,
        from_="+19377292126",
        body=f"Your verification code is: {code}"
    )
    return code
