class TupleList:
    def __init__ (self):
        self.countries_list=[]
        self.country_name=""
        self.population=0
        self.continent=""

    #Funcion que solicita al usuario nro de paises a crear
    def total_countrys(self):
        print(" Ingresa la sifuiente informacón")
        print("==========================================")
        while True:
            try:
                number_countries=int(input("Cantidad a añadir: "))
                for country in range(number_countries):
                    self.country_name = input("      Pais>> ")
                    while True:
                        try:
                            self.population=int(input("      Población>>  "))
                            self.continent=input("        Continente>>  ")
                            print("-------------------------------------------")
                            #Añadimos una tupla con los valores correspondientes
                            self.countries_list.append((self.country_name,self.population,self.continent))
                            break
                        except ValueError:
                            print(">>Se esperaba un numero<<")

                print(self.countries_list)
            except ValueError:
                print(" >>> Error en el tipo de dato suministrado <<<")