from model import User, Preference, PersonalityTrait, UserPersonalityTrait, UserPreference, connect_to_db, db

def create_user(first_name, last_name, email, password, over_21, user_zipcode):
    """creates and returns a new user"""

    user = User(first_name=first_name, last_name=last_name, email=email, password=password, over_21=over_21, user_zipcode=user_zipcode)

    db.session.add(user)
    db.session.commit()

    return user

def create_preference(preference_name):
    """creates and returns a preference"""

    preference = Preference(preference_name=preference_name)

    db.session.add(preference)
    db.session.commit()

    return preference

def create_trait(trait_name):
    """creates and returns a trait"""

    ptrait = PersonalityTrait(trait_name=trait_name)

    db.session.add(ptrait)
    db.session.commit()

    return ptrait

def create_user_ptrait(user_id, trait_id):
    """creates and returns a user personality trait"""

    user_ptrait = UserPersonalityTrait(user_id=user_id, trait_id=trait_id)

    db.session.add(user_ptrait)
    db.session.commit()

    return user_ptrait

def create_user_preference(user_id, preference_id):
    """creates and returns a user preference"""

    user_prence = UserPreference(user_id=user_id, preference_id=preference_id)

    db.session.add(user_prence)
    db.session.commit()

    return user_prence

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


