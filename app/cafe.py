import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        # Check vaccine key
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccinated")

        # Check vaccine expiration
        vaccine = visitor["vaccine"]
        expiration_date = vaccine.get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError("Vaccine is outdated")

        # Check mask
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("Visitor is not wearing a mask")

        return f"Welcome to {self.name}"
