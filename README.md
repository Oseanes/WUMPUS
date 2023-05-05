# JOGO WUMPUS
Aqui será desenvolvido várias versões do jogo chamado "Wunpus". Esse jogo é composto por 4 agentes, são eles: caçador, wumpus, ouro e buraco. Cada um desses personagem possui caracteristias importante para a dinâmica do jogo, vejamos:
1. **Caçador:**
   * O caçador só poderá andar pelas caças adjacentes a sua casa atual;
   * O Caçador terá apenas uma flexa para atirá no wumpus;
   * O caçador pode perceber sensações que o ambiente emana;
   * O caçador pode pegar o ouro;
2. **Wumpus:**
   * O wumpus ensala fedor nas casa adjacentes a sua;
   * O Wumpuns mata o caçador, caso esse entre em sua casa com ele vivo;
3. **Ouro:**
   * Brilha, seu brilho é sentido pelo caçado apenas na casa que está o ouro.
4. **Buraco:**
   * O Buraco emana fedor as casa adjacente a sua posição, caso o caçador entre em uma cas com buraco ele morre.
  
# Wumpus - Reativo
Nessa etapa do jogo os agentes não possuiem memória, não faz nenhum tipo de inferencia para tomar decisão. Assim, as decições são escolhidas totalmete randomica. Além disso, essa é a fase em que são programadas todas a ações do ambiente, como:
  + atirar;
  + Andar no ambiente;
  + Pegar ouro;
  + Matar Wumpus
  + Etc.
  

### **OBSERVAÇÃO:**
Os números na matrix corresponde ao respectivos agente:

  * 1 -  Caçador;
  * 2 - Wumpus;
  * 3 - Ouro;
  * 4 - Buraco.
  
![Wumpus - reativo](img/Wumpus-reativo.GIF)
  
  
  
  
