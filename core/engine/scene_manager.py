# core/engine/scene_manager.py
class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None
        self.next_scene = None
        self.transition_time = 0

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def switch_to(self, name, transition_ms=0):
        if name in self.scenes:
            self.next_scene = name
            self.transition_time = transition_ms

    def update(self):
        if self.next_scene:
            # Gérer la transition (par exemple avec un délai)
            self.current_scene = self.scenes[self.next_scene]
            self.next_scene = None
        if self.current_scene:
            self.current_scene.update()

    def draw(self, surface):
        if self.current_scene:
            self.current_scene.draw(surface)

    def handle_event(self, event):
        if self.current_scene:
            self.current_scene.handle_event(event)