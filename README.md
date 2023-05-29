# JOGO WUMPUS
Aqui será desenvolvido várias versões do jogo chamado "Wunpus". Esse jogo é composto por 4 agentes, são eles: caçador, wumpus, ouro e buraco. Cada um desses personagens possuem caracteristicas importantes para a dinâmica do jogo, vejamos:
1. **Caçador:**
   * O caçador só poderá andar pelas casas adjacentes a sua casa atual;
   * O Caçador terá apenas uma flecha para atirar no wumpus;
   * O caçador pode perceber sensações que o ambiente emana;
   * O caçador pode pegar o ouro;
2. **Wumpus:**
   * O wumpus exala fedor nas casas adjacentes a sua;
   * O Wumpuns mata o caçador, caso esse entre em sua casa com ele vivo;
3. **Ouro:**
   * Brilha, seu brilho é sentido pelo caçado apenas na casa que está o ouro.
4. **Buraco:**
   * O Buraco emana brisa nas casas adjacente a sua posição, caso o caçador entre em uma casa com buraco ele morre.
  
# Wumpus - Reativo
Nessa etapa do jogo os agentes não possuem memória, não fazem nenhum tipo de inferencia para tomar decisão. Assim, as decições são escolhidas randomicamente. Além disso, essa é a fase em que são programadas todas a ações do ambiente, como:
  + atirar;
  + Andar no ambiente;
  + Pegar ouro;
  + Matar Wumpus
  + Etc.
  

### **OBSERVAÇÃO:**
Os números na matrix corresponde ao respectivos agente:

  * 1 - Caçador;
  * 2 - Wumpus;
  * 3 - Ouro;
  * 4 - Buraco.
  
![Wumpus - reativo](Docs/Wumpus-reativo.GIF)

![Descrição breve do projeto](Docs/Breve_relatorio_Proj_Wumpus.pdf)
  
  
  
  
