class Animation:
    
    def __init__(self, sprites, frame_duration):
        self.sprites = sprites
        self.frame_duration = frame_duration  # Длительность каждого кадра в обновлениях
        self.current_frame = 0
        self.elapsed_time = 0

    def update(self):
        self.elapsed_time += 1
        if self.elapsed_time >= self.frame_duration:
            self.elapsed_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.sprites)

    def get_current_sprite(self):
        return self.sprites[self.current_frame]