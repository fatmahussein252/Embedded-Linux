while pygame.mixer.get_busy():
    pygame.time.wait(100)  # Wait 100 milliseconds