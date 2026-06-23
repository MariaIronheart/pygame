#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame import Surface
from pygame.ftfont import Font

from code.entity import Entity
from code.entityFactory import EntityFactory
from code.enemy import Enemy
from code.Const import COLOR_WHITE, PLAYER_LIVES, WIN_SCORE


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Layer'))

        self.player = EntityFactory.get_entity('Player')
        self.entity_list.append(self.player)

        self.spawn_timer = 0
        self.spawn_interval = 90
        self.lives = PLAYER_LIVES
        self.score = 0

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.spawn_timer += 1
            if self.spawn_timer >= self.spawn_interval:
                self.spawn_timer = 0
                self.entity_list.append(EntityFactory.get_entity('bat'))

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # Ataque da bruxa contra morcegos
            if self.player.attacking:
                self.window.blit(source=self.player.attack_surf, dest=self.player.attack_rect)
                attack_hitbox = pygame.Rect(
                    self.player.attack_rect.x,
                    self.player.attack_rect.y - 40,
                    30,
                    110
                )
                for ent in self.entity_list[:]:
                    if isinstance(ent, Enemy) and attack_hitbox.colliderect(ent.get_hitbox()):
                        self.entity_list.remove(ent)
                        self.player.attacking = False
                        self.player.attack_rect = pygame.Rect(-100, -100, 30, 30)
                        self.score += 1
                        break

            # Colisão morcego -> bruxa (perde vida)
            player_hitbox = self.player.rect.inflate(
                -self.player.rect.width * 0.5, -self.player.rect.height * 0.5
            )
            for ent in self.entity_list[:]:
                if isinstance(ent, Enemy) and player_hitbox.colliderect(ent.get_hitbox()):
                    self.entity_list.remove(ent)
                    self.lives -= 1

            # Morcego saiu da tela sem ser atingido (perde vida)
            for ent in self.entity_list[:]:
                if isinstance(ent, Enemy) and ent.rect.right < 0 and not ent.passed:
                    ent.passed = True
                    self.entity_list.remove(ent)
                    self.lives -= 1

            self.draw_hud()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            clock.tick(60)

            if self.lives <= 0:
                return 'GAME_OVER'
            if self.score >= WIN_SCORE:
                return 'WIN'

    def draw_hud(self):
        font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=26)

        score_surf: Surface = font.render(f"Score: {self.score}", True, COLOR_WHITE)
        self.window.blit(source=score_surf, dest=(10, 10))

        live_surf: Surface = font.render(f"Live: {self.lives}", True, COLOR_WHITE)
        self.window.blit(source=live_surf, dest=(10, 40))