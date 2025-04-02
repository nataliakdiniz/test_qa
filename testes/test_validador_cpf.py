import unittest
from app.validador_cpf import validar_cpf

class TestValidadorCPF(unittest.TestCase):
    def test_cpf_valido(self):
        # Teste com CPF válido sem formatação
        self.assertTrue(validar_cpf('52998224725'))
        # Teste com CPF válido com formatação
        self.assertTrue(validar_cpf('529.982.247-25'))

    def test_cpf_invalido(self):
        # Teste com CPF inválido sem formatação
        self.assertFalse(validar_cpf('12345678900'))
        # Teste com CPF inválido com formatação
        self.assertFalse(validar_cpf('123.456.789-00'))

    def test_cpf_sequencia_repetida(self):
        # Teste com CPF com todos os dígitos iguais
        self.assertFalse(validar_cpf('11111111111'))
        self.assertFalse(validar_cpf('22222222222'))
        self.assertFalse(validar_cpf('99999999999'))

    def test_cpf_tamanho_incorreto(self):
        # Teste com CPF com menos de 11 dígitos
        self.assertFalse(validar_cpf('1234567890'))
        # Teste com CPF com mais de 11 dígitos
        self.assertFalse(validar_cpf('123456789012'))

    def test_cpf_caracteres_especiais(self):
        # Teste com CPF contendo caracteres especiais
        self.assertTrue(validar_cpf('529.982.247-25'))
        self.assertTrue(validar_cpf('52998224725'))
        self.assertTrue(validar_cpf('529-982-247.25'))

if __name__ == '__main__':
    unittest.main() 