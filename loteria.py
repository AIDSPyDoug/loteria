import numpy as np
import time
def jogo():
  rng = np.random.default_rng()
  return sorted(rng.choice(range(0,61), size=6, replace=False))
def espera():
  return(np.random.randint(0, 10))
def jogar(qtde):
  for i in range(qtde):
    delay = espera()
    print('esperando', delay, 'segundos para o próximo jogo')
    time.sleep(delay)
    combinacao = jogo()
    
    print('Jogo', i+1, ':' , combinacao)
qtde=10
jogar(qtde)
