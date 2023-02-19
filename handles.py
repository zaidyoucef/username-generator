def name_to_username(first_name: str, last_name: str) -> str:
    """
    Return a username for a user based on their first and last name.
    """
    T = []
    T.extend([last_name+first_name, first_name + last_name, last_name+"."+first_name,
              first_name+"."+last_name, first_name[0]+"."+first_name,
              first_name+"."+last_name[0], last_name[0]+"."+first_name,
              last_name[0]+first_name[0]+"."+first_name +
              last_name, last_name[0]+first_name[0]+"."+last_name+first_name,
              first_name[0]+last_name[0]+"."+first_name+last_name, first_name[0]+last_name[0]+"."+last_name+first_name])

    return T


print(name_to_username("John", "Doe"))
