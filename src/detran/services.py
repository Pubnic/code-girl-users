from .models import VehicleModel, DebtModel
from vehicle.services import VehicleService


class DetranService:
    def __init__(self):
        self.vehicle_service = VehicleService()

    def get_full_vehicle(self, license_plate: str):
        vehicle = VehicleModel.objects.filter(license_plate=license_plate).last()

        if not vehicle:
            # Criar um véiculo e débito que ainda não existem no BD
            _vehicle = self.vehicle_service.create_vehicle(license_plate)
            _debts = self.vehicle_service.create_debts()

            # Aqui estou criando de fato no BD
            vehicle = VehicleModel.objects.create(
                license_plate=_vehicle.license_plate,
                renavam=_vehicle.renavam,
                document=_vehicle.document,
                brand=_vehicle.brand,
                model=_vehicle.model,
                year=_vehicle.year,
                color=_vehicle.color
            )
            debts = []
            for debt in _debts:
                debts.append(DebtModel.objects.create(
                    vehicle=vehicle,
                    agency=debt.agency,
                    value=debt.value,
                    date=debt.date
                ))
        else:  # Caso já exista um veículo no BD
            debts = vehicle.debts.all()

        return vehicle, debts
