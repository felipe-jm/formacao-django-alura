from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Chrome('/Users/felipejung/Developer/alura/django_tdd/tdd_busca_animal/chromedriver')
    self.animal = Animal.objects.create(
      nome_animal = 'Ornitorrinco',
      predador = 'Sim',
      venenoso = 'Sim',
      domestico = 'Não',
    )

  def tearDown(self):
    self.browser.quit()

  def test_abre_janela_do_chrome(self):
    self.browser.get(self.live_server_url)

  # def test_deu_ruim(self):
  #   """Teste de exemplo de erro"""
  #   self.fail('Teste falhou')

  def test_buscando_um_novo_animal(self):
    """
    Testa se um usuário encontra um animal na pesquisa
    """
    home_page = self.browser.get(self.live_server_url + '/')
    brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
    self.assertEqual('Busca Animal', brand_element.text)

    buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
    self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso...')

    buscar_animal_input.send_keys('ornitorrinco')
    self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

    caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
    self.assertGreater(len(caracteristicas), 3)