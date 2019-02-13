class Iterator:

    def __call__(self, symbols, dim):
        return __init__(self, symbols, dim)

    def __init__(self, symbols, dim):

        self.combination = [symbols[0] for x in range (0, dim)]
        self.aux = [0 for x in range (0, dim)]
        self.symbols = symbols
        self.dim = dim


    def __iter__(self) :

        return self

    def __next__(self) :

        self.aux[0]+= 1
        #Comprobamos casos especiales de caracter a final de symbol
        for i in range (0, self.dim):
            #En caso de que encontremos un simbolo final
            if self.aux[i] >= len(self.symbols) :

                #Si este esta en el ultimo caracter no hay mas iteraciones
                if i == len(self.aux)-1 :

                    raise StopIteration

                else :
                    self.aux[i] = 0
                    self.aux[i+1]+= 1


            else :
                break

        for i in range (0, self.dim) :
            self.combination[self.dim-1-i]= self.symbols[self.aux[i]]
