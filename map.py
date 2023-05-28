#dodać do stałych. Odległości działają przy rozdzielczości 1600x900. Możliwe, że potem trzeba będzie to zmienić

LANE_WIDTH = (SCREEN_WIDTH - 4 * 390) // 3  # Szerokość pojedynczego pasa ruchu
TOR_OFFSET = (SCREEN_WIDTH - (3 * LANE_WIDTH + 2 * 105)) // 2  # Przesunięcie toru względem lewej krawędzi. Te 105 to moja zabawa pikselami, może to trzeba będzie usunąć
MIN_DISTANCE_BETWEEN_OBSTACLES = 500  # Minimalna odległość między przeszkodami. 500 jest chyba optymalne, od 400 i mniej gra może stać się niemożliwa do przejścia. Można tego używać do manipulowania poziomem trudności.
