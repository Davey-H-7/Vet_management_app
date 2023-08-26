from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet
import pdb

def save (pet):
    sql = "INSERT INTO pets (name, dob, species, owner, contact_no, vet_id, treatment_notes) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.name, pet.dob, pet.species, pet.owner, pet.contact_no, pet.vet.id, pet.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet