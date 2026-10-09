"""Queries behind the views. Part 2 of the lab happens in this file."""
from blog.models import Post


def posts_for_front_page():
    # author is a ForeignKey (one per post): select_related joins it in the same
    # query. tags is many-to-many: prefetch_related loads all of them in one
    # extra query. Two queries total, no matter how many posts there are.
    return (
        Post.objects.filter(published=True)
        .select_related("author")
        .prefetch_related("tags")
        .order_by("-published_at")
    )
