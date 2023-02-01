class ProfileNotFoundException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Linkedin profile not found"
