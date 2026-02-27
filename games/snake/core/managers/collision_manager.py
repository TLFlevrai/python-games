class CollisionManager:
    @staticmethod
    def check_food_collision(snake_head, food_position):
        return snake_head == food_position

    @staticmethod
    def check_wall_collision(snake_head, grid_width, grid_height):
        x, y = snake_head
        return x < 0 or x >= grid_width or y < 0 or y >= grid_height

    @staticmethod
    def check_self_collision(snake_body):
        return snake_body[0] in snake_body[1:]