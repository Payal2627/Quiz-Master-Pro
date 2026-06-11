def validate_question_id(question_id):
    return len(question_id.strip()) > 0


def validate_username(username):

    if len(username) < 3:
        return False

    return True


def validate_password(password):

    if len(password) < 4:
        return False

    return True