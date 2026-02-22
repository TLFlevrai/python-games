import pygame
import random

class SubtitleManager:
    """
    Gestionnaire de sous-titres multiples.
    Permet de faire tourner plusieurs phrases amusantes.
    """

    def __init__(self):

        # ---------- LISTE DES SOUS-TITRES ----------
        self.subtitles = [
            #v.0.0.0.4.5 - 10 comment
            "GG WP",
            "Powered by Pygame & passion",
            "Bug-free* gaming (*probably)",
            "made from scratch",
            "From 'Hello World' to 'Game Over'",
            "Code • Play • Repeat",
            "Coded with Py and <3",
            "No bugs, just features",
            "One game at a time",
            #v.0.0.0.5 + 10 comment
            "made by TLF",
            "work smarter, not harder",
            "code - debug - run - repeat",
            "new v.0.0.5 !", #special comment about the 0.5
            "no more hardcoded", #special comment about the 0.5
            "quality > quantity",
            "no more hardcoded",
            "Game Over? Never heard of it" ,
            "404: Error Not Found",
            "Classic never dies",
            "dev.skills += 1"
        ]

        # ---------- CONFIGURATION ----------
        self.current_index = 0
        self.mode = "random"  # "random" ou "sequential"
        
        # Timer pour changement automatique (optionnel)
        self.auto_change = False
        self.change_interval = 3000  # ms (3 secondes)
        self.last_change = pygame.time.get_ticks()

        # Sélectionner le premier sous-titre
        self.select_subtitle()

    # ---------- SELECTION ----------

    def select_subtitle(self):
        """Sélectionne un sous-titre selon le mode"""
        
        if self.mode == "random":
            self.current_index = random.randint(0, len(self.subtitles) - 1)
        
        elif self.mode == "sequential":
            self.current_index = (self.current_index + 1) % len(self.subtitles)
        
        return self.get_current()

    def next_subtitle(self):
        """Passe au sous-titre suivant manuellement"""
        return self.select_subtitle()

    def get_current(self):
        """Retourne le sous-titre actuel"""
        return self.subtitles[self.current_index]

    # ---------- CONFIGURATION ----------

    def set_mode(self, mode):
        """Change le mode de rotation ('random' ou 'sequential')"""
        if mode in ["random", "sequential"]:
            self.mode = mode

    def enable_auto_change(self, interval=3000):
        """Active le changement automatique avec intervalle (ms)"""
        self.auto_change = True
        self.change_interval = interval
        self.last_change = pygame.time.get_ticks()

    def disable_auto_change(self):
        """Désactive le changement automatique"""
        self.auto_change = False

    # ---------- UPDATE ----------

    def update(self):
        """Met à jour le gestionnaire (changement auto si activé)"""
        
        if self.auto_change:
            now = pygame.time.get_ticks()
            
            if now - self.last_change >= self.change_interval:
                self.select_subtitle()
                self.last_change = now
                return True  # Indique qu'il y a eu un changement
        
        return False

    # ---------- GESTION DE LA LISTE ----------

    def add_subtitle(self, text):
        """Ajoute un nouveau sous-titre à la liste"""
        if text not in self.subtitles:
            self.subtitles.append(text)

    def remove_subtitle(self, text):
        """Retire un sous-titre de la liste"""
        if text in self.subtitles and len(self.subtitles) > 1:
            self.subtitles.remove(text)

    def clear_subtitles(self):
        """Vide la liste (garde au moins un élément)"""
        self.subtitles = ["Python Games"]

    def set_subtitles(self, subtitle_list):
        """Remplace la liste complète de sous-titres"""
        if subtitle_list and len(subtitle_list) > 0:
            self.subtitles = subtitle_list
            self.current_index = 0