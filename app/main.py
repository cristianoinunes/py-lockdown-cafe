from app.cafe import Cafe
import datetime


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    not_vaccinated = 0
    expired = 0
    no_mask = 0

    for friend in friends:
        vaccine = friend.get("vaccine")

        if not vaccine:
            not_vaccinated += 1
            continue

        if vaccine["expiration_date"] < datetime.date.today():
            expired += 1
            continue

        if not friend.get("wearing_a_mask", False):
            no_mask += 1

    if not_vaccinated > 0 or expired > 0:
        return "All friends should be vaccinated"

    if no_mask > 0:
        return f"Friends should buy {no_mask} masks"

    return f"Friends can go to {cafe.name}"
