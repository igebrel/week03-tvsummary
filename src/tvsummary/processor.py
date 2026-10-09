def count_genres(records):
    """Count how many TV shows belong to each genre."""
    genre_counts = {}

    for show in records:
        genres = show.get("genres") or []

        for genre in genres:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts

def average_rating_by_language(records):
    """Calculate the average TV show rating for each language."""
    rating_totals = {}
    rating_counts = {}

    for show in records:
        language = show.get("language") or "Unknown"
        rating = (show.get("rating") or {}).get("average")

        if isinstance(rating, (int, float)):
            rating_totals[language] = rating_totals.get(language, 0) + rating
            rating_counts[language] = rating_counts.get(language, 0) + 1

    averages = {
        language: round(rating_totals[language] / rating_counts[language], 2)
        for language in rating_totals
    }

    return averages