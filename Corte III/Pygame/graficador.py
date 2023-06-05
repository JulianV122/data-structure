import pygame
import random
class Drawer:
    def __init__(self, screen, x, y, width, height, users, relationships):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.users = users
        self.relationships = relationships
        self.node_positions = {}
        self.set_positions()
        self.font_names = pygame.font.SysFont("Arial",15)

    def draw(self):
        self.draw_connections()
        self.draw_nodes()


    def draw_connections(self):
        for user_id, friends in self.relationships.items():
            start_pos = self.node_positions.get(int(user_id))  # Verificar si la clave existe en node_positions
            if start_pos is not None:
                for friend_id in friends:
                    end_pos = self.node_positions.get(friend_id)  # Verificar si la clave existe en node_positions
                    if end_pos is not None:
                        pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos, 2)

    def draw_nodes(self):
        for user in self.users:
            pos = self.node_positions.get(user["id"])  # Verificar si la clave existe en node_positions
            if pos is not None:
                x, y = pos
                name = self.font_names.render(user.get("name"),True,"Black")
                profile_image = user.get("profile_image")
                if profile_image is not None:
                    image_width, image_height = profile_image.get_size()
                    image_x = x - image_width // 2
                    image_y = y - image_height // 2
                    self.screen.blit(profile_image, (image_x, image_y))
                    self.screen.blit(name,(x-10,y+40))

    def set_positions(self):
        # Calcular las coordenadas de los nodos
        x_spacing = (self.width) // (len(self.users) + 1)
        y_spacing = self.height // (len(self.users) + 1)
        y_positions = [random.randint(y_spacing, self.height - y_spacing) for _ in range(len(self.users))]
        for i, user in enumerate(self.users):
            x = (i + 1) * x_spacing
            y = y_positions[i]
            self.node_positions[user["id"]] = (x, y)


    def set_data(self, users, relationships):
        self.users = users
        self.relationships = relationships
        self.set_positions()