def count_genres(records):
    """Count how many TV shows belong to each genre."""
    genre_counts = {}

    for show in records:
        genres = show.get("genres") or []

        for genre in genres:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts