import re
from django.core.exceptions import ValidationError

def only_digits(value):
    return re.sub(r'\D', '', value or '')

def validate_cpf(value):
    cpf = only_digits(value)
    if len(cpf) != 11:
        raise ValidationError("CPF deve ter 11 dígitos.")
    if cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido.")
    def calc_digit(digs):
        s = sum(int(d)*w for d, w in zip(digs, range(len(digs)+1, 1, -1)))
        r = (s * 10) % 11
        return '0' if r == 10 else str(r)
    d1 = calc_digit(cpf[:9])
    d2 = calc_digit(cpf[:9] + d1)
    if cpf[-2:] != d1 + d2:
        raise ValidationError("CPF inválido.")

def validate_cnpj(value):
    cnpj = only_digits(value)
    if len(cnpj) != 14:
        raise ValidationError("CNPJ deve ter 14 dígitos.")
    if cnpj == cnpj[0] * 14:
        raise ValidationError("CNPJ inválido.")
    def calc_digit(digs, weights):
        s = sum(int(d) * w for d, w in zip(digs, weights))
        r = s % 11
        return '0' if r < 2 else str(11 - r)
    weights1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    weights2 = [6] + weights1
    d1 = calc_digit(cnpj[:12], weights1)
    d2 = calc_digit(cnpj[:12] + d1, weights2)
    if cnpj[-2:] != d1 + d2:
        raise ValidationError("CNPJ inválido.")
