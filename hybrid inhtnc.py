class grandfather:
    def grandfather_method():
        return "this is grandfather method"
class father(grandfather):
    def father_method():
        return "this is a father method"
class mother:
    def mother_method():
        return "this is a mother method"
class child(father,mother):
    def child_method():
        return "i have properties of mother and father"
grandfather_obj=grandfather
father_obj=father
mother_obj=mother
child_obj=child
print(grandfather_obj.grandfather_method())
print(father_obj.father_method())
print(father_obj.grandfather_method())
print(mother_obj.mother_method())
print(child_obj.child_method())
print(child_obj.father_method())
print(child_obj.grandfather_method())
print(child_obj.mother_method())
