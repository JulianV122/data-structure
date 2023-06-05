from io import BytesIO
import json
import random
import requests
import urllib.parse
import pygame
import networkx as nx
import matplotlib.pyplot as plt
from faker import Faker
from PIL import Image
from combo_box import ComboBox
import pygame
from graficador import Drawer
fake = Faker()

# Configuración de la ventana
class facebook:
    def __init__(self,screen):
        self.WINDOW_WIDTH = 980
        self.WINDOW_HEIGHT = 600
        self.screen = screen
        self.rect = pygame.Rect(0,60,980,600)
        self.rect2 = pygame.Rect(980,60,300,600)
        self.BACKGROUND_COLOR = (255, 255, 255)
        self.combo_box_rect1= pygame.Rect(1013,100,219,28)
        self.combo_box_rect2= pygame.Rect(1013,221,219,28)
        self.combo_box_rect3= pygame.Rect(1013,423,219,28)
        self.combo_box_rect4= pygame.Rect(1013,554,219,28)
        self.acceptRect = pygame.Rect(1048,293,150,28)
        self.list_users= []
        self.list_friends =[]
        pygame.display.set_caption("Red de Usuarios de Facebook")
        self.combo1 = ComboBox(self.screen,self.list_users,self.combo_box_rect1,"Black","Arial Black",15,4,"White","White",40," Seleccione un usuario")
        self.combo2 = ComboBox(self.screen,["Red de amigos","Red de familiares","Red de comunidades","Red de Ciudad"],self.combo_box_rect2,"Black","Arial Black",15,4,"White","White",40," Seleccione un usuario")
        self.combo3 = ComboBox(self.screen,self.list_friends,self.combo_box_rect3,"Black","Arial Black",15,4,"White","White",40," Seleccione un usuario")
        self.combo4 = ComboBox(self.screen,["Comunidades que ambos siguen"],self.combo_box_rect4,"Black","Arial Black",15,4,"White","White",40," Seleccione un usuario")
        self.clock = pygame.time.Clock()
        self.aux = False
        

        # Generar datos falsos y escribir el archivo JSON
        self.data, self.graph = self.generate_fake_data(10)
        self.write_json_file(self.data, "facebook_data.json")

        # Leer y mostrar los datos del archivo JSON
        self.read_facebook_data("facebook_data.json")

        # Ejecutar la función principal
        self.read_data()

        self.node_positions = {}

        self.get_positions(self.users)
        self.graficador = Drawer(self.screen,0,60,980,600,self.users,self.relationships)
        

    def generate_profile_image_url(self, name):
        # Generar una URL de imagen de perfil falsa con un avatar generado
        style = random.choice(["female", "male"])
        encoded_name = urllib.parse.quote(name)
        url = f"https://avatars.dicebear.com/api/{style}/{encoded_name}.png"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error al generar la imagen de perfil: {response.status_code}")
        content_type = response.headers.get("content-type")
        if "image" not in content_type:
            raise Exception("La respuesta no es una imagen válida.")
        return url

    def generate_fake_data(self, num_users):
        users = []
        relationships = {}

        for i in range(num_users):
            try:
                name = fake.name()
                profile_image_url = self.generate_profile_image_url(name)
                user = {
                    "id": i + 1,
                    "name": name,
                    "email": f"{name}@example.com",
                    "birthdate": "1990-01-01",
                    "profile_image_url": profile_image_url,
                    "liked_photos": [],
                    "family": [],
                    "groups": [],
                    "communities": [],
                    "city":random.choice(["Manizales","Pereira","Cartagena","Barranquilla"])
                }
                users.append(user)
                self.list_users.append(user["name"])
                num_family_members = 3
                num_family_members = min(num_family_members, len(users))
                family_members = random.sample(users, num_family_members)
                for family_member in family_members:
                    if family_member["name"] != user["name"]:
                        member = {
                            "name": family_member["name"],
                            "relation": random.choice(["Father", "Mother", "Sibling"]),
                            "id": family_member["id"],
                            "profile_image_url":family_member["profile_image_url"]
                            
                        }
                    else:
                        member = None
                    if member is not None:
                        user["family"].append(member)

                num_community_members = 4
                num_community_members = min(num_community_members, len(users))
                community_members = random.sample(users, num_community_members)
                for community_member in community_members:
                    if community_member["name"]!=user["communities"]:
                        community = {
                            "id": str(random.randint(10,50)),
                            "name": random.choice(["PS","XBOX","PC","NINTENDO"]),
                            "profile_image_url":community_member["profile_image_url"]
                        }
                        community_name = community["name"]
                        community["profile_image_url"] = community_name + ".png"
                    else:
                        community=None
                    if community is not None and community not in user["communities"]:
                        user["communities"].append(community)
                
                '''num_citys_members = 1
                num_citys_members = min(num_citys_members,len(users))
                num_citys = random.sample(users, num_citys_members)
                for num_city in num_citys:
                    city{
                        "nombre":random.choice([""])
                    }
'''
            except Exception as e:
                print(f"Error al generar el usuario {i + 1}: {e}")
            self.combo1.updateOptions(self.list_users)

        graph = nx.DiGraph()

        for user in users:
            graph.add_node(user["id"], data=user)

        for user in users:
            num_friends = random.randint(1, 5)
            friends = random.sample(users, num_friends)
            relationship_ids = [friend["id"] for friend in friends]
            relationships[user["id"]] = relationship_ids
            for friend in friends:
                graph.add_edge(user["id"], friend["id"])

        data = {
            "users": users,
            "relationships": relationships,
        }

        return data, graph

    def write_json_file(self, data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)

        print(f"El archivo {filename} ha sido creado exitosamente.")

    def read_facebook_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)

            # Leer usuarios
            print("Usuarios:")
            for user in data["users"]:
                print("ID:", user["id"])
                print("Nombre:", user["name"])
                print("Email:", user)
                print("Fecha de nacimiento:", user["birthdate"])
                print("URL de imagen de perfil:", user["profile_image_url"])
                print("Miembros de la familia:")
                for family_member in user["family"]:
                    print("Nombre:", family_member["name"])
                    print("Relación:", family_member["relation"])
                print("------------------------")

            # Leer relaciones de amistad
            print("Relaciones de amistad:")
            for user_id, friends in data["relationships"].items():
                print("ID de usuario:", user_id)
                print("Amigos:", friends)
                print("------------------------")

    def load_profile_images(self):
        for user in self.users:
            try:
                response = requests.get(user["profile_image_url"])
                if response.status_code == 200:
                    image_data = response.content
                    image = Image.open(BytesIO(image_data))
                    image = image.resize((80, 80))  # Ajusta el tamaño de la imagen si es necesario
                    image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
                    user["profile_image"] = image
                for family in user["family"]:
                    response = requests.get(family["profile_image_url"])
                    if response.status_code == 200:
                        image_data = response.content
                        image = Image.open(BytesIO(image_data))
                        image = image.resize((80, 80))  # Ajusta el tamaño de la imagen si es necesario
                        image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
                        family["profile_image"] = image
                for community in user["communities"]:
                    image= community["profile_image_url"]
                    image= pygame.image.load(f"Corte III/pygame/logoImages/{image}")
                    community["profile_image"]= image
            except Exception as e:
                print(f"Error al cargar la imagen de perfil para el usuario {user['id']}: {e}")
    
    def get_positions(self, users):
        # Calcular las coordenadas de los nodos
        x_spacing = self.WINDOW_WIDTH // (len(users) + 1)
        y_spacing = self.WINDOW_HEIGHT // (len(users) + 1)
        y_positions = [random.randint(y_spacing, self.WINDOW_HEIGHT - y_spacing) for _ in range(len(users))]
        for i, user in enumerate(users):
            x = (i + 1) * x_spacing
            y = y_positions[i]
            self.node_positions[user["id"]] = (x, y)


    def draw(self):
        self.graficador.draw()

    def draw_family_red(self):
        if self.combo1.getIndex() != -1:
            user_select = self.list_users[self.combo1.getIndex()-1]
            for user in self.users:
                if user["name"] == user_select:
                    relationship ={}
                    relationship[user["id"]]=[family["id"] for family in user["family"]]
                    self.graficador.set_data(user["family"]+[user],relationship)

    def draw_friends_red(self):
        if self.combo1.getIndex() != -1:
            relationship = {}
            user_select = self.users[self.combo1.getIndex()-1]
            relationship[user_select["id"]] = self.relationships[str(user_select["id"])]
            id_friends = self.relationships[str(user_select['id'])]
            friends = list(filter(lambda x: x['id'] in id_friends ,[user for user in self.users]))
            self.graficador.set_data([user_select] + friends, relationship)


    def draw_communities_red(self):
        if self.combo1.getIndex() != -1:
            user_select = self.list_users[self.combo1.getIndex()-1]
            for user in self.users:
                if user["name"] == user_select:
                    relationship ={}
                    relationship[user["id"]]=[community["id"] for community in user["communities"]]
                    self.graficador.set_data(user["communities"]+[user],relationship)


    def search_friends(self):
        user_select = self.list_users[self.combo1.getIndex()-1]
        for user in self.users:
            if user["name"] == user_select:
                id_friends= self.relationships[str(user["id"])]
                self.list_friends = [friend["name"] for friend in self.users if friend["id"] in id_friends]
                self.combo3.updateOptions(self.list_friends)
                return self.list_friends

    def similar_comunitis(self):
        name = self.combo1.getValue()
        nameFriend = self.combo3.getValue()
        nodes ={}
        nodes2={}
        nodes3={}
        relationships={}
        relationships2={}
        for user in self.users:
            if user["name"] in name:
                for community in user["communities"]:
                    for userFriend in self.users:
                        if userFriend["name"] == nameFriend:
                            for comunnity_friend in userFriend["communities"]:
                                if community["name"] == comunnity_friend["name"]:
                                    nodes[user["id"]] = [userFriend["id"], community["id"]]
                                    relationships[user["id"]]=[community["id"] for user in user["communities"]]
                                    nodes2[userFriend["id"]] = [user["id"],community["id"]]
                                    nodes3[community["id"]]= [user["id"], userFriend["id"]]
                                    nodes.update(nodes2)
                                    nodes.update(nodes3)
                                    self.graficador.set_data([user]+[community]+[userFriend],nodes)

    def similar_city(self):
        if self.combo1.getIndex() != -1:
            name = self.combo1.getValue()
            for user in self.users:
                if user["name"] == name:
                    relationship = {}
                    id_friends = self.relationships[str(user["id"])]
                    list_cityfriends_user = []
                    for friend in self.users:
                        if friend["id"] in id_friends and friend["city"] == user["city"]:
                            list_cityfriends_user.append(friend["id"])
                    relationship[user["id"]] = id_friends
                    self.graficador.set_data([user] + list_cityfriends_user,relationship)

    def draw_Rect(self):
        pygame.draw.rect(self.screen,"White",self.rect)
        pygame.draw.rect(self.screen,"darkgrey",self.rect2)
        pygame.draw.rect(self.screen,"black",self.combo_box_rect1,border_radius=3)
        pygame.draw.rect(self.screen,"black",self.combo_box_rect2,border_radius=3)
        pygame.draw.rect(self.screen,"black",self.combo_box_rect3,border_radius=3)
        pygame.draw.rect(self.screen,"black",self.combo_box_rect4,border_radius=3)
        pygame.draw.rect(self.screen,"Green",self.acceptRect,border_radius=3)

    def draw_Text(self, text, color, font, size, x, y):
        font_type = pygame.font.SysFont(font, size)
        new_text = font_type.render(text, False, color)
        self.screen.blit(new_text, (x, y))

    def show_Text(self):
        self.draw_Text("Selecciona un usuario de FB","Black","Arial",16,1013,80)
        self.draw_Text("Selecciona el tipo de grafo a visualizar","Black","Arial",16,1013,176)
        self.draw_Text("Selecciona un amigo de la red de usuario","Black","Arial",16,1013,376)
        self.draw_Text("Selecciona el tipo de grafo a visualizar","Black","Arial",16,1013,520)
        self.draw_Text("Aceptar","Black","Arial",16,1090,298)

    def read_data(self):
        # Leer y cargar los datos del archivo JSON
        with open("facebook_data.json", "r") as file:
            data = json.load(file)
            self.users = data["users"]
            self.relationships = data["relationships"]
            self.load_profile_images()


    def is_click_accept(self):
        if self.acceptRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and self.aux is False:
            self.aux = True
            if self.combo2.getIndex() == 1 and self.aux is True:
                self.draw_friends_red()
                self.search_friends()
            if self.combo2.getIndex() == 2 and self.aux is True:
                self.draw_family_red()
            if self.combo2.getIndex() == 3 and self.aux is True:
                self.draw_communities_red()
            if self.combo2.getIndex() == 4 and self.aux is True:
                self.similar_city()
            if self.combo4.getIndex() == 1 and self.aux is True:
                self.similar_comunitis()
        if not pygame.mouse.get_pressed()[0]:
            self.aux = False

    def draw_combos(self):
        self.combo4.draw()
        self.combo3.draw()
        self.combo2.draw()
        self.combo1.draw()
        
    def run(self):
        self.draw_Rect()
        self.show_Text()
        self.draw()
        self.clock.tick(60)
        self.draw_combos()
        self.is_click_accept()
        self.graficador.draw()
