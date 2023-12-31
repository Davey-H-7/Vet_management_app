import pdb

from models.pet import Pet
from models.vet import Vet
from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

pet_repository.delete_all()
vet_repository.delete_all()
owner_repository.delete_all()

vet1 = Vet('Martha', 'Jones', 'Head Veterinarian')
vet_repository.save(vet1)
vet2 = Vet('Rose', 'Tyler', 'Junior Veterinarian')
vet_repository.save(vet2)
vet3 = Vet('Bill', 'Sickley', 'Exotic Animal Specialist')
vet_repository.save(vet3)

owner1 = Owner('Carol', 'Hill', '09876 455 322')
owner_repository.save(owner1)
owner2 = Owner('Malcolm', 'Hunter', '07823 567 211')
owner_repository.save(owner2)
owner3 = Owner('Donatello', ' Turtle', '01564 768 900')
owner_repository.save(owner3)

pet1 = Pet('Sid', '2013-06-05', 'Cat', owner2, vet1, 'old and heavy')
pet_repository.save(pet1)
pet2 = Pet('Skye', '2017-01-25', 'Dog', owner1, vet2, 'No major issues')
pet_repository.save(pet2)
pet3 = Pet('Finn', '2022-08-19', 'Snake', owner1, vet3, 'Hip transplant')
pet_repository.save(pet3)
pet4 = Pet('Percy', '2018-03-12', 'Parrot', owner3, vet3, 'Cracker addiction')
pet_repository.save(pet4)
pet5 = Pet('Hamburg', '2020-02-24', 'Hamster', owner3, vet1, 'Antibiotics prescriped')
pet_repository.save(pet5)
pet6 = Pet('Vera', '2023-06-07', 'Dog', owner2, vet1, 'Growing well')
pet_repository.save(pet6)

# pet4.name = 'Polly'
# pet_repository.update(pet4)
# owner2.first_name ='Lauren'
# owner_repository.update(owner2)

owner = owner_repository.select(3)
# pets =pet_repository.pets_for_owner(owner1)
# owner = owner_repository.owner_for_pet(pet2)




# pet_repository.delete_all()
# pet_repository.delete(2)

# pet1.name = 'Molly'
# pet_repository.update(pet1)

# pet = pet_repository.select(3)
# pdb.set_trace()
# pdb.set_trace()

# vet3 = vet_repository.select(1)

# vet_repository.delete(1)
# vets = vet_repository.select_all()

# vet1 = Vet('Martin', 'Jones', 'Head Veterinarian')
# vet_repository.update(vet1)
# vets = vet_repository.select_all()

# vet = vet_repository.vet_for_pet(pet2)
# pet = pet_repository.pets_for_vet(vet1)


# pdb.set_trace()

