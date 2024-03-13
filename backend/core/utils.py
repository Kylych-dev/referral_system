import uuid

def generate_ref_code():
    code = str(uuid.uuid4()).replace('-', '')[:12]
    return code


def normalize_email(email):
    """
    Нормализует адрес электронной почты
    """
    return email.strip().lower()
