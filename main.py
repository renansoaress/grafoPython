from Grafo import *

grafo = Grafo(5,5)

grafo.inserirAresta(0,1)
grafo.inserirAresta(1,2)
grafo.inserirAresta(2,2)

grafo.mostrarGrafo()

grafo.quantidadeGraus()
grafo.quantidadeLacos()
grafo.quantidadeVerticesIsolados()

grafo.isEuleriano()
grafo.quantidadeVerticesDesconexo()
grafo.numeroCromatico()
grafo.grauVerticesDecrescente()