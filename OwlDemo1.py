from owlready2 import *

# Load the OWL file
onto = get_ontology("LocalSuperMarketOntology.owl").load()

# Get classes and their subclasses
print("Classes:")
for cls in onto.classes():
    print("Class:", cls)
    print("  Subclasses:", list(cls.subclasses()))

# Get object properties and their domains and ranges
print("\nObject Properties:")
for prop in onto.object_properties():
    print("Property:", prop)
    print("  Domain:", list(prop.domain))
    print("  Range:", list(prop.range))

# Get individuals and their types
print("\nIndividuals:")
for ind in onto.individuals():
    print("Individual:", ind)
    print("  Types:", list(ind.is_a))

