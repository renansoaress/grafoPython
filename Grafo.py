import numpy as np

class Grafo:

    def __init__(self, tamanhoX, tamanhoY):
        self.grafo = np.zeros((tamanhoX, tamanhoY), dtype=np.int)
        self.graus = 0
        self.lacos = {}

    def inserirAresta(self, verticeX, verticeY):
        if not self.checarAresta(verticeX, verticeY):
            if verticeX == verticeY:
                self.lacos['{}:{}'.format(verticeX, verticeY)] = True
                self.grafo[verticeX, verticeY] = 1
                self.grafo[verticeY, verticeX] = 1
                print("Laço {}:{} criado!".format(verticeX, verticeY))
                self.graus += 2
            else:
                self.grafo[verticeX, verticeY] = 1
                self.grafo[verticeY, verticeX] = 1
                self.graus += 2
                print("Aresta {}:{} criada!".format(verticeX, verticeY))

            return True
        else:
            return False

    def excluirAresta(self, verticeX, verticeY):
        if self.checarAresta(verticeX, verticeY):
            if verticeX == verticeY:
                del self.lacos['{}:{}'.format(verticeX, verticeY)]
                self.graus -= 2
            else:
                self.grafo[verticeX,verticeY] = 0
                self.grafo[verticeY,verticeX] = 0
                self.graus -= 2
                print("Aresta {}:{} excluida!".format(verticeX, verticeY))
            return True
        else:
            return False

    def checarAresta(self, verticeX, verticeY):
        if self.grafo[verticeX, verticeY] == 1 and self.grafo[verticeY,verticeX] == 1:
            print("Existe aresta na posição {}:{}".format(verticeX,verticeY))
            return True
        else:
            print("Não existe aresta na posição {}:{}".format(verticeX,verticeY))
            return False

    def mostrarGrafo(self):
        print(self.grafo)

    def quantidadeVerticesIsolados(self):
        quantidade = 0
        for x in self.grafo:
            if not 1 in x:
                quantidade += 1
        print("Total de vertices isolados: {}".format(quantidade))
        return quantidade

    def apagarGrafo(self):
        print("Grafo apagados")
        self.grafo = np.zeros((5, 5), dtype=np.int)

    def quantidadeGraus(self):
        print("A quantidade de graus do grafo é: {}".format(self.graus))
        return self.graus

    def quantidadeLacos(self):
        print("A quantidade de laços do grafo é: {}".format(len(self.lacos)))
        return len(self.lacos)

    def imprimeComplemento(self):
        copiaGrafo = self.grafo
        for x in range(len(copiaGrafo)):
            for y in range(len(copiaGrafo[x])):
                if copiaGrafo[x][y] == 0:
                    copiaGrafo[x][y] = 1
                else:
                    copiaGrafo[x][y] = 0
        print(copiaGrafo)

    def isEuleriano(self):
        quantidadeImpares = 0
        for x in range(len(self.grafo)):
            verticesGrau = 0
            for y in range(len(self.grafo[x])):
                if self.grafo[x][y] != 0:
                    verticesGrau+=1
                    if x == y:
                        verticesGrau+=1
            if verticesGrau % 2 != 0:
                quantidadeImpares+1
        if quantidadeImpares == 2 or quantidadeImpares == 0:
            print("Essa grafo é Euleriano.")
            return True
        else:
            print("Essa grafo nāo é Euleriano.")
            return False

    def quantidadeVerticesDesconexo(self):
        resultado = 0
        for x in range(len(self.grafo)):
            verticesGrau = 0
            for y in range(len(self.grafo[x])):
                if self.grafo[x][y] != 0:
                    verticesGrau += 1
                    if x == y:
                        verticesGrau += 1
            if verticesGrau < 1:
                resultado += 1
        print("Vertices Desconexos: {}".format(resultado))
        return resultado

    def numeroCromatico(self):
        contadorAux = 0
        contadorNumeroCromatico = 0
        for x in range(len(self.grafo)):
            for y in range(len(self.grafo[x])):
                if self.grafo[x][y] == 1:
                    contadorAux+=1
            if contadorAux > contadorNumeroCromatico:
                contadorNumeroCromatico = contadorAux
            contadorAux = 0
        print("Numero cromatico: {}".format(contadorNumeroCromatico))
        return contadorNumeroCromatico

    def grauVerticesDecrescente(self):
        listaGraus = []
        for x in range(len(self.grafo)):
            verticesGrau = 0
            for y in range(len(self.grafo[x])):
                if self.grafo[x][y] != 0:
                    verticesGrau+=1
                    if x == y:
                        verticesGrau+=1
            listaGraus.append(verticesGrau)
        listaGraus = sorted(listaGraus, reverse=True)
        print("Graus dos vertices decrescente: {}".format(listaGraus))
        return listaGraus





if __name__ == '__main__':
    grafo = Grafo(5, 5)

    grafo.inserirAresta(0, 1)
    grafo.inserirAresta(1, 2)
    grafo.inserirAresta(2, 2)

    grafo.mostrarGrafo()

    grafo.quantidadeGraus()
    grafo.quantidadeLacos()
    grafo.quantidadeVerticesIsolados()

    grafo.isEuleriano()
    grafo.quantidadeVerticesDesconexo()
    grafo.numeroCromatico()
    grafo.grauVerticesDecrescente()
